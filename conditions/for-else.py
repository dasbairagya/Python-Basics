nums = [9,12,15,19,24]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not found")