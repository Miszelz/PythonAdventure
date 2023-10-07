'''
def main():
    print('Hello World!')

if __name__ == '__main__':
    main()
name = input('Jak masz na imie?')

print ('Siema {}!'.format(name))


temp = False
print(type(temp))
print(temp)



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



num = int(input())

if num > 80:
    print(f'The score is {num} you did well!')
elif num > 50:
    print(f'Good job you scored {num}!')
else:
    print(f'{num}... too bad!')


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

    '''

## git init (tylko za pierwszym razem jak zakladasz repo)
## git add .
## git commit -m "Siema toi jest wiadomosc szczegolowo opisujaca ten commit"
## git push