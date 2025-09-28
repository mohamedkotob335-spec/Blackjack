import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    results = {
        "Draw":"Draw 😊 \n\n",
        "user_over": "You went over 21, Sorry 🫢 \n\n",
        "computer_over": "Computer went over 21, you win ⭐️ \n\n",
        "user_21": "You got a blackjack 😎👌🔥 \n\n",
        "computer_21": "Sorry, computer had a blackjack 😱 \n\n",
        "user_win": "You win 🥰 \n\n",
        "user_lose": "You lose 😢 \n\n",
    }

    if user_score == computer_score:
        return results["Draw"]
    elif user_score == 0:
        return results["user_21"]
    elif computer_score == 0:
        return results["computer_21"]
    elif user_score > 21:
        return results["user_over"]
    elif computer_score > 21:
        return results["computer_over"]
    elif user_score > computer_score:
        return results["user_win"]
    else:
        return results["user_lose"]

def blackjack_logo():
    print(r"""
██████   ██       █████   ██████  ██   ██      ██      ██   ██  █████   ██████ ██   ██
██   ██  ██      ██   ██ ██       ██   ██      ██      ██   ██ ██   ██ ██      ██  ██ 
██████   ██      ███████ ██   ███ ███████      ██      ███████ ███████ ██      █████  
██       ██      ██   ██ ██    ██ ██   ██      ██      ██   ██ ██   ██ ██      ██  ██ 
██       ███████ ██   ██  ██████  ██   ██      ███████ ██   ██ ██   ██  ██████ ██   ██
    """)

def froggy_logo():
    print(r"""
     __     __
    ( _\---/_ )
     /       \
    |         |
     \_/^\_/^/
      (_/ \_)
     Froggy Game 🐸
    """)

def snake_logo():
    print(r"""
      /^\/^\
    _|__|  O|
\/     /~   \_/ \
 \____|_________|
        \_______/
      Snake Game 🐍
    """)

def game():
    blackjack_logo()
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            break
        else:
            user_needs_another_card = input("Get another card? (Y/N): ").upper()
            if user_needs_another_card == 'Y':
                user_cards.append(deal_card())
            else:
                break

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# ========= القائمة الرئيسية =========
while True:
    clear_screen()
    print(r"""
   ____                       _             
  / ___| __ _ _ __ ___   __ _| | ___  _ __  
 | |  _ / _` | '_ ` _ \ / _` | |/ _ \| '_ \ 
 | |_| | (_| | | | | | | (_| | | (_) | | | |
  \____|\__,_|_| |_| |_|\__, |_|\___/|_| |_|
                        |___/               
         🎮 Welcome to Game Center 🎮
    """)
    
    choice = input("Choose a game to start .... \n\n1- Froggy \n2- Twenty one\n3- Snake \n4- Exit\n\nYour choice: ")

    if choice == "1":
        clear_screen()
        froggy_logo()
        print("\n🚧 Froggy is under construction 🚧\n")
        time.sleep(3)

    elif choice == "2":
        clear_screen()
        game()
        input("\nPress Enter to go back to menu...")

    elif choice == "3":
        clear_screen()
        snake_logo()
        print("\n🚧 Snake is under construction 🚧\n")
        time.sleep(3)

    elif choice == "4":
        clear_screen()
        print("\nExiting... Goodbye 👋\n")
        time.sleep(2)
        break

    else:
        print("\nInvalid choice, try again ❌\n")
        time.sleep(2)
