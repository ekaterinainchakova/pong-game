# Pong Game (Python, Pygame)

A two-player Pong game written in Python with Pygame. Originally written in May 2025 as coursework for a Computer Science course (Education First); repaired and documented in November 2026.

## Features

- Two paddles controlled from the same keyboard, a bouncing ball, collision detection and live score display.
- Simple demo login before the game starts (3 attempts).
- Each finished game is saved with Pandas to `pong_game_results.csv` (timestamp, both scores, winner).

## Controls

| Player | Up | Down |
|---|---|---|
| Player 1 (left) | `W` | `S` |
| Player 2 (right) | `Up arrow` | `Down arrow` |

Close the window to end the game and save the result.

## Install and run

```bash
pip install -r requirements.txt
python pong.py
```

When asked, log in with the demo account: username `player1`, password `pong123`. This login is hard-coded for learning purposes only and is not secure.

## Technologies

Python 3, Pygame, Pandas.

## Known limitations and future improvements

- There is no winning score: the game runs until the window is closed.
- A draw is currently recorded as a win for Player 2.
- `pong_game_results.csv` is overwritten after every game instead of appending a new row.
- Replace the hard-coded login with real user accounts.
