import json as js
import random as rand

from os import path

class GameRandomizer:
    def __init__(self, *args):
        self.args_lookup = {
            "quest_1": "A Mirror in the Dark",
            "quest_2": "Total Eclipse of the Sun",
            "quest_3": "Risen from the Mire",
            "quest_4": "At the Foundations of the World",
            "quest_5": "Ripples in Time",
            "quest_6": "What Lies Beneath",
            "quest_7": "Frozen in Time",
            "quest_8": "Vengeful Sands",
            "quest_9": "Clockwork Destiny",
            "barricades": "Barricades"
        }
        self.owned_sets = {self.args_lookup[value]: True for value in args}
        self.cards = self.load_cards()
        self.deck_pool = {
            "Heros":{},
            "Weapons": {},
            "Spells": {},
            "Items": {},
            "Treasure": {},
            "Legendaries": {},
            "Monsters": {"1":{}, "2":{}, "3":{}},
            "Dungeon Rooms": {"1":{}, "2":{}, "3":{}},
            "Guardians": {}
        }
        self.randomized_decks = {
            "Heros":{},
            "Weapons": {},
            "Spells": {},
            "Items": {},
            "Treasure": {},
            "Legendaries": {},
            "Monsters": {"1":{}, "2":{}, "3":{}},
            "Dungeon Rooms": {"1":{}, "2":{}, "3":{}},
            "Guardians":{}
        }

        self.create_deck_pool()
        self.select_from_pool()
    
    def create_deck_pool(self):
        """
        Create a combined pool of decks from all the sets selected by the user.

        If all the values in owned_sets are set to false return a bool 
        value of zero.  Otherwise return a nested dictionary containg guild, 
        marketplace, treasure, dungeon, monster, and guardian decks from the 
        selected sets.

        The results will be placed in the deck_pool class variable.
        """
        # Create a list including only quests that the user selected
        included_quests = [
            key for key in self.owned_sets.keys() if self.owned_sets[key] is True
        ]

        # Iterate through the list of selected quests and fill the appropriate
        # card categories in the self.deck_pool class variable
        for quest in included_quests:
            for key in self.deck_pool.keys():
                if key in ["Monsters", "Dungeon Rooms"]:
                    for level in ["1", "2", "3"]:
                        self.deck_pool[key][level].update(self.cards["Quest"][quest][key][level])
                else:
                    self.deck_pool[key].update(self.cards["Quest"][quest][key])

    def load_cards(self):
        """
        Open the cards.json and load the results into the self.cards class
        variable as a dictionary.

        :return: dict - a nested dictionary containing all the values in the
        cards.json file.
        """
        data_path = path.join(
            path.dirname(path.abspath(__file__)), 
            "data", 
            "cards.json"
        )
        with open(data_path) as data_file:
            data_dict = js.load(data_file)
            data_file.close()
        
        return data_dict

    def select_from_pool(self):
        """
        Loop through the nested dictionary created by the create_deck_pool 
        method selecting decks to match the count required by each pool.

        The results will be placed in the randomized_decks class var.
        """
        deck_counts = {
            "Heros":{"need": 4, "current": 0},
            "Market":{
                "need": 8, 
                "current": 0, 
                "Items": 0, 
                "Weapons": 0, 
                "Spells": 0
            },
            "Legendaries": {"need": True, "current": 0},
            "Monsters": {
                "1":{"need": 1, "current": 0}, 
                "2":{"need": 1, "current": 0}, 
                "3":{"need": 1, "current": 0}
            },
            "Dungeon Rooms": {
                "1":{"need": 2, "current": 0}, 
                "2":{"need": 2, "current": 0}, 
                "3":{"need": 2, "current": 0}
            },
            "Treasure":{},
            "Guardians":{"need": 1, "current": 0}
        }

        for key in deck_counts.keys():
            # Create Market decks list
            if key == "Market":
                while deck_counts[key]["current"] != deck_counts[key]["need"]:
                    type = rand.choice(["Weapons", "Spells", "Items"])
                    # make sure that no one market item type ever has more than
                    # three decks.
                    if deck_counts[key][type] == 3:
                        pass
                    else:
                        choice = rand.choice(list(self.deck_pool[type].keys()))
                        value = self.deck_pool[type].pop(choice)
                        self.randomized_decks[type][choice] = value
                        deck_counts[key]["current"] += 1
                        deck_counts[key][type] += 1
            # Create Dungeon Rooms and Monsteres lists
            elif key in ["Monsters", "Dungeon Rooms"]:
                for level in ["1", "2", "3"]:
                    while deck_counts[key][level]["current"] != deck_counts[key][level]["need"]:
                        choice = rand.choice(list(self.deck_pool[key][level].keys()))
                        value = self.deck_pool[key][level].pop(choice)
                        self.randomized_decks[key][level][choice] = value
                        deck_counts[key][level]["current"] += 1
            # Create Heros list
            elif key == "Heros":
                while deck_counts[key]["current"] != deck_counts[key]["need"]:
                    choice = rand.choice(list(self.deck_pool[key].keys()))
                    value = self.deck_pool[key].pop(choice)
                    self.randomized_decks[key][choice] = value
                    deck_counts[key]["current"] += 1
            # Choose a random guardian
            elif key == "Guardians": 
                self.randomized_decks[key].update(self.deck_pool[key][rand.choice(list(self.deck_pool[key].keys()))])
            # Add all Treasures and Legendaries cards
            else:
                self.randomized_decks[key].update(self.deck_pool[key])
    
