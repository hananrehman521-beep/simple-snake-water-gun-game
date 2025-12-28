import random

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

your_score = 0
computer_score = 0
rounds = 0

print("Snake 🐍 Water 💧 Gun 🔫 Game!")
print("Enter: 's' for Snake | 'w' for Water | 'g' for Gun | 'q' to Quit")

while True:
    youstr = input("\nYour move: ").lower()

    if youstr == 'q':
        print("\nExiting game...")
        break

    if youstr not in youDict:
        print("❌ Invalid input! Try again.")
        continue
    you = youDict[youstr]
    computer = random.choice([-1, 0, 1])

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == you:
        print("🤝 It's a draw!")
    elif (computer - you) in [-1, 2]:
        print("💀 You lose this round!")
        computer_score += 1
    else:
        print("🎉 You win this round!")
        your_score += 1

    rounds += 1
    print(f"Score => You: {your_score} | Computer: {computer_score}")

print("\n📊 Game Over!")
print(f"Total rounds played: {rounds}")
print(f"Your score: {your_score} | Computer score: {computer_score}")

if your_score > computer_score:
    print("🏆 Congratulations! You won the game.")
elif your_score < computer_score:
    print("😢 Better luck next time. Computer won.")
else:
    print("⚖ It's a tie overall.")
