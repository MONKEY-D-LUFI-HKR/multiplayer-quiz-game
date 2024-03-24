import time

def ask_question(question, correct_answer):
    answer = input(question + " ")
    if answer.lower() == correct_answer.lower():
        print("Well done! You're correct :) +2 points!")
        return 2
    else:
        print("Incorrect! The correct answer is:", correct_answer)
        return 0

print("Welcome to the Computer Quiz!")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time! Goodbye.")
    quit()

while True:
    players = input("Okay! Enter the number of players please (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2 and 4.")
    else:
        print("Invalid input! Please enter a number between 2 and 4.")

max_score = 8
player_scores = [0] * players

questions = [
    ("What does CPU stand for?", "Central Processing Unit"),
    ("What does GPU stand for?", "Graphics Processing Unit"),
    ("What does RAM stand for?", "Random Access Memory"),
    ("What does PSU stand for?", "Power Supply Unit"),
    ("Which part of the computer shows you information from the computer?", "Monitor"),
    ("Which part of the computer is the brain of the computer?", "CPU")
]

for question, correct_answer in questions:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, ", it's your turn!")
        print("Your current score is:", player_scores[player_idx], "\n")
        time.sleep(1)  # Adds a small delay for better pacing
        current_score = ask_question(question, correct_answer)
        player_scores[player_idx] += current_score
        time.sleep(1)  # Adds a small delay for better pacing

print("\n--- Results ---")
for idx, score in enumerate(player_scores):
    print("Player", idx + 1, "scored:", score)

winning_score = max(player_scores)
winning_players = [idx + 1 for idx, score in enumerate(player_scores) if score == winning_score]

if len(winning_players) == 1:
    print("\nPlayer", winning_players[0], "is the winner with a score of", winning_score, "points!")
else:
    print("\nIt's a tie between players:", ", ".join(map(str, winning_players)), "each with", winning_score, "points!")
