# Author: Abdul-Kudus Alhassan
# Date: 02/22/2023
# Purpose: defining a function for to integrate quick sort using partition function

# Partition sorts a section of a list based on specified indices
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]  # all other numbers based on this value and it is always the last element in the list
    while j < r:
        if compare_func(the_list[j], pivot):  # compares the values at the two indices based on the compare function
            i += 1  # incrementing the position before which all the elements are in their right positions

            # swapping  values
            temp = the_list[j]
            the_list[j] = the_list[i]
            the_list[i] = temp
            j += 1
        else:
            j += 1

    # swaping the pivot into it's right position
    temp = the_list[r]
    the_list[r] = the_list[i + 1]
    the_list[i + 1] = temp

    return i + 1


# QUICK SORT uses partition to sort and entire list by passing bits into partition function
def quicksort(the_list, p, r, compare_func):
    if p < r:
        res = partition(the_list, p, r, compare_func)  # uses partition to find the index of the pivot
        quicksort(the_list, p, res - 1, compare_func)  # call the function recursively
        quicksort(the_list, res + 1, r, compare_func)  # call the function recursively


# sort uses the quicksort to sort a list
def sort(the_list, compare_func):
    # Initializing the parameters for quicksort
    p = 0
    r = len(the_list) - 1

    quicksort(the_list, p, r, compare_func)
