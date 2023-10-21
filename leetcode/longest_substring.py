def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    str_pos = 0
    substrings = []
    for value in s:
        try:
            substrings[str_pos].append(value)
        except:
           substrings.append([value])
    print(substrings)
        

print(lengthOfLongestSubstring('abcabcbb'))