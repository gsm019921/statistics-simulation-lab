import random
import matplotlib.pyplot as plt

def roll_one_die():
    roll = random.choice(range(1, 7))
    return roll

def simulate_one_die_rolls(number_of_rolls):
    proportions = {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
    }

    counts = {
        "side_one": 0,
        "side_two": 0,  
        "side_three": 0,
        "side_four": 0,
        "side_five": 0,  
        "side_six": 0,
    }

    for i in range(number_of_rolls):
        roll = roll_one_die()

        if roll == 1:
            counts["side_one"] += 1
        if roll == 2:
            counts["side_two"] += 1
        if roll == 3:
            counts["side_three"] += 1
        if roll == 4:
            counts["side_four"] += 1
        if roll == 5:
            counts["side_five"] += 1
        if roll == 6:
            counts["side_six"] += 1

    proportions["1"].append(counts["side_one"] / number_of_rolls)
    proportions["2"].append(counts["side_two"] / number_of_rolls)
    proportions["3"].append(counts["side_three"] / number_of_rolls)
    proportions["4"].append(counts["side_four"] / number_of_rolls)
    proportions["5"].append(counts["side_five"] / number_of_rolls)
    proportions["6"].append(counts["side_six"] / number_of_rolls)
    
    return counts, proportions

def simulate_two_dice_rolls(number_of_rolls):
    sums = []
    sums_count = {}
    proportions = {str(x): [] for x in range(2, 12)}
    rolls = 0

    for i in range(number_of_rolls):
        die_one_roll = roll_one_die()
        die_two_roll = roll_one_die()
        rolls += 1
        dice_sum = die_one_roll + die_two_roll
        if dice_sum not in sums:
            sums.append(dice_sum)
            sums_count[str(dice_sum)] = 1
        else: 
            sums_count[str(dice_sum)] += 1
        
        for key, value in proportions.items():
            if sums_count[str(dice_sum)] not in sums_count: 
                proportions[key].append(0)
            else: 
                proportions[key].append(sums_count[str(dice_sum)] / rolls)
        
    return sums_count, proportions

def plot_one_die_results():
    ...

def plot_two_dice_results():
    ...

# Settings
sample_sizes = [10, 100, 1000, 10000]
main_simulation_size = 10000
one_die_counts = []
one_die_proportions = []


# Run simulations
for number in sample_sizes:
    counts, proportions = simulate_one_die_rolls(number)
    one_die_counts.append(counts)
    one_die_proportions.append(proportions)

# Print results
print("---Sample Size Comparison: One Die---")
for number in sample_sizes: 
    print(f"Rolls: {number}")
    for roll, proportion in proportions.items():
        print(f"{roll}: {proportion:.3f}")

# Plot graphs
...

# Conclusion
...