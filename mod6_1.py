#Create a list between 5.5 and 20.5
nums = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("\nOriginal list of Integers:")
print(nums)


#Using the lambda function to count the even and odd numbers on the list
even_nums =list(filter(lambda x: (x % 2 == 0), nums))
odd_nums = list(filter(lambda x: (x % 2 != 0), nums))
print("{0} even numbers and {1} odd numbers in the Original List of Integers.".format(len(even_nums), len(odd_nums)))

#Using the lambda function that squares and cubes every number on the list
print("\nSquare the numbers in the list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

print("\nCube the numbers in the list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)