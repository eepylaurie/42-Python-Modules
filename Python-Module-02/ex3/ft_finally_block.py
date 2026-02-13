def water_plants(plant_list: list[str | None]) -> None:
    print("Opening watering system")
    success = True
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
        success = False
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    good_plant_list = ["tomato", "lettuce", "carrots"]
    bad_plant_list = ["tomato", None, "carrots"]
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    water_plants(good_plant_list)
    print()
    print("Testing with error...")
    water_plants(bad_plant_list)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
