import heapq

# Initialize a list with some values
values = [5, 1, 3, 7, 4, 2]

# Convert the list into a heap
heapq.heapify(values)

# Print the heap
print("Heap:", values)

# Add a new value to the heap
heapq.heappush(values, 6)

# Print the updated heap
print("Heap after push:", values)

# Remove and return the smallest element from the heap
smallest = heapq.heappop(values)

# Print the smallest element and the updated heap
print("Smallest element:", smallest)
print("Heap after pop:", values)

# Get the n smallest elements from the heap
n_smallest = heapq.nsmallest(3, values)

# Print the n smallest elements
print("Smallest 3 elements:", n_smallest)

# Get the n largest elements from the heap
n_largest = heapq.nlargest(2, values)

# Print the n largest elements
print("Largest 2 elements:", n_largest)