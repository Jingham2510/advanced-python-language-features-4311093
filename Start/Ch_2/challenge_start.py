# Example file for Advanced Python: Language Features by Joe Marini
# Challenge solution file for Advanced Functions

# Challenge:
# Write a function that performs the following actions:
# 1: accepts a variable number of strings and numbers. Other types ignored
# 2: accepts a keyword-only argument to return a unique-only result
# 3: combines all the arguments into a single string
# 4: returns a string containing all arguments combined as one string
# 5: Has a docstring that explains how it works
# If the unique-only argument is True (default False), then the result
# combined string will not contain any duplicate characters


def string_combiner(*args, unique=False):
    """
    string_combiner(*args, unique=False)
    Arguments:
    *args: The variable argument 
    unique: A boolean to determine whether the result can contain duplicate characters

    Combines all the provided argument characters together
    """

    result = ""

    # YOUR CODE HERE
    #Go through all the arguments
    for arg in args:
        #check the type of the argument - ignore nonstrings or nonints
        if (typ := type(arg)) is int or typ is str:
            #Check if unique
            if unique:
                #Check to ensure the character isnt in results
                for char in str(arg):
                    if char in result:
                        pass
                    else:
                        result = result + str(char)

            else:
                result = result + str(arg)



    return result


# test code:
print(string_combiner.__doc__)
output = string_combiner("This", "is", 1, "test", "string!", unique=False)
print(output)
output = string_combiner("This", "is", 1, "test", "string!", unique=True)
print(output)
output = string_combiner("This", "is", 1, True, "string!", unique=False)
print(output)
output = string_combiner("This", "is", [1, 2], "string!", unique=False)
print(output)
