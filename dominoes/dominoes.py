"""Domino game"""
import random


# Define a class for the Domino Game
class DominoGame:
    def __init__(self):
        # Create the stock pieces, distribute them among players and reserve, and set starting piece
        self.stock_pieces = self.create_stock_pieces()
        self.computer_pieces, self.player_pieces, self.reserve_pieces = self.distribute_pieces()
        self.domino_snake = []
        self.status, self.domino_snake = self.set_starting_piece()

    # Static method to create stock pieces
    @staticmethod
    def create_stock_pieces():
        pieces = []
        for i in range(7):
            for j in range(i, 7):
                pieces.append([i, j])
        random.shuffle(pieces)
        return pieces

    # Distribute pieces among players and reserve
    def distribute_pieces(self):
        reserve = self.stock_pieces[:14]
        computer = self.stock_pieces[14:21]
        player = self.stock_pieces[21:28]
        return computer, player, reserve

    # Set the starting piece for the game
    def set_starting_piece(self):
        for piece in self.player_pieces:
            if piece[0] == piece[1]:
                self.domino_snake.append(piece)
                self.player_pieces.remove(piece)
                return "player", self.domino_snake
        for piece in self.computer_pieces:
            if piece[0] == piece[1]:
                self.domino_snake.append(piece)
                self.computer_pieces.remove(piece)
                return "computer", self.domino_snake
        random.shuffle(self.player_pieces)
        random.shuffle(self.computer_pieces)
        return self.set_starting_piece()

    # Display the game status
    def display_game_status(self):
        print("=" * 70)
        print("=" * 70)
        print("Stock size:", len(self.reserve_pieces))
        print("Computer pieces:", len(self.computer_pieces))
        if len(self.domino_snake) > 6:
            print(f"{self.domino_snake[:3]}...{self.domino_snake[-3:]}")
        else:
            print(self.domino_snake)
        print("Your pieces:")
        for idx, piece in enumerate(self.player_pieces, 1):
            print(f"{idx}:[{piece[0]}, {piece[1]}]")
        if self.status == "computer":
            print("Status: Computer is about to make a move. Press Enter to continue...")
        elif self.status == "player":
            print("Status: It's your turn to make a move. Enter your command.")

    # Check if the game is over
    def is_game_over(self):
        if not self.player_pieces:
            return "The game is over. You won!"
        elif not self.computer_pieces:
            return "The game is over. The computer won!"
        elif len(self.domino_snake) > 6 and self.domino_snake[:3] == self.domino_snake[-3:]:
            return "The game is over. It's a draw!"
        return None

    # Handle player's move
    def player_move(self):
        while True:
            try:
                move = int(input("> "))
                if move == 0:
                    if self.reserve_pieces:
                        self.player_pieces.append(self.reserve_pieces.pop())
                        break
                    else:
                        print("Illegal move. The reserve is empty.")
                elif 1 <= move <= len(self.player_pieces):
                    domino = self.player_pieces[move - 1]
                    if domino[0] == self.domino_snake[0][0]:
                        self.domino_snake.insert(0, domino)
                    elif domino[1] == self.domino_snake[0][0]:
                        self.domino_snake.insert(0, domino[::-1])
                    elif domino[0] == self.domino_snake[-1][1]:
                        self.domino_snake.append(domino)
                    elif domino[1] == self.domino_snake[-1][1]:
                        self.domino_snake.append(domino[::-1])
                    else:
                        print("Illegal move. Please try again.")
                        continue
                    self.player_pieces.remove(domino)
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid move. Please enter a number.")

            if self.domino_snake[0][0] != self.domino_snake[-1][1]:
                if self.domino_snake[0][0] == self.domino_snake[0][1]:
                    self.domino_snake[0] = self.domino_snake[0][::-1]
                elif self.domino_snake[-1][0] == self.domino_snake[-1][1]:
                    self.domino_snake[-1] = self.domino_snake[-1][::-1]

    # Evaluate pieces for the computer's move
    def evaluate_pieces(self):
        num_counts = [0] * 7
        for piece in self.computer_pieces + self.domino_snake:
            num_counts[piece[0]] += 1
            num_counts[piece[1]] += 1

        scores = []
        for piece in self.computer_pieces:
            score = num_counts[piece[0]] + num_counts[piece[1]]
            scores.append((piece, score))

        return scores

    # Handle computer's move
    def computer_move(self):
        # Check if there are moves available for the computer
        moves_available = False
        for piece in self.computer_pieces:
            if piece[0] == self.domino_snake[-1][1] or piece[1] == self.domino_snake[-1][1] \
                    or piece[1] == self.domino_snake[0][0] or piece[0] == self.domino_snake[0][0]:
                moves_available = True
                break

        if moves_available:
            scores = self.evaluate_pieces()
            scores.sort(key=lambda x: x[1], reverse=True)

            for piece, _ in scores:
                if piece[0] == self.domino_snake[-1][1]:
                    self.domino_snake.append(piece)
                    self.computer_pieces.remove(piece)
                    break
                elif piece[1] == self.domino_snake[-1][1]:
                    self.domino_snake.append(piece[::-1])
                    self.computer_pieces.remove(piece)
                    break
                elif piece[1] == self.domino_snake[0][0]:
                    self.domino_snake.insert(0, piece)
                    self.computer_pieces.remove(piece)
                    break
                elif piece[0] == self.domino_snake[0][0]:
                    self.domino_snake.insert(0, piece[::-1])
                    self.computer_pieces.remove(piece)
                    break
        else:
            if self.reserve_pieces:
                self.computer_pieces.append(self.reserve_pieces.pop())
            else:
                print("Computer skips the move because there are no available moves and the reserve is empty.")

    # Play the game until it's over
    def play_game(self):
        while True:
            self.display_game_status()
            if self.status == "player":
                print("Enter your move or 0 to take from the reserve:")
                self.player_move()
            elif self.status == "computer":
                input("Press Enter to allow the computer to make a move...")
                self.computer_move()
            game_result = self.is_game_over()
            if game_result:
                print("=" * 70)
                print("=" * 70)
                print(game_result)
                if game_result != "The game is over. It's a draw!":
                    print("Snake ends:", self.domino_snake[:3], "...", self.domino_snake[-3:])
                else:
                    print("Snake ends:", self.domino_snake)
                break
            self.status = "player" if self.status == "computer" else "computer"


game = DominoGame()
game.play_game()
