"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    try:
        model.move(origin, dest)
    except IllegalMoveError:
        print("")
        print("Invalid Move")


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        print("")
        print("")
        print("Hi there and welcome to the tower of Anne Hoi")
        print("The idea of this game is too move all the cheese")
        print("from one stool to another without putting a larger")
        print("cheese on top of a smaller cheese")
        print("stools are numbered off starting from 0 to 3")
        print("in order to move a cheese, one must type")
        print("the number of the source stool followed by enter,")
        print("followed by the number of the")
        print("destination stool")
        print("all moves must be numbers")
        print("good luck and have fun")
        print("If you would like to exit the game, simple type 'exit' when")
        print("prompted for a move")
        print("")
        print("")
        toah = TOAHModel(self.number_of_stools)
        toah.fill_first_stool(self.number_of_cheeses)
        print(toah)
        
        game_exit = False
        while not game_exit:
            src = input("please enter the source stool or 'exit': ")
            if src == 'exit':
                game_exit = True
            else:

                dest = input("please enter the destination stool or 'exit': ")
                if dest == 'exit':
                    game_exit = True
                else:
                    
                    try:
                        move(toah,int(src),int(dest))
                        print("")
                        print("Number of moves: "+ str(toah.number_of_moves()))
                        print(toah)
                    except ValueError:
                        print("")
                        print("invalid move input... INTEGERS only")
                        print("")
                        print("Number of moves: "+ str(toah.number_of_moves()))
                        print(toah)
            
        print("thanks for playing")

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.

    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.
    #import python_ta
    #python_ta.check_all(config="consolecontroller_pyta.txt")
    a = ConsoleController(5,4)
    a.play_loop()