#lab3b
#1.
def check_anagram(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()
    
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False



string1 = "listen"
string2 = "silent"

result = check_anagram(string1, string2)

if result:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#2.
def hex_to_decimal(hex_string):
    try:
        return int(hex_string, 16)
    except ValueError:
        return "Error: Invalid hexadecimal input."


hex_string = input("Enter a hexadecimal string: ")
result = hex_to_decimal(hex_string)

if isinstance(result, int):
    print("The corresponding base-10 value is:", result)
else:
    print(result)