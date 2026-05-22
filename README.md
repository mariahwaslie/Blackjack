# Blackjack Game in Python

A simple command-line Blackjack game built in Python using object-oriented programming concepts. This project simulates a basic Blackjack game between a player and a dealer, including betting, card dealing, score calculation, and dealer AI logic.

---

## Features

- Creates and shuffles a full 52-card deck
- Player betting system
- Dealer and player card dealing
- Hit or Stay gameplay
- Ace value selection (1 or 11)
- Dealer automatic drawing logic
- Win/Loss detection
- Object-oriented design using classes

---

## Technologies Used

- Python 3
- Built-in `random` module

---

## How the Game Works

1. The player places a bet.
2. A shuffled deck is created.
3. The player and dealer each receive 2 cards.
4. The player chooses:
   - **Hit** → draw another card
   - **Stay** → end their turn
5. The dealer automatically draws cards until stopping conditions are met.
6. The winner is determined based on Blackjack rules.

---

## Classes Overview

### `BankAccount`
Stores dealer and player balances.

### `Bet`
Handles user betting input.

### `Deck`
Creates and shuffles the deck of cards.

### `Dealer_player_cards`
Deals starting cards to the player and dealer.

### `Player_One`
Handles:
- Player scoring
- Ace handling
- Hit/Stay decisions
- Bust checking

### `Dealer`
Controls dealer logic and automatic card drawing.

---

## Example Gameplay

```bash
Place your bet $50

your cards ['Hearts 10', 'Spades Ace']
dealer card Clubs 7

do you want your Ace to be worth 1 point or 11 points? 11

21

Hit or Stay: Stay

18

the player has won $50
```

---

## Running the Program

1. Make sure Python 3 is installed.

2. Save the file as:

```bash
blackjack.py
```

3. Run the program:

```bash
python blackjack.py
```

---

## Project Structure

```bash
blackjack.py
README.md
```

---

## Blackjack Rules Used

- Number cards are worth their face value
- Face cards (King, Queen, Jack) are worth 10
- Aces can be worth 1 or 11
- Going over 21 results in a Bust
- Dealer draws automatically based on score logic

---

## Known Issues / Future Improvements

- Some bust-checking logic is marked with `FIX ME`
- Dealer logic could be improved to better follow official Blackjack rules
- Input validation is limited
- Betting balances are not permanently stored
- Multiplayer support could be added
- GUI version could be implemented using:
  - Tkinter
  - Pygame
  - PyQt

---

## Concepts Demonstrated

This project demonstrates:

- Object-Oriented Programming (OOP)
- Classes and objects
- Lists and dictionaries
- Loops and conditionals
- User input handling
- Randomization and shuffling
- Basic game development logic

---

## Author

Created as a Python Blackjack practice project for learning object-oriented programming and game logic.
