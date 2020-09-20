def ageinDays(days):
    years = days // 365
    months = (days % 365) // 30
    days = (days % 365) % 30  

    print(f'{years} year(s), {months} month(s) and {days} day(s)')

days = int(input())
ageinDays(days)