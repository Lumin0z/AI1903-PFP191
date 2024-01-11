#Q3 Write a program that performs the following tasks: 1. Calculate the multiplication and sum of two numbers

num1 = input("enter num 1:")
num2 = input("enter num 2:" )
print('Sum: ', +int(num1)+int(num2))
print('Product: ', +int(num1)*int(num2))
# 3. Display three string “Name”, “Is”, “James” as “Name**Is**James”

print('Name','Is','James',sep='**' )

# 2. Print the sum of the current number and the previous number

temp = 0
for i in range(10):
    print('Sum of the current and previous number: ',i +temp)
    temp = i


#Q4 Write a program that performs the following tasks: 1. Convert Decimal number to octal using print() output formatting
def decimal_to_octal(decimal):
 octal = ""
 while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
 return octal



decimal = int(input("Enter a decimal number: "))

octal = decimal_to_octal(decimal)
print("Octal: " + octal)
# 2. Display float number with 2 decimal places using print()

floatnum = 567.876876
print('Display float number with 2 decimal places {:.2f}'.format(floatnum))