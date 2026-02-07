def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def helper(remaining: int, day: int) -> None:
        if remaining == 0:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(remaining - 1, day + 1)

    helper(days, 1)
