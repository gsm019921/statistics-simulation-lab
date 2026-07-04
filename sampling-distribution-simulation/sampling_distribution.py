import random
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).parent
FIGURES_DIR = BASE_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


def generate_die_sample_mean(sample_size):
    rolls = [random.randint(1, 6) for _ in range(sample_size)]
    sample_mean = sum(rolls) / len(rolls)
    return sample_mean


def generate_many_sample_means(sample_size, number_of_samples):
    sample_means = []

    for _ in range(number_of_samples):
        sample_means.append(generate_die_sample_mean(sample_size))

    return sample_means


def summarize_sample_means(sample_means):
    min_sample_mean = min(sample_means)
    max_sample_mean = max(sample_means)
    avg_sample_mean = sum(sample_means) / len(sample_means)
    range_sample_mean = max_sample_mean - min_sample_mean

    return min_sample_mean, max_sample_mean, avg_sample_mean, range_sample_mean


def plot_sample_means(sample_means, sample_size):
    plt.figure(figsize=(8, 5))

    plt.hist(
        sample_means,
        bins=20,
        range=(1, 6),
        weights=[1 / len(sample_means)] * len(sample_means),
        color="skyblue",
        edgecolor="black",
        alpha=0.7
    )

    plt.axvline(3.5, linestyle="--", label="True Mean = 3.5")

    plt.title(f"Sampling Distribution of Sample Means (n={sample_size})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Proportion")
    plt.xlim(1, 6)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend()

    plt.savefig(FIGURES_DIR / f"sample_means_n_{sample_size}.png", dpi=300, bbox_inches="tight")
    plt.close()


def compare_sample_sizes(sample_sizes, number_of_samples):
    sample_sizes_summaries = []

    for sample_size in sample_sizes:
        sample_size_summary = {}
        sample_size_summary["sample_size"] = sample_size

        means = generate_many_sample_means(sample_size, number_of_samples)
        plot_sample_means(means, sample_size)

        (
            sample_size_summary["min"],
            sample_size_summary["max"],
            sample_size_summary["avg"],
            sample_size_summary["range"],
        ) = summarize_sample_means(means)

        sample_sizes_summaries.append(sample_size_summary)

    for summary in sample_sizes_summaries:
        print(f"\nSample size: {summary['sample_size']}")
        print(f"Minimum sample mean: {summary['min']:.3f}")
        print(f"Maximum sample mean: {summary['max']:.3f}")
        print(f"Average sample mean: {summary['avg']:.3f}")
        print(f"Range of sample means: {summary['range']:.3f}")

    return sample_sizes_summaries


def main():
    sample_sizes = [2, 5, 10, 30, 100]
    number_of_samples = 1000

    compare_sample_sizes(sample_sizes, number_of_samples)


if __name__ == "__main__":
    main()