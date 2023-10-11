'''
# executing code

def main():
    print('Hello World!')

if __name__ == '__main__':
    main()
name = input('Jak masz na imie?')

print ('Siema {}!'.format(name))


temp = False
print(type(temp))
print(temp)

# arythmetics

x=4
y=2.3

print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print(x // y) 
print(x % y)

x += 2.2
y %= 3


print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print(x // y) 
print(x % y)


x = 3
y = 3

print(x == y) 
print(x != y)
print(x > y )
print(x < y )
print(x >= y) 
print(x <= y) 


x = 7
y = 7

print(x == y and x > y)
print(x > y or x < y)
print(not(x >= y and x == y))

# else if

num = int(input())

if num > 80:
    print(f'The score is {num} you did well!')
elif num > 50:
    print(f'Good job you scored {num}!')
else:
    print(f'{num}... too bad!')

# loops
    
nums = [2, 4, 6, 4]

for x in nums:
    print(x * (x - 1))

i = 1
while i < 3:
    
    print(x)
    i += 1

for x in range(3):
    print(x)

for x in nums[0:4:1]:
    print(x)

# try, except and finally

Lst = [2, 4, 6, 8, 'd']


try:
    print(sum(Lst))
except:
    print("error")
finally:
    print("end")



# Functions

def add_three(x, y, z):
    sum = x + y + z
    return sum

output = add_three(1,2,3)

print(output)

def f_test(input):
    if input > 10:
        out = "Good"
    elif input >= 5:
        out = 'Med'
    elif input < 5:
        out = 'Bad'

    print(out)

f_test(int(input()))


# Recursion

x = 10
Lst = []

def factorial(x):
    
    if x == 1:
        print(x)
        Lst.append(x)
        print(Lst)
        return 1
    else:
        print(x)
        Lst.append(x)
        print(Lst)
        return x * factorial(x-1)
        

factorial(x)

'''



## git init (tylko za pierwszym razem jak zakladasz repo)
## git add .
## git commit -m "Siema toi jest wiadomosc szczegolowo opisujaca ten commit"
## git push