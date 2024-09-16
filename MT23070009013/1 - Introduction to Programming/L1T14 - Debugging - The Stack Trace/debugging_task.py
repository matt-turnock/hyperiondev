# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # k didnt exist, this should have been key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": 'd\'oh!', # Add escape character for special character ' inside string
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, {'lisa', 'bart', 'homer'}) # Function expects two args, but four were being passed in.  Change these previous 3 values into a set using { }

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''