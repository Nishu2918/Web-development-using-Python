# creating a tuple

numbers = (24,34,65,87,545,67,54,5,654)
print(numbers)
fruits = ('banana', 'apples', 'grapes')
print(fruits)
print(numbers[4])

numbers = ('marks', 'age', 24,34,65,87,545,67,54,5,654)
print(numbers)

print(type(numbers))

# using index position to slice a tuple

stock_prices = (34, 43, 55, 12, 34, 21, 65, 76, 32)
print(stock_prices[6:])
print ('location' in numbers)

# # iterating through the elements of a tupple

stocks = ("AAPL", "ULVR", "BMW")

for i in stocks:
    print(i)

stock_prices = (34, 43, 55, 12, 34, 21, 65, 76, 32)
del (stock_prices[6:])


# # ()
# # immutable
# # deleting an iten is not works
# # orderd
# # dubplicate