# Learning python basics
# GDSC 30 days challenge

# 1- Valid Number Information

print("Welcome !")
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
total = 0

for number in numbers :
    if (number >= 0 and number <= 100) :
        valid_numbers.append(number)

for number in valid_numbers :
    total += number

average = total / len(valid_numbers)

print(f"valid_numbers = {valid_numbers}\nTotal = {total}\nAverage = {average}")

# 2- Number Analysis Program

print("\n Enter a serie of 20 numbers : ")
user_numbers = []
total_numbers = 0
i = 0

while (i != 20) :
    user_numbers.append(float(input(f"Enter the number {i+1} : ")))
    total_numbers += user_numbers[i]
    i = i + 1

user_numbers.sort()

print(f"The lowest number : {user_numbers[0]}")
print(f"The Highest number : {user_numbers[-1]}")
print(f"The total of the numbers : {total_numbers}")
print(f"The average of the numbers : {total_numbers / len(user_numbers)}\n")
