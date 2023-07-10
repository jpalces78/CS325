def max_independent_set(nums):
    # create a dp table to find the max sum at index i
    dp = [0 for i in range(len(nums))]

    # set first index with value of first element
    dp[0] = nums[0]

    # set first index with value of second element
    dp[1] = nums[1]

    # loop from second third index to last
    for i in range(2, len(nums)):
        # store max of when either element is added to previous max or the max of the previous one
        # or the element alone or the previous max alone
        dp[i] = max(nums[i], nums[i] + dp[i - 2], dp[i - 2], dp[i - 1])

    # initialise i to last index
    i = len(nums) - 1

    # empty list to store the elements
    lis = []

    # while i is more than 2
    while (i > 1):
        # if max sum at current index is same as previous one decrease i by 1
        if dp[i] == dp[i - 1]:
            i -= 1

        # if current max is same as current element append to list reverse it and return
        elif dp[i] == nums[i]:
            lis.append(nums[i])
            lis.reverse()
            return lis

        # if current max is current element + previous max add is to list and decrease i by 2
        elif dp[i] == dp[i - 2] + nums[i]:
            lis.append(nums[i])
            i = i - 2

        # otherwise decrease i by 2 as the max sum is 2 index behind
        else:
            i = i - 2

    # if i is 0
    if i == 0:
        # if the current element is more than 0 or list length is 0 than append it to list
        if (nums[i] > 0 or len(lis) == 0):
            lis.append(nums[i])

    # if i is 1, find max of 0 and 1 index
    else:
        t = max(nums[0], nums[1])
        # if max of these two is more than 0 or the list is of 0 length append it to list
        if (t > 0 or len(lis) == 0):
            lis.append(t)

    # reverse the constructed list
    lis.reverse()

    # return list
    return lis

