import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_2_bst = BSTNode("")

for name in names_2:
    names_2_bst.insert(name)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for n1 in names_1:
    if names_2_bst.contains(n1):
        duplicates.append(n1)


end_time = time.time()
print("BST Version:")
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time2 = time.time()

dupes = []
names2_set = set(names_2)

for n1 in names_1:
    # if n1 in names_2:
    if n1 in names2_set:
        dupes.append(n1)

end_time2 = time.time()

print("\n\n\nList Version:")
print(f"{len(dupes)} duplicates:\n\n{', '.join(dupes)}\n\n")
print(f"runtime: {end_time2 - start_time2} seconds")
