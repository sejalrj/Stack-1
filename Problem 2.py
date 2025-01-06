class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0: return []
        greater_elements = {}
        stack = deque()
        stack.append(nums2[0])
        
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                top = stack.pop()
                greater_elements[top] = nums2[i]
            
            stack.append(nums2[i])
        
        # print(greater_elements)

        return [greater_elements[i] if i in greater_elements else -1 for i in nums1 ]

    
