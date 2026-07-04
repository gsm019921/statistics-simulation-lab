import random
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


def roll_one_die():
    return random.randint(1, 6)


def generate_one_die_rolls(number_of_rolls):
    rolls = []

    for _ in range(number_of_rolls):
        rolls.append(roll_one_die())

    return rolls


def generate_two_dice_sums(number_of_rolls):
    sums = []

    for _ in range(number_of_rolls):
        dice_sum = roll_one_die() + roll_one_die()
        sums.append(dice_sum)

    return sums


def summarize_outcomes(outcomes, possible_values):
    counts = {value: 0 for value in possible_values}

    for outcome in outcomes:
        counts[outcome] += 1

    proportions = {}

    for outcome, count in counts.items():
        proportions[outcome] = count / len(outcomes)

    return counts, proportions


def calculate_average(outcomes):
    return sum(outcomes) / len(outcomes)


def plot_one_die_results(counts, output_filename):
    fig, ax = plt.subplots(figsize=(6, 4))

    x_values = counts.keys()
    y_values = counts.values()

    ax.bar(x_values, y_values, color="skyblue", edgecolor="black")

    ax.set_title("One Die Roll Frequencies")
    ax.set_xlabel("Die Face")
    ax.set_ylabel("Counts")

    plt.savefig(FIGURES_DIR / output_filename, dpi=300, bbox_inches="tight")
    plt.show()


def plot_two_dice_results(counts, output_filename):
    fig, ax = plt.subplots(figsize=(6, 4))

    x_values = counts.keys()
    y_values = counts.values()

    ax.bar(x_values, y_values, color="skyblue", edgecolor="black")

    ax.set_title("Two Dice Sum Frequencies")
    ax.set_xlabel("Dice Sum")
    ax.set_ylabel("Counts")

    plt.savefig(FIGURES_DIR / output_filename, dpi=300, bbox_inches="tight")
    plt.show()


def main():
    sample_sizes = [10, 100, 1000, 10000]
    main_simulation_size = 10000

    one_die_possible_values = range(1, 7)
    two_dice_possible_values = range(2, 13)

    one_die_results_by_sample_size = []

    one_die_rolls = generate_one_die_rolls(main_simulation_size)
    two_dice_sums = generate_two_dice_sums(main_simulation_size)

    for sample_size in sample_sizes:
        sample_rolls = one_die_rolls[:sample_size]
        counts, proportions = summarize_outcomes(
            sample_rolls,
            one_die_possible_values,
        )

        result = {
            "sample_size": sample_size,
            "counts": counts,
            "proportions": proportions,
        }

        one_die_results_by_sample_size.append(result)

    main_one_die_counts, main_one_die_proportions = summarize_outcomes(
        one_die_rolls,
        one_die_possible_values,
    )

    two_dice_counts, two_dice_proportions = summarize_outcomes(
        two_dice_sums,
        two_dice_possible_values,
    )

    one_die_average = calculate_average(one_die_rolls)
    two_dice_average = calculate_average(two_dice_sums)

    print("---One Die Sample Size Comparison---")

    for result in one_die_results_by_sample_size:
        print(f"\nRolls: {result['sample_size']}")

        for side, proportion in result["proportions"].items():
            print(f"{side}: {proportion:.3f}")

    print("\n---Two Dice Simulation---")
    print(f"Total Rolls: {main_simulation_size}\n")

    for dice_sum in two_dice_possible_values:
        count = two_dice_counts[dice_sum]
        proportion = two_dice_proportions[dice_sum]

        print(f"Sum {dice_sum}: {count} rolls, proportion: {proportion:.3f}")

    print("\n---Expected Value---")
    print(f"Average One Die Roll: {one_die_average:.3f}")
    print("Theoretical One Die Expected Value: 3.500\n")

    print(f"Average Two Dice Sum: {two_dice_average:.3f}")
    print("Theoretical Two Dice Expected Value: 7.000")

    plot_one_die_results(
        main_one_die_counts,
        "one_die_frequencies.png",
    )

    plot_two_dice_results(
        two_dice_counts,
        "two_dice_sum_frequencies.png",
    )

    print("\n---Conclusion---")
    print(
        "In the one-die simulation, each side appeared close to one-sixth of the time\n"
        "as the number of rolls increased. This shows that a fair die produces a roughly\n"
        "uniform distribution over many trials.\n"
    )

    print(
        "In the two-dice simulation, the sums were not equally likely. The sum 7 appeared\n"
        "most often because there are more combinations that produce 7 than sums like\n"
        "2 or 12.\n"
    )

    print(
        "The simulated averages were close to the theoretical expected values: 3.5 for\n"
        "one die and 7.0 for two dice. This shows how long-run averages approach\n"
        "expected values."
    )


if __name__ == "__main__":
    main()