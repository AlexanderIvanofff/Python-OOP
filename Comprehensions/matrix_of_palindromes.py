"""
Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in
the examples below.

•	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
•	Columns + rows define the middle letter:
•	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
•	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
"""


rows, cols = [int(x) for x in input().split()]

result = [[f"{chr(num)}{chr(nested_num)}{chr(num)}" for nested_num in range(num, num + cols)]for num in range(97, 97 + rows)]

print(*[" ".join(el) for el in result], sep='\n')