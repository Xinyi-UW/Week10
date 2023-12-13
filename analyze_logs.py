# analyze_logs.py
import pandas as pd
import matplotlib.pyplot as plt

def load_logs():
    return pd.read_csv('./logs/tictactoe_log.csv', header=None, names=['Mode', 'Winner'])

def generate_statistics(logs):
    #Counting wins per player
    win_counts = logs['Winner'].value_counts()

    #Bar chart of wins
    plt.bar(win_counts.index, win_counts.values)
    plt.title('Wins per Player')
    plt.xlabel('Player')
    plt.ylabel('Number of Wins')
    plt.savefig('wins_per_player.png')  # Save the plot as an image file
    plt.show()
    


if __name__ == '__main__':
    logs_data = load_logs()
    #3 interesting statistics
    #1. Wins per player
    win_counts = logs_data['Winner'].value_counts()
    print("Wins per Player:")
    print(win_counts)

    #2.Global Win Percentage
    total_games = len(logs_data)
    win_percentages = (logs_data['Winner'].value_counts() / total_games) * 100
    print("Global Win Percentage:")
    print(win_percentages)

    #3.Winning Streaks
    winning_streaks = logs_data.groupby('Winner').apply(lambda x: x['Winner'].eq(x['Winner'].shift(1)).cumsum())
    longest_streaks = winning_streaks.groupby('Winner').max()
    print("Longest Winning Streaks:")
    print(longest_streaks)


    generate_statistics(logs_data)
