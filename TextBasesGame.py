#Anthony See

#Short function to enable debug prints
def debugPrint(toPrint):
    if enablePrintsDebug == 'Y':
        print(toPrint)

enablePrintsDebug = input('Enable debug prints? (Y/N)').capitalize()
debugPrint("Enabled debugging prints")

# Variables declared for functions
debugPrint("Loading variables")
exitGameBool = 0
playerMovingBool = 0
playerLocation = 'Entrance'
playerInventory = []
pickupWords = ['Pickup']
theBaconBool = 0


# Nested dictionaries that contain all the rooms, room information, descriptions, lore, and anything else room related.
# There may be a better way to do this by using a template or importing, but because of all the different text needed,
# I chose to type it all out here. The only thing this dictionary doesn't contain is the inventory.
debugPrint('Loading Rooms')
bunkerRooms = {
    'Entrance': {'East': 'Hallway', 'South': 'Power Room', 'Item': 'None', 'Item Requirement': 'None', 'Bacon Item?': 'N',
                 'Accepted Pickups': 'NA',
                 'Item Description': 'NA',
                 'Item Pickup':      'NA',
                 'Item Aquired':     'NA',
                 'Item Needed':      'NA',
                 'Room Description': 'You are in the entrance of the bunker. It has a small desk and a check in area.\n'
                                     'Although, you feel like that is no longer needed.' 'To the east is a hallway that\n'
                                     'goes deeper into the dark bunker. You can tell several rooms connect to it.\n'
                                     'To the south is a room with what looks like a bunch of old wires and circuit breakers.'},

    'Hallway': {'North': 'Side Storage', 'East': 'Food Storage', 'South': 'Large Hall', 'West': 'Entrance', 'Item': 'Computer Battery', 'Item Requirement': 'None', 'Bacon Item?': 'Y',
                'Accepted Pickups': 'Pickup Computer Battery',
                'Item Description':  'Looking around, you see what looks like a small car battery on the ground.\n'
                                     'It\'s too small for a car, though. But, it should have enough juice to power a small\n'
                                     'machine or computer for a short time.',
                'Item Pickup':       'You\'ve picked up the small battery!',
                'Item Aquired':      'There\'s nothing else of use here besides the battery you picked up.',
                'Item Needed':       'NA',
                'Room Description':  'Moving into the hallway, you can see four separate directions you can take.\n'
                                     'To the north looks like another hallway except smaller and with some shelves and boxes.\n'
                                     'To the east looks like a room with a bunch of food. You can smell the old grease coming from it.\n'
                                     'To the south is a large hall which looks like it used to serve as a common area for the bunker, but\n'
                                     'now, there is a sign that says stay out. You hear thunderous bombs in the room.\n'
                                     'To the west is the entrance where you came into the bunker.'},

    'Side Storage': {'East': 'Weapon Room', 'South': 'Hallway', 'West': 'Armor Room', 'Item': 'Dead Energy Core', 'Item Requirement': 'None', 'Bacon Item?': 'N',
                 'Accepted Pickups': 'Pickup Dead Energy Core',
                 'Item Description': 'Rummaging around the old boxes and shelves, you find a cylindrical battery of some sort.\n'
                                     'It seems to replicate an energy core for your mechanical walker. It is dead though.\n'
                                     'Maybe there is a place to charge is somewhere in this bunker?',
                 'Item Pickup':      'You\'ve picked up an energy core! It\'s still dead, though',
                 'Item Aquired':     'You already have the energy core from here. Nothing else is of use.',
                 'Item Needed':      'NA',
                 'Room Description': 'Entering the storage area, you find it\'s full of shelves, boxes and other small equipment.\n'
                                     'To the east is a barricaded door that is slightly ajar. The label says \'Weapon Room\'.\n'
                                     'To the south is the hallway that you used to get to this side of the bunker.\n'
                                     'To the west is another door that looks similar to the weapon\'s door, excpet this\n'
                                     'one says \'Armor Room\'.'},

    'Armor Room': {'East': 'Side Storage', 'Item': 'Walker Chest Armor', 'Item Requirement': 'None', 'Bacon Item?': 'Y',
                 'Accepted Pickups': 'Pickup Walker Chest Armor',
                 'Item Description': 'Looking across all the armor plates and heavy metals, you find something that can\n'
                                     'can fit onto your walker\'s centeral chest area.',
                 'Item Pickup':      'You picked up the chest armor! It easily fits snug onto the front of your walker.',
                 'Item Aquired':     'You already have a chest piece for your mechanical walker.',
                 'Item Needed':      'NA',
                 'Room Description': 'Entering the room, you see a ton of different armor pieces, plates and even\n'
                                     'some mechanical armor pieces, some of which look similar to your walker\'s armor.\n'
                                     'To the east is the door you came through, leading to the storage room.'},

    'Weapon Room': {'West': 'Side Storage', 'Item': 'Walker Plasma Gun', 'Item Requirement': 'None', 'Bacon Item?': 'Y',
                 'Accepted Pickups': 'Pickup Walker Plasma Gun',
                 'Item Description': 'Amongst the weapons and guns, you find a plasma gun that should fit just right\n'
                                     'with your walker. Although, it seems to need ammo cartridges. ',
                 'Item Pickup':      'You\'ve picked up the plasma gun! It easy fits onto your walker\'s arm.',
                 'Item Aquired':     'You already got the most useful weapon here.',
                 'Item Needed':      'NA',
                 'Room Description': 'Walking into the room, you find a ton of different guns and weapons. Ranging from\n'
                                     'kenetic, like bullet weapons, rocket launchers, and energy weapons. \n'
                                     'To the west is the door you came through from the storage hallway.'},

    'Food Storage': {'West': 'Hallway', 'Item': 'Bacon and Beans', 'Item Requirement': 'None', 'Bacon Item?': 'Y',
                 'Accepted Pickups': 'Pickup Bacon and Beans Food Pickup Food',
                 'Item Description': 'Rummaging around the shelves of food, you find some bacon and beans. This should\n'
                                     'suffice in keeping your energy up...plus it has bacon!',
                 'Item Pickup':      'You pick up and eat the beans and bacon. It\'s tasty and fills you with energy.',
                 'Item Aquired':     'You found the bacon and beans already. Don\'t think there\'s anything better for you.',
                 'Item Needed':      'NA',
                 'Room Description': 'Entering the room, you can see a ton of shelves containing lots of cans and food.\n'
                                     'Although, most of it has rotten, there still should be something edible.\n'
                                     'To the west is the hallway, which looks like it connects to a lot of different rooms\n'
                                     'To the south is a hole that\'s too high to get to. Maybe it comes from another room?'},

    'Power Room': {'North': 'Entrance', 'South': 'Experimental Room', 'Item': 'Charged Energy Core', 'Item Requirement': 'Dead Energy Core', 'Bacon Item?': 'Y',
                 'Accepted Pickups': 'Charging Energy Pickup Charge Energy Core',
                 'Item Description': 'You find what looks like a charging station for a large, cylindrical battery. It\'s \n'
                                     'still connected to the power and should be able to charge a battery',
                 'Item Pickup':      'You put the energy core into the charging station. In no time, it fills the battery\n'
                                     'and you slide it into your walker, hearing the telltale sign buzzing sound. mmmMMMM',
                 'Item Aquired':     'You\'re energy core is already at full power!',
                 'Item Needed':      'You need an energy core to accept the power!',
                 'Room Description': 'Entering the room, you find a ton of wires, circuit breakers, and a large \n'
                                     'generator. To the north is the entrance to the bunker from where you came into the bunker.\n'
                                     'On the south side you find a hole that leads into a larger room. It\'s too dark\n'
                                     'to tell what\'s in the room unless you enter it.',},

    'Experimental Room': {'East': 'Experimental Hallway', 'Item': 'Shield Projector', 'Item Requirement': 'Charged Energy Core', 'Bacon Item?': 'Y',
                 'Accepted Pickups': 'Pickup Shield Projector',
                 'Item Description': 'Sorting through all the machinery and random technology, you find a shield projection'
                                     'unit for your walker. Although, it does need a fully charged walker to be attached.',
                 'Item Pickup':      'Picking up the projector, it snuggly fits on your walker\'s free arm',
                 'Item Aquired':     'You\'ve already picked up the most useful thing in this room!',
                 'Item Needed':      'You can\'t pickup the projector yet. You need a fully charged walker for that!',
                 'Room Description': 'Heading into the dark room, you see a ton of random machinery, monitoring equipment\n'
                                     'and experimental technology. To the east, the door to this room, which leads into\n'
                                     'another hallway connecting other rooms. Above you, you see a hole to a room with a \n'
                                     'bunch of cables. But, it\'s too high to get to.'},

    'Experimental Hallway': {'North': 'Large Hall', 'East': 'Experimental Data', 'West': 'Experimental Room', 'Item': 'Plasma Gun Ammo', 'Item Requirement': 'None', 'Bacon Item?': 'Y',
                 'Accepted Pickups': 'Pickup Plasma Gun Ammo',
                 'Item Description': 'Rummaging around the hallway, you find some energy cartridges. Maybe they could be used'
                                     'for a type of energy gun?',
                 'Item Pickup':      'You\'ve picked up the plasma gun ammunition!',
                 'Item Aquired':     'There is nothing else of use here.',
                 'Item Needed':      'NA',
                 'Room Description': 'Walking into the hallway, you see a bunch of random crates containing data sheets,\n'
                                     'random pieces of machinery, and experimental technology. To the north you see a large\n'
                                     'hall that seems to be the common area of the bunker. Loud, thunderous booms can be\n'
                                     'heard coming from it. To the east looks like a data center for the experimentations.\n'
                                     'To the west is what looks like the room where all the experimental stuff was tested.'},

    'Experimental Data': {'North': 'Food Storage', 'West': 'Experimental Hallway', 'Item': 'Digital Files', 'Item Requirement': 'Computer Battery', 'Bacon Item?': 'Y',
                 'Accepted Pickups': 'Pickup Digital Files Read Files',
                 'Item Description': 'You find a working computer while looking through the area. Although, it does seem to\n'
                                     'need a power source in order for it to work.',
                 'Item Pickup':      'You\'ve found some files on the computer! Reading into them, you can tell what is causing those\n'
                                     'loud booms in the large room. It seems an experiment went wrong with a mechanical walker.\n'
                                     'Who ever was here was trying to infuse organic material with the mechanics of the walker.\n'
                                     'They were succesfull in this endevour, all the way to the last minute, where they were infusing\n'
                                     'a human body and BRAIN with the walker. The walker went rouge and started to kill everything and\n'
                                     'everyone in the bunker. They tried to shut it down but it was too powerful. The workers\n'
                                     'abandoned this area, leaving the rogue cyborg locked away...until you stumbled upon it.\n'
                                     'Looking through more files, you find ways to kill the walker, but it won\'t be easy.\n'
                                     'Better gather as much loot from the bunker as you can before taking on this beast.\n'
                                     '(Type a direction to continue)',
                 'Item Aquired':     'You\'ve already seen the computer files! No need to look again!',
                 'Item Needed':      'You try to turn on the computer but it doesn\'t power on. Maybe you should find a power source?',
                 'Room Description': 'Entering the room, you see a ton of different computers, monitors and equipement that\n'
                                     'was used to collect and analyze data from the experiments. To the north is a hole \n'
                                     'that looks like it enters another room full of food. To the west is a hallway\n'
                                     'where this room is connected to.'},

    # I like using BACON keywords for very important things. THE BACON pertains to every item in the game.
    'Large Hall': {'North': 'Hallway', 'South': 'Experimental Hallway', 'Item': 'Rouge Walker', 'Item Requirement': 'THE BACON', 'Bacon Item?': 'N',
                 'Item Description': 'With quick actions that even surpise you, you jump up, the energy core giving you'
                                     'powerful legs, missing the beast\'s first strike. Pulling out the plasma gun, you\n'
                                     'aim your walker towards the weak spot, unloading several rounds. A loud mechanical\n'
                                     'sounding yowl comes from the rouge walker. It swings back around and hits you.\n'
                                     'With quick thinking, you raise your new found shield and block the hit. Counter attacking\n'
                                     'you drive your walkers free arm straight into the chest of the beast, grabbing hold\n'
                                     'of the intermingled computer and beating heart. Pulling back, you pull it out, causing\n'
                                     'the rouge walker to scream in agony. It falls to the ground and you can hear, with\n'
                                     'it\'s last breathe, \"Thank you.\" before it dies in front of you. You have defeated\n'
                                     'the beast! YOU WIN!',
                 'Item Pickup':      'There\'s nothing here to pickup!',
                 'Item Aquired':     'NA',
                 'Item Needed':      'You\'re too slow to miss the first strike of the beast. Even your walker is too weak\n'
                                     'to deal with the beast. The ending is something you don\'t want to see. YOU LOST.',
                 'Room Description': 'Entering the dark room, you see a ton of broken chairs, tables, buffets tables, and even\n' 
                                     'personal computers. This is the central room in the bunker and it\'s the largest, so\n' 
                                     'it\'s not a surpise that what ever is making the noises is in here. All of a sudden\n'
                                     'the ground starts to shake and you hear loud clanking and booming heading straight\n'
                                     'for you. You turn around and see the massive mechanical beast of a walker running\n'
                                     'towards you. It\'s a twisted mess of grown flesh and machine. A big cannon on the\n'
                                     'one arm and a claw on the other. Glowing red eyes and steel for teeth. It\'ll soon\n'
                                     'be upon you. Do you have everything you need? (Type Fight)'},


    #This room is not needed, but it is here for copy/paste purposes, ease of reading and, in future versions of the game,
    # a template for players creating their own rooms, items and descriptions
    #'Example Room' is the name of the room, which the program uses to access the rest of the room's info
    #After that, follows the directional elements, with each one declaring what room it goes to.
    #'Item' is the item of the room. None is default
    #'Item Requirement' means, if not 'none', the palyer needs to grab a different item before getting this one
    #'Bacon Item' is how the game creates the list for the win/loss function. If Y, it is added and needed to win. 'N' by default
    #Accepted Pickups are the...accepted pickup words for the room. Currently, the program tests THREE different lists/text for pickups
    #Item description is the item description
    #item pickup is the text displayed when the player picks up the item
    #Item aquired is the text displayed if the player already has picked up the item
    #item needed is the text displayed if the player tries to pickup the room item but doesnt have the required item
    #Room description is the text displayed when the player enters the room
    'Example Room': {'North': 'Room', 'East': 'Room', 'South': 'Room', 'West': 'Room', 'Item': 'None', 'Item Requirement': 'None', 'Bacon Item?': 'N',
                 'Accepted Pickups': 'Pickup',
                 'Item Description': 'PLACEHOLDER',
                 'Item Pickup':      'PLACEHOLDER',
                 'Item Aquired':     'PLACEHOLDER',
                 'Item Needed':      'PLACEHOLDER',
                 'Room Description': 'PLACEHOLDER',},

}
debugPrint("Room loading is complete")

debugPrint("Loading theBaconInventory")
theBaconInventory = []
for room in bunkerRooms:
        if bunkerRooms[room]['Bacon Item?'] == 'Y':
            debugPrint(room)
            debugPrint("Trying to append " + bunkerRooms[room]['Item'] + " to theBaconInventory")
            theBaconInventory.append(bunkerRooms[room]['Item'])
            debugPrint(str(theBaconInventory) + "\n")
debugPrint("theBaconInventory is complete")
debugPrint("For cheats, type: allyourbasearebelongtome")


debugPrint("Loading functions")
#This function displays the room information and inventory to the player. I've decided to not format the way inventory is
#displayed because I actually like the way it is displayed now. It fits the theme of the game/bunker
def showPlayerStats(Location, Inventory):
    print("\n")
    roomEnter = bunkerRooms[Location]['Room Description']
    print("You're in the", Location)
    print(roomEnter)
    if bunkerRooms[Location]['Item'] != 'None' or bunkerRooms[Location] == 'Large Hall':
        if bunkerRooms[Location]['Item'] not in Inventory:
            print(bunkerRooms[Location]['Item Description'])
    print("---------------------------------------------")
    print("Inventory:", Inventory)
    return

#This function is the pickup function. It's simple, uses a few if statements, and just uses a list for inventory.
def pickupItem(Location, Inventory):
    shortLocal = bunkerRooms[Location]
    itemToPickup = shortLocal['Item']

    if itemToPickup in Inventory:
        print(shortLocal['Item Aquired'])
        return

    elif shortLocal['Item Requirement'] == 'None':
        print(shortLocal['Item Pickup'])
        playerInventory.append(shortLocal['Item'])
        return

    elif shortLocal['Item Requirement'] != 'None':
        if shortLocal['Item Requirement'] in Inventory:
            print(shortLocal['Item Pickup'])
            playerInventory.remove(shortLocal['Item Requirement'])
            playerInventory.append(shortLocal['Item'])
        else:
            print(shortLocal['Item Needed'])
        return

    else:
        debugPrint('Error in func(pickupItem')
        return

# Main part of the 'brain' in the code. Takes player input and decides what to do with it
def decisionMaking(playerInput, Location):
    global playerLocation
    global exitGameBool
    global playerMovingBool
    global theBaconInventory
    locationDict = bunkerRooms[Location]
    debugPrint("Testing player input")

    if len(playerInput) <= 3:
        print("Must be more than 3 characters")
        return
    if playerInput == 'Allyourbasearebelongtome':
        print("Commencing the cheats")
        for item in theBaconInventory:
            if item not in playerInventory:
                playerInventory.append(item)
        print(playerInventory)
        print("Cheats have been added")

    elif playerInput == "Exit":
        exitGameBool = 1
        return

    elif playerLocation != 'Entrance' and (playerInput in pickupWords or playerInput in bunkerRooms[Location]['Item'] or playerInput in bunkerRooms[Location]['Accepted Pickups']):
        debugPrint("Player input is a pickup word. Moving to pickup function")
        pickupItem(Location, playerInventory)

    elif playerInput not in locationDict.keys():
        print("That's not an action or you can't go that way. Try again.")

    elif playerInput == "North":
        playerLocation = bunkerRooms[Location]['North']
        debugPrint("Heading North\n")
        playerMovingBool += 1

    elif playerInput == "East":
        playerLocation = bunkerRooms[Location]['East']
        debugPrint("Heading East\n")
        playerMovingBool += 1

    elif playerInput == "South":
        playerLocation = bunkerRooms[Location]['South']
        debugPrint("Heading South\n")
        playerMovingBool += 1

    elif playerInput == "West":
        playerLocation = bunkerRooms[Location]['West']
        debugPrint("Heading West\n")
        playerMovingBool += 1

    else:
        print("Error in func(decisionMaking")

def theEndBacon(Input, Inventory):
    global exitGameBool
    while exitGameBool == 0:
        if exitGameBool == 1:
            break
        if Input != 'Fight':
            print("Either you're trying to flee, which you can't, or that won't work. You need to try and FIGHT.")
            Input = input().capitalize()
        elif Input == 'Fight':
            print(theBaconInventory)
            print(Inventory)
            for item in theBaconInventory:
                if item in Inventory:
                    debugPrint("Continueing with" + item)
                    theBaconBool = 1
                elif item not in Inventory:
                    print(bunkerRooms['Large Hall']['Item Needed'])
                    exitGameBool = 1
                    theBaconBool = 0
                    break
            if theBaconBool:
                print(bunkerRooms['Large Hall']['Item Description'])
            break


debugPrint("Function loading is complete")


# Is the game loop. This will keep the game running until exit breaks it. The first showPlayerStats is the begining of
# the game and still needs to be called. It is outside of the loop because it only needs to be called once

debugPrint("Starting game")
print('\n\n')

print("Mechanical Walker and the Experimental Bunker game")
print("Collect all the required items before battling the boss. Some items require others though!")
print("Move commands: north, east, south, west")
print("Add to inventory: 'Pickup' or at least part of the item name")
showPlayerStats(playerLocation, playerInventory)
while not exitGameBool:

    if playerLocation == 'Large Hall':
        print(bunkerRooms['Large Hall']['Room Description'])
        playerInput = input("Enter command: ").capitalize()
        theEndBacon(playerInput, playerInventory)
        print("Exiting game")
        break

    if exitGameBool:
        print("Exiting game")
        break

    if playerMovingBool == 1:
        showPlayerStats(playerLocation, playerInventory)
        playerMovingBool = 0

    playerInput = input("Enter command: ").capitalize()
    decisionMaking(playerInput, playerLocation)


