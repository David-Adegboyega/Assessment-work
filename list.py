def list_analyser(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    smallest_index = 0
    largest_index = 0
    total = 0
    index = 0

    for number in numbers:
        if number < smallest:
            smallest = number
            smallest_index = index
        
        if number > largest:
            largest = number
            largest_index = index

        index += 1
        total += number

    average = total / len(numbers)

    above_average = 0

    for number in numbers:
        if number > average:
            above_average += 1

    return (  
        smallest, 
        smallest_index,
        largest,
        largest_index,  
        total, 
        average,
        above_average, 
 ) 

numbers = [12, 5, 27, 8, 14, 27, 3]
(  
    smallest, 
    smallest_index,
    largest,
    largest_index,  
    total, 
    average,
    above_average, 
 ) = list_analyser(numbers)


print(f"Smallest: {smallest} at index {smallest_index}")
print(f"Largest: {largest} at index {largest_index}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"the numbers greater than  average is {above_average}")



