#sum of first 10 even number
numbers= range(1,11)
sumA =0
for i in numbers:
    if i % 2 == 0:
        sumA+=i
print("the sum of first 10 even number is {} " .format(sumA))
