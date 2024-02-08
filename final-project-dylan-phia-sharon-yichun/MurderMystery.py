import json
import FrontEnd as fe

#creates mansion dict, which contains all the rooms, objects and dialogue
def createMansion():
     with open('Mansion.json', 'r',encoding='utf-8') as file:
        mansion_json = file.read()
        mansion = json.loads(mansion_json)
        return mansion

#prints all options in a list of options
def printOptions(options): 
    optionsString = ""
    for i in range(1, len(options)+1):
        optionsString +=(str(i) + ': ' + options[i-1] + '/') #format as / delimited string
    return optionsString

#choose an option from a list
def chooseOption(options,title, question):
    while True:
        try:
            decision = int(fe.prompt_question(title, question)) #must be int
            if decision > len(options) or decision < 1: #must be in range of options
                continue
            else: 
                return(decision)
        except:
            continue

#take an action in the current room
def decide(mansion, currentRoom):
    #add the option to move to different room
    room = mansion[currentRoom]
    options = list(room.keys())
    options.append('Move to a different room. ') #add moving room option
    options.append('Quit Game') # add quit option

    #make move
    fe.print_conversation(currentRoom, room['Description'],printOptions(options[1:]))
    choice = int(chooseOption(options[1:],"Inspection", 'Choose what to inspect (Type the number of your option)'))

    #execute results of choice
    if choice == len(options)-2: #'Move to a different room'
        return 'move'
    elif room[options[choice]] == 'choose murderer': #if in the courtyard, can choose final suspect
        return 'deduce'
    elif choice == len(options)-1 == 'quit': #quit game
        return 'quit'
    else: #print result of choice
        fe.print_conversation(options[choice], room[options[choice]],printOptions(['Keep looking in this room','Go to a different room']))
        choice = chooseOption([1,2], "Inspection", "Keep looking or go elsewhere?")

        #choose to stay or go to different room
        if choice == 1:
            return 'inspected'
        elif choice == 2: 
            return 'move'
    
#go to a different room
def goToRoom(mansion):
    #get list of rooms
    rooms = list(mansion.keys())
    fe.print_conversation(title = 'Rooms', options = printOptions(rooms))

    #change current room
    return rooms[chooseOption(rooms,"Room Selection", "Choose a room to move to: ")-1]
    
#make the final choice of suspect
def deduceMurderer():
    #open json and read dat
    sus_file = open('Suspects.json', 'r',encoding='utf-8')
    sus_data = sus_file.read()
    sus_file.close()

    #create suspect choice list
    suspects = list(json.loads(sus_data).keys())
    suspects.append('Let me think about this some more.')

    #choose final suspect
    fe.print_conversation('Who murdered the owner?', "I've spoken to the suspects. I've inspected the crime scene. I've gathered the evidence. It's time to make my decision. ",printOptions(suspects))
    choice = chooseOption(suspects,"Suspect Accusation", "Who is the murderer? ")
    with open('Suspects.json', 'r',encoding='utf-8') as file: #load suspect responses
        suspects_json = file.read()
        suspects = json.loads(suspects_json)
        if choice == 1:
            fe.print_conversation("Cook", suspects['Cook']) #cook is correct
            return 1
        elif choice == 2:
            fe.print_conversation("Servant", suspects['Servant']) #Servant is correct
            return 2
        elif choice == 3:
            fe.print_conversation("Ex Wife", suspects['Ex-Wife']) #ex wife is wrong
            return 0
        elif choice == 4:
            fe.print_conversation("Son", suspects['Son']) #Son is wrong
            return 0
        elif choice == 5: # think some more
            return -1
        
def playGame():
    #initialize turtle screen
    fe.initialize()

    #create mansion dictionary
    mansion = createMansion()

    #begin the game in the courtyard
    currentRoom = 'Courtyard'

    visitedRooms = [] #keep track of visited rooms
    
    #print intro story
    with open('introduction.txt', 'r',encoding='utf-8') as file:
        setting = file.read()
        options = ['Begin','Quit']
        fe.print_conversation("Murder Mystery", setting, printOptions(options))
        if chooseOption(options,"Begin", 'Begin Game? (Type the number of your option)') == 2:
            return 0
    
    #main game loop
    while True: 
        #decide to inspect a suspect or evidence
        decision = decide(mansion, currentRoom)

        #special choices
        if decision == 'move': #move rooms
            currentRoom = goToRoom(mansion)
            if currentRoom not in visitedRooms:
                visitedRooms.append(currentRoom)
        elif decision == 'quit':
            break
        elif decision == 'deduce': #choose final suspect
            if len(visitedRooms) < 5: #must visit at least 5 rooms before you can deduce the murderer
                fe.print_conversation('Detective',"I don't have enough evidence yet. Maybe I should explore more of the mansion? (Check at least 5 rooms)")
                chooseOption('1',"Inspection", "Enter 1 to move on. ")
                continue
            #choose the final suspect
            choice = deduceMurderer()
            if  choice == 1: #cook is mostly correct
                chooseOption('1', "Game Over", "Congratulations! But perhaps there's more to the story... (Enter 1 to quit.)")
                break
            elif choice == 2: #servant is most correct
                chooseOption('1', "Game Over", "Congratulations! You solved the mystery (Enter 1 to quit.) ")
                break
            elif choice == -1:
                continue
            else:  #any other choice is wrong
                chooseOption('1', "Game Over,", "Although you feel confident in your choice, something doesn't seem right... (Enter 1 to quit.) ")
                break

#main
playGame()