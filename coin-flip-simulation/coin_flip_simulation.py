import random
import matplotlib.pyplot as plt

def simulate_coin_flips(number_of_flips):
    heads = 0
    tails = 0

    for i in range(number_of_flips): 
        flip = random.choice(["heads", "tails"])
        if flip == "heads": 
            heads += 1
        else: 
            tails += 1
    
    proportion_heads = heads / number_of_flips

    return {"heads": heads, "tails": tails, "proportion": proportion_heads}

def track_running_proportions(number_of_flips):
    proportions = []
    heads = 0
    tails = 0

    for i in range(number_of_flips): 
        flip = random.choice(["heads", "tails"])
        flips = i + 1
        if flip == "heads": 
            heads += 1
        else: 
            tails += 1
        running_proportion = heads / flips
        proportions.append(running_proportion)
    
    final_proportion_heads = heads / number_of_flips

    summary = {
        "heads": heads,
        "tails": tails,
        "proportion": final_proportion_heads
    }

    return summary, proportions

def find_max_streaks(number_of_flips):
    heads_streak = 0
    max_heads_streak = 0
    tails_streak = 0
    max_tails_streak = 0

    for i in range(number_of_flips): 
        flip = random.choice(["heads", "tails"])
        if flip == "heads": 
            tails_streak = 0
            heads_streak += 1
            if heads_streak > max_heads_streak: 
                max_heads_streak = heads_streak
        else: 
            heads_streak = 0
            tails_streak += 1
            if tails_streak > max_tails_streak: 
                max_tails_streak = tails_streak 

    return max_heads_streak, max_tails_streak

# Settings
sample_sizes = [10, 100, 1000, 10000]
running_simulation_size = 10000
results = []

# Run experiments 
for number in sample_sizes:
    result = simulate_coin_flips(number)
    results.append(result)

summary, proportions = track_running_proportions(running_simulation_size)

max_heads_streak, max_tails_streak = find_max_streaks(running_simulation_size)

# Print results
print("---Sample Size Comparison---")
for sample_size, result in zip(sample_sizes, results):
    print(f"Flips: {sample_size}")
    print(f"Heads: {result['heads']}")
    print(f"Tails: {result['tails']}")
    print(f"Proportion Heads: {result['proportion']:.3f}\n")

print("---Running Proportions---")
print(f"Total Flips: {running_simulation_size}")
print(f"Total Heads: {summary['heads']}")
print(f"Total Tails: {summary['tails']}")
print(f"Final Proportion Heads: {summary['proportion']:.3f}\n")

print(f"After 10 flips: {proportions[9]:.3f}")
print(f"After 100 flips: {proportions[99]:.3f}")
print(f"After 500 flips: {proportions[499]:.3f}")
print(f"After 1000 flips: {proportions[999]:.3f}")
print(f"After 10000 flips: {proportions[9999]:.3f}\n")

print("---Streak Analysis---")
print(f"Total Flips: {running_simulation_size}")
print(f"Longest Heads Streak: {max_heads_streak}")
print(f"Longest Tails Streak: {max_tails_streak}\n")

# Plot graph

# Full running proportion graph
flip_numbers = range(1, len(proportions) + 1)

fig, ax = plt.subplots()
ax.plot(flip_numbers, proportions)
ax.axhline(0.5)

ax.set_title("Running Proportion of Heads Over 10,000 Flips")
ax.set_xlabel("Number of Flips")
ax.set_ylabel("Proportion of Heads")
ax.set_xlim(1, running_simulation_size)

plt.savefig("figures/coin_flip_running_proportion_full.png")
plt.show()

# Zoomed-in graph: first 100 flips
first_100_flip_numbers = range(1, 101)
first_100_proportions = proportions[:100]

fig, ax = plt.subplots()
ax.plot(first_100_flip_numbers, first_100_proportions)
ax.axhline(0.5)

ax.set_title("Running Proportion of Heads: First 100 Flips")
ax.set_xlabel("Number of Flips")
ax.set_ylabel("Proportion of Heads")
ax.set_xlim(1, 100)

plt.savefig("figures/coin_flip_running_proportion_first_100.png")
plt.show()

# Conclusion
print("---Conclusion---")
print("Small samples often produced proportions far from 0.5, but as the number of flips increased, \n" \
"the proportion of heads became more stable and moved closer to 0.5. The streak analysis also showed that \n" \
"long streaks can happen naturally even with a fair coin.")
