import sys

count = 1

while True:
    tmp = int(input())
    if tmp == 0:
        break

    print("Case %d: %d"%(count,tmp))
    count += 1