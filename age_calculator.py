import datetime

currunt_date=datetime.datetime.now()
date=currunt_date.day
month=currunt_date.month
year=currunt_date.year

birth_date=int(input('Enter date of your birth(digits):'))
birth_month=int(input('Enter month of your birth(digits):'))
birth_year=int(input('Enter year of your birth(digits):'))
# Years
if(month>birth_month):
  x=year-birth_year
elif(month<birth_month):
  x=year-birth_year-1
elif(month==birth_month):
  if(date>birth_date):
    x=year-birth_year
  elif(date<birth_date):
    x=year-birth_year-1
  elif(date==birth_date):
    x=year-birth_year
  else:
    print('Invalid input')
years=x

# Months
if(month>birth_month):
  x=month-birth_month
elif(month<birth_month):
  x=12-(birth_month-month)
elif((month==birth_month)and(date>=birth_date)):
  x=0
elif((month==birth_month)and(date<birth_date)):
  x=11
else:
  x='invalid input'
months=x

# Days
if(date>birth_date):
  y=date-birth_date
elif(date<birth_date):
  if(month==1):
    y=31-(birth_date-date)
  elif(month==2):
    y=28-(birth_date-date)
  elif(month==3):
    y=31-(birth_date-date)
  elif(month==4):
    y=30-(birth_date-date)
  elif(month==5):
    y=31-(birth_date-date)
  elif(month==6):
    y=30-(birth_date-date)
  elif(month==7):
    y=31-(birth_date-date)
  elif(month==8):
    y=31-(birth_date-date)
  elif(month==9):
    y=30-(birth_date-date)
  elif(month==10):
    y=31-(birth_date-date)
  elif(month==11):
    y=30-(birth_date-date)
  elif(month==12):
    y=31-(birth_date-date)
  else:
    y='invalid input'
else:
  y='invalid input'
days=y

print(f'Your are {years} years,{months} months & {days} days old')
y=input()
