numberList = [21,34,54,56,43,23, 'ram']
numberTuple = (21,34,54,56,43,23, 'sam')
numberSet = {21,34,54,56,43,23, 'jack'}

print(numberList)
print(type(numberList))

print(numberTuple)
print(type(numberTuple))

print(numberSet)
print(type(numberSet))

numberSet.add(25)
print(numberSet)

numberSet.remove(21)
print(numberSet)


old_prices = {21,34,54,56,43,23}

new_prices = {32,23,43,54,64,54}

print(old_prices.intersection(new_prices))

# #functions
# #{}
# #unorderd
# #non dubplicate


# # how many difference between list,tuple and sets