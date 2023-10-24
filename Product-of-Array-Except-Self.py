# this is leet code problem solution (238)

def productExceptSelf(nums):
    n = len(nums)
    prefix_product = [1] * n
    suffix_product = [1] * n
    result = [0] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        prefix_product[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        suffix_product[i] = suffix
        suffix *= nums[i]

    # Calculate result
    for i in range(n):
        result[i] = prefix_product[i] * suffix_product[i]

    return result

# Example usage:
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]
