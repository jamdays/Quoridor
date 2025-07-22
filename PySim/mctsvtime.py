import pandas as pd
import re
import matplotlib.pyplot as plt

data = """MCTS with .9 vs .5 (4s): 27 vs 23
		MCTS with .5 vs .9 (4s): 24 vs 26
MCTS with .9 vs .5 (10s): 24 vs 26
		MCTS with .5 vs .9 (10s): 24 vs 26
MCTS with .9 vs .5 (20s): 21 vs 29
		MCTS with .5 vs .9 (20s): 22 vs 28
		MCTS with .9 vs .5 (40s): 21 vs 29
		MCTS with .5 vs .9 (40s): 21 vs 29
		MCTS with .9 vs .5 (80s): 15 vs 35
		MCTS with .5 vs .9 (80s): 25 vs 25"""

lines = data.strip().split('\n')

parsed_data = []

for line in lines:
    match = re.search(r'MCTS with \.([\d]+) vs \.([\d]+) \((\d+)s\): (\d+) vs (\d+)', line)
    if match:
        mcts_val1 = float("0." + match.group(1))
        mcts_val2 = float("0." + match.group(2))
        time = int(match.group(3))
        score1 = int(match.group(4))
        score2 = int(match.group(5))

        # MCTS as player 1
        parsed_data.append({
            'Time': time,
            'MCTS_Player_Type': 'p1',
            'MCTS_Value': mcts_val1,
            'Score': score1
        })
        # MCTS as player 2
        parsed_data.append({
            'Time': time,
            'MCTS_Player_Type': 'p2',
            'MCTS_Value': mcts_val2,
            'Score': score2
        })

df = pd.DataFrame(parsed_data)

# Calculate the mean score for each combination of Time, MCTS_Player_Type, and MCTS_Value
df_pivot = df.pivot_table(index='Time', columns=['MCTS_Player_Type', 'MCTS_Value'], values='Score', aggfunc='mean')

# Plotting the data
plt.figure(figsize=(12, 7))

# Define colors for p1 and p2, with slight variations for the values
colors = {
    ('p1', 0.5): 'skyblue',
    ('p1', 0.9): 'steelblue',
    ('p2', 0.5): 'lightcoral',
    ('p2', 0.9): 'firebrick'
}

for (player_type, mcts_value) in df_pivot.columns:
    label = f'MCTS {player_type} {mcts_value}'
    plt.plot(df_pivot.index, df_pivot[(player_type, mcts_value)], marker='o', label=label, color=colors[(player_type, mcts_value)])

plt.title('MCTS Performance by Player Type and Value Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Average Score')
plt.xticks(df_pivot.index)
plt.grid(True)
plt.legend(title='MCTS Configuration')
plt.tight_layout()
plt.savefig('../TestingGraphs/mcts_performance.png')

print("The data has been plotted and saved as 'mcts_performance.png'.")
