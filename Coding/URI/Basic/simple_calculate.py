def calculatePrice(products):
    sum = 0
    for values in products.values():
        print(f'Quantity:{int(values[0])}, Price:{float(values[1])}')
        sum = sum + int(values[0]) * float(values[1])
    
    print(f'Total amount to pay:{sum}')


products ={}

total = 2
for x in range(total):
    productID, unit, price = input().split()
    products[productID] = [unit, price]

calculatePrice(products)