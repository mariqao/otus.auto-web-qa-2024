def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return int(average)


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
