"""Game Blukachka"""

import random


class Room:
    """Room class"""

    def __init__(self, name, floor='Floor 1'):
        """Constructor

        Args:
            name (str): Name of the room
        """
        self.name = name
        self.character = None
        self.directions = {'1': None,
                           '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, 'f1': None, 'f2': None, 'f3': None}
        self.item = None

    def set_description(self, description):
        """Sets description for the room

        Args:
            description (str): Description of the room
        """
        self.description = description

    def link_room(self, room, direction):
        """Joins rooms

        Args:
            room (object): room
            direction (str): direction where you can go
        """
        self.directions[direction] = room

    def set_character(self, character):
        """Link character to the room

        Args:
            character (object): Creature
        """
        self.character = character

    def set_item(self, item):
        """Link item to the room

        Args:
            item (object): Item which you can take
        """
        self.item = item

    def get_details(self):
        """Prints details about some room
        """
        print(f"{self.name}\n--------------------\n{self.description}")
        for i in self.directions:
            if self.directions[i] != None:
                print(f'{i} - {self.directions[i].name}')
        if self.character != None:
            print(f'{self.character.name} is here!\n{self.character.description}')
        if self.item != None:
            print(f'The [{self.item.name}] is here - {self.item.description}')

    def get_character(self):
        """Gets character

        Returns:
            Object: Character in the room
        """
        return self.character

    def get_item(self):
        """Gets Item

        Returns:
            Object: Item in the room
        """
        return self.item

    def move(self, direction):
        """Moves to another room

        Args:
            direction (str): direction where you can move

        Returns:
            Object: Room to which you moved
        """
        if self.directions[direction] != None:
            return self.directions[direction]
        print('\nPoltergeist, is it you? There are no room in this direction!')
        return self


class Creature:
    """Creature class"""

    def __init__(self, name, description):
        """Constructor

        Args:
            name (str): Creature name
            description (str): Description for the creature
        """
        self.name = name
        self.description = description

    def set_conversation(self, message):
        """Sets words of character

        Args:
            message (list): replics
        """
        self.message = message

    def describe(self):
        """Describes creature

        Returns:
            str: Room description
        """
        return self.description

    def talk(self):
        """Print character's words
        """
        message = random.choice(self.message)
        print(f'[{self.name} says]: {message}')


class Enemy(Creature):
    defeated = 0

    def set_weakness(self, weakness):
        """Sets weakness for the Enemy

        Args:
            weakness (str): weakness
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """Fighting process

        Args:
            fight_with (object): Object which you will fight

        Returns:
            bool: Result of the fight
        """
        if fight_with == self.weakness:
            print(f'You fend {self.name} off with the {fight_with}')
            return True
        return False

    def get_defeated(self):
        """How many enemies you won

        Returns:
            int: amount of dead Enemy's
        """
        Enemy.defeated += 1
        return Enemy.defeated


class Friend(Creature):
    def __init__(self, name, description):
        """Constructor

        Args:
            name (str): Creature name
            description (str): Description for the creature
        """
        super().__init__(name, description)

    def set_weakness(self, weakness):
        """Sets weakness for the Friend

        Args:
            weakness (str): weakness
        """
        self.weakness = weakness

    def set_trade(self, item):
        self.trade = item


class Item:
    """Item class"""

    def __init__(self, name):
        """Constructor

        Args:
            name (str): name of the Item
        """
        self.name = name

    def set_description(self, description):
        """Sets description for the Item

        Args:
            description (str): description for the Item
        """
        self.description = description

    def describe(self):
        """Describes Item

        Returns:
            str: description of the Item
        """
        return self.description

    def get_name(self):
        """Gets name for the Item

        Returns:
            str: name for the Item
        """
        return self.name
