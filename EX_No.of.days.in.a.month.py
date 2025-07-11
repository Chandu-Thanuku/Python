def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:

                return True
            else:
              return False
        else:
            return True

    else:
        return False
def days_in_month(year,month):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 'february as 29 days'
    else:
        return days[month-1]
year=int(input('Enter year: '))
month=int(input('Enter month (1-12) as 1-january,2-feb,3-march....: '))
if month<=12 and month>=0:
    print(days_in_month(year,month))
else:
    print('Invalid input')
