class Plant:
    """Blueprint representing a plant."""
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        """Initialize plant attributes."""
        self.name: str = name
        self.height_cm: int = height_cm
        self.age_days: int = age_days

    def grow(self) -> None:
        """Increase height by 1cm."""
        self.height_cm += 1

    def age(self) -> None:
        """Increase age by 1 day."""
        self.age_days += 1

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


def main() -> None:
    """Run growth simulation."""
    plants: list[Plant] = [
        Plant("Hibiscus", 40, 60),
        Plant("Plumeria", 50, 90),
        Plant("Aloe Vera", 35, 200),
    ]
    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())
    start_height = {plant: plant.height_cm for plant in plants}
    day = 1
    while day < 7:
        for plant in plants:
            plant.grow()
            plant.age()
        day += 1
    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        growth = plant.height_cm - start_height[plant]
        print(f"Growth this week: +{growth}cm")
        print()


if __name__ == "__main__":
    main()
