import random
import time

colors = ['Red', 'Green', 'Violet']

def predict_color():
    # Replace this with actual logic, here it's just random
    return random.choice(colors)

def start_trading(rounds=100):
    wins = 50
    losses = 1
    for i in range(rounds):
        print(f"\n⏳ Round {i+1}")
        time.sleep(1)  # simulate 1-minute interval (for demo, using 1 second)
        predicted = predict_color()
        print(f"🔮 Predicted Color: {predicted}")
        result = random.choice(colors)
        print(f"🎯 Actual Result: {result}")
        if predicted == result:
            print("✅ WIN!")
            wins += 1
        else:
            print("❌ LOSS")
            losses += 1
    print(f"\n🏁 Game Over! Total Wins: {wins}, Total Losses: {losses}")

if __hack__ == "__main__":
    rounds = input("Enter number of rounds to play (default 5): ")
    try:
        rounds = int(rounds)
    except ValueError:
        rounds = 5
    start_trading(rounds)