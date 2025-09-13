# Intermediate Sample 1: List processing with efficiency concerns
def find_duplicates(numbers):
    """Find duplicate numbers in a list - inefficient approach"""
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates

# Test the function
test_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]
result = find_duplicates(test_list)
print("Duplicates found:", result)

# More efficient approach using sets (for comparison):
# def find_duplicates_efficient(numbers):
#     seen = set()
#     duplicates = set()
#     for num in numbers:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)
#     return list(duplicates)
