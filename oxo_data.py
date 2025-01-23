import os, pickle
 
def saveGame(game):
    try:
        with open("oxogame.dat", "wb") as f:
            pickle.dump(game, f)
    except IOError:
        raise IOError("Could not save game")
 
def restoreGame():
    try:
        with open("oxogame.dat", "rb") as f:
            game = pickle.load(f)
            return game
    except IOError:
        raise IOError("Could not restore game")
