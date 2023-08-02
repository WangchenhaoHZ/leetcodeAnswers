class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
    # def findMedianSortedArrays(self, nums1:list, nums2:list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1 = len(nums1)
        len2 = len(nums2)
        half_index = (len1 + len2) // 2
        # len1 - (len1+len2)/2 = (len1 - len2)/2 > 0
        head = 0
        tail = len1 - 1
        if tail == -1: mid = -1
        else: mid = (head + tail+1) // 2
        left_index = half_index - mid - 1
        while head < tail:
            mid = (head + tail+1) // 2
            left_index = half_index - mid - 1
            if   (left_index>=len2) or (nums1[mid] < nums2[left_index]):
                head, tail = mid, tail
            if (left_index< 0) or(nums1[mid] >= nums2[left_index]):
                if tail == mid: break
                head, tail = head, mid
        if head < tail:
            if nums1[head] >= nums2[half_index - head - 1]:
                mid = head
                left_index = half_index - head - 1
        if mid == -1:
            n_plus_1 = nums2[left_index]
            n = nums2[left_index-1]
        else:
            if nums1[mid] >= nums2[left_index]:
                #print("No. n+1 or n+2", nums1[mid])
                if (left_index + 1==len2):
                    #print("No. n+1: ", nums1[mid])
                    n_plus_1 = nums1[mid]
                else:
                    if nums2[left_index + 1] < nums1[mid]:
                        #print("No. n+1: ", nums2[left_index + 1])
                        n_plus_1 = nums2[left_index + 1]
                    else:
                        #print("No. n+1: ",nums1[mid])
                        n_plus_1 = nums1[mid]
                if (mid==0):
                    #print("No. n: ", nums2[left_index])
                    n = nums2[left_index]
                else:
                    if nums2[left_index] < nums1[mid-1]:
                        #print("No. n:", nums1[mid-1])
                        n = nums1[mid-1]
                    else:
                        #print("No. n:", nums2[left_index])
                        n = nums2[left_index]
            else: 
                if (left_index-1>=0) and (nums1[mid] <= nums2[left_index-1]):
                    n = nums2[left_index-1]
                else:
                    #print("No. n: ", nums1[mid])
                    n = nums1[mid]
                if mid+1==len1:
                    #print("No. n+1: ", nums2[left_index])
                    n_plus_1 = nums2[left_index]
                else:
                    if nums1[mid+1] > nums2[left_index]:
                        #print("No. n+1: ", nums2[left_index])
                        n_plus_1 = nums2[left_index]
                    else:
                        #print("No. n+1: ", nums1[mid+1])
                        n_plus_1 = nums1[mid+1]
        if (len1+len2) % 2 == 0: return (n+n_plus_1)/2
        else: return n_plus_1
        
        
print(
    Solution().findMedianSortedArrays(
    #nums1=[1,3], nums2=[2]
    #nums1=[2,3], nums2=[]
    #nums1=[1,3,5,7,9], nums2=[2,4,6,8]
    #nums1=[1,3,5,7], nums2=[2,4,6,8]
    #nums1=[2,4,6,8], nums2=[1,3,5,7]
    #nums1=[5,6,7,8], nums2=[1,2,3,4]
    #nums1=[4,6,7,8], nums2=[1,2,3,5]
    #nums1=[1,2,3,4], nums2=[5,6,7,8]
    nums1=[1], nums2=[2,3,4]
    )
)