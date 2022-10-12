#Author: Jay Dwivedi
#Course: SSW540

# Variables definition
user_input = ""
var_1 = ('o','ch', 's', 'sh', 'x', 'z', 'es')
# list of exceptions
vowels = ('a','e','i','o','u')
# list of vowels
error1 = "Only letters are accepted"
comma = ','
validity = False

# Ask the user to provide a list of nouns
def user_str():
    user_input = input("Please, enter a list of nouns to be transferred to plural separated by a space: ")
    return user_input

# Modify
def set_plural(str_in):
    lower_string = ""
    my_words = str_in.split(' ')
    for w in my_words:
        if not w[:-1].lower().endswith(vowels) and w[-1].lower() == 'y' :
            lower_string = lower_string + w[:-1] + "ies "
        elif w.lower().endswith(var_1):
            lower_string = lower_string + w + "es "
        else:
            lower_string = lower_string + w + "s "
    return lower_string

# Validate the user input
while not validity:
    user_input = user_str()
    for each in user_input:
        if not each.isnumeric() and each != comma:
            validity = True
        else:
            validity = False
            print(error1)

print(set_plural(user_input))