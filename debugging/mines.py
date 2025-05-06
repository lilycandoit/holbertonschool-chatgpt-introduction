#!/usr/bin/python3
import random
import os

# Utility function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Randomly choose mine locations (by flat index)
        self.mines = set(random.sample(range(width * height), mines))
        # Board holds display characters
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        # Track what cells have been revealed
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        # Print column headers
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    # Show mine or number
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')  # Unrevealed cell
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        # Check 8 surrounding cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False  # Hit a mine

        self.revealed[y][x] = True

        # Auto-reveal neighbors if no mines nearby
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width and
                        0 <= ny < self.height and
                        not self.revealed[ny][nx]):
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        # If all non-mine cells are revealed, you win
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 Game Over! You hit a mine.")
                    break
                elif self.check_win():
                    self.print_board(reveal=True)
                    print("🎉 Congratulations! You cleared the minefield!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            except IndexError:
                print("Out of range. Please enter valid coordinates.")

# Entry point
if __name__ == "__main__":
    game = Minesweeper()
    game.play()
