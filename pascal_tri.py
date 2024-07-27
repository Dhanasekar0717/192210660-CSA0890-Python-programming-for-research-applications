def generate_pascals_triangle(numRows):
    triangle = []
    for row_num in range(numRows):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
    return triangle
numRows = int(input("Enter the number of rows: "))
result = generate_pascals_triangle(numRows)
for row in result:
    print(row)
