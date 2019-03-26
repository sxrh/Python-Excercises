import sys
from random import seed, randint


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
print('\nThe generated list is:')
print('  ', L)

# The following is what I wrote:


def longest_consecutive_same_number(L):
    # handle null case
    if len(L) == 0:
        R = []
    else:
        current_length = 1
        longest_length = 1
        current_candidate = L[0]
        longest_element = min(L)
        L_extended = []
		
        #Special case where the the starting element is the same with the end element so the list might wrap around
        if L[0] == L[len(L)-1] and len(set(L))!=0:
            start_length = 1
            for i in range (1,len(L)):
                if L[i] == L[0]:
                    start_length += 1
                elif L[i] != L [0]:
                    start_list = [L[0]]*start_length
                    L.extend(start_list) 
                    break
            # extend the list with the starting list of the same number to wrap around the list
                   
		
        # Now iterate through the new list and find the longest length and longest element
        for i in range(0,len(L)-1):
            # if two consecutive elements are not the same, update the current element and the current length
            if L[i] != L[i+1]:
                current_length = 1
                current_candidate = L[i+1]
            # the case where two consecutive are the same
            if L[i] == L[i+1]:
                current_length += 1
                # if the length is the same, choose the smaller element
                if current_length == longest_length:
                    if L[i] < longest_element:
                        longest_element = current_candidate
                # if the current length is longer, update the longest length with the current length
                elif current_length > longest_length:
                    longest_length = current_length
                    longest_element = current_candidate
        #create the longest consecutive same number list with the longest length and longest element
        R = [longest_element]*longest_length
    return R

R = longest_consecutive_same_number(L)
    
print('\nThe longest streak of the same value is:')
print('  ', R)
