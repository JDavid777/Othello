from math import inf


def alphabeta_search(state, game):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Figure 5.7], this version searches all the way to the leaves."""

    player = game.to_move()

    # Functions used by alphabeta
    def max_value(state, alpha, beta,depth):

        if game.terminal_test(state[:],depth):
            return game.utility(state[:], player)
        v = -inf
        for a in game.actions(state[:]):
            v = max(v, min_value(game.result(state[:], a), alpha, beta,depth+1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta,depth):

        if game.terminal_test(state[:],depth):
            return game.utility(state[:], player)
        v = inf
        for a in game.actions(state[:]):
            v = min(v, max_value(game.result(state[:], a), alpha, beta,depth+1),)
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_search:
    best_score = -inf
    beta = inf
    best_action = None
    for a in game.actions(state[:]):
        v = min_value(game.result(state[:], a), best_score, beta, 0)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action
