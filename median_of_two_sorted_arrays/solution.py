# Accepted

def findMedianSortedArrays(nums1, nums2):
        merged_arr = nums1 + nums2;
        merged_arr.sort();
        median = 0;
        if len(merged_arr) % 2 == 0:
            index1 = len(merged_arr) // 2 - 1;
            index2 = index1 + 1;
            median = merged_arr[index1] + merged_arr[index2];	
            median = median / 2;
        else: 
            index = len(merged_arr) // 2;		
            median = merged_arr[index];
        return median;


print(findMedianSortedArrays([1, 2], [3, 4]));
print(findMedianSortedArrays([1, 0, -1, 2], [9, 3, 4]));
print(findMedianSortedArrays([1, 2], [3, 4]));
