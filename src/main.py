import math
from random import randint as rnd

'''
1) Input

amount_required: float  # total amount to retrieve 
number_of_coin_types: int  # Number of different coin types; 1 <= N <= 1_000
number_of_available_coins_per_type: int  # Number of coins of each type. Space separated values; 1 <= nbc <= 1_000
vales_of_each_coin: int  # Value of each type of coin. Space separated values; 1 <= cv <= 1_000


2) Examples

8
1
5
6

8 is the amount desired
1 is the number of coin types in the pocket
5 is the number of coins per coin type present in the pocket
6 is the values of each coin type respectively

A more complex scenario is

8
3
1, 2, 3
4, 3, 1

3) In plain English 

There are 3 different coins. 4 of them have a of value 1, 3 of them a value 2, and 1 of them a value 
of 3.

The objective is to calculate, for each and any configuration, how many coins have to be drawn in order to ensure 
having a total value above and as close as possible to the 'required amount' (the top value).


4) Expected output

result: int 

It will be the number of coins needed to be pulled out to satisfy the objective. Return -1 if there is no solution to
the problem (cases in the actual code)
'''


def format_input(generated_input) -> list:

    list_of_lines = generated_input.split('\n')
    list_of_lines_copy = list_of_lines.copy()

    # removes trailing spaces from each line
    for index, line in enumerate(list_of_lines_copy):
        list_of_lines[index] = line.strip()

    list_of_lines_copy = list_of_lines.copy()

    # converts the items inside the list, which are strings, to integers. Iteration for a flat list.
    if list_of_lines_copy[1] == '1':
        list_of_lines = list(map(int, list_of_lines_copy))
        return list_of_lines

    # converts the items inside the list, which are strings, to integers. Iteration for nested lists.
    else:

        for index, item in enumerate(list_of_lines_copy):
            number_of_items = len(item.split(','))

            if number_of_items == 1:
                list_of_lines[index] = int(item)
            else:
                list_of_lines[index] = list(map(int, item.split(',')))

    return list_of_lines

def has_solution(values_and_coins: dict, amount_required: int) -> bool:
    """If the amount required cannot be reached by the total amount of coins, the problem has no solution."""

    total = int()

    for value, number_of_coins in values_and_coins.items():
        total += value * number_of_coins

    return amount_required <= total

def roll_random_number(upper_bound, lower_bound=0) -> int:
    return rnd(lower_bound, upper_bound)

def is_within_bounds(n) -> bool:
    """1 <= N <= 1_000 """
    if n < 1 or n > 1_000:
        return False
    return True

def create_values_and_coins_dict(values, number_of_coins_of_each_type, number_of_different_coins=1, debug=False) -> dict:

    coins_dict = dict()

    if debug:
        print(f'\nnumber_of_different_coins: {number_of_different_coins}')
        print(f'number_of_coins_of_each_type: {number_of_coins_of_each_type}')
        print(f'values: {values}\n')

    if number_of_different_coins != 1:
        for coins, values in zip(number_of_coins_of_each_type, values):

            if debug:
                print(f'\nnumber of coins for this coin: {coins}, value of these coins: {values}\n')
            coins_dict[values] = coins
    else:
        coins_dict[values] = number_of_coins_of_each_type

    return coins_dict

def main(debug=False) -> int:

    one_coin = '''8
    1
    5
    6'''

    three_types_of_coins = '''5
    3
    3, 3, 1
    1, 2, 3'''

    initial_input = format_input(three_types_of_coins)
    amount_required, number_of_types, number_of_coins_per_type, values = initial_input

    current_amount = int()
    result = int()

    coins_dict = create_values_and_coins_dict(
        values=values,
        number_of_coins_of_each_type=number_of_coins_per_type,
        number_of_different_coins=number_of_types,
    )

    # print(coins_dict)
    # print(initial_input)

    run = True

    if run:
        # logic and requirements checks
        solution_exists = has_solution(coins_dict, amount_required)
        coin_check = all(list(is_within_bounds(number) for number in number_of_coins_per_type))
        coin_types_check = is_within_bounds(number_of_types)
        coin_values_check = all(list(is_within_bounds(number) for number in values))

        # if any of the logic or requirements fail, -1 is returned immediately.
        if not solution_exists or not coin_types_check or not coin_check or not coin_values_check:
            return -1

        # if there is only one type of coins, the result is basically total amount / coin value, rounded up
        if number_of_types == 1:
            return math.ceil(amount_required / values)

        # if none of the forks apply, we calculate the result
        else:

            if debug:
                print(coins_dict)

            while amount_required > current_amount:

                if debug:
                    print(f'\namount_required: {amount_required}')
                    print(f'current_amount: {current_amount}\n')

                # keeps track of how many different coin types are currently available to draw from
                types_available = number_of_types - 1

                # rolls a random coin type
                random_roll = roll_random_number(upper_bound=types_available)

                if debug:
                    print(f'random roll: {random_roll}')

                # converts the roll to a corresponding key from the coin_dict
                roll_correspondence_to_dict_key = list(coins_dict.keys())[random_roll]

                if debug:
                    print(f'roll_correspondence_to_dict_key: {roll_correspondence_to_dict_key}')
                    print(f'amount of coins of that type available (before): {coins_dict[roll_correspondence_to_dict_key]}')

                current_amount += list(coins_dict.keys())[random_roll]

                if debug:
                    print(f'amount added to the current amount: {list(coins_dict.keys())[random_roll]}')

                # decreases the pool of the specific coin by 1
                coins_dict[roll_correspondence_to_dict_key] -= 1

                if debug:
                    print(f'amount of coins of that type available (after): {coins_dict[roll_correspondence_to_dict_key]}')

                # if the available number of coins for a given coin value inside the dict is 0, remove the key and
                # decrease the type of available coins by 1 to also decrease the roll upper bound
                if coins_dict[roll_correspondence_to_dict_key] < 1:

                    if debug:
                        print(f'Coins with value {list(coins_dict.keys())[random_roll]} will be rendered unavailable. ({coins_dict[roll_correspondence_to_dict_key]})')

                    coins_dict.pop(roll_correspondence_to_dict_key)
                    types_available -= 1

                    if debug:
                        print(coins_dict)
                        print(f'number of type of coins remaining available: {types_available}')

                result += 1

            return result

if __name__ == "__main__":

    printing = True

    if printing:
        print(main())
