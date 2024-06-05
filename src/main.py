
"""
P(E) = n(E) / n(S)

Given an unknown configuration of coins, comprised of a random amount of coins, with a random number of coins of
different, random, coin values, calculate how many coins one must draw (from an imaginary pool) in order to reach a
random amount required.

P(X) = P(E) * P(E)

Expected outcome = P(E) * Value

The goal is to calculate the expected outcome

"""


def calculate_odds(desired_outcomes, total_possible_outcomes) -> float:
    return round(desired_outcomes / total_possible_outcomes, 2)


def calculate_base_rates(coins) -> dict:
    base_rates = dict()

    total_number_of_coins = sum(coins.values())

    for coin_value, coin_count in coins.items():
        base_rates[coin_value] = calculate_odds(coin_count, total_number_of_coins)

    return base_rates


'''def calculate_expected_value(coin_values, distribution) -> float:
    current_odds = float()

    for value, dist in zip(coin_values, distribution):
        current_odds *= value * dist

    return current_odds'''


def main():

    coins = {
        1: 2,
        2: 4,
    }

    base_rates = calculate_base_rates(coins)

    print(base_rates)


if __name__ == "__main__":
    main()
