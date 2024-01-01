"""
455. Assign Cookies
Problem Statement :
    Assume you are an awesome parent and want to give your children some cookies.
    But, you should give each child at most one cookie.
    Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
    and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
    Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
    Input: g = [1,2,3], s = [1,1]
    Output: 1
    Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
    And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
    You need to output 1.

Example 2:
    Input: g = [1,2], s = [1,2,3]
    Output: 2
    Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
    You have 3 cookies and their sizes are big enough to gratify all of the children,
    You need to output 2.

Constraints:
    1 <= g.length <= 3 * 10^4
    0 <= s.length <= 3 * 10^4
    1 <= g[i], s[j] <= 2^31 - 1

Explanation Link : https://leetcode.com/problems/assign-cookies/solutions/4485000/easy-explanation-2-pointer-sorting-greedy/
"""
from typing import List


class Solution:
    # Time Complexity : O(nlogn)
    # Space Complexity : O(1)
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        first we sort the array , g = [1, 4, 9] and s = [2, 3 ,10];
        intialize two pointer i = 0 and j = 0 to iterate on g and s respecitvely and a count to track the assign cookies.
        if g[i] <= s[j], means we can assign jth cookie to ith child, increase the count and increment i and j pointer. e.g., g[0] < s[0], so we would increment i, j and count to 1;
        else we will increase the cookie pointer j till we get g[i] <= s[j] e.g., g[1] > s[1], so we would only j to 2 and in nex iteration we would compare g[1] and s[2], as g[1] < s[2] we would assign the count to 2.
        """
        # sort the arrays
        g.sort()
        s.sort()

        # Initialize count for tracking assignments of cookies
        count = 0
        # Initialize two pointers i and j to iterate on g and s
        i, j = 0, 0

        # Iterate through the arrays
        while i < len(g) and j < len(s):
            # If the size of the cookie is greather than or equal to the child's greed,
            # assign the cookie to the child and move both pointers
            if g[i] <= s[j]:
                count += 1
            i += 1
            # Move the cookie pointer to the next cookie, regardless of assignment
            j += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.findContentChildren(g=[1, 2, 3], s=[1, 1]))
    print(s.findContentChildren(g=[1, 2], s=[1, 2, 3]))
