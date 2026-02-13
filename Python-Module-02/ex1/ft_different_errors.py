def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()

    print("Testing KeyError...")
    try:
        plant = {"name": "Hibiscus", "height": 40}
        print(plant["age"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError) as e:
        print(f"Caught an error, but program continues! ({e})")
    print()


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
