import random
import matplotlib.pyplot as plt

def roll_one_die():
    return random.randint(1, 6)

def simulate_one_die_rolls(number_of_rolls):
    counts = {x: 0 for x in range(1, 7)}

    for i in range(number_of_rolls):
        roll = roll_one_die()
        counts[roll] += 1

    proportions = {}

    for side, count in counts.items():
        proportions[side] = count / number_of_rolls
    
    return counts, proportions

def simulate_two_dice_rolls(number_of_rolls):
    sums_count = {x: 0 for x in range(2, 13)}
    proportions = {}

    for i in range(number_of_rolls):
        die_one_roll = roll_one_die()
        die_two_roll = roll_one_die()
        dice_sum = die_one_roll + die_two_roll
        sums_count[dice_sum] += 1

    for key, value in sums_count.items():
        proportions[key] = value / number_of_rolls
        
    return sums_count, proportions

def plot_one_die_results(counts):
    plt.figure(figsize=(6, 4))
    x_values = counts.keys()
    y_values = counts.values()
    plt.bar(x_values, y_values, color="skyblue", edgecolor="black")

    plt.title("One Die Roll Frequencies")
    plt.xlabel("Die Face")
    plt.ylabel("Counts")

    plt.savefig('figures/one_die_frequencies.png', dpi=300, bbox_inches='tight')

    plt.show()

def plot_two_dice_results(sums_counts):
    plt.figure(figsize=(6, 4))
    x_values = sums_counts.keys()
    y_values = sums_counts.values()
    plt.bar(x_values, y_values, color="skyblue", edgecolor="black")

    plt.title("Two Dice Sum Frequencies")
    plt.xlabel("Dice Sums")
    plt.ylabel("Counts")

    plt.savefig("figures/two_dice_sum_frequencies.png", dpi=300, bbox_inches="tight")

    plt.show()

# Settings
sample_sizes = [10, 100, 1000, 10000]
main_simulation_size = 10000

one_die_counts_by_sample_size = []
one_die_proportions_by_sample_size = []

# Run one-die sample size comparison
for number in sample_sizes:
    counts, proportions = simulate_one_die_rolls(number)
    one_die_counts_by_sample_size.append(counts)
    one_die_proportions_by_sample_size.append(proportions)

# Run main one-die simulation for graph
main_one_die_counts, main_one_die_proportions = simulate_one_die_rolls(main_simulation_size)

# Run main two-dice simulation
sums_count, sums_proportions = simulate_two_dice_rolls(main_simulation_size)

# Calculate averages
one_die_average = sum(side * count for side, count in main_one_die_counts.items()) / main_simulation_size
two_dice_average = sum(dice_sum * count for dice_sum, count in sums_count.items()) / main_simulation_size

# Print results
print("---One Die Sample Size Comparison---")
for number, proportions in zip(sample_sizes, one_die_proportions_by_sample_size): 
    print(f"\nRolls: {number}")
    for roll, proportion in proportions.items():
        print(f"{roll}: {proportion:.3f}")

print("\n---Two Dice Simulation---")
print(f"Total Rolls: {main_simulation_size}\n")
for (k1, v1), (k2, v2) in zip(sums_count.items(), sums_proportions.items()):
    print(f"Sum {k1}: {v1} rolls, proportion: {v2:.3f}")

print("\n---Expected Value---")
print(f"Average One Die Roll: {one_die_average:.3f}")
print("Theoretical One Die Expected Value: 3.500\n")

print(f"Average Two Dice Sum: {two_dice_average:.3f}")
print("Theoretical Two Dice Expected Value: 7.000")
    
# Plot graphs
plot_one_die_results(main_one_die_counts)
plot_two_dice_results(sums_count)

# Conclusion
print("\n---Conclusion---")
print(
    "In the one-die simulation, each side appeared close to one-sixth of the time "
    "as the number of rolls increased. This shows that a fair die produces a roughly "
    "uniform distribution over many trials.\n"
)
print(
    "In the two-dice simulation, the sums were not equally likely. The sum 7 appeared "
    "most often because there are more combinations that produce 7 than sums like 2 or 12.\n"
)
print(
    "The simulated averages were close to the theoretical expected values: 3.5 for one die "
    "and 7.0 for two dice. This shows how long-run averages approach expected values."
)