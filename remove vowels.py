def disemvowel(s):
    for c in "aeiouAEIOU":
        s=s.replace(c,"")
    return s
