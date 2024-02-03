#include <stdio.h>
#include <stdlib.h>

// brute-force solution!
// [status] : Passed!

int	*twoSum(int* nums, int numsSize, int target, int *returnSize)
{
    int *res = NULL;
	int	i = 0;
    int j = 0;
    res = malloc(sizeof(int) * (2));
	while (i < numsSize)
	{
        j = i + 1;
		while (j < numsSize)
		{
			if (target == nums[i] + nums[j])
			{
				res[0] = i;
				res[1] = j;
                *returnSize = 2;
				break ;
			}
			else
				j++;
		}
		i++;
	}
	return (res);
}

/*
int	main()
{
	int	nums[] = {10, 90, 20};
	print(nums, 3);
	printf("\n");
	int	*res = twoSum(nums, 3, 30);
	print(res, 2);
	return 0;
}
*/
