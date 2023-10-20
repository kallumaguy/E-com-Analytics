#import this


'''
Multi commented line
Author: Adil
USN   : 007
'''

print('Hello World')

#variables
a = 1
print(a)
print(type(a))

b = 1.2
print(b)
print(type(b))

c = 'MCA'
print(c)
print(type(c))

print('The value of a is '+str(a))

a = 6
b = 90
c = a + b
print(c)

player1 = 'Rafel Nadal'
player2 = 'Sania Mirza'
player3 = 'Roger Federer'

print(player1,player2,player3)

'''
Invalid variable declaration

1player
player-name
player name

'''
#Valid var declaration
_player_name = ''
playerName = ''
Player_Name = ''

#conditional statements
a = 10

if a >= 10:
    print('a is greater')
else:
    print('a is not greater')

dialog = 'I am Groot'

if 'Groot' in dialog:
    print("It's present")
else:
    print('It\'s not present')

#loop statements
#nested loops
for n in range(1,16):
    print(n)
    for j in range(1,5):
        print(j)

#function defining
def add():
    a = 5
    b = 6
    return a + b

print(add())

#function returntype
def multiply(a,b):
    return a * b

print(multiply(5,7))

#arbitrary function
def display(*a):
    print(a[1])

display(1,2,3)
