def sum_range(start, end):
    if start > end:
        end, start = start, end
        return sum(range(start, end + 1))
    print(sum)

start = int(input())
end = int(input())
sum_range(start,end)