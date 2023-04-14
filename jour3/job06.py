s = "abcdefghijklmnopqrstuvwxyz" * 10
n = len(s)
i = 0
k = 1
while i < n:
    print(s[i:i+k])
    i += k
    k += 1