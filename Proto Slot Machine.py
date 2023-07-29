import random

def spin_slot_machine():
    symbols = ['🍒', '🍊', '🍋', '🍇', '🍓', '🍉']
    return [random.choice(symbols) for _ in range(3)]

def calculate_payout(spin_result, bet_amount):
    payout_table = {
        '🍒🍒🍒': 3,
        '🍊🍊🍊': 5,
        '🍋🍋🍋': 10,
        '🍇🍇🍇': 20,
        '🍓🍓🍓': 30,
        '🍉🍉🍉': 50
    }
    spin_str = ''.join(spin_result)
    if spin_str in payout_table:
        return bet_amount * payout_table[spin_str]
    else:
        return -bet_amount

def main():
    initial_money = 1000
    money = initial_money

    print("Welcome to the Slot Machine Game!")
    print(f"You have ${money} to play with.")

    while money > 0:
        print("==========")
        bet_amount = int(input("Place your bet (0 to quit): "))

        if bet_amount == 0:
            break

        if bet_amount > money:
            print("You don't have enough money to place that bet.")
            continue

        spin_result = spin_slot_machine()
        print(' '.join(spin_result))

        payout = calculate_payout(spin_result, bet_amount)
        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
        else:
            print(f"Sorry, you lost ${bet_amount}. Try again!")

        money += payout

    print("==========")
    print(f"Game over. You finished with ${money}.")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
