"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """
    # Step 2: The first item is the current round (just `number`).
    li = []
    li.append(number)
    # Step 2: The second item is the round right after it (`number` plus 1).
    li.append(number + 1)
    # Step 3: The third item is the round after that (`number` plus 2).
    li.append(number + 2)
    # Step 5: Return that list (replace the `pass`).
    return li


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    # Concatenate the two lists together using the + operator
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    # Use the `in` operator to check if the number is in the list
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    # Step 1: Find the formula for Mean: Sum of all values / Number of values
    mean = sum(hand) / len(hand)
    # Return the mean value
    return mean


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    # Step 1: Calculate the True Average
    true_average = card_average(hand)
    # Step 2: Find A - First + last / 2
    A = (hand[0] + hand[-1]) / 2
    # Step 3 find B - Middle card
    B = hand[len(hand) // 2]
    # Return comparison
    return A == true_average or B == true_average


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """
    # Step 1: slice all the even slots and get average
    even_seats = hand[::2]    # Indexes 0, 2, 4, 6...
    even_average = sum(even_seats) / len(even_seats)
    # Step 2: Slice all odd slots and get average
    odd_seats = hand[1::2]    # Indexes 1, 3, 5, 7...
    odd_average = sum(odd_seats) / len(odd_seats)
    # Return Comparison
    return even_average == odd_average


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    # Constant to store jack number
    JACK = 11

    # Make a new list (works for tuples too) so the original hand is never changed
    new_hand = list(hand)
    # Only double if the hand is not empty and the last card is a Jack
    if new_hand and new_hand[-1] == JACK:
        new_hand[-1] = JACK * 2
    # Both outcomes return the same kind of thing: a list
    return new_hand