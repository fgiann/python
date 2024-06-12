"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

# Define the preparation time for each layer
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(timeInOven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - timeInOven


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers of the lasagna.
    :return: int - preparation time of the lasagna, based on the number of layers and 'PREPARATION_TIME'.

    Function that takes the number of layers of the lasagna as
    an argument and returns how many minutes the preparation requires
    based on the `PREPARATION_TIME`.
    """

    return number_of_layers * PREPARATION_TIME


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time from the beginning of the preparation.

    :param number_of_layers: int - number of layers of the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total number of minutes of cook.

    Function that takes the layers of the lasagna and the actual minutes the lasagna has been in the oven as
    an argument and returns the total time of cook.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time;