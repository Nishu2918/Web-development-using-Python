name = "kiran kumar"
print(name)
print(type(name))
print(name[10])

product = "nishanth"
print(product[:5])

product = "nishnath"
print(product[0:15:1])

product = "nishnath"
print(product[0:15:2])

#lower
product = "nishanth"
print(product.islower())

#alpha
product = "TreasureBills"
product.isalpha()

#digit
product = "TreasureBills"
print(product.isdigit())

#split
product = "Never invest emergency savings in the stock market"
print(product.split())

#lower
product = "Never invest emergency savings in the stock market"
print(product.lower())

#upper
product = "Never invest emergency savings in the stock market"
print(product.upper())

#title
product = "Never invest emergency savings in the stock market"
print(product.title())

#capitalize
product = "Never invest emergency savings in the stock market"
print(product.capitalize())

#swapcase
product = "Never invest emergency savings in the stock market"
print(product.swapcase())

#replace
print(product.replace("invest","update"))

