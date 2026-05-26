#Monte Carlo Slot Machine Simulation(Casino)
# ---------------------------------------------------
# SLOT MACHINE CASINO GAME RULES
# ---------------------------------------------------
# 1. This project simulates a casino slot machine game.
# 2. The player spins a slot machine with 3 reels.
# 3. Each reel generates a random number from 1 to 3.
# 4. Every play/spin costs $1.
# 5. Winning Conditions:
#    a) If all 3 reels match:
#          - player wins $5
#          - this is called JACKPOT
#    b) If any 2 reels match:
#          - player wins $2
#    c) If no reels match:
#          - player wins $0
# 6. Profit/Loss Calculation:
#       profit = winnings - play_cost
#    Example:
#       winnings = $5
#       play cost = $1
#       profit = $4
# 7. The game is simulated many times using Monte Carlo Simulation.
# 8. Monte Carlo Simulation means:
#       - repeat random experiment many times
#       - estimate average outcome
# 9. The program tracks:
#       - total profit/loss
#       - average gain/loss per play
# 10. Final output shows:
#       expected average profit or loss for one play

import random
def play_slot_machine():
    reel1 = random.randint(1,3)
    reel2 = random.randint(1,3)
    reel3 = random.randint(1,3)

    if reel1 == reel2 == reel3:
        return 5
    elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        return 2
    else:
        return 0
    
def estimate_average(num_spins):
    total_profit = 0
    for i in range(num_spins):
        winnings = play_slot_machine()
        profit = winnings -1 
        total_profit += profit
    average_profit = total_profit / num_spins
    return average_profit

average = estimate_average(100000)
print(f"Estimated average profit per spin: ${average:.2f}")
