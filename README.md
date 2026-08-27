# Pygame Sudoku

A fully functional, interactive Sudoku game built in Python with a graphical interface. Includes a custom board generator, interactive cell selection, arrow key navigation, and automated solution validation.

## Features

* **Interactive Gameplay:** Click or use the **arrow keys** to navigate the grid.
* **Dynamic Generation:** Automatically generates valid Sudoku boards with varying difficulty levels.
* **Clean UI:** Modular Pygame interface separating cell rendering, board state, and main loop.

## Project Structure

* `sudoku.py` - Main application entry point handling game loop, events, and UI integration.
* `board.py` - Manages overall grid state, rendering, and board-level operations.
* `cell.py` - Represents individual grid cells, handling values, sketched numbers, and draw state.
* `sudoku_generator.py` - Backend algorithm responsible for creating and validating Sudoku puzzles.
* `main.sh` - Quick launch bash script to start the application.

## Getting Started

### Prerequisites

* Python 3.x
* Pygame library

Install dependencies:
```bash
pip install pygame
