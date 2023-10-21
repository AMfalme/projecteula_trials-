"""
    Given a string, find the length of the longest
    substring in it with no more than K distince characters.

    Input: String = "araaci", K =2
    Output: 4
    Explanation: The longest substring with no more 
    than '2' distince characters is "araa".


    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more 
    than '1' distince characters is "aa".

    Input: String = "cbbebi:, K=3
    Output: 5
    Explanation: The longest substrings with no more 
    than '3' distinct characters are "cbbeb" & "bbebi" 
"""


def longest_substring(string, k):
    chars_k = {

    }
    substrings = []
    for s in string:
        chars_k[s] += 1
        if chars_k.keys == k:
            substrings.append(chars_k.values)
    
    print(substrings)

print(longest_substring('araaci',2))