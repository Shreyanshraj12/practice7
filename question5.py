def reverseStr(s, k):
    chars = list(s)
    n = len(chars)

    for i in range(0, n, 2*k):
        chars[i:i+k] = chars[i:i+k][::-1]

    return ''.join(chars)
s = "abcdefg"
k = 2
print(reverseStr(s, k))
