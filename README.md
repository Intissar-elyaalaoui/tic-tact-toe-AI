# Tic-Tac-Toe Game with AI

This is a classic Tic-Tac-Toe game implemented using Python and Pygame, where you can play against an AI opponent. The AI has three difficulty levels: Easy, Medium, and Hard, providing different levels of challenge for players. The game also includes a graphical interface with smooth animations and pop-up messages indicating the game result.

### Features:
Single-Player Mode: Play against an AI opponent with varying levels of difficulty.

### AI Difficulty Levels:
Easy: The AI makes random moves, providing an easy challenge.
Medium: The AI alternates between random moves and optimal moves, making it moderately challenging.
Hard: The AI uses the Minimax algorithm to always play optimally, providing the toughest challenge.
Graphical User Interface (GUI): Built using Pygame, with clear graphics for the grid, X's, and O's.
Result Pop-Up: Displays a message indicating the winner or if the game is a draw.
Smooth Animations: Updates the board dynamically after each move.

### How to Play:
Choose the Difficulty: When the game starts, a difficulty selection screen allows you to pick between Easy, Medium, or Hard difficulty.
Make Your Move: Click on any empty cell to place your 'X'. The AI will then make its move.
Win the Game: Try to get three of your marks (X's) in a row—horizontally, vertically, or diagonally—before the AI does.
Game Over: The game will display a pop-up message indicating whether you won, lost, or if it was a draw.

### Requirements:
Python 3.x , 
Pygame library

### How the AI Works
The AI uses different strategies depending on the difficulty level:

Easy: Makes random moves without any strategy.
Medium: Chooses between making a random move or using an optimal strategy.
Hard: Uses the Minimax algorithm, which simulates all possible moves to find the best move for the AI, making it unbeatable.

### Project Structure:
tic_tac_toe.py: The main Python file that contains the game logic and Pygame interface.
README.md: Project description and instructions.

### Future Improvements:
Add two-player mode for playing with a friend.
Enhance the GUI with sound effects and animations.
Add a scoring system to track wins, losses, and draws over multiple rounds.
Implement a smarter AI that adapts its strategy over time.
