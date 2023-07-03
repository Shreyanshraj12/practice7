def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    s2 = s + s
    if goal in s2:
        return True
    else:
        return False
s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))
