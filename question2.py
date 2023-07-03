def isStrobogrammatic(num):
    mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    left = 0
    right = len(num) - 1

    while left <= right:
        left_char = num[left]
        right_char = num[right]

        if left_char not in mapping or mapping[left_char] != right_char:
            return False

        left += 1
        right -= 1

    return True
num = "69"
print(isStrobogrammatic(num))
