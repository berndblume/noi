# noi
Towers of Hanoi, animated using Curses, written in Python3

## Game
![Towers of Hanoi with Bitcoin, Cardano Ada and Dogecoin](img/LogoNoi.jpg)
The goal is to move a stack of coins from spot A to spot C, using spot B as a helper.
The catch? You're only allowed to move ONE coin at a time, and NEVER can a larger coin rest on top of a smaller coin.
While you can use coins of different sizes such as quarters, nickels and dimes,
it way more fun to think of them as crypto coins, such as Bitcoin, Dogecoin or Cardano/Ada.

I wish you much wow playing the game!

## Rationale
This project was originally a time killer on a long flight with no Internet.
I had an old jailbroken iPad on the flight with terminal access and Python.

## Usage
`./noi.py <n>`

Will run a Towers of Hanoi simulation for a stack of `n` coins.
If `n` is not given, not numeric, or out of bounds, the maximum possible for the screen size will be assumed.

## Screenshots
![Calculating Hanoi Moves](img/calc.jpg)

![Animated Towers of Hanoi Solution](img/ScreenNoi.jpg)

## Feedback
This was not just an exercise in getting the task done, but also in being
as elegant and pyhthonic as possible. Let me know where I can improve.
