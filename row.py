matrix = [
    [2, 4, 6], 
    [1, 3, 5], 
    [10, 20, 30]
]



def total(n):
    numbers = 0

    for num in n:
        numbers += num
    return numbers


def Mat(matrix):
    for row_number, row in enumerate(matrix, start=1):
        print(f"Row {row_number} total: {total(row)} | Average: {total(row)/len(row)}")

    for column_index in range(len(matrix[0])):
        column_total = 0

        for row in matrix:
            column_total += row[column_index]

        print(f"Column {column_index + 1} total: {column_total}")

Mat(matrix)




# def Mat(matrix):
#     for i in range(len(matrix)):
#         print(f"Row {i+1} total: {total(matrix[i])}")