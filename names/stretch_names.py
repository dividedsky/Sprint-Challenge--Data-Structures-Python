# stretch solution, not as efficient as BST solution
import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# sort the list, then do binary search on names_2
names_1.sort()


def find_name(names, target):
    mid = len(names) // 2
    if len(names) <= 1:
        return names[0] == target
    if names[mid] == target:
        duplicates.append(target)
    if names[mid] > target:
        find_name(names[:mid], target)
    else:
        find_name(names[mid:], target)


for name in names_2:
    find_name(names_1, name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
