def gametime(start, end):
    if start ==0 and end == 0:
        print(f'O JOGO DUROU 24 HORA(S)')
    elif end < start:
        print(f'O JOGO DUROU {24-start + end} HORA(S)')
    else:
        print(f'O JOGO DUROU {end - start} HORA(S)')

#start, end  = input().split()
#gametime(int(start), int(end))

start, end = list(map(int, input().split()))
gametime(start, end)

# 16 2