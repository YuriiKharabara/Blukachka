import game


svyatyy = game.Room('Svyatyy shop')
svyatyy.set_description("Works round the clock.")

outdoor = game.Room("Outdoor")
outdoor.set_description("You're on the street")

# ----------------------------------------------------------------------------------------
lyceum = game.Room("Physmat lyceum")
lyceum.set_description("Boarding school at UCU")

wardrobe = game.Room("Wardrobe")
wardrobe.set_description("Just a wardrobe...")

floor_1 = game.Room("Floor 1")
floor_1.set_description(
    "A lot of classes, but all of them are closed, except gym...")

gym = game.Room("gym")
gym.set_description(
    "A large green hall with a volleyball net and basketball hoops")

# -----------------------------------------------------------------------------------------
class_206 = game.Room("Class 206")
class_206.set_description("Shelter for Oksanka")

syanka = game.Room("Oksana's *Bohdanivna* room")
syanka.set_description(
    "Small room where you always can find Ihor Telychyn if you need him.")

ilkovych = game.Room("Ilkovych's class")
ilkovych.set_description("A big room with piano, projector ...")

headmaster = game.Room("Mr. Dobosevych class")
headmaster.set_description("Nobody saw what's there")

teachers_room_2 = game.Room("Teacher's room")
teachers_room_2.set_description("Shelter of linguist")

floor_2 = game.Room("Floor 2")
floor_2.set_description(
    "If you arrive before the first lesson begins, expect a cake in the middle of the hallway :)")
# ------------------------------------------------------------------------------------------
it_class = game.Room("It class")
it_class.set_description(
    "Here are a lot of computer's for word 2003 and board for coding.")

teachers_room_3 = game.Room("Teacher's room")
teachers_room_3.set_description("Shelter of Chemists")

floor_3 = game.Room("Floor 3")
floor_3.set_description(
    "It's scary ... There are physicists ...")


svyatyy.link_room(outdoor, '1')

outdoor.link_room(svyatyy, '1')
outdoor.link_room(lyceum, '2')

lyceum.link_room(outdoor, '1')
lyceum.link_room(wardrobe, '2')

wardrobe.link_room(lyceum, "1")
wardrobe.link_room(floor_1, "f1")

floor_1.link_room(wardrobe, '1')
floor_1.link_room(gym, '2')
floor_1.link_room(floor_2, 'f2')

gym.link_room(floor_1, 'f1')
# ----------------------------------------------------------------------------
floor_2.link_room(class_206, '1')
floor_2.link_room(syanka, '2')
floor_2.link_room(ilkovych, '3')
floor_2.link_room(headmaster, '4')
floor_2.link_room(teachers_room_2, '5')
floor_2.link_room(floor_1, 'f1')
floor_2.link_room(floor_3, 'f3')

class_206.link_room(floor_2, 'f2')
syanka.link_room(floor_2, 'f2')
ilkovych.link_room(floor_2, 'f2')
headmaster.link_room(floor_2, 'f2')
teachers_room_2.link_room(floor_2, 'f2')
# ----------------------------------------------------------------------------
floor_3.link_room(it_class, '1')
floor_3.link_room(teachers_room_3, '2')
floor_3.link_room(floor_2, 'f2')

it_class.link_room(floor_3, 'f3')
teachers_room_3.link_room(floor_3, 'f3')


dmytrych = game.Enemy(
    "Dmytrovych", "Self-proclaimed CEO of linguists. He is extremely afraid of mathematics.")
dmytrych.set_conversation("Мені 13ий минало...")
dmytrych.set_weakness("Oksana's photo")
teachers_room_2.set_character(dmytrych)

vasylko = game.Enemy("Kemist", "Free hands")
vasylko.set_conversation("You will achieve nothing in life without chemistry")
vasylko.set_weakness("Slave-owner")
teachers_room_3.set_character(vasylko)

rostyk = game.Enemy("Rostyk", "IT Specialist")
rostyk.set_conversation("Did you write the program on leaflets at home?")
rostyk.set_weakness("Password")
it_class.set_character(rostyk)

m4 = game.Enemy("4M4", "Bodybuilder")
m4.set_conversation("Look at me, I'm a beautiful creature...")
m4.set_weakness("Toilet paper")
gym.set_character(m4)

prybyralka = game.Creature("Cleaning manager", "Always has clean table")
prybyralka.set_conversation(
    "Come on, don't delay the queue. The bell has already rung.")
wardrobe.set_character(prybyralka)


dobosevych = game.Friend('Maryan Dobosevych', 'Director of the lyceum')
dobosevych.set_conversation("Where is my signet?")
dobosevych.set_weakness("Signet")
headmaster.set_character(dobosevych)

Oksanka = game.Friend('Oksanka', 'Math teacher')
Oksanka.set_conversation("I can't find you homework!!!")
Oksanka.set_weakness("Homework")
syanka.set_character(Oksanka)

Ilkovych = game.Creature('Ilkovych', 'Just friend to everyone.')
Ilkovych.set_conversation("Have a nice day!!!")
ilkovych.set_character(Ilkovych)

pani_liuba = game.Friend('Pania Liuba', 'Seller.')
pani_liuba.set_conversation("Are you 18 years old?")
pani_liuba.set_weakness("Money")
svyatyy.set_character(pani_liuba)

yrmych = game.Friend('YurMych', 'History teacher')
yrmych.set_conversation("Do you remember Philip Orlyk's Constitution?")
yrmych.set_weakness("Vodka")
floor_1.set_character(yrmych)

p_halya = game.Friend("Pani Halya", '206 cleaner')
p_halya.set_conversation("Haven't you seen my keys?")
p_halya.set_weakness("Keys")
class_206.set_character(p_halya)

keys = game.Item("Keys")
keys.set_description("Small silver keys")
lyceum.set_item(keys)


toilet_paper = game.Item("Toilet paper")
toilet_paper.set_description("Kohabynka")

homework = game.Item("Homework")
homework.set_description("Math")
class_206.set_item(homework)

syanka_photo = game.Item("Oksana's photo")
syanka_photo.set_description("Just a photo, not what you thought!")

signet = game.Item('Signet')
signet.set_description('Lyceum signet')
teachers_room_3.set_item(signet)

password = game.Item('Password')
password.set_description('Password to all acounts of character')

money = game.Item("Money")
money.set_description("130 UAH")
ilkovych.set_item(money)

vodka = game.Item("Vodka")
vodka.set_description("Nemiroff Delikat")

phone = game.Item("Slave-owner")
phone.set_description("iPhone")

dobosevych.set_trade(password)
Oksanka.set_trade(syanka_photo)
pani_liuba.set_trade(vodka)
yrmych.set_trade(phone)
p_halya.set_trade(toilet_paper)

current_room = outdoor
backpack = []

dead = False
one_more_try = 1
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

    if command in ["1", "2", "3", "4", "5", "6", "7", "f1", "f2", "f3"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print('Never take these pills again!... Here is nobody you can talk with!')
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
                    if inhabitant.get_defeated() == 4:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    if one_more_try == 1:
                        one_more_try = 0
                        print("Oh dear, you lost the fight.")
                        print("You have one more life. Be careful!")
                    else:
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
    elif command == 'backpack':
        print(backpack)
    # Idea by Paul Kryven!
    elif command == 'trade' and type(inhabitant) == game.Friend:
        exchange = input("What do you want to trade: ")
        if exchange in backpack:
            if exchange == inhabitant.weakness:
                print(f'You exchanged {exchange} for {inhabitant.trade.name}')
                backpack.remove(exchange)
                backpack.append(inhabitant.trade.name)
            else:
                print(f"{inhabitant.name} doesn't want this")
        else:
            print("You don't have this item")
    elif command == 'trade' and type(inhabitant) != game.Friend:
        print(f"{inhabitant.name} doesn't want to trade anything!")
    elif command == 'help' or command == '-h' or command == '--help' or command == '--h':
        print("""
        You can fight, talk and trade with characters.
        To move through the lyceum follow the instructions on the screen. (To move through floors "f2" means "f"+"2")

        fight: fight with enemies.
        talk: talk with creatures
        trade: trade with friends
        take: take item in room
        backpack: Look what you have in your backpack.
        help, --help, -h: help
        """)
    else:
        print("I don't know how to " + command)
        print("""
        You can fight, talk and trade with characters.
        To move through the lyceum follow the instructions on the screen. (To move through floors "f2" means "f"+"2")

        fight: fight with enemies.
        talk: talk with creatures
        trade: trade with friends
        take: take item in room
        backpack: Look what you have in your backpack.

        Also you can call this menu by typing
        help, --help, -h
        """)
