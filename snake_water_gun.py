import random

def check(computer, user):
  if(computer==user):
    return 0
  if(computer==1 and user==2):
    return -1
  if(computer==2 and user==3):
    return -1
  if(computer==3 and user==1):
    return -1
  return 1

computer=random.randint(1,3)
user=int(input('Press 1 for Snake,2 for Water,3 for Gun:\n'))

print(f'User={user}\nComputer={computer}')

points=check(computer, user)

if(points==0):
  print('Draw')
elif(points==-1):
  print('You loose')
else:
  print('You win!')
y=print()