#include <stdio.h>
#include <stdlib.h>


/*** 	

	explanation :	https://www.youtube.com/watch?v=luicuNOBTAI

****/

int	*two_sum(int *nums, int numsSize, int target, int *returnSize)
{
    // Create a dictionary (hash table) to store numbers and their indices
    int	*seen = (int*)malloc(numsSize * sizeof(int) * 2);  // Assuming each number appears at most twice
    *returnSize = 0;

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];

        // Check if the complement exists in the dictionary
        for (int j = 0; j < *returnSize; j += 2) {
            if (seen[j] == complement) {
                int* result = (int*)malloc(2 * sizeof(int));
                result[0] = seen[j + 1];
                result[1] = i;
                free(seen);
                *returnSize = 2;
                return result;
            }
        }

        // Add the current number and its index to the dictionary
        seen[*returnSize] = nums[i];
        seen[*returnSize + 1] = i;
        *returnSize += 2;
    }

    free(seen);
    *returnSize = 0;  // If no solution is found
    return NULL;
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;

    int* result = twoSum(nums, sizeof(nums) / sizeof(nums[0]), target, &returnSize);

    if (returnSize == 2) {
        printf("Indices: %d, %d\n", result[0], result[1]);
        free(result);  // Don't forget to free the allocated memory
    } else {
        printf("No solution found.\n");
    }

    return 0;
}

