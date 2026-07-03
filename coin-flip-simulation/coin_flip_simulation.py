import random
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


def simulate_coin_flips(number_of_flips):
    heads = 0
    tails = 0

    for _ in range(number_of_flips):
        flip = random.choice(["heads", "tails"])

        if flip == "heads":
            heads += 1
        else:
            tails += 1

    proportion_heads = heads / number_of_flips

    return {
        "heads": heads,
        "tails": tails,
        "proportion_heads": proportion_heads,
    }


def track_running_proportions(number_of_flips):
    proportions = []
    heads = 0
    tails = 0

    for i in range(number_of_flips):
        flip = random.choice(["heads", "tails"])
        flip_number = i + 1

        if flip == "heads":
            heads += 1
        else:
            tails += 1

        running_proportion = heads / flip_number
        proportions.append(running_proportion)

    summary = {
        "heads": heads,
        "tails": tails,
        "proportion_heads": heads / number_of_flips,
    }

    return summary, proportions


def find_max_streaks(number_of_flips):
    current_heads_streak = 0
    max_heads_streak = 0

    current_tails_streak = 0
    max_tails_streak = 0

    for _ in range(number_of_flips):
        flip = random.choice(["heads", "tails"])

        if flip == "heads":
            current_tails_streak = 0
            current_heads_streak += 1
            max_heads_streak = max(max_heads_streak, current_heads_streak)
        else:
            current_heads_streak = 0
            current_tails_streak += 1
            max_tails_streak = max(max_tails_streak, current_tails_streak)

    return max_heads_streak, max_tails_streak


def plot_running_proportion(proportions, output_filename):
    flip_numbers = range(1, len(proportions) + 1)

    fig, ax = plt.subplots()
    ax.plot(flip_numbers, proportions)
    ax.axhline(0.5)

    ax.set_title("Running Proportion of Heads Over 10,000 Flips")
    ax.set_xlabel("Number of Flips")
    ax.set_ylabel("Proportion of Heads")
    ax.set_xlim(1, len(proportions))

    plt.savefig(FIGURES_DIR / output_filename, dpi=300, bbox_inches="tight")
    plt.show()


def plot_first_100_proportions(proportions, output_filename):
    first_100_proportions = proportions[:100]
    first_100_flip_numbers = range(1, len(first_100_proportions) + 1)

    fig, ax = plt.subplots()
    ax.plot(first_100_flip_numbers, first_100_proportions)
    ax.axhline(0.5)

    ax.set_title("Running Proportion of Heads: First 100 Flips")
    ax.set_xlabel("Number of Flips")
    ax.set_ylabel("Proportion of Heads")
    ax.set_xlim(1, len(first_100_proportions))

    plt.savefig(FIGURES_DIR / output_filename, dpi=300, bbox_inches="tight")
    plt.show()


def main():
    sample_sizes = [10, 100, 1000, 10000]
    running_simulation_size = 10000
    results = []

    for number_of_flips in sample_sizes:
        result = simulate_coin_flips(number_of_flips)
        results.append(result)

    summary, proportions = track_running_proportions(running_simulation_size)

    max_heads_streak, max_tails_streak = find_max_streaks(running_simulation_size)

    print("---Sample Size Comparison---")
    for sample_size, result in zip(sample_sizes, results):
        print(f"Flips: {sample_size}")
        print(f"Heads: {result['heads']}")
        print(f"Tails: {result['tails']}")
        print(f"Proportion Heads: {result['proportion_heads']:.3f}\n")

    print("---Running Proportions---")
    print(f"Total Flips: {running_simulation_size}")
    print(f"Total Heads: {summary['heads']}")
    print(f"Total Tails: {summary['tails']}")
    print(f"Final Proportion Heads: {summary['proportion_heads']:.3f}\n")

    checkpoints = [10, 100, 500, 1000, 10000]

    for checkpoint in checkpoints:
        print(f"After {checkpoint} flips: {proportions[checkpoint - 1]:.3f}")

    print()

    print("---Streak Analysis---")
    print(f"Total Flips: {running_simulation_size}")
    print(f"Longest Heads Streak: {max_heads_streak}")
    print(f"Longest Tails Streak: {max_tails_streak}\n")

    plot_running_proportion(
        proportions,
        "coin_flip_running_proportion_full.png",
    )

    plot_first_100_proportions(
        proportions,
        "coin_flip_running_proportion_first_100.png",
    )

    print("---Conclusion---")
    print(
        "Small samples often produced proportions far from 0.5, but as the number "
        "of flips increased, the proportion of heads became more stable and moved "
        "closer to 0.5. The streak analysis also showed that long streaks can "
        "happen naturally even with a fair coin."
    )


if __name__ == "__main__":
    main()