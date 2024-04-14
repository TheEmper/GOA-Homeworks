def find_last_even(numbers_list):
    for i in range(len(numbers_list) - 1, -1, -1): # first argument is where it starts from, second argument is where it stops and third is how many "steps" it takes
        if numbers_list[i] % 2 == 0: # The for loops goes over the list in a backwards motion, meaning it starts from the end(index[-1]) and goes over the whole list. The first even number that it finds, will be the last one in the list.
            return numbers_list[i]

print(find_last_even([1,2,3,4,5]))