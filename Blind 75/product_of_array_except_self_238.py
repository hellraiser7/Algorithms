def product_except_self(nums):
    # can use division operation for first approach
    output = []
    product = getProduct(nums)
    for i in range(len(nums)):
        output.append(product//nums[i])
    return output

def getProduct(nums):
    product = 1
    for i in nums:
        product = product * i
    return product

if __name__ == "__main__":
    nums = [1,2,3,4]
    print("Product except self: ", product_except_self(nums))

