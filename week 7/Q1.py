''' Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's']. '''

def unique_letters():
    string = input("Enter a string: ")
    unique = list(set(string))
    # Sort the list without using sorted function
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if unique[i] > unique[j]:
                unique[i], unique[j] = unique[j], unique[i] # Swapping the i and j elements
    print("The unique letters in '%s' are: %s" % (string, unique))

unique_letters()