"""Write a python program to build a Binary Subset Builder using Python. They will learn how binary numbers can act as masks to select items from a list,
generate a power set, check individual bits using a bit probe, enumerate all subsets with two loops, and compare the bit difference between two numbers."""

items = [1,2,3,5]
n = len(items)
totalSubsets = 2**n

print("Power Set")
print(f"Items: {items}")
print(f"n: {n}")
print(f"Total Subsets: {totalSubsets}")
print()

print("Binary Mask Table")

mask = 0

while mask < totalSubsets:
    bit3 = (mask >> 3) & 1
    bit2 = (mask >> 2) & 1
    bit1 = (mask >> 1) & 1
    bit0 = mask & 1

    print(f"Mask: {mask}")
    print(f"[5], [3], [2], [1]: {bit3}, {bit2}, {bit1}, {bit0}")
    mask = mask + 1
print()

print("Bit Probe")

sampleMask = 4
print(f"Mask: {sampleMask}")
print(f"Binary: {bin(sampleMask)}")

j = 0

while j < n:
    probe = 1 << j

    if sampleMask & probe:
        print(f"Bit {items[j]} is set")
        print(f"Item {items[j]} is selected")
    else:
        print(f"Bit {items[j]} is set")
        print(f"Item {items[j]} is selected")

    j = j + 1
print()

print("All Subsets")

mask = 0

while mask < totalSubsets:
    subset = []

    j = 0
    while j < n:
        probe = 1 << j

        if mask & probe:
            subset.append(items[j])

        j = j + 1

    print(f"Mask: {mask}, Subset: {subset}")
    mask = mask + 1

print()

print("Bit Difference")


def bitDifference(a, b):
    differenceCount = 0

    while a > 0 or b > 0:
        lastBita = a & 1
        lastBitb = b & 1

        if lastBita != lastBitb:
            differenceCount += 1

        a = a >> 1
        b = b >> 1

    return differenceCount

a = 12
b = 26

print(f"{a} and {b}: {bitDifference(a, b)}")
print(f"Binary: {bin(a)[2:]}, {bin(b)[2:]}")