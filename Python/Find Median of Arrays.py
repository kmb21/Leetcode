def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if len(nums1) == 0 and len(nums2) == 0:
        return 0
    elif len(nums1) == 0 and len(nums2) == 1:
        return float(nums2[0])
    elif len(nums1) == 1 and len(nums2) == 0:   
        return float(nums1[0])
    newList = nums1 + nums2
    newList.sort()
    lenList = len(newList)
    if (lenList)%2 == 0:
        n = int(lenList/2)
        secondTerm = newList[n]
        firstTerm = newList[n-1]
        median = float((firstTerm + secondTerm)/2)
        return median            
        
    else:
        return float(newList[lenList//2])
    
