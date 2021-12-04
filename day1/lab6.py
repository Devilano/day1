#sum of first 10 odd number
number =range(1,11)
sumA =1
for i in number:
    if i % 2 == 1:
        sumA+=i
print("thr sum of 10 odd number is{}" .format(sumA))
