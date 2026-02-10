class SecurePlant:
    """Plant that protects its data from invalid values."""
    def __init__(self, name: str) -> None:
        """Initialize a secure plant with safe defaults."""
        self.name: str = name
        self._height: int = 0
        self._age: int = 0

    def set_height(self, height: int) -> None:
        """Set height if valid."""
        if height < 0:
            print()
            print(
                f"Invalid operation attempted: "
                f"height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            print()
            return
        self._height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set age if valid."""
        if age < 0:
            print()
            print(
                f"Invalid operation attempted: "
                f"age {age} days [REJECTED]"
            )
            print("Security: Negative age rejected")
            print()
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Return height in cm."""
        return self._height

    def get_age(self) -> int:
        """Return age in days."""
        return self._age

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name} ({self._height}cm, {self._age} days)"


def main() -> None:
    """Demo the garden security system."""
    plant = SecurePlant("Hibiscus")
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(40)
    plant.set_age(60)
    plant.set_height(-5)
    print(f"Current plant: {plant.get_info()}")


if __name__ == "__main__":
    main()
