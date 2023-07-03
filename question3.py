def addStrings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0 or carry != 0:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        temp = x + y + carry
        result = str(temp % 10) + result
        carry = temp // 10
        i -= 1
        j -= 1

    return result
num1 = "11"
num2 = "123"
print(addStrings(num1, num2))
