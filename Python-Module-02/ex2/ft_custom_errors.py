class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(name: str, is_healthy: bool) -> None:
    if not is_healthy:
        raise PlantError(f"The {name} plant is wilting!")


def check_water(level: int) -> None:
    if level < 1:
        raise WaterError("Not enough water in the tank!")


def garden_operations() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", False)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", False)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print()


def test_custom_error_types() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    garden_operations()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_error_types()
