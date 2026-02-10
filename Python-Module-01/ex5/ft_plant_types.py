class Plant:
    """Base plant with shared attributes."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize common plant attributes."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return basic plant information."""
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.height}cm, {self.age} days"
        )


class Flower(Plant):
    """Flower plant type with a color and bloom behavior."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        """Return bloom message."""
        return f"{self.name} is blooming beautifully!"

    def get_info(self) -> str:
        """Return flower info."""
        return f"{super().get_info()}, {self.color} color"


class Tree(Plant):
    """Tree plant type with trunk diameter and shade behavior."""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        """Initialize a tree."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        """Return shade message."""
        shade = self.trunk_diameter * 1.56
        return f"{self.name} provides {shade:.0f} square meters of shade"

    def get_info(self) -> str:
        """Return tree info."""
        return f"{super().get_info()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Vegetable plant type with harvest season and nutrition info."""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """Initialize a vegetable."""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def describe_nutrition(self) -> str:
        """Return info about nutritional value."""
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_info(self) -> str:
        """Return vegetable info."""
        return f"{super().get_info()}, {self.harvest_season} harvest"


def main() -> None:
    """Create and display specialized plant types."""
    flowers: list[Flower] = [
        Flower("Hibiscus", 40, 60, "pink"),
        Flower("Plumeria", 50, 90, "white"),
    ]
    trees: list[Tree] = [
        Tree("Mango Tree", 250, 700, 35),
        Tree("Coconut Palm", 300, 800, 45),
    ]
    vegetables: list[Vegetable] = [
        Vegetable("Chili Pepper", 70, 90, "summer", "vitamin C"),
        Vegetable("Taro", 150, 250, "autumn", "potassium"),
    ]
    print("=== Garden Plant Types ===")
    for f in flowers:
        print()
        print(f"{f.get_info()}")
        print(f.bloom())
    for t in trees:
        print()
        print(f"{t.get_info()}")
        print(t.produce_shade())
    for v in vegetables:
        print()
        print(f"{v.get_info()}")
        print(v.describe_nutrition())


if __name__ == "__main__":
    main()
