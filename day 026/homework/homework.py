# 1 Manual Sum Function: 

def manual_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

print(sum([1, 2, 3]))

# 2 Manual Max Function:

def manual_max(arr):
    maximum = 0
    for i in arr:
        for n in arr:
            if n > i:
                maximum = n

    return maximum

print(manual_max([1, 2, 3]))

# 3 Manual Min Function: 

def manual_min(arr):
    minimum = 1
    for i in arr:
        for n in arr:
            if n < i:
                minimum = n

    return minimum

print(manual_min([4, 2, 3]))

# 4 Manual len function:

def manual_len(arr):
    count = 0
    for i in arr:
        count += 1

    return count

print(manual_len([4, 5, 6 ,7 ,8]))

# 5 Manual reduce function:

