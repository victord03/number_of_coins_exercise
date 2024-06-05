
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


def calculate_expected_value():
    ...


def main():
    ...


if __name__ == "__main__":

    printing = True

    if printing:
        print(main())
