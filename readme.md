# PyTSQ Randomizer

This project is a learning project intended to be an easily extensible tool for
randomizing the cards used in a non-epic game of Thunderstone Quest.  Future
versions will also contain the ability to select specific quests and have the 
correct card lists shown.  Eventually this will grow to be a component of a 
digital version of TSQ

__author__ = "David Marienburg"  
__version__ = "0.04b"  
__last_updated__ = "2020/10/31"

***

## How To Use

***

In its current state pyTSQ Randomizer can be used to create a fully randomized game of Thunderstone Quest.  To do this simply call the class GameRandomizer using the quests you wish to draw from as parameters.  These parameters should be entered as quest_x where "x" is the quest number.

```
from TSQ_Randomizer.pyTSQR import GameRandomizer

a = GameRandomizer("quest_1", "quest_9")
print(a.ranomized_decks)
```

To create a new randomized set of decks, perhaps because you weren't in love with the first ones you got, simply call the select_from_pool method and print the randomzied decks class variable again.

```
a.select_from_pool()
print(a.randomized_decks)
```

***

## Updates

***

### Version 0.04b - 2020/10/31

* Lots of minor bug fixes
* When GameRandomizer is invoked it now:
  * generates a pool of cards from all the quests called as args
    * quests args are called by quest number using the quest_1 format
  * generates a random game with the correct deck counts of each type
    * decks should never repeat but more testing will be needed to make sure that this is functioning 100% correctly
  * calling the GameRandomizer objects randomized_decks class variable will provide the random deck selections in a nested dictionary format.

### Version 0.03b - 2020/10/25

* Added a method for loading the cards.json into a dict
* Added a method for creating a deck pool
  * Monsters and Dungeon Rooms will be added to the correct level

### Version 0.02b - 2020/10/24

* Added names and counts for cards in quest 9
* Added names and counts for cards up through quest 8

### Version 0.01b - 2020/10/12

* Created initial outline of json
* Added card names for quests 1-7 to the json 
