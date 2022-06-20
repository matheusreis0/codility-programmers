def quicksort(numbers: list[int]) -> list[int]:
    # base case
    if len(numbers) < 2:
        return numbers
    # recursive case
    else:
        pivot = numbers[0]
        minors = [i for i in numbers[1:] if i <= pivot]
        greatest = [i for i in numbers[1:] if i > pivot]
        return quicksort(minors) + [pivot] + quicksort(greatest)


print(quicksort([1,34,12,3,45]))
