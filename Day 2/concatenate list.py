# list adding

prices_yesterday = [ 23, 45, 11, 98]
prices_today = [ 49, 66, 45]

prices_combined = prices_yesterday + prices_today
print(prices_combined)

# creating nested list

customer_1 = ["tommy", 23]
customer_2 = ["jack", 27]
customer_3 = ["macy", 24]
customer_4 = ["jenny", 19]

customers = [customer_1, customer_2, customer_3, customer_4]
print(customers)

print(customers[1])

# iterating nested list


emp_1, emp_2, emp_3, emp_4 = (("tom", 23), ("rom", 27), ("mac", 24), ("jan", 19))
employees =[emp_1, emp_2, emp_3, emp_4]
print(employees)

# finding the maximum value 


stock_prices = [23, 24, 27, 28, 32, 22]
print(max(stock_prices))



# sorting list

stocks = ["ULVR", "BMW", "aapl", "AAPL"]
print(sorted(stocks))


# use the del keyword to delete a few elements from the list

stock_prices = [23, 24, 27, 28, 32, 22]
del stock_prices[1:4]
print(stock_prices)


# for empty list

stock_prices = [23, 24, 27, 28, 32, 22]
del stock_prices[:]
print(stock_prices)


# employee and student list (work)