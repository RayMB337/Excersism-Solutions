"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the PreparationTime in Minutes

    Parameters:
        number_of_layers (int): number of lasagna layers

    Returns:
        int: how many minutes spent making the layers

    function that takes the number_of_layers you want to add to the lasagna and returns the number of minutes spent making it.
    """    
    
    return number_of_layers * PREPARATION_TIME



#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the number of minutes taken to prepare the lasagna

    Parameters:
        number_of_layers (int): Number of Lasagna Layers
        elapsed_bake_time (int): Number of minutes the lsagna has spent in the oven.

    Returns:
        int: Number of minutes in kitchen preparing lasagna

    function takes two parameters number_of_layers and elapsed_bake_time to calculate how much time it takes to prepare a lasagna.
    """    
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
