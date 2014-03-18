import time
from subprocess import call

# Create a class named Life to encapsulate all game logic
class Life:

    # When the Life class is instantiated, initialize it by creating
    # a new dict and assigning it into the board data attribute.
    def __init__(self):
        self.board = {}

    # Decide whether a cell is alive or not by retrieving from
    # the board dict the object corresponding to the key given
    # by the cell_key parameter. The method returns true if the
    # dictionary contains the cell_key and the object returned
    # is equal to the string "alive", and false otherwise.
    # parameter cell_key: a string in the format "X,Y"
    def is_alive(self, cell_key):
        return cell_key in self.board and self.board[cell_key] == "alive"

    # Set a cell as alive by assigning the string "alive" into the
    # board dict using the key given by the cell_key parameter.
    # parameter cell_key: a string in the format "X,Y"
    def become_alive(self, cell_key):
        self.board[cell_key] = "alive"

    # Run the game
    def run(self):
        while True:                 # Start a never-ending loop
            self.__print_board()    # Print the board as it currently exists
            time.sleep(0.1)         # Sleep briefly to make the printed output visible
            self.__tick()           # Call tick to replace the board with the next generation

    # Print the visible area of the board to the console
    def __print_board(self):
        call("clear")                                  # Clear the console before printing anything

        for y in range(30):                            # Iterate over the first 30 rows
            row = ''                                   # Create a new string to contain the row
            for x in range(80):                        # Iterate over the first 80 columns
                if self.is_alive("%d,%d" % (x, y)):    # Build the cell key and ask if that cell is alive
                    row += "#"                         # If the cell is alive, add '#' to the row string
                else:
                    row += "."                         # If the cell is dead, add '.' to the row string
            print row                                  # Print the row string to the console

    # In a single discrete step, build the next generation
    # of living cells and replace the board with a new one.
    def __tick(self):
        # Create a new dict to represent the new board,
        # wherein all cells start off as dead
        new_board = {}

        # Iterate over all candidate cells within the current board
        for cell_key in self.__candidate_cells():
            # Determine how many alive neighbors the current cell has
            num_alive = self.__number_of_alive_neighbors(cell_key)

            # Decide if the current cell will continue living or become
            # alive according to the rules of John Conway's Game of Life
            if self.is_alive(cell_key) and num_alive == 2 or num_alive == 3:
                # If so, set the cell as alive in the new board
                new_board[cell_key] = "alive"

        # Finally, assign the new board into the board data attribute
        self.board = new_board

    # Returns a set of keys for cells that could be alive in
    # the next generation of life. This includes cells that are
    # currently alive and might stay alive, and cells that are
    # currently dead and might come alive through reproduction.
    def __candidate_cells(self):
        # Create a new set of keys that will be returned
        cell_keys = set()

        # Iterate over all cell keys known to the current board
        for cell_key in self.board.keys():
            # Ask if this cell is alive
            if self.is_alive(cell_key):
                # Include this cell because it's currently alive
                cell_keys.add(cell_key)

                # And also any neighbor cells (alive or dead)
                # which might either stay alive or come alive
                cell_keys.update(self.__neighbor_cells(cell_key))

        # Return the set of keys
        return cell_keys

    # Return a list of keys for cells that are neighbors to
    # the cell indicated by the given cell_key parameter.
    def __neighbor_cells(self, cell_key):
        # Parse X and Y from the cell_key string and convert them to integers
        x, y = cell_key.split(',')
        x = int(x)
        y = int(y)

        # Create a new list of keys that will be returned
        neighbor_keys = []

        # Build keys for all eight neighbors and add them to the list of keys
        neighbor_keys.append('%d,%d' % (x-1, y-1))
        neighbor_keys.append('%d,%d' % (x,   y-1))
        neighbor_keys.append('%d,%d' % (x+1, y-1))
        neighbor_keys.append('%d,%d' % (x-1, y))
        neighbor_keys.append('%d,%d' % (x+1, y))
        neighbor_keys.append('%d,%d' % (x-1, y+1))
        neighbor_keys.append('%d,%d' % (x,   y+1))
        neighbor_keys.append('%d,%d' % (x+1, y+1))

        # Return the list of keys
        return neighbor_keys

    # Return the number of alive cells that are neighbors to
    # the cell indicated by the given cell_key parameter.
    def __number_of_alive_neighbors(self, cell_key):
        # Create a new integer to represent the count
        count = 0

        # Iterate over the cell keys for all neighbors
        for neighbor_key in self.__neighbor_cells(cell_key):
            # Ask if this neighbor cell is alive
            if self.is_alive(neighbor_key):
                # If so, increment the count by 1
                count += 1

        # Return the count
        return count


# Create a new instance of the Life class
game = Life()

# Seed the game instance by marking initial cells as alive
game.become_alive("1,5")
game.become_alive("2,5")
game.become_alive("1,6")
game.become_alive("2,6")
game.become_alive("13,3")
game.become_alive("14,3")
game.become_alive("12,4")
game.become_alive("16,4")
game.become_alive("11,5")
game.become_alive("17,5")
game.become_alive("11,6")
game.become_alive("15,6")
game.become_alive("17,6")
game.become_alive("18,6")
game.become_alive("11,7")
game.become_alive("17,7")
game.become_alive("12,8")
game.become_alive("16,8")
game.become_alive("13,9")
game.become_alive("14,9")
game.become_alive("25,1")
game.become_alive("23,2")
game.become_alive("25,2")
game.become_alive("21,3")
game.become_alive("22,3")
game.become_alive("21,4")
game.become_alive("22,4")
game.become_alive("21,5")
game.become_alive("22,5")
game.become_alive("23,6")
game.become_alive("25,6")
game.become_alive("25,7")
game.become_alive("35,3")
game.become_alive("36,3")
game.become_alive("35,4")
game.become_alive("36,4")
game.become_alive("62,6")
game.become_alive("63,6")
game.become_alive("64,6")
game.become_alive("68,6")
game.become_alive("69,6")
game.become_alive("70,6")
game.become_alive("60,8")
game.become_alive("65,8")
game.become_alive("67,8")
game.become_alive("72,8")
game.become_alive("60,9")
game.become_alive("65,9")
game.become_alive("67,9")
game.become_alive("72,9")
game.become_alive("60,10")
game.become_alive("65,10")
game.become_alive("67,10")
game.become_alive("72,10")
game.become_alive("62,11")
game.become_alive("63,11")
game.become_alive("64,11")
game.become_alive("68,11")
game.become_alive("69,11")
game.become_alive("70,11")
game.become_alive("62,13")
game.become_alive("63,13")
game.become_alive("64,13")
game.become_alive("68,13")
game.become_alive("69,13")
game.become_alive("70,13")
game.become_alive("60,14")
game.become_alive("65,14")
game.become_alive("67,14")
game.become_alive("72,14")
game.become_alive("60,15")
game.become_alive("65,15")
game.become_alive("67,15")
game.become_alive("72,15")
game.become_alive("60,16")
game.become_alive("65,16")
game.become_alive("67,16")
game.become_alive("72,16")
game.become_alive("62,18")
game.become_alive("63,18")
game.become_alive("64,18")
game.become_alive("68,18")
game.become_alive("69,18")
game.become_alive("70,18")

# Run the game instance!
game.run()
