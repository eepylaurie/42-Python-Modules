class Plant:
    """Blueprint representing a plant created by the factory."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


def main() -> None:
    """Create plants efficiently and display them."""
    plant_data: list[Plant] = [
        ("Hibiscus", 40, 60),
        ("Mango Tree", 250, 700),
        ("Aloe Vera", 35, 200),
        ("Plumeria", 50, 90),
        ("Monstera", 90, 180),
    ]
    plants = []
    for name, height, age in plant_data:
        plants.append(Plant(name, height, age))
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.get_info()}")
    print()
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
