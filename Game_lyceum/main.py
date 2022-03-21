from matplotlib.pyplot import hlines
import game

floor_1=game.Floor("Floor 1")
floor_2=game.Floor("Floor 2")
floor_3=game.Floor("Floor 3")

svyatyy = game.Room('Svyatyy shop')
svyatyy.set_description("Works round the clock.")

outdoor=game.Room("You're on the street")
#----------------------------------------------------------------------------------------
lyceum = game.Room("Physmat lyceum")
lyceum.set_description("Works from 8:30 to 18:00")

wardrobe = game.Room("Wardrobe")
wardrobe.set_description("Just a wardrobe...")

hall_1 = game.Room("Hall")
hall_1.set_description("A lot of classes, but all of them are closed except gym.")

gym=game.Room("gym")
gym.set_description("A large green hall with a volleyball net and basketball hoops")

#-----------------------------------------------------------------------------------------
class_206=game.Room("Class 206")
class_206.set_description("Ааххахаха, придумай шось сюди")

syanka=game.Room("Oksana's *Bohdanivna* room")
syanka.set_description("Small room where you always can find Ihor Telychyn if you need")

ilkovych=game.Room("Ilkovych's class")
ilkovych.set_description("A big room with piano, projector ...")

headmaster=game.Room("Mr. Dobosevych class")
headmaster.set_description("Nobody saw what's there")

teachers_room_2=game.Room("Teacher's room")
teachers_room_2.set_description("Shelter of linguist")

hall_2 = game.Room("Hall")
hall_2.set_description("A lot of classes, but all of them are closed except gym.")
#------------------------------------------------------------------------------------------
it_class=game.Room("It class")
it_class.set_description("Here are a lot of computer's")

teachers_room_3=game.Room("Teacher's room")
teachers_room_3.set_description("Shelter of Chemists")

hall_3 = game.Room("Hall")
hall_3.set_description("A lot of classes, but all of them are closed except gym.")

svyatyy.link_room(outdoor, '1')

outdoor.link_room(svyatyy, '1')
outdoor.link_room(lyceum, '2')

lyceum.link_room(outdoor, '1')
lyceum.link_room(wardrobe, '2')

wardrobe.link_room(lyceum, "1")
wardrobe.link_room(hall_1, "2")

hall_1.link_room(wardrobe, '1')
hall_1.link_room(gym, '2')

gym.link_room(hall_1, '1')
#----------------------------------------------------------------------------
hall_2.link_room(class_206, '1')
hall_2.link_room(syanka, '2')
hall_2.link_room(ilkovych, '3')
hall_2.link_room(headmaster, '4')
hall_2.link_room(teachers_room_2, '5')

class_206.link_room(hall_2, '1')
syanka.link_room(hall_2, '1')
ilkovych.link_room(hall_2, '1')
headmaster.link_room(hall_2, '1')
teachers_room_2.link_room(hall_2, '1')
#----------------------------------------------------------------------------
hall_3.link_room(it_class, '1')
hall_3.link_room(teachers_room_3, '2')

it_class.link_room(hall_3, '1')
teachers_room_3.link_room(hall_3, '1')


dmytrych = game.Enemy("Dmytrovych", "Self-proclaimed CEO of linguists")
dmytrych.set_conversation("Мені 13ий минало...")
dmytrych.set_weakness("Oksanka's photo")
teachers_room_2.set_character(dmytrych)

vasylko = game.Enemy("Kemist", "Free hands")
vasylko.set_conversation("You will achieve nothing in life without chemistry")
vasylko.set_weakness("Slave-owner")
teachers_room_3.set_character(vasylko)

rostyk = game.Enemy("Rostyk", "IT Specialist")
rostyk.set_conversation("Today we talk about <code on the board>.")
rostyk.set_weakness("password")
it_class.set_character(rostyk)

m4 = game.Enemy("4M4", "Bodybuilder")
m4.set_conversation("Wait a minute, I'm going to the toilet...")
m4.set_weakness("Toilet paper")
gym.set_character(m4)

prybyralka = game.Creature("Cleaning manager", "Always has clean table")
prybyralka.set_conversation("Come on, don't delay the queue. The bell has already rung.")
wardrobe.set_character(prybyralka)


dobosevych=game.Friend('Maryan Dobosevych', 'Director of the lyceum')
dobosevych.set_conversation("Where is my signet?")
dobosevych.set_weakness("signet")
headmaster.set_character(dobosevych)

Oksanka=game.Friend('Oksanka', 'Math teacher')
Oksanka.set_conversation("I can't find you homework!!!")
Oksanka.set_weakness("homework")
syanka.set_character(dobosevych)

Ilkovych=game.Friend('Ilkovych', 'Just friend to everyone.')
Ilkovych.set_conversation("Have a nice day!!!")
Ilkovych.set_weakness("homework")
ilkovych.set_character(Ilkovych)

pani_liuba=game.Friend('Pania Liuba', 'Seller.')
pani_liuba.set_conversation("Are you 18 old?")
pani_liuba.set_weakness("money")
svyatyy.set_character(pani_liuba)



toilet_paper = game.Item("Toilet paper")
toilet_paper.set_description("Kohabynka")
ballroom.set_item(cheese)

book = game.Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

current_room = kitchen
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)