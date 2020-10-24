import json as js
import random as rand

class GameRandomizer:
    def __init__(self, **kwargs):
        self.owned_sets = {
            "A Mirror in the Dark": True
            "Total Ecliplse of the Sun": False,
            "Risen from the Mire": True,
            "At the Foundations of the World": False,
            "Barricades": False,
            "Ripples in Time": False,
            "What Lies Beneath": False,
            "Vengeful Sands": False,
            "Clockwork Destiny": False
        }

        self.deck_pool = {}
        self.randomized_decks = {}
    
    def create_deck_pool(self):
        """
        Create a combined pool of decks from all the sets selected by the user.

        If all the values in owned_sets are set to false return a bool 
        value of zero.  Otherwise return a nested dictionary containg guild, 
        marketplace, treasure, dungeon, monster, and guardian decks from the 
        selected sets.

        The results will be placed in the deck_pool class variable.
        """
        pass

    def select_from_pool(self):
        """
        Loop through the nested dictionary created by the create_deck_pool 
        method selecting decks to match the count required by each pool.

        The results will be placed in the randomized_decks class var.
        """
        pass
    