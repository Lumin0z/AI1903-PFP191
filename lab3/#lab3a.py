#lab3a
#Q1 1.
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
breakpoint   
#Q1 2.

number = int(input("Enter the number: "))
sum=0
for i in range(1, number+1):
    sum = sum+i
print(sum)
#Q2 1.

numbers_list = [45, 120, 200, 68, 232, 36, 550, 180]

for number in numbers_list:
    if number > 500:
       
        break

    if number > 150:
        continue

    if number % 5 == 0:
        print(number)
#Q2 2.

def count_Digit(n): 
    count = 0
    while n != 0:
        n //= 10
        int(n)
        count += 1
    return count  
n = int(input("Enter a number:")) 
print("Number of digits : % d" % (count_Digit(n))) 
#Q2 3.

original_list = [1, 7, 12, 26, 39, 42, 50]

for i in range(len(original_list)-1, -1, -1):
 print(original_list[i])
#Q3 1.
 
def get_middle_four_chars(str1):
    print("Original String is", str1)

    mid = int(len(str1) / 2)

    res = str1[mid - 2:mid + 2]
    print("Middle four chars are:", res)

get_middle_four_chars("BundauMamtom")
get_middle_four_chars("CapheSuada")
#Q3 2.

def new_str(str1,str2):
    mid = int(len(str1) / 2)
    str3 = str1[:mid:]
    
    str3 = str3+str2
   
    str3 = str3+str1[mid:]
    print(str3)
new_str(input("Enter str1:"),input("Enter str2:"))
#Q3 3.

def mix_str(str1, str2):
    char_dau = str1[0]+str2[0]

    char_giua = str1[int(len(str1) // 2)] + str2[int(len(str2) // 2)]

    char_cuoi = str1[len(str1) - 1]+str2[len(str2) - 1]

    res = char_dau+char_giua+char_cuoi
    print("Mix String is ", res)

str1 = input("str1:")
str2 = input("str2:")
mix_str(str1, str2)
#Q3 4.

str1 =input("Enter string contain both upper and lower letter:")
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str = ''.join(lower + upper)
print(sorted_str)
#Q3 5.
def count_digits_chars_symbols(string):
    chars_count = 0
    digits_count = 0
    symbols_count = 0

    for char in string:
        if char.isalpha():
            chars_count += 1
        elif char.isdigit():
            digits_count += 1
        else:
            symbols_count += 1
  
    print("Chars= ", chars_count) 
    print("Digits= ", digits_count)
    print("Symbols= ", symbols_count)

string= "Pagscahcua323@#$$^^^&()()(&^)"
print("total counts of chars, Digits, and symbols \n")
count_digits_chars_symbols(string)
#Q4 1.

str1 = "I got 10$ for the rest of the week and there are 3 days left until the end of the week"
print("The given string is:")

print(str1)

print("Removing all the characters except digits")
print(''.join(i for i in str1 if i.isdigit()))
#Q4 2.

import string

a_string = "H[e]llo c@an ! you sh(o)w me the# way to the cine^ma?"
new_string = a_string.translate(str.maketrans('', '', string.punctuation))

print(new_string)