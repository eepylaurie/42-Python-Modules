class Plant:
    """Base plant with name and height."""
    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant."""
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        """Grow the plant by 1cm."""
        self.height += 1


class FloweringPlant(Plant):
    """A plant that has flowers and can be blooming."""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant."""
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = False

    def grow(self) -> None:
        """Grow by 1cm and bloom."""
        super().grow()
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    """A flowering plant that can accumulate prize points."""
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        """Initialize a prize flower."""
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def grow(self) -> None:
        """Grow by 1cm and bloom (prize points stay constant)."""
        super().grow()


class GardenManager:
    """
    Manage multiple gardens and provide analytics.
    Includes a nested helper class for stats calculations.
    """
    class GardenStats:
        """Helper class for calculating statistics for a garden."""
        def __init__(self, plants: list[Plant], total_growth: int) -> None:
            """Initialize stats helper with a garden."""
            self.plants: list[Plant] = plants
            self.total_growth: int = total_growth

        def plants_added(self) -> int:
            """Return number of plants in the garden."""
            return len(self.plants)

        def get_total_growth(self) -> int:
            """Return total growth across all plants."""
            return self.total_growth

        def type_counts(self) -> tuple[int, int, int]:
            """Return (regular, flowering, prize) counts."""
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return (regular, flowering, prize)

    def __init__(self) -> None:
        """Initialize manager with no gardens."""
        self.gardens: dict[str, list[Plant]] = {}
        self.growth_log: dict[str, int] = {}

    def add_plant(self, owner: str, plant: Plant) -> None:
        """Add a plant to an owner's garden."""
        if owner not in self.gardens:
            self.gardens[owner] = []
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str) -> None:
        """Grow all plants in the given owner's garden by 1 step."""
        plants = self.gardens.get(owner, [])
        self.growth_log[owner] = self.growth_log.get(owner, 0) + len(plants)
        print(f"{owner} is helping all plants grow...")
        for plant in plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def report(self, owner: str) -> None:
        """Print a report for an owner's garden."""
        plants = self.gardens.get(owner, [])
        total = self.growth_log.get(owner, 0)
        stats = GardenManager.GardenStats(plants, total)
        regular, flowering, prize = stats.type_counts()
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in plants:
            self.print_plant_line(plant)
        print(
            f"Plants added: {stats.plants_added()}, "
            f"Total growth: {stats.get_total_growth()}cm"
        )
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers"
        )

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Create a demo network of gardens."""
        manager = cls()
        manager.gardens["Laurie"] = []
        manager.gardens["Fabio"] = []
        return manager

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility validation that doesn't depend on a specific garden."""
        return height >= 0

    @staticmethod
    def garden_score(plants: list[Plant]) -> int:
        """Compute a garden score (utility function)."""
        score = 0
        for plant in plants:
            score += plant.height
            if isinstance(plant, FloweringPlant):
                score += 10
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    def print_plant_line(self, plant: Plant) -> None:
        if isinstance(plant, PrizeFlower):
            blooming = "(blooming)" if plant.is_blooming else ""
            print(
                f"- {plant.name}: {plant.height}cm, {plant.color} flowers "
                f"{blooming}, Prize points: {plant.prize_points}"
            )
        elif isinstance(plant, FloweringPlant):
            blooming = "(blooming)" if plant.is_blooming else ""
            print(
                f"- {plant.name}: {plant.height}cm, {plant.color} flowers "
                f"{blooming}"
            )
        else:
            print(f"- {plant.name}: {plant.height}cm")


def main() -> None:
    """Demo the garden management system."""
    manager = GardenManager.create_garden_network()
    print("=== Garden Management System Demo ===")
    print()
    manager.add_plant("Laurie", Plant("Mango Tree", 250))
    manager.add_plant("Laurie", FloweringPlant("Hibiscus", 40, "pink"))
    manager.add_plant("Laurie", PrizeFlower("Plumeria", 50, "white", 10))
    print()
    manager.add_plant("Fabio", Plant("Japanese Maple", 120))
    manager.add_plant("Fabio", Plant("Black Pine", 140))
    manager.add_plant("Fabio", FloweringPlant("Red Spider Lily", 40, "red"))
    manager.add_plant("Fabio", PrizeFlower("Sakura Bonsai", 30, "pink", 20))
    print()
    manager.grow_all("Laurie")
    print()
    manager.grow_all("Fabio")
    print()
    manager.report("Laurie")
    print()
    manager.report("Fabio")
    print()
    print(f"Height validation test: {GardenManager.validate_height(10)}")
    laurie_score = GardenManager.garden_score(manager.gardens["Laurie"])
    fabio_score = GardenManager.garden_score(manager.gardens["Fabio"])
    print(f"Garden scores - Laurie: {laurie_score}, Fabio: {fabio_score}")
    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    main()
