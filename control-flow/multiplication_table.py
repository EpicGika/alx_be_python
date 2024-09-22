number = int(input("enter a number to see its multiplication table:"))

multiplication_table = (1, 2, 3, 4, 5, 7, 8, 9, 10)

for x in multiplication_table:
    product = x*number
    print(f"{number} * {x} = {product}")
