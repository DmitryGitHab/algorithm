# 1 Two Sum
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        different = target - num
        if different in num_dict:
            return [num_dict[different], i]
        num_dict[num] = i
    return []


nums = [2, 7, 15, 17]
target = 9
print(twoSum(nums, target))


#9 Palindrome Number
"""Given an integer x, return true if x is a 
palindrome, and false otherwise."""
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    new_num = 0
    temp = x
    while temp != 0:
        digit = temp % 10
        new_num = new_num * 10 + digit
        temp //= 10
    return new_num == x

def isPalindrome_str(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

# print(isPalindrome(323))
# print(isPalindrome_str(323))

def intToRoman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    n = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
         4: 'IV', 1: 'I'}
    r = ''

    for i in values:
        while num >= i:
            num -= i
            r += n[i]
    return r

print(intToRoman(1994))