def sequence_sum(start, end):
    total = 0
    if start > end:
        start, end = end, start

    total = sum([total+x for x in range(start, end+1)])
    print(sum)

start, end = list(map(int, input().split()))
sequence_sum(start, end)