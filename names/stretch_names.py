# stretch solution, not as efficient as BST solution
import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open("names_2.txt", "r")
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()


duplicates = []

# sort the list, then do binary search on names_2
names_1.sort()


def find_name(names, target):
    mid = len(names) // 2
    if len(names) <= 1:
        # if names[0] == target:
        #     duplicates.append(target)
        return
    if len(names) == 0:
        return
    if names[mid] == target:
        duplicates.append(target)
    if names[mid] > target:
        find_name(names[:mid], target)
    else:
        find_name(names[mid:], target)


with open("names_2.txt", "r") as f:
    for line in f:
        name = line.strip()
        find_name(names_1, name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
