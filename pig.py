import random
random.seed(0)
class Dice():
    '''This class represents a single die of variable sides.'''
    def __init__(self, sides):
        self.sides = sides
class Player():
    '''This class represents a player for a dice-based game with methods to roll and hold.'''
    def __init__(self, name):
        self.name = name
    def roll(self, dice):
        return int('{:1.0f}'.format(random.uniform(1, dice.sides)))
    def hold(self, running_total):
        print(f"...\n{self.name}, you've added {running_total} to your score.")
        return running_total
class Game():
    '''This is a parent class of games.'''
    def __init__(self):
        pass
class Pig(Game):
    '''This a child class of Game for the specific game Pig.
    It contains the rules and method to play.'''
    def __init__(self):
        self.name = "Pig"
        self.rules = '''The goal of Pig is to reach 100 points before the other player.
During your turn you may roll the die until either a 1 is rolled or until you choose to hold.
Holding scores the sum of rolls for that round. If a 1 is rolled, no points are received.'''
    def __str__(self):
        return f"This is a game called {self.name}."
    def play(self, player, total_score, dice):
        result = 0
        running_total = 0
        choice = input(f"{player.name}, please enter 'r' to roll >>> ")
        while choice != 'r' and choice != 'h':
            choice = input("Invalid entry. Please enter 'r' to roll or 'h' to pass your turn >>> ")
        while choice == 'r' and not result == 1 and not running_total >= 100:
            result = player.roll(dice)
            print(f"...\nYou rolled a {result}.")
            if result == 1:
                running_total = 0
                return running_total
            else:
                running_total += result
                print(f"Your running total is {running_total}.")
                if running_total >= 100 or (running_total + total_score) >= 100:
                    return running_total
                else:
                    print(f"Your total score is {running_total + total_score}.")
                    choice = input("Please enter 'r' to roll again or 'h' to hold >>> ")
                    while choice != 'r' and choice != 'h':
                        choice = input("Invalid entry. Please enter 'r' to roll or 'h' hold >>> ")
                    if choice == 'h':
                        return player.hold(running_total)
        if choice == 'h':
            return player.hold(running_total)
def main():
    '''This is the main function. It instantiates class objects for players, dice, and the game Pig.
    It calls the play method of the game Pig, changes turns, and prints the winner.'''
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    dice = Dice(6)
    game = Pig()
    p1_score = 0
    p2_score = 0
    print(f"***{game.name}***".center(93))
    print(f"{game.rules}\n")
    while p1_score < 100 and p2_score < 100:
        p1_score += int(game.play(player1, p1_score, dice))
        print(f"Your total score is {p1_score}.\n")
        if p1_score >= 100:
            break
        p2_score += game.play(player2, p2_score, dice)
        print(f"Your total score is {p2_score}.\n")
    if p1_score > p2_score:
        print(f"Congratulations {player1.name}! You've won!")
    else:
        print(f"Congratulations {player2.name}! You've won!")

if __name__ == "__main__":
    main()