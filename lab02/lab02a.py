#Q1 1.
def print_func1(*args):
   for i in args:
        print(i)
print("Printing values:")
print_func1(20,40,60)
print("Printing values:")
print_func1(40,60)

#2.
def Calculation(a,b):
   x=a+b
   y=a-b
   print(x,y)
res=Calculation(60,30)
print(res)
#Q2 1.
def showEmployee(a,b=9000):
    print("Name:", a, "pay", b )
showEmployee("Ben",12000)
showEmployee("Jessica")

#2.
def outfunc(a,b):
    def infunc(a,b):
        return a+b
    return infunc(a,b) + 5
res=outfunc(5,10)
print(res)

#Q3 1.
def recur_func(a,i = 0, temp = 0):
    if i <= a:
        temp=temp + i
        i += 1
        return recur_func(a, i, temp)
    else:
        return temp
res=recur_func(10)
print(res)
#2.
def display_student(name,age):
    print(name,age)
show_student=display_student
show_student("Emma",18)
#Q4 1.
def Palindrome(a, b=0, n=0):
    while a > 1:
        temp = a%10
        b = temp*pow(10,n)
        n = n+1
        a = a/10
    if b == a:
        return b
    else:
        return b
if Palindrome(141):
    print("is a palindrome number")
else:
    print("isnt a palindrome number")
#2.
def max():
   max = 0
   x = [2, 24, 5, 4 ,9, 12]
 

   array = list(x)
   for i in range(len(array)):
        if array[i] > max:
            max = array[i]
   return max       
maximum = max()
print(maximum)