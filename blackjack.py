import random


def blackjack():
    # List of possible card values
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Initializing player and dealer hands
    player_cards = [random.choice(cards), random.choice(cards)]
    dealer_card_1 = random.choice(cards)
    dealer_card_2 = random.choice(cards)
    dealer_cards = [dealer_card_1, dealer_card_2]
    if sum(player_cards) == 21 and sum(dealer_cards) == 21:
        print("Blackjack! Draw")
    elif sum(player_cards) == 21 and sum(dealer_cards) != 21:
        print("Blackjack! You win!")
    elif sum(player_cards) != 21 and sum(dealer_cards) == 21:
        print("Blackjack! Dealer wins")

    player_game = True

    while player_game:
        print(f"Your cards: {player_cards}, dealer's visible card: {dealer_card_1} and [X]")
        summa_p = sum(player_cards)
        take_another_card = input("Do you want another card? y or n? ").strip().lower()

        if take_another_card == "y":
            player_cards.append(random.choice(cards))  # Player takes another card
            summa_p = sum(player_cards)
            if summa_p > 21:
                for i in range(len(player_cards)):
                    if player_cards[i] == 11:
                        player_cards[i] = 1
                        summa_p = sum(player_cards)
                        break
                if summa_p > 21:  #  Still over 21? Player loses immediately
                    print(f"\nYour final hand: {player_cards}, final score: {summa_p}")
                    print("You lose! Bust!")  # Player loses instantly
                    return  #  **Stop the function immediately**



        else:
            player_game = False  # Exit the loop

    dealer_game = True
    while dealer_game:

        # Calculate dealer's total first
        summa_d = sum(dealer_cards)

        # Dealer keeps taking cards until reaching at least 17
        if summa_d <= 16:
            new_card = random.choice(cards)
            dealer_cards.append(new_card)
            summa_d += new_card  # Update dealer's sum correctly

        elif summa_d > 21:
            for i in range(len(dealer_cards)):
                if dealer_cards[i] == 11:
                    dealer_cards[i] = 1
                    summa_d = sum(dealer_cards)
                    break
            if summa_d > 21:  # Still over 21? Dealer loses
                dealer_game = False
        else:
            dealer_game = False

    # Calculate final player sum

    print(f"\nYour final hand: {player_cards}, final score: {summa_p}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {summa_d}")

    if summa_d > summa_p:
        print("You lose!")
    elif summa_p > summa_d:
        print("You win!")
    else:
        print("Draw")

    new_game=input("Do you want to play again? y on n?")
    if new_game=="y":
        blackjack()

blackjack()

