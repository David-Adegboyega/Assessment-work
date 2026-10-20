values = [14, 7, 22, 9, 7, 31,]
target = 55

def linear_search(values, target):
    indices = []
    count = 0
    first = None
    last = None


    for  num in range(len(values)):
        if values[num] == target:
            indices.append(num)
            count += 1

            if first is None:
                first = num

            last = num

    if count == 0:
        return('Target not found')

    return (f"found at indices {indices} | count {count} | first {first}| last {last}")

print(linear_search(values, target))

