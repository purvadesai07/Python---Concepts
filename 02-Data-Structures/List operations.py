nums = [10, 35, 27, 7, 62, 50, 70]
print("Original List: ", nums)
nums.append(5)
print("List after Adding element: ", nums)
nums.insert(2, 70)
print("List after Inserting element: ", nums)
nums.remove(70)
print("List after removing element: ", nums)
nums.pop(5)
print("List after popping elemt: ", nums)
del nums[0]
print("List after deleting element: ", nums)

numbers=[10, 67, 28, 30, 5, 16, 67]
numbers[2]= 25
print("List after modifying: ", numbers)
numbers.sort()
print("List in Ascending Order: ",numbers)
numbers.reverse()
print("List in Descending Order: ", numbers)
print("Maximum Number: ", max(numbers))
print("Minimum Number: ", min(numbers))
print("Sum of all Numbers: ", sum(numbers))
unique_list = list(set(numbers))
print("List after removing duplicates: ", unique_list)
print("SubList from 1 to 4: ", numbers[1:5])
print("Reverse List: ", numbers[ : : -1])
