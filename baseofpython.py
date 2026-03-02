# Find a maximum number
#dont use max(), For Loop is allowed
numbers = [3,7,2,9,4]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)