class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> str:
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low"
            f" (min 2)"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high"
            f" (max 12)"
        )

    return (
        f"{plant_name}: healthy"
        f" (water: {water_level}, sun: {sunlight_hours})"
    )


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(
        self,
        plant_name: str,
        water_level: int,
        sunlight_hours: int
    ) -> None:
        try:
            report = check_plant_health(
                plant_name,
                water_level,
                sunlight_hours
            )
            print(report)
        except ValueError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management() -> None:
    garden = GardenManager()

    print("=== Garden Management System ===")
    print()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print()

    print("Watering plants...")
    garden.water_plants()
    print()

    print("Checking plant health...")
    garden.check_health("tomato", 5, 8)
    garden.check_health("lettuce", 15, 8)
    print()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
