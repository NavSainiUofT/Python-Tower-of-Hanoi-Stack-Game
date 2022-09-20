"""
TOAHModel:  Model a game of Tour of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Tour of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro, Ritu Chaturvedi, Samar Sabie
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
#



class Stack:
    '''
    Stack class to be give as an instance of each stool.
    '''
    def __init__(self):
        """
        Creates a stack via the list data type
        """
        self.stool_stack = []
        
    def size_value(self):
        """returns the height of the stack
        
        @param None
        @rtype int
        
        >>> m = Stack()
        >>> m.stool_stack
        []
        >>> m.push(5)
        >>> m.size_value()
        1
        """
        return len(self.stool_stack)
        
    def push(self, item):
        """
        anyData -> None
        
        adds an item to the top of the stack
        
        >>> a = Stack()
        >>> a.stool_stack
        []
        >>> a.push(5)
        >>> a.stool_stack
        [5]
        """
        self.stool_stack.append(item)
        
    def pick_up(self):
        """
        None -> None
        
        removes an item from the top of the stack and returns it
        
        >>> a = Stack()
        >>> a.push(10)
        >>> a.push(5)
        >>> a.pick_up()
        5
        >>> a.stool_stack
        [10]
        >>> b = Stack()
        >>> b.pick_up()
        
        >>>
        """
        if self.is_empty():
            return None
        else:
            return self.stool_stack.pop(-1)

        
    def is_empty(self):
        """
        None -> None
        
        returns True or False if the stack is empty or not respectivly
        
        >>> a = Stack()
        >>> a.is_empty()
        True
        >>> a.push(5)
        >>> a.is_empty()
        False
        """
        return len(self.stool_stack) < 1
    
    def peak(self):
        """
        returns the top item of the stack without removing it
        @param None
        @rtype Bool
        
        """
        if not self.is_empty():
            
            return self.stool_stack[-1]
    
    def __eq__(self, other):
        """returns if a stack is equal to another stack
        
        A stack in this case is equal to another stack if 
        the stacks have the same items in the same order because
        in a stack order matters
        
        @param self: Stack
        @param other: Stack
        @rtype Bool
        
        >>> m = Stack()
        >>> n = Stack()
        >>> m.push(5)
        >>> m == n
        False
        >>> n.push(5)
        >>> m==n
        True
        
        """
        x = self.stool_stack[:]
        y = other.stool_stack[:]
        if len(x) != len(y):
            return False
        else:
            val = True
            for i in range(len(x)):
                if not x[i] == y[i]:
                    val = False
            return val
    
#EXCEPTIONS ___    
class NegativeCheese(Exception):
    """ Exception indicating an invalid number of \
    cheeses for TOAHModel.fill_first_stool
    """
    pass

class IllegalMoveError(Exception):
    """ Exception indicating move that violate TOAHModel
    """
    pass
#EXCEPTIONS ^^^

class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty stools
        to hold stools of cheese.

        @param TOAHModel self:
        @param int number_of_stools:
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        # you must have _move_seq as well as any other attributes you choose
        self._move_seq = MoveSequence([])
        self._stools = []
        self.number_of_cheeses = 0               
        for stool in range(number_of_stools):
            self._stools.append(Stack())
            stool += 1

        
    def move(self, from_stool, to_stool):
        """ Moves from the source stool to the destination stool if possible
        
        each parameter is an integer representing an index which a stool takes
        if the indexes are valid, this method proceeds to pick up a cheese from 
        the source stool and push it into the destination stool. If the cheese
        is larger than the top cheese of the destination stool, than 
        this method raises the IllegalMoveError
        
        @param int
        @param int
        @rtype None
        
        >>> m = TOAHModel(3)
        >>> m.fill_first_stool(5)
        >>> m.move(0,1)
        >>> m.move(0,2)
        >>> m.move(1,2)
        """
        try:
            if from_stool == to_stool:
                raise IllegalMoveError
            if self._stools[from_stool].is_empty():
                raise IllegalMoveError
                
            else:
                chs = self._stools[from_stool].pick_up()
            
            if self._stools[to_stool].is_empty():
                self.add(chs, to_stool)
                self._move_seq.add_move(from_stool, to_stool)
            else:
                if chs < self.get_top_cheese(to_stool):
                    self.add(chs, to_stool)
                    self._move_seq.add_move(from_stool, to_stool)              
                else:
                    self.add(chs, from_stool)
                    raise IllegalMoveError("invalid move")
        except IndexError:
            self._stools[from_stool].push(chs)
            print("stool number doesn't exist")
            
                    
                
        #I used these to test my errors to make sure it was working
        #except IndexError as e:
            #print(e)
        #except IllegalMoveError as s:
            #print (s)
            
            
            
    
    def get_top_cheese(self, stool_index):
        """returns the top cheese from the stool at given index without removing
        the cheese
        
        If given a valid stool index this method returns the value at the top
        of that stool which would be the cheese. If the stool is empty it passes
        
        @param int
        @rtype Cheese
        
        >>> m = TOAHModel(3)
        >>> m.fill_first_stool(5)
        >>> m.get_top_cheese(0) == Cheese(1)
        True
        >>> m.move(0,2)
        >>> m.get_top_cheese(0) == Cheese(2)
        True
        """
        try:
            if self._stools[stool_index].is_empty():
                pass
            else:
                return self._stools[stool_index].peak()
        #used this to check for index errors to verify my method    
        except IndexError as e:
            print(e)

    def get_cheese_location(self, cheese):
        """returns which stool index a particular cheese is on
        
        takes a cheese and compares the size of the cheese to the cheeses
        on the stools because sizes are distinct to find which stool that
        cheese is on
        
        @param Cheese
        @rtype int
        
        >>> m = TOAHModel(3)
        >>> m.fill_first_stool(5)
        >>> m.get_cheese_location(Cheese(5))
        0
        >>> m.move(0,2)
        >>> m.get_cheese_location(Cheese(1))
        2
        
        """
        counter = 0
        for i in self._stools:
            for j in i.stool_stack:
                if cheese.size == j.size:
                    return counter

            counter += 1
            
    def get_number_of_cheeses(self):
        """returns the total number of cheeses in the toahmodel instance
        @param None
        @rtype int
        
        >>> m = TOAHModel(3)
        >>> m.fill_first_stool(5)
        >>> m.get_number_of_cheeses()
        5
        >>> m.move(0,1)
        >>> m.get_number_of_cheeses()
        5
        """
        return self.number_of_cheeses
    
    def get_number_of_stools(self):
        """returns the number of stools in the toah model instance
        @param None
        @rtype int
        
        >>> m = TOAHModel(3)
        >>> m.fill_first_stool(5)
        >>> m.get_number_of_stools()
        3
        >>> m.move(0,1)
        >>> m.get_number_of_stools()
        3
        """
        return len(self._stools)

    def fill_first_stool(self, number_of_cheeses):
        """pushes a given number of Cheese instances onto the first stool
        
        Adds number_of_cheeses instances of Cheese to the stool which is a Stack
        instance with decrementing size values.
        
        @param int
        @rtype None
        
        >>> m = TOAHModel(3)
        >>> m.fill_first_stool(5)
        >>> n = TOAHModel(5)
        >>> n.fill_first_stool(8)
        """
        
        
        try:
            
            cheese_size = number_of_cheeses
            if number_of_cheeses > 0:
                self.number_of_cheeses = number_of_cheeses
                for i in range(number_of_cheeses):
                    self.add(Cheese(cheese_size), 0)
                    cheese_size -= 1
                    i += 1
                self.number_of_cheeses = number_of_cheeses
            else:
                raise NegativeCheese("Invalid Number of cheeses")
                
        except NegativeCheese as n:
            print(n)
        
    def add(self, a_cheese, index):
        """adds a cheese to a given stool
        
        Takes a cheese and if given a valid index
        adds that cheese to the stool at the index
        
        @param Cheese
        @param int
        @rtype None
        
        >>> m = TOAHModel(3)
        >>> m.fill_first_stool(5)
        >>> m.get_top_cheese(0).size
        1
        >>> m.add(Cheese(100),0)
        >>> m.get_top_cheese(0).size
        100
        
        """
        try:
            self._stools[index].push(a_cheese)
                
        except IndexError as e:
            print(e)
    
                    
    def number_of_moves(self):
        """returns the number of moves in the move sequence
         
        @param None
        @rtype int
        
        >>> m = TOAHModel(4)
        >>> m.fill_first_stool(8)
        >>> m.move(0,1)
        >>> m.move(1,3)
        >>> m.number_of_moves()
        2
        >>> m.move(0,2)
        >>> m.number_of_moves()
        3

        
        
        """
        return self._move_seq.length()
    
    def get_move_seq(self):
        """ Return the move sequence

        @type self: TOAHModel
        @rtype: MoveSequence

        >>> toah = TOAHModel(2)
        >>> toah.get_move_seq() == MoveSequence([])
        True
        """
        return self._move_seq

    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.

        Two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other

        @type self: TOAHModel
        @type other: TOAHModel
        @rtype: bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        if self.number_of_cheeses == other.number_of_cheeses \
           and len(self._stools) == len(other._stools):
            value = True
            for i in range(len(self._stools)):
                if not self._stools[i] == other._stools[i]:
                    value = False
            return value
                

        else:
            return False
            

    def _cheese_at(self, stool_index, stool_height):
        """ Return (stool_height)th from stool_index stool, if possible.
        
        @type self: TOAHModel
        @type stool_index: int
        @type stool_height: int
        @rtype: Cheese | None
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        if 0 <= stool_height < len(self._stools[stool_index].stool_stack):
            return self._stools[stool_index].stool_stack[stool_height]
        else:
            return None

    def __str__(self):
        """
        Depicts only the current state of the stools and cheese.

        @param TOAHModel self:
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines


class Cheese:
    """ A cheese for stacking in a TOAHModel

    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.

        @param Cheese self:
        @param int size:
        @rtype: None

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __eq__(self, other):
        """ Is self equivalent to other?

        We say they are if they're the same
        size.

        @param Cheese self:
        @param Cheese|Any other:
        @rtype: bool

        """
        return self.size == other.size
    def __lt__(self, other):
        """
        we say cheese is smaller if size is smaller
        @other is a cheese class instance
        @self is cheese class instance
        @size is int
        """
        return self.size < other.size

class MoveSequence(object):
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.

        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def get_move(self, i):
        """ Return the move at position i in self

        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        try:
            return self._moves[i]
        
        except IndexError as i:
            print(i)

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.

        @param MoveSequence self:
        @param int src_stool:
        @param int dest_stool:
        @rtype: None
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.

        @param MoveSequence self:
        @rtype: int

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)
    def __eq__(self, other):
        """
        checks if 2 move sequences are the same
        """
        return self._moves[:] == other._moves[:]

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
         after moves in self.

        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.

        @param MoveSequence self:
        @param int number_of_stools:
        @param int number_of_cheeses:
        @rtype: TOAHModel

        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model

if __name__ == '__main__':
    #import doctest
    #doctest.testmod(verbose=True)
    # Leave lines below to see what python_ta checks.
    # File toahmodel_pyta.txt must be in same folder.
    import python_ta
    python_ta.check_all(config="toahmodel_pyta.txt")
