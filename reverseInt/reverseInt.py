def reverse_int(number: int) -> None:
    result: int = 1
    while number > 0:
        result = number % 10
        print(result, end="")
        number = number // 10
    print("")

reverse_int(123)
