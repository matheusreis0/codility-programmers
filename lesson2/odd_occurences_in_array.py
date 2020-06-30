def solution(A):
    result = 0

    for item in A:
        result ^= item

    return result

"""
    result = 0

    for item in A:
        result ^= item

    return result

    for item in A:
        found = 0
        for i in A:
            if i == item:
                found += 1

        if found % 2 != 0:
            item_unpaired = item

    return item_unpaired

    for item in A:
        print(item, end="--")
        
        found = 0
        for i in A:
            print(i, end=' ')

            if i == item:
                found += 1
            if found >= 2:
                break
        if found % 2 != 0:
            item_unpaired = item
        print()

    return item_unpaired
"""

# array = [9, 3, 9, 3, 9, 7] + [9] * 3 + [3] * 4
# array = [3, 3, 3, 3, 9, 9, 7]
array = [9, 9, 7, 7] * 123 + [3]
print(solution(array))
