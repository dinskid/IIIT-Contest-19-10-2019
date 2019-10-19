no = int(input())
li = list(map(int, input().split()))
i, j = list(map(int, input().split()))
print(sum(li[i: j+1]))
