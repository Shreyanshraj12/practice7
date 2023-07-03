def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}

    for s_char, t_char in zip(s, t):
        if s_char in s_dict:
            if s_dict[s_char] != t_char:
                return False
        else:
            s_dict[s_char] = t_char

        if t_char in t_dict:
            if t_dict[t_char] != s_char:
                return False
        else:
            t_dict[t_char] = s_char

    return True
s = "egg"
t = "add"
print(isIsomorphic(s, t))
