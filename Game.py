
from abc import ABC,abstractmethod
class Game(ABC):
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement actions,
    result, utility, and terminal_test. You may override display and
    successors or you can inherit their default methods. You will also
    need to set the .initial attribute to the initial state; this can
    be done in the constructor."""

    @abstractmethod
    def actions(self, state):
        """Return a list of the allowable moves at this point."""
        raise NotImplementedError

    @abstractmethod
    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        raise NotImplementedError

    @abstractmethod
    def utility(self, state, player):
        """Return the value of this final state to player."""
        raise NotImplementedError

    @abstractmethod
    def terminal_test(self, state,depth):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    @abstractmethod
    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

    @abstractmethod
    def display(self):
        """Print or otherwise display the state."""

    @abstractmethod
    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @abstractmethod
    def play_game(self):
        """Play an n-person, move-alternating game."""
        raise NotImplementedError
        

