# Input
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]

# Process
if len(nums) < 2:
    print("List must contain at least two numbers.")
else:
    # Remove duplicates to avoid issues
    unique_nums = list(set(nums))
    
    if len(unique_nums) < 2:
        print("All elements are equal. No second largest exists.")
    else:
        unique_nums.sort(reverse=True)
        second_largest = unique_nums[1]
        print("Second Largest Number:", second_largest)
# Output
        # The output is printed directly in the process section above.