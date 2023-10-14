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
# print(twoSum(nums, target))


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

# print(intToRoman(1994))

# 14. Longest Common Prefix
"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ''."""
def longestCommonPrefix(strs: List[str]) -> str:
    ans = ''

    for i, val in enumerate(zip(*strs)):
        if len(set(val)) == 1:
            ans += val[0]
        else:
            break
    return ans

# print(longestCommonPrefix(["flower","flow","flight"]))

# 20. Valid Parentheses

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

def isValid(s: str) -> bool:
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c in brackets:
            # print(c)
            stack.append(c)
            # print(stack)
        elif stack and c == brackets[stack.pop()]:
            continue
        else:
            return False
    print(stack)
    return not stack

# print(isValid('()[]{}'))

# 21. Merge Two Sorted Lists
'''You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.'''


'''Definition for singly-linked list.'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __str__(self):
    #     # return "dafsdf"
    #     return str(self.val)

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node
    dummy = ListNode(0)
    cur = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next

        cur = cur.next

    # In case any has still nodes left, just append them
    cur.next = l1 if l1 else l2

    return dummy.next

list1 = ListNode([1,4,5,5,9])
list2 = ListNode([1,3,6,8,8])

# print(mergeTwoLists(list1,list2))
# mergeTwoLists(list1,list2)


# 26. Remove Duplicates from Sorted Array
"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k."""
from collections import OrderedDict

def removeDuplicates(nums: List[int]) -> int:
    # nums[:] =  OrderedDict.fromkeys(nums)
    # return len(nums)
    nums[:] = sorted(set(nums))
    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(removeDuplicates([1,1,2]))