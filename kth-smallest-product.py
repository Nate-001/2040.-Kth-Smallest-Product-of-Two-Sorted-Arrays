from bisect import bisect_left, bisect_right

class Solution(object):
    # Helper function to count how many products <= given middle
    def search(self, middle, nums1, nums2):
        count = 0
        for a in nums1:
            if a > 0:
                # We're solving when a is positive: a * b <= middle → b <= middle // a
                threshold = middle // a
                # Count how many b in nums2 are ≤ threshold
                count += bisect_right(nums2, threshold)
            elif a < 0:
                # when a is negative: a * b <= middle → b ≥ ceil(middle / a)
                # We use adjusted integer division to simulate ceiling
                threshold = (middle + (-a - 1)) // a
                # Count how many b in nums2 are ≥ threshold
                count += len(nums2) - bisect_left(nums2, threshold)
            else:
                # If a == 0, all products will be 0 → valid if middle ≥ 0
                if middle >= 0:
                    count += len(nums2)
        return count

    # Main function to find kth smallest product
    def kthSmallestProduct(self, nums1, nums2, k):
        # We identify the range of possible products
        # smallest * smallest 
        # smallest * biggest 
        # biggest * smallest 
        # biggest * biggest 
        products = [
            min(nums1) * min(nums2),
            min(nums1) * max(nums2),
            max(nums1) * min(nums2),
            max(nums1) * max(nums2),
        ]
        low = min(products)
        high = max(products)

        # Binary search for the smallest product such that
        # at least k products are ≤ that value
        while low < high:
            middle = (low + high) // 2
            count = self.search(middle, nums1, nums2)

            if count < k:
                # Not enough products ≤ middle → search right
                low = middle + 1
            else:
                # Possibly enough or too many → search left
                high = middle

        # When loop ends, low is the kth smallest product
        return low



        #linear search
'''
        productlist = []
        for i in nums1:
            for j in nums2:
                productlist.append(i * j)
        
        productlist.sort()
        return productlist[k-1]
'''
