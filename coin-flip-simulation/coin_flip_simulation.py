import random
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

def generate_flips(number_of_flips):
    return random.choices(["heads", "tails"], k=number_of_flips)

def summarize_flips(sample_flips):
    heads_count = sample_flips.count("heads")
    tails_count = sample_flips.count("tails")
    proportion_heads = heads_count / len(sample_flips)

    return {
        "heads": heads_count,
        "tails": tails_count,
        "proportion_heads": proportion_heads
    }

def track_running_proportions(sample_flips):
    proportions = []
    heads = 0

    for index, side in enumerate(sample_flips):
        if side == "heads":
            heads += 1

        running_proportion = heads / (index + 1)
        proportions.append(running_proportion)

    return proportions


def find_max_streaks(sample_flips):
    current_heads_streak = 0
    max_heads_streak = 0

    current_tails_streak = 0
    max_tails_streak = 0

    for flip in sample_flips:
        if flip == "heads":
            current_tails_streak = 0
            current_heads_streak += 1
            max_heads_streak = max(max_heads_streak, current_heads_streak)
        else:
            current_heads_streak = 0
            current_tails_streak += 1
            max_tails_streak = max(max_tails_streak, current_tails_streak)

    return max_heads_streak, max_tails_streak


def plot_running_proportions(proportions, output_filename):
    flip_numbers = range(1, len(proportions) + 1)

    fig, ax = plt.subplots()
    ax.plot(flip_numbers, proportions)
    ax.axhline(0.5)

    ax.set_title(f"Running Proportion of Heads Over {len(proportions):,} Flips")
    ax.set_xlabel("Number of Flips")
    ax.set_ylabel("Proportion of Heads")
    ax.set_xlim(1, len(proportions))

    plt.savefig(FIGURES_DIR / output_filename, dpi=300, bbox_inches="tight")
    plt.show()


def plot_first_n_proportions(proportions, number_of_flips, output_filename):
    first_n_proportions = proportions[:number_of_flips]
    first_n_flip_numbers = range(1, len(first_n_proportions) + 1)

    fig, ax = plt.subplots()
    ax.plot(first_n_flip_numbers, first_n_proportions)
    ax.axhline(0.5)

    ax.set_title(f"Running Proportion of Heads: First {len(first_n_proportions):,} Flips")
    ax.set_xlabel("Number of Flips")
    ax.set_ylabel("Proportion of Heads")
    ax.set_xlim(1, len(first_n_proportions))

    plt.savefig(FIGURES_DIR / output_filename, dpi=300, bbox_inches="tight")
    plt.show()


def main():
    sample_sizes = [10, 100, 1000, 10000]
    running_simulation_size = 10000
    results = []

    main_flips = generate_flips(running_simulation_size)
    full_summary = summarize_flips(main_flips)

    for sample_size in sample_sizes:
        sample_flips = main_flips[:sample_size]
        summary = summarize_flips(sample_flips)
        results.append(summary)

    proportions = track_running_proportions(main_flips)

    max_heads_streak, max_tails_streak = find_max_streaks(main_flips)

    print("---Sample Size Comparison---")
    for sample_size, result in zip(sample_sizes, results):
        print(f"Flips: {sample_size}")
        print(f"Heads: {result['heads']}")
        print(f"Tails: {result['tails']}")
        print(f"Proportion Heads: {result['proportion_heads']:.3f}\n")

    print("---Running Proportions---")
    print(f"Total Flips: {running_simulation_size}")
    print(f"Total Heads: {full_summary['heads']}")
    print(f"Total Tails: {full_summary['tails']}")
    print(f"Final Proportion Heads: {full_summary['proportion_heads']:.3f}\n")

    checkpoints = [10, 100, 500, 1000, 10000]

    for checkpoint in checkpoints:
        print(f"After {checkpoint} flips: {proportions[checkpoint - 1]:.3f}")

    print()

    print("---Streak Analysis---")
    print(f"Total Flips: {running_simulation_size}")
    print(f"Longest Heads Streak: {max_heads_streak}")
    print(f"Longest Tails Streak: {max_tails_streak}\n")

    plot_running_proportions(
        proportions,
        "coin_flip_running_proportion_full.png",
    )

    plot_first_n_proportions(
    proportions,
    100,
    "coin_flip_running_proportion_first_100.png",
)

    print("---Conclusion---")
    print(
        "Small samples often produced proportions far from 0.5, but as the number\n"
        "of flips increased, the proportion of heads became more stable and moved\n"
        "closer to 0.5. The streak analysis also showed that long streaks can\n"
        "happen naturally even with a fair coin."
    )


if __name__ == "__main__":
    main()