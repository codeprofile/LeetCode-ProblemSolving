# 852. Peak Index in a Mountain Array
"""
An array arr a mountain if the following properties hold:
    >> arr.length >= 3
    >>There exists some i with 0 < i < arr.length - 1 such that:
        > arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        > arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    >> Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Constraints:
    >> 3 <= arr.length <= 10^5
    >> 0 <= arr[i] <= 10^6
    >> arr is guaranteed to be a mountain array.
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        -> Constraint : `arr is guaranteed to be a mountain array.`
        that means will always get an `arr.length` >=3 and  index that is represents a peak
        -> O(log(arr.length)) hints for binary search
        -> unsorted array : variation of binary search
        :param arr:
        :return:
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                # The peak must be on the right side of mid
                left = mid + 1
            else:
                # The peak must be on the left side of or at mid
                right = mid
        # At this point, left and right both point to the peak index
        return left


if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray(arr=[0, 1, 0]))
    print(s.peakIndexInMountainArray(arr=[0,2,1,0]))
    print(s.peakIndexInMountainArray(arr=[0,10,5,2]))
