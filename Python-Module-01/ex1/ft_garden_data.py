class Plant:
    """Blueprint representing a plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant attributes."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    """Create and display plant registry."""
    plants: list[Plant] = [
        Plant("Hibiscus", 40, 60),
        Plant("Plumeria", 50, 90),
        Plant("Aloe Vera", 35, 200),
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant.get_info())


if __name__ == "__main__":
    main()
