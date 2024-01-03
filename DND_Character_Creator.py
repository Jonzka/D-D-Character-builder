#Time spent here: 34h

#Import necessary modules
import os
import random
import sys
import math

#Change working directory to the directory this .py file is contained in.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Function for welcoming user
def Welcome():
    print("Welcome!")
    print("This is a free D&D 5th edition character builder.")
    print("This program uses the Systems Reference Document v5.1 provided by Wizards of the Coast under Creative Commons licensing.")
    print("Full original PDF file can be found in this folder.")
    print("Anyways, let's get started!\n")
    print("Do you wish to write character to a new file?")
    print("Select yes (y) if you're creating a new character.")
    print("Select no (n) if you wish to exit program.")
    global CharFilePath #Define CharFile as a global variable, as this is the path and file the program will write to later.
    while True:
        CharFile = input("\nWrite character to new file (y/n)? ")
        if CharFile.lower()  == "y":
            print("\nCall the file anything you want, but do not include .txt")
            print("or any other file extension at the end.")
            CharFile = input("\nWhat should the file be called? (any): ")
            try:
                print("Creating file...")
                OpenFile = open(f"My Characters/{CharFile}.txt", "x")
            except FileExistsError:
                print("\nSorry, that file already exists. Please set a different name. File was not created. Closing file")
                continue
            print("File has been successfully created. Closing file.\n")
            OpenFile.close()
            break

        if CharFile.lower() == "n":
            sys.exit()
        else:
            print("Sorry, not a valid input. Try again.")
    CharFilePath = (f"My Characters/{CharFile}.txt") #Set character file path a global variable
Welcome()


#Following section defines functions for getting user's character information, such as the name and class.

#Function for setting character's name
def CharName():
    print("----------Character Name----------")
    print("\nWhat should your character be called?")
    while True:
        CharName = input("\nCharacter's name: ")
        if CharName == "":
            print("Sorry, name can't be empty. Try again.")
        else:
            print(CharName + ", eh? That's a great name!\n")
            return CharName

#Function for setting character's class.
def CharClass():
    AvailableClassesList = os.listdir("Data/Classes")
    AvailableClassesStr = ", ".join(os.listdir("Data/Classes/")) #Previous list as a more readable string
    global CharClass #Set CharClass as a global variable. Used in pathing.

    print("----------Character Class----------")
    print("\nThen, let's choose your character's class.")
    print("You can choose any of the following:", AvailableClassesStr, "\n")
    while True:
        ClassInfo = input("Do you need more information about the different classes? (y/n): ")
        if ClassInfo.lower() == "n":
            break
        if ClassInfo.lower() == "y":
            while True:
                ClassInfo = input("\nWhich class do you need more information about? (exit with empty input): ")
                if ClassInfo == "":
                    print("Empty input. Leaving class descriptions. \n")
                    break
                else:
                    ClassInfo = ClassInfo.lower() #Turn into all lowercase to ensure next line works correctly
                    ClassInfo = ClassInfo[0].upper() + ClassInfo[1:]#Capitalise first letter of ClassInfo, class directories are case sensitive
                    if ClassInfo not in AvailableClassesList:
                        print("Sorry, not a valid input. Try that again.")
                        continue

                    ClassDescriptionFile = os.path.join(f"Data/Classes/{ClassInfo}/Description.txt") #Path to description file
                    ClassDescriptionFile = open(ClassDescriptionFile, "r")
                    ClassDescription = ClassDescriptionFile.read()
                    print(ClassDescription, "\n")
                    ClassDescriptionFile.close()
        else:
            print("Sorry, not a valid input. Try that again.\n")

    while True:
        print("\nWhat should your character's class be?")
        CharClass = input("\nCharacter's class: ")
        if CharClass == "":
            print("Input can't be empty. Try again.")
            continue

        CharClass.lower() #Turn to lowercase to make sure next line works correctly
        CharClass = CharClass[0].upper() + CharClass[1:] #Capitalise first letter of user's input because directory names are case-sensitive

        if CharClass not in AvailableClassesList:
            print("Sorry, not a valid input. Try that again.")
        else:
            print("Set", CharClass, "as your class.\n")
            break
    return CharClass

#Function for setting character's subclass
def CharSubClass():
    global CharSubClass #Global variable for use in pathing
    AvailableSubClasses = os.listdir(f"Data/Classes/{CharClass}") #List files in class' directory
    AvailableSubClasses.remove("Description.txt") #Remove description file from list
    AvailableSubClasses.remove(f"{CharClass}.txt") #Remove main race from list
    AvailableSubClassesStr = "".join(AvailableSubClasses) #Join into one string, set as a separate variable. List is needed for comparing if the user made a valid input.
    AvailableSubClassesStr = AvailableSubClassesStr.replace(".txt", "") #Remove file format from the string

    print("----------Character subclass----------")
    if len(AvailableSubClasses) >= 1: #All class directories should contain the main race and a description file. #All other files are assumed to be subraces.
        print("\nFound available subclasses:", AvailableSubClassesStr)
        while True:
            CharSubClass = input("\nPick which subclass?: ")
            if CharSubClass == "":
                print("Sorry, input can't be empty. Try again.\n")
                continue

            CharSubClass = CharSubClass.lower() #Turn to lowercase to make sure next line works correctly
            CharSubClass = CharSubClass[0].upper() + CharSubClass[1:] + ".txt" #Capitalise first letter of user's input because directory names are case-sensitive. Needs file format at the end for comparing for a valid input.

            if CharSubClass not in AvailableSubClasses:
                print("Sorry, not an available subclass. Try again.")
            else: #Goes here if user picked a valid subclass
                break
        
        CharSubClass = CharSubClass.replace(".txt", "") #Remove file format from the string again
        print("Picked", CharSubClass, "for your subclass.\n")
        return CharSubClass
    else:
        print("No available subclasses for this class.\n")
        return "No subclass selected"

#Function for setting character's race.
def CharRace():
    global CharRace #Set as a global variable, used for file paths
    AvailableRacesList = os.listdir("Data/Races/")
    AvailableRacesStr = ", ".join(os.listdir("Data/Races/"))

    print("----------Character Race----------")
    print("\nLet's choose your character's race.")
    print("You can choose any of the following:", AvailableRacesStr)
    while True:
        RaceInfo = input("\nDo you need more information about the different races? (y/n): ")
        if RaceInfo.lower() == "n":
            break
        if RaceInfo.lower() == "y":
            while True:
                RaceInfo = input("\nWhich race do you need more information about? (exit with empty input): ")
                if RaceInfo == "":
                    print("Empty input. Leaving class descriptions.")
                    break
                RaceInfo = RaceInfo.lower() #Turn into an all-lowercase string to ensure next line works correctly.
                RaceInfo = RaceInfo[0].upper() + RaceInfo[1:] #Capitalise first letter of input, class directories are case-sensitive.
                if RaceInfo not in AvailableRacesList:
                    print("Sorry, not a valid input. Try that again.")
                    continue
                try:
                    RaceDescriptionFile = os.path.join(f"Data/Races/{RaceInfo}/Description.txt") #Path to description file
                    RaceDescriptionFile = open(RaceDescriptionFile, "r")
                    print("Reading file...")
                    RaceDescription = RaceDescriptionFile.read()
                    print("\n", RaceDescription, "\n")
                    print("Finished reading file. Closing.")
                    RaceDescriptionFile.close()
                except FileNotFoundError:
                    print("Sorry, description file could not be found.")
                    continue
        else:
            print("Sorry, not a valid input. Try that again.")

    print("\nWhat should your character's Race be?")
    while True:
        CharRace = input("Character's Race: ")
        if CharRace == "":
            print("Sorry, input can't be empty. Try again.\n")
            continue

        CharRace = CharRace[0].upper() + CharRace[1:] #Capitalise first letter of user's input, as folder names are case-sensitive
        if CharRace not in AvailableRacesList:
            print("Sorry, not a valid input. Try that again.\n")
        else:
            print("Set", CharRace + " as your race.\n")
            break
    return CharRace

def CharSubRace():
    global CharSubRace #Needs to be a global variable for pathing
    AvailableSubRaces = os.listdir(f"Data/Races/{CharRace}")
    AvailableSubRaces.remove("Description.txt") #Remove description file from list
    AvailableSubRaces.remove(f"{CharRace}.txt") #Remove main race from list
    AvailableSubRacesStr = "".join(AvailableSubRaces) #Join into one string
    AvailableSubRacesStr = AvailableSubRacesStr.replace(".txt", "") #Remove file format from the string

    print("----------Character subrace----------")
    if len(AvailableSubRaces) >= 1: #All race directories should contain the main race and a description file.
                                    #All other files are assumed to be subraces.
        print("\nFound available subraces:", AvailableSubRacesStr)
        while True:
            CharSubRace = input("\nPick which subrace?: ")
            if CharSubRace == "":
                print("Sorry, input can't be empty. Try again.")
                continue

            CharSubRace = CharSubRace.lower() #Turn to lowercase to make sure next line works correctly
            CharSubRace = CharSubRace.title() #Capitalise each first letter
            CharSubRace = CharSubRace + ".txt" #Used for comparing on the following if statement

            if CharSubRace not in AvailableSubRaces:
                print("Sorry, not an available subrace. Try again.")
            else:
                break

        CharSubRace = CharSubRace.replace(".txt", "") #Remove file format from the string again
        print("Picked", CharSubRace, "for your subrace.")
        return CharSubRace
    else:
        print("No available subraces for this race.\n")
        return "No subrace selected"

#Function for setting character's background
def CharBackground():
    AvailableBGList = os.listdir("Data/Backgrounds")
    AvailableBGStr = ", ".join(AvailableBGList)
    AvailableBGStr = AvailableBGStr.replace(".txt", "") #Remove file format from the string
    print("\n----------Character Background----------")
    print("\nLet's set your background.")
    print("Your background is a good indicator of where your character comes from,")
    print("and may give some items, features and extra languages.")
    print("\nAvailable backgrounds:", AvailableBGStr)
    while True:
        CharBG = input("\nChoose which background?: ")
        CharBG = CharBG.lower()
        CharBG = CharBG.title()
        CharBG = CharBG + ".txt"
        if CharBG not in AvailableBGList: #Ensures user chooses a valid background
            print("Sorry, not a valid background. Try again please.")
        else:
            CharBG = CharBG.replace(".txt", "")
            print("Chose", CharBG + ".")
            break
    
    print("\nReading background information...")
    OpenFile = open(f"Data/Backgrounds/{CharBG}.txt", "r")
    Content = OpenFile.readlines()
    CharBG = Content #CharBG set to equal content in the file
    CharBG = "".join(CharBG) #Join into a readable string
    print("Background information found. ")
    print("Closing file.\n")
    OpenFile.close()
    return CharBG

#Function for setting character's personality traits.
def CharPersonality():
    TraitsList = []
    Count = 1

    print("----------Character Personality----------")
    print("\nThen, let's set your character's personality traits.")
    print("These are for roleplay reasons, and can be left empty.")
    print("Write each personality trait on a new input.")
    print("Can write a maximum of 5 traits.")
    print("Can also write fewer, simply make an empty input to exit.")

    while Count <= 5:
        Trait = input(f"\nPersonality trait {Count}: ")
        if Trait == "":
            break
        else:
            Count += 1
            TraitsList.append(Trait + "\n")

    print("Personality traits set.\n")
    TraitsList = "\n".join(TraitsList)
    return TraitsList

#Function for setting character's ideals.
def CharIdeals():
    IdealsList = []
    Count = 1

    print("----------Character Ideals----------")
    print("\nThen, let's set your character's ideals.")
    print("Ideals can be anything from tradition to power to charity.")
    print("These are for roleplay reasons, and can be left empty.")
    print("Write each personality trait on a new input.")
    print("Can write a maximum of 5 ideals.")
    print("Can also write fewer, simply make an empty input to exit.")

    while Count <= 5:
        Ideal = input(f"\nIdeal {Count}: ")
        if Ideal == "":
            break
        else:
            Count += 1
            IdealsList.append(Ideal + "\n")

    print("Ideals set.\n")
    IdealsList = "\n".join(IdealsList)
    return IdealsList

#Function for getting character's bonds
def CharBonds():
    BondsList = []
    Count = 1
    print("----------Character Bonds----------")
    print("\nLet's set your character's bonds.")
    print("Bonds represent your character's... well, bonds.")
    print("Things like your tribe, family, etc.")
    print("These are for roleplay reasons, and can be left empty.")
    print("Write each bond on a new input.")
    print("Can write a maximum of 5 bonds.")
    print("Can also write fewer, simply make an empty input to exit.")

    while Count <= 5:
        Bond = input(f"\nBond {Count}: ")
        if Bond == "":
            break
        else:
            Count += 1
            BondsList.append(Bond + "\n")

    print("Bonds set.\n")
    BondsList = "\n".join(BondsList)
    return BondsList

#Function for setting character's flaws
def CharFlaws():
    FlawsList = []
    Count = 1
    print("----------Character Flaws----------")
    print("\nLet's set your character's Flaws.")
    print("Flaws are things like indulging in pleasures too often or being gullible.")
    print("These are for roleplay reasons, and can be left empty.")
    print("Write each flaw on a new input.")
    print("Can write a maximum of 5 flaws.")
    print("Can also write fewer, simply make an empty input to exit.")

    while Count <= 5:
        Flaw = input(f"\nFlaw {Count}: ")
        if Flaw == "":
            break
        else:
            Count += 1
            FlawsList.append(Flaw + "\n")

    print("Flaws set.\n")
    FlawsList = "\n".join(FlawsList)
    return FlawsList

#Function for setting character's alignment.
def CharAlignment():
    AlignmentsList = ["lawful good", "neutral good", "chaotic good", "lawful neutral", "neutral", "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"]
    AlignmentsAbbreviated = ["lg", "ng", "cg", "ln", "n", "cn", "le", "ne", "ce"]

    print("----------Character Alignment----------")
    print("\nLet's set your character's alignment.")
    print("An alignment is basically how good or evil your character is,")
    print("and how true they are to laws vs tending toward chaos.\n")
    print("Setting your character's alignment in D&D is mostly for roleplay reasons")
    print("and **usually** has no in-game effects.\n")
    print("Can choose from:")
    print("Lawful Good, Neutral Good, Chaotic Good")
    print("Lawful Neutral, Neutral, Chaotic neutral")
    print("Lawful Evil, Neutral Evil, Chaotic Evil")
    print("Can also be left empty.\n")
    print("You can also use the first letter of both words to set alignment, so")
    print("for example, Lawful Good would be input as LG.")
    while True:
        Alignment = input("\nAlignment: ")
        Alignment = Alignment.lower() #Turn to all lowercase
        if Alignment in AlignmentsList or Alignment in AlignmentsAbbreviated: #Accepts an empty input or abbreviated or fully typed out alignment
            break
        elif Alignment == "":
            print("Leaving empty for now.\n")
            return "Alignment not set"
        else:
            print("Not a valid alignment or not empty. Please try again.")

    if Alignment in AlignmentsAbbreviated:
        Alignment = Alignment.upper()
        print("Set alignment to:", Alignment, "\n")
        return Alignment
    
    if Alignment in AlignmentsList:
        Alignment = Alignment[0].upper() + Alignment[1:] #Capitalise first letter, looks neat
        print("Set alignment to:", Alignment, "\n")
        return Alignment

#Function for setting character's level. Can be between 1 to 20.
def CharLevel():
    global CharLevel

    print("----------Character Level----------")
    print("\nThen, we shall set the character's level.")
    print("Usually adventurers start at level 1, but if you're unsure ask your Dungeon Master.")
    print("Maximum level is 20.")
    while True:
        try:
            CharLevel = int(input("\nCharacter's level: "))
        except ValueError:
            print("Sorry, not an integer. Try that again.")
            continue
        if CharLevel > 20:
            print("Sorry, level can't be above 20. Try that again.")
            continue
        if CharLevel < 1:
            print("Sorry, level can't be zero or negative. Try that again.")
            continue
        else:
            print("Set character's level to", str(CharLevel) + ".\n")
            return CharLevel

#Define function for setting character's ability scores
def CharAbilityScores():
    #Define abilities as global variables so they can be used outside this function
    global Str
    global Dex
    global Con
    global Int
    global Wis
    global Cha
    global StrMod
    global DexMod
    global ConMod
    global IntMod
    global WisMod
    global ChaMod
    AbilityList = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    print("----------Character Ability Scores----------")
    print("\nLet's set your character's ability scores.")
    print("Ability scores measure how well your character excels in certain abilites.")
    print("10 is considered average compared to the normal human.")
    print("\nYou can either roll the stats yourself, or let this program roll for you.")
    print("If you choose yes, the program will roll stats as according to the official rules.")
    print("If you roll manually, get out your 4d6 and start rolling. The program will ask for your rolls.")

    Reroll = "y" #Set temporary value to this variable. Used in breaking out of loops when asking if the user wants to reroll stats.
    while True:
        RollYesNo = input("\nLet the program roll for you? (y/n): ")
        if RollYesNo.lower() == "y":
            while True:
                RollList = []
                FinalList = []
                Count = 0
                ScoreTotal = 0
                #Loop repeats six times, for each ability score.
                for Roll in range(6):
                    #Loop repeats 4 times so each ability score is rolled 4 times.
                    for Roll in range(4):
                            Roll = random.randint(1,6)
                            RollList.append(str(Roll))
                    Count += 1
                    print(f"Roll {Count}: {", ".join(RollList)}")
                    RollList.remove(min(RollList)) #Remove lowest roll from the list (D&D rules)
                    RollListInt = map(int, (RollList)) #Remap list to contain integers so they can be summed
                    SummedRolls = sum(RollListInt) #Sum items in the list
                    FinalList.append(SummedRolls) #Append the roll to the final list of scores user can allot
                    ScoreTotal += SummedRolls #Add roll to the score total
                    print(f"Total, lowest removed: {SummedRolls}\n")
                    RollList = []

                print("Total score to allot from rolls:", ScoreTotal)
                print("Final rolls to allot:", ", ".join(map(str, FinalList))) #Must be remapped to a string to avoid errors
                print("\nIf you're not satisfied with these rolls, you can reroll them.")
                while True:
                    Reroll = input("\nReroll ability scores? (y/n): ")
                    Reroll = Reroll.lower()
                    if Reroll == "y":
                        ScoreTotal = 0
                        print("\n")
                        break
                    if Reroll == "n":
                        break #Breaks out of the first loop
                    else:
                        print("Sorry, not a valid input. Try again.")
                        continue #Continues this loop with an invalid input

                if Reroll == "n": #Breaks out of the loop for rolling if user put no
                    break
                else: #If the input was yes, restart the loop that rolls for stats
                    continue
        if Reroll == "n": #Breaks out of the loop asking if the program should roll for the user if user puts no
            break

        if RollYesNo.lower() == "n":
            FinalList = [] 
            print("Roll your stats with real life dice and set values accordingly.")
            while len(FinalList) <= 5:
                try:
                    Stat = int(input("\nFinal roll, lowest removed: "))
                    if Stat > 18:
                        print("Sorry, a roll can't be higher than 18. Try again.")
                        continue
                    if Stat <= 3:
                        print("Sorry, a roll can't be lower than 3. Try again.")
                        continue
                    if Stat <= 18:
                        FinalList.append(Stat)
                except ValueError:
                    print("Sorry, not an integer. Try again.")
                    continue
            break

        else:
            print("Sorry, not a valid input. Try again.")

    print("--------------------")
    print("\nNow, let's get to assigning the rolls to your character's abilities.")
    print("We will go down the list as in the official 5th edition character sheet.\n")

    while True:
        print("Scores left to allot:", ", ".join(map(str, FinalList)))
        print("Abilities left to allot:", ", ".join(AbilityList))
        try:
            Str = int(input("Strength score: "))
        except ValueError:
            print("Not an integer. Try again please.\n")
            continue
        if Str not in FinalList:
            print("That is not a value you rolled. Try again please.")
        else:
            print("\nAssigned", Str, "to Strength.")
            StrMod = math.floor((Str-10)/2)
            print("Your strength modifier is:", StrMod, "\n")
            FinalList.remove(Str)
            AbilityList.remove("Strength")
            break

    while True:
        print("Scores left to allot:", ", ".join(map(str, FinalList)))
        print("Abilities left to allot:", ", ".join(AbilityList))
        try:
            Dex = int(input("Dexterity score: "))
        except ValueError:
            print("Not an integer. Try again please.\n")
            continue
        if Dex not in FinalList:
            print("That is not a value you rolled. Try again please.\n")
        else:
            print("\nAssigned", Dex, "to Dexterity.")
            DexMod = math.floor((Dex-10)/2)
            print("Your dexterity modifier is:", DexMod, "\n")
            FinalList.remove(Dex)
            AbilityList.remove("Dexterity")
            break
    
    while True:
        print("Scores left to allot:", ", ".join(map(str, FinalList)))
        print("Abilities left to allot:", ", ".join(AbilityList))
        try:
            Con = int(input("Constitution score: "))
        except ValueError:
            print("Not an integer. Try again please.\n")
            continue
        if Con not in FinalList:
            print("That is not a value you rolled. Try again please.\n")
        else:
            print("\nAssigned", Con, "to Constitution.")
            ConMod = math.floor((Con-10)/2)
            print("Your constitution modifier is:", ConMod, "\n")
            FinalList.remove(Con)
            AbilityList.remove("Constitution")
            break

    while True:
        print("Scores left to allot:", ", ".join(map(str, FinalList)))
        print("Abilities left to allot:", ", ".join(AbilityList))
        try:
            Int = int(input("Intelligence score: "))
        except ValueError:
            print("Not an integer. Try again please.\n")
            continue
        if Int not in FinalList:
            print("That is not a value you rolled. Try again please.\n")
        else:
            print("\nAssigned", Int, "to Intelligence.")
            IntMod = math.floor((Int-10)/2)
            print("Your intelligence modifier is:", IntMod, "\n")
            FinalList.remove(Int)
            AbilityList.remove("Intelligence")
            break

    while True:
        print("Scores left to allot:", ", ".join(map(str, FinalList)))
        print("Abilities left to allot:", ", ".join(AbilityList))
        try:
            Wis = int(input("Wisdom score: "))
        except ValueError:
            print("Not an integer. Try again please.\n")
            continue
        if Wis not in FinalList:
            print("That is not a value you rolled. Try again please.\n")
        else:
            print("\nAssigned", Wis, "to Wisdom.")
            WisMod = math.floor((Wis-10)/2)
            print("Your wisdom modifier is:", WisMod, "\n")
            FinalList.remove(Wis)
            AbilityList.remove("Wisdom")
            break

    while True:
        print("Scores left to allot:", ", ".join(map(str, FinalList)))
        print("Abilities left to allot:", ", ".join(AbilityList))
        try:
            Cha = int(input("Charisma score: "))
        except ValueError:
            print("Not an integer. Try again please.\n")
            continue
        if Cha not in FinalList:
            print("That is not a value you rolled. Try again please.\n")
        else:
            print("\nAssigned", Cha, "to Charisma.")
            ChaMod = math.floor((Cha-10)/2)
            print("Your charisma modifier is:", ChaMod, "\n")
            FinalList.remove(Cha)
            AbilityList.remove("Charisma")
            break
    print("--------------------")
    print("\nDone setting ability scores.")
    print("\nAssigned the following:")
    print(f"Strength: {Str}, modifier: {StrMod}\nDexterity: {Dex}, modifier: {DexMod}\nConstitution: {Con}, modifier: {ConMod}")
    print(f"Intelligence: {Int}, modifier: {IntMod}\nWisdom: {Wis}, modifier: {WisMod}\nCharisma: {Cha}, modifier: {ChaMod}")

#Following section defines functions for setting character's proficiencies and features as well as armor class, hitpoints, hit dice, and physical traits.
#All of the functions work virtually the same, just with different variable names.
#I shall explain how the following function works, as well as CharClassFeats() due to the slight difference. 

#Function for automatically finding and setting character's hit dice
def CharHitDice():
    global HitDice #Set to a global variable for use in determining hitpoints
    LineIndex = 0 #Variable used to determine which line hitdice data is in
    HitDiceFound = False #Variable used to determine if the data was found, set to true if found
    HitDiceLookup = "[Hit Dice]" #String to search for in the file. The following line after this contains hit dice data

    print("\n----------Character Hit Dice----------")
    print("\nAutomatically searching for hit dice data...")
    OpenFile = open(f"Data/Classes/{CharClass}/{CharClass}.txt", "r") #Open character class' file for reading
    Content = OpenFile.readlines() #Read through file content

    #This loop will read each line until it finds the lookup variable.
    for Line in Content:
        LineIndex += 1 #Increases by one for each iterated line
        if HitDiceLookup in Line:
            HitDiceFound = True #Set HitDiceFound to true if the lookup was found
            break #Break once the lookup is found

    if HitDiceFound == True: #Determines if the lookup was found
        HitDice = (Content[LineIndex:LineIndex+1]) #Get data as a list, looks like a mess. Line index variables are used to cut what content the program reads.
        HitDice = "".join(HitDice) #Join into a readable string
        HitDice = HitDice.rstrip() #Remove newline
        HitDice = HitDice[10::] #Parse first 10 characters from the line, so the variable's data looks something like "1d12" (formatted as Hit dice: 1dxx in the file)
        HitDiceWithLevel = f"{CharLevel}{HitDice[1::]}" #Variable is a string that looks like "2d12" if the character's level is 2, and hit die is the d12.
        print(f"Your hit dice: {HitDiceWithLevel}")
        print("Hit Dice automatically set according to level. Closing file.\n")
        OpenFile.close() #Close file
        return HitDiceWithLevel
            
    else: #Goes here if the lookups were not found, and hence HitDiceFound is still set to false
        print("Hit dice information could not be found in the file.")
        print("Please set your character's hit dice manually.")
        print(f"Hit dice information can be found under Data/Classes/{CharClass}/{CharClass}.txt")
        print("Closing file.")
        OpenFile.close()

#Function for setting character's hitpoints. Defined here because this is the order the functions are called in.
def CharHP():
    HitPointTotal = 0
    HitDiceNumber = int(HitDice[2::]) #Turn the global HitDice (which looks like 1d12 for example) into simply the number after the d (eg. 1d12 turns into 12)
    HitDiceAverage = HitDiceNumber / 2 + 1 #Average + 1, D&D rules
    print("----------Character Hitpoints----------")
    print("\nYour character is level", str(CharLevel) + ".")
    print("Your character's hit die is the", HitDice[1::] + ".")
    print(f"Do you wish to roll or use the average ({HitDiceAverage}) for increasing hit points per level?")
    while True:
        RollOrAverage = input("\nRolls (r) or average (a)? ")
        
        if RollOrAverage == "r":
            for HitPointsRoll in range(CharLevel): #Character level used to determine how many times hitpoints need to be rolled for
                HitPointsRoll = random.randint(1,(HitDiceNumber))
                print("\nRolled:", str(HitPointsRoll) + ".")
                print("Adding constitution modifier", ConMod, "to the roll:", HitPointsRoll + ConMod)
                HitPointTotal += HitPointsRoll + ConMod
            print("\nHit point total:", str(HitPointTotal) + ".\n")
            return HitPointTotal
        
        if RollOrAverage == "a":
            print("\nCalculating total hit points...")
            for x in range(CharLevel): #Repeat an amount of times equal to character's level
                HitPointTotal += HitDiceAverage
                HitPointTotal += ConMod
            print("\nHit points total:", HitPointTotal, "\n")
            return HitPointTotal
        else:
            print("Sorry, not a valid input. Try again please.\n")

#Function for character's AC
def CharAC():
    print("----------Character Armor Class----------")
    print("\nFor setting the character's armor class, you unfortunately have to")
    print("see what it is manually and put it here.")
    print("\nArmor class without armor is 10 + your dexterity modifier.")
    print("Armor class with armor depends on the armor you're equipping.")
    print("Can also leave it empty and edit it later in the character file.")
    while True:
        try:
            ArmorClass = int(input("\nArmor class: "))
        except ValueError:
            print("Sorry, not an integer. Try again.\n")
            continue
        if ArmorClass == "":
            print("Leaving empty for now.\n")
            return "Armor class left empty"
        else:
            print("Set armor class to", ArmorClass, "\n")
            return ArmorClass

#Function for setting character's class features, works the same as CharClassFeats() but with an extra lookup.
def CharClassFeats():
    global FeaturesStartLineIndex #Set these two to global variables for finding proficiency bonus later.
    global FeaturesEndLineIndex   #This is because the proficiency bonus function needs to iterate through the lines between these two indexes.
    FeaturesStartLineIndex = 0 #Variable used to determine which line features start in
    FeaturesEndLineIndex = 0 #Variable used to determine which line features end in
    FeaturesStartLookup = "[Start Features and Levels Info]" #String to search for in the file to indicate the start of class features
    FeaturesEndLookup = "[End Features and Levels Info]" #String to search for in the file to indicate the end of class features
    FeaturesStart = False #Variable used to determine if the start of features were found, set to true if found
    FeaturesEnd = False #Variable used to determine if the end of features were found, set to true if found
    print("----------Character Features and Levels----------")
    print("\nSearching for class features and levels automatically...")
    OpenFile = open(f"Data/Classes/{CharClass}/{CharClass}.txt", "r") #Open relevant file for reading
    print("Reading file...")
    Content = OpenFile.readlines() #Read through file content

    #This loop will read each line until it finds FeaturesStartLookup.
    for Line in Content:
        FeaturesStartLineIndex += 1 #Increases by one for each iterated line
        if FeaturesStartLookup in Line:
            FeaturesStart = True #Set FeaturesStart to true if the lookup was found
            break #Break once the lookup is found

    #Same as the previous loop, except for finding the end of the class features data.
    for Line in Content:
        FeaturesEndLineIndex += 1
        if FeaturesEndLookup in Line:
            FeaturesEnd = True #Set FeaturesEnd to true if the lookup was found
            break #Break once the lookup is found

    if FeaturesStart == True and FeaturesEnd == True: #Determines if the lookups were found
        ClassFeatures = (Content[FeaturesStartLineIndex:FeaturesEndLineIndex-1]) #Get class features as a list, looks like a total mess. Line index variables are used to cut what content the program reads.
        ClassFeatures = "".join(ClassFeatures) #To make it readable, join into one string.
        print("Found class features and levels. Closing file.\n")
        OpenFile.close() #Close file
        return ClassFeatures #Returns all class features as one list
    
    else: #If FeaturesEnd and/or FeaturesStart is false, run this. Means the relevant data could not be found in the file.
        print("Class features could not be set automatically.")
        print("Please set them manually.")
        print(f"Class features information can be found under Data/Classes/{CharClass}/{CharClass}.txt")
        print("Closing file.")
        OpenFile.close()

#Function for setting character's subclass' features
def CharSubClassFeats():
    print("----------Character Subclass features----------")
    print("\nReading subclass file...")
    OpenFile = open(f"Data/Classes/{CharClass}/{CharSubClass}.txt", "r")
    Content = OpenFile.readlines()
    SubClassFeats = Content
    SubClassFeats = "".join(SubClassFeats) #Join into a readable string
    print("Subclass features found. Closing file.\n")
    OpenFile.close()
    return SubClassFeats

#Function for finding race features.
#Same as CharClassFeatures(), just with different variable names.
def CharRaceFeats():
    StartLineIndex = 0
    EndLineIndex = 0
    FeatsStartLookup = "[Start Features]"
    FeatsEndLookup = "[End Features]"
    FeatsStart = False
    FeatsEnd = False
    print("----------Character Features (Race)----------")
    print("\nSearching for race features automatically...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if FeatsStartLookup in Line:
            FeatsStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if FeatsEndLookup in Line:
            FeatsEnd = True
            break

    if FeatsStart == True and FeatsEnd == True:
        RaceFeats = (Content[StartLineIndex:EndLineIndex-1])
        RaceFeats = "".join(RaceFeats)
        print("Found race features automatically. Closing file.\n")
        OpenFile.close()
        return RaceFeats
    
    else:
        print("Class features could not be set automatically.")
        print("Please set them manually.")
        print(f"Race features information can be found under Data/Races/{CharRace}/{CharRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for finding subrace features.
#Same as CharClassFeatures(), just with different variable names.
def CharSubRaceFeats():
    StartLineIndex = 0
    EndLineIndex = 0
    FeatsStartLookup = "[Start Features]"
    FeatsEndLookup = "[End Features]"
    FeatsStart = False
    FeatsEnd = False
    print("----------Character Features (Subrace)----------")
    print("\nSearching for subrace features automatically...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharSubRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if FeatsStartLookup in Line:
            FeatsStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if FeatsEndLookup in Line:
            FeatsEnd = True
            break

    if FeatsStart == True and FeatsEnd == True:
        SubRaceFeats = (Content[StartLineIndex:EndLineIndex-1])
        SubRaceFeats = "".join(SubRaceFeats)
        print("Found subrace features automatically. Closing file.\n")
        OpenFile.close()
        return SubRaceFeats
    
    else:
        print("Class features could not be set automatically.")
        print("Please set them manually.")
        print(f"Race features information can be found under Data/Races/{CharSubRace}/{CharSubRace}.txt")
        print("Closing file.")
        OpenFile.close()


#Following section is for setting character proficiencies. Still virtually same as CharClassFeatures(), just with different variable names.
#Function for finding character's proficiency bonus according to level
def CharProfBonus():
    LineIndex = 0
    ProfBonusFound = False
    LevelLookup = f"Level {CharLevel}" #Character level used here to find the correct proficiency bonus
    print("----------Character Proficiency Bonus----------")
    print("\nAutomatically searching for proficiency bonus data according to level...")
    OpenFile = open(f"Data/Classes/{CharClass}/{CharClass}.txt", "r")
    Content = OpenFile.readlines()
    Content = Content[FeaturesStartLineIndex:FeaturesEndLineIndex] #Iterate through the lines between these two indexes, hence why they needed to be global

    for Line in Content:
        LineIndex += 1
        if LevelLookup in Line:
            ProfBonusFound = True
            break

    if ProfBonusFound == True:
        ProfBonus = (Content[LineIndex:LineIndex+1])
        ProfBonus = "".join(ProfBonus)
        ProfBonus = ProfBonus.rstrip()
        ProfBonus = ProfBonus[20::]
        print("Your proficiency bonus:", ProfBonus)
        print("Proficiency bonus automatically set. Closing file.\n")
        OpenFile.close()
        return ProfBonus
            
    else:
        print("\nProficiency bonus data could not be found in the file.")
        print("Please set your character's proficiency bonus manually.")
        print(f"Data can be found under Data/Classes/{CharClass}/{CharClass}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for finding character's proficiencies, provided by selected class.
#Same as CharClassFeatures(), just with different variable names.
def CharClassProfs():
    StartLineIndex = 0
    EndLineIndex = 0
    ProfsStartLookup = "[Start Proficiencies and Hit Dice]"
    ProfsEndLookup = "[End Proficiencies and Hit Dice]"
    ProfsStart = False
    ProfsEnd = False
    print("----------Character Proficiencies (Class)----------")
    print("\nSearching for class proficiencies automatically...")
    OpenFile = open(f"Data/Classes/{CharClass}/{CharClass}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if ProfsStartLookup in Line:
            ProfsStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if ProfsEndLookup in Line:
            ProfsEnd = True
            break
    
    if ProfsStart == True and ProfsEnd == True:
        ClassProfs = (Content[StartLineIndex:EndLineIndex-1])
        ClassProfs = "".join(ClassProfs)
        print("Found class features automatically. Closing file.\n")
        OpenFile.close()
        return ClassProfs
    
    else:
        print("Class features could not be set automatically.")
        print("Please set them manually.")
        print(f"Class features information can be found under Data/Classes/{CharClass}/{CharClass}.txt")
        print("Closing file.")
        OpenFile.close()

#Function for setting character's proficiencies provided by the chosen race.
#Same as CharClassFeatures(), just with different variable names.
def CharRaceProfs():
    StartLineIndex = 0
    EndLineIndex = 0
    ProfsStartLookup = "[Start Proficiencies]"
    ProfsEndLookup = "[End Proficiencies]"
    ProfsStart = False
    ProfsEnd = False
    print("----------Character Proficiencies (Race)----------")
    print("\nSearching for race proficiencies automatically...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if ProfsStartLookup in Line:
            ProfsStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if ProfsEndLookup in Line:
            ProfsEnd = True
            break

    if ProfsStart == True and ProfsEnd == True:
        RaceProfs = (Content[StartLineIndex:EndLineIndex-1])
        RaceProfs = "".join(RaceProfs)
        print("Found race proficiencies automatically. Closing file.\n")
        OpenFile.close()
        return RaceProfs
    
    else:
        print("Race features could not be set automatically.")
        print("Please set them manually.")
        print(f"Race features information can be found under Data/Races/{CharRace}/{CharRace}.txt")
        print("Closing file.")
        OpenFile.close()

#Function for setting subrace's proficiencies
#Same as CharClassFeatures(), just with different variable names.
def CharSubRaceProfs():
    StartLineIndex = 0
    EndLineIndex = 0
    ProfsStartLookup = "[Start Proficiencies]"
    ProfsEndLookup = "[End Proficiencies]"
    ProfsStart = False
    ProfsEnd = False
    print("----------Character Proficiencies (Subrace)----------")
    print("\nSearching for subrace proficiencies automatically...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharSubRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if ProfsStartLookup in Line:
            ProfsStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if ProfsEndLookup in Line:
            ProfsEnd = True
            break

    if ProfsStart == True and ProfsEnd == True:
        SubRaceProfs = (Content[StartLineIndex:EndLineIndex-1])
        SubRaceProfs = "".join(SubRaceProfs)
        print("Found subrace proficiencies automatically. Closing file.\n")
        OpenFile.close()
        return SubRaceProfs
    
    else:
        print("\nSubrace proficiencies could not be set automatically.")
        print("Please set them manually.")
        print(f"Subrace proficiencies can be found under Data/Races/{CharRace}/{CharSubRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for setting character's ability score increases (race)
def CharRaceASI():
    StartLineIndex = 0
    EndLineIndex = 0
    ASIStartLookup = "[Ability Score Increase Start]"
    ASIEndLookup = "[Ability Score Increase End]"
    ASIStart = False
    ASIEnd = False
    print("----------Character Ability Score Increase (Race)----------")
    print("\nSearching for ability score increases...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if ASIStartLookup in Line:
            ASIStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if ASIEndLookup in Line:
            ASIEnd = True
            break

    if ASIStart == True and ASIEnd == True:
        CharASI = (Content[StartLineIndex:EndLineIndex-1])
        CharASI = "".join(CharASI)
        print("Found ability score increases automatically. Closing file.\n")
        OpenFile.close()
        return CharASI
    
    else:
        print("\nCharacter ability score increase could not be set automatically.")
        print("Please set them manually.")
        print(f"Ability score increases can be found under Data/Races/{CharRace}/{CharRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for setting character's ability score increase from subrace
def CharSubRaceASI():
    StartLineIndex = 0
    EndLineIndex = 0
    ASIStartLookup = "[Ability Score Increase Start]"
    ASIEndLookup = "[Ability Score Increase End]"
    ASIStart = False
    ASIEnd = False
    print("----------Character Ability Score Increase (Subrace)----------")
    print("\nSearching for ability score increases...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharSubRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if ASIStartLookup in Line:
            ASIStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if ASIEndLookup in Line:
            ASIEnd = True
            break

    if ASIStart == True and ASIEnd == True:
        CharASI = (Content[StartLineIndex:EndLineIndex-1])
        CharASI = "".join(CharASI)
        print("Found ability score increases automatically. Closing file.\n")
        OpenFile.close()
        return CharASI
    
    else:
        print("\nCharacter ability score increases could not be set automatically.")
        print("Please set them manually.")
        print(f"They can be found under Data/Races/{CharRace}/{CharSubRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for setting character's speed
def CharSpeed():
    LineIndex = 0
    SpeedFound = False
    SpeedLookup = "[Speed]"
    print("----------Character Speed----------")
    print("\nAutomatically searching for character's speed...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharRace}.txt", "r")
    Content = OpenFile.readlines()
    for Line in Content:
        LineIndex += 1
        if SpeedLookup in Line:
            SpeedFound = True
            break

    if SpeedFound == True:
        CharSpeed = (Content[LineIndex:LineIndex+1])
        CharSpeed = "".join(CharSpeed)
        CharSpeed = CharSpeed.rstrip()
        print("Character's speed found automatically.")
        print("Closing file.\n")
        OpenFile.close()
        return CharSpeed
            
    else:
        print("\nSpeed data could not be found in the file.")
        print("Please set your character's speed manually.")
        print(f"Speed can be found under Data/Races/{CharRace}/{CharRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for finding character's size and weight
def CharSizeWeight():
    StartLineIndex = 0
    EndLineIndex = 0
    SWStartLookup = "[Size and Weight Start]"
    SWEndLookup = "[Size and Weight End]"
    SWStart = False
    SWEnd = False
    print("----------Character Size and Weight----------")
    print("\nSearching for character size and weight...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if SWStartLookup in Line:
            SWStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if SWEndLookup in Line:
            SWEnd = True
            break

    if SWStart == True and SWEnd == True:
        CharSizeWeight = (Content[StartLineIndex:EndLineIndex-1])
        CharSizeWeight = "".join(CharSizeWeight)
        print("Found size and weight automatically. Closing file.\n")
        OpenFile.close()
        return CharSizeWeight
    
    else:
        print("\nCharacter size and weight could not be set automatically.")
        print("Please set it manually.")
        print(f"Size and weight can be found under Data/Races/{CharRace}/{CharRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for finding character's age
def CharAge():
    StartLineIndex = 0
    EndLineIndex = 0
    AgeStartLookup = "[Age Start]"
    AgeEndLookup = "[Age End]"
    AgeStart = False
    AgeEnd = False
    print("----------Character Age----------")
    print("\nSearching for character's age...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if AgeStartLookup in Line:
            AgeStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if AgeEndLookup in Line:
            AgeEnd = True
            break

    if AgeStart == True and AgeEnd == True:
        CharAge = (Content[StartLineIndex:EndLineIndex-1])
        CharAge = "".join(CharAge)
        print("Found character age automatically. Closing file.\n")
        OpenFile.close()
        return CharAge
    
    else:
        print("\nCharacter age could not be set automatically.")
        print("Please set it manually.")
        print(f"Age information can be found under Data/Races/{CharRace}/{CharRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

#Function for finding character's languages
def CharLangs():
    StartLineIndex = 0
    EndLineIndex = 0
    LangStartLookup = "[Languages Start]"
    LangEndLookup = "[Languages End]"
    LangStart = False
    LangEnd = False
    print("----------Character Languages----------")
    print("\nSearching character languages...")
    OpenFile = open(f"Data/Races/{CharRace}/{CharRace}.txt", "r")
    print("Reading file...")
    Content = OpenFile.readlines()

    for Line in Content:
        StartLineIndex += 1
        if LangStartLookup in Line:
            LangStart = True
            break

    for Line in Content:
        EndLineIndex += 1
        if LangEndLookup in Line:
            LangEnd = True
            break

    if LangStart == True and LangEnd == True:
        CharLangs = (Content[StartLineIndex:EndLineIndex-1])
        CharLangs = "".join(CharLangs)
        print("Found languages automatically. Closing file.\n")
        OpenFile.close()
        return CharLangs
    
    else:
        print("\nCharacter languages could not be set automatically.")
        print("Please set them manually.")
        print(f"Languages can be found under Data/Races/{CharRace}/{CharRace}.txt")
        print("Closing file.\n")
        OpenFile.close()

def CharLevelFeats():
    global Str
    global Dex
    global Con
    global Int
    global Wis
    global Cha
    global StrMod
    global DexMod
    global ConMod
    global IntMod
    global WisMod
    global ChaMod
    global FeatsList
    Feats = 0
    #Check how many feats or ability score increases user has
    if CharLevel >= 4:
        Feats += 1
    if CharLevel >= 8:
        Feats += 1
    if CharLevel >= 12:
        Feats += 1
    if CharLevel >= 16:
        Feats += 1
    if CharLevel >= 19:
        Feats += 1

    print("----------Character Level Features----------")
    print("\nEvery 4 levels your character gets to pick either an ability score increase, or a feat.")
    print("With an ability score increase, you can increase one ability score by two, or two ability scores by one.")
    print("Feats on the other hand can be powerful in combat or give additional proficiencies and languages.")
    print("\nYou can choose", Feats, "feats or ability score increases at your current level.")

    while Feats >= 1: #Stops this loop and exits function if the user doesn't have more available feats or ability increases
        print("\n--------------------")
        print("\nYou have", str(Feats), "feats or ability score increases left.")
        FeatOrASI = input("\nFeat (f) or ability score increase (asi)?: ")
        if FeatOrASI.lower() == "f":
                Exit = False #Used to keep track of exiting loops
                Feats -= 1 #User wanted a feat, reduce available feats by 1
                FeatsList = [] #List of feats selected by the user
                AvailableFeatsList = os.listdir("Data/Feats")
                AvailableFeatsStr = ", ".join(AvailableFeatsList)
                AvailableFeatsStr = AvailableFeatsStr.replace(".txt", "") #Remove file format from the string
                print("\n--------------------")
                print("\nAvailable feats:", AvailableFeatsStr)

                while True:
                    InfoSelect = input("\nShow information about a feat (i) or select one (s): ") #Goes back here if the info loop breaks
                    if InfoSelect == "":
                        print("Sorry, input can't be empty. Try again.")
                        continue #Restart loop if empty input detected

                    InfoSelect = InfoSelect.lower() #Make string into lowercase for comparing in the if statements

                    if InfoSelect == "i":
                        while True:
                            print("Available feats:", AvailableFeatsStr)
                            SelectFeat = input("\nShow info about which feat? (exit with empty input): ")
                            if SelectFeat == "":
                                print("Empty input. Exiting.\n")
                                break #Exit with empty input

                            SelectFeat = SelectFeat.lower() #Make string lowercase
                            SelectFeat = SelectFeat.title() #Capitalise first letter
                            SelectFeat = SelectFeat + ".txt" #Join .txt file format to the end to compare in the following if statement

                            if SelectFeat not in AvailableFeatsList:
                                print("Sorry, not a valid input. Try again.")
                                continue #Restarts loop to ask if the user wants info about a feat

                            else: #Goes here with a valid input
                                SelectFeat = SelectFeat.replace(".txt", "") #Remove .txt file format
                                print("\nReading file...")
                                OpenFile = open(f"Data/Feats/{SelectFeat}.txt", "r")
                                Content = OpenFile.readlines()
                                SelectFeat = Content
                                SelectFeat = "".join(SelectFeat) #Join into a readable string
                                print("\n" + SelectFeat)
                                print("\nFinished reading file. Closing.")
                                OpenFile.close()
                                print("--------------------")

                    if InfoSelect == "s":
                        while True:
                            SelectFeat = input("\nSelect which feat?: ")
                            if SelectFeat == "":
                                print("Sorry, input can not be empty. Try again.\n")
                                continue #Restart this loop

                            SelectFeat = SelectFeat.lower()
                            SelectFeat = SelectFeat.title()
                            SelectFeat = SelectFeat + ".txt"

                            if SelectFeat not in AvailableFeatsList:
                                print("Sorry, not a valid input. Try again.\n")
                            else:
                                SelectFeat = SelectFeat.replace(".txt", "")
                                print("\nReading file...")
                                OpenFile = open(f"Data/Feats/{SelectFeat}.txt", "r")
                                Content = OpenFile.readlines()
                                SelectFeat = Content
                                SelectFeat = "".join(SelectFeat) #Join into a readable string
                                FeatsList.append(SelectFeat)
                                print("Finished reading file. Closing.")
                                OpenFile.close()
                                Exit = True #Set to true
                                break

                    if Exit == True: #Exits the loop for selecting a feat
                        break
                    if InfoSelect != "s" or InfoSelect != "i":
                        print("\nSorry, not a valid input. Try again.")

        if FeatOrASI.lower() == "asi":
            AbilityList = ["str", "dex", "con", "int", "wis", "cha"]
            Score = 2 #Tracks how many points an ability can be increased by
            Feats -= 1
            print("\n--------------------")
            print("\nYour current ability scores:")
            print(f"Strength: {Str}, modifier: {StrMod}\nDexterity: {Dex}, modifier: {DexMod}\nConstitution: {Con}, modifier: {ConMod}")
            print(f"Intelligence: {Int}, modifier: {IntMod}\nWisdom: {Wis}, modifier: {WisMod}\nCharisma: {Cha}, modifier: {ChaMod}")

            while Score <= 2 and Score != 0: #Loop stops if user has no ability increases (Score) left
                print("\nYou can increase an ability", Score, "more times.")
                Ability = input("\nIncrease which ability? (use first three letters): ")
                if Ability not in AbilityList:
                    print("\nSorry, not a valid input. Try again.")

                else:
                     #All the checks for which ability was selected work the same way, so I shall only comment the first one.
                    if Ability == "str":
                        if Str >= 20: #D&D rules don't allow to go past 20
                            print("Sorry, can't increase abilities past 20.")
                            continue
                        while True:
                            try:
                                Points = int(input("Increase by how many points? (1 or 2): "))
                            except ValueError:
                                print("Sorry, not an integer. Try again.\n")
                                continue
                            if Points == "":
                                print("Sorry, input can't be empty. Try again.")
                                continue
                            if Points == 2 and Score == 2: #Checks if ability can be increased by 2 by comparing the input to Score. Score keeps track of increases.
                                if Str + Points > 20: #D&D rules don't allow to go past 20
                                    print("Sorry, can't increase abilities past 20.")
                                    continue #Goes back to asking how many points to increase by. Because the user is already blocked from
                                             #increasing an ability if it's at 20, this still allows the user to increase by one if the ability is at 19.
                                Str += Points #Str is a global variable for keeping track of the respetive ability
                                Score -= 2 #Decrease score by the amount the ability was increased
                                print("Increased strength by 2.")
                                break #Breaks out of the loop asking how many points to increase by
                                      #Because score is 0 and this loop breaks, goes back to the loop asking if the user wants an ASI or feature

                            if Points == 1 and Score >= 1: #Increase ability score by one
                                Str += Points
                                Score -= 1
                                print("Increased strength by 1.")
                                break #Breaks this loop, but stays in the ASI loop
                            else: #Goes here if user tries to increase by more than two or can not increase by 2 because only 1 increase remains
                                print("\nSorry, can't increase by more than 2, or you only had one increase left\n")
                                break #Breaks this loop, goes back to the loop asking which ability to increase

                    if Ability == "dex":
                        if Dex >= 20:
                            print("Sorry, can't increase abilities past 20.")
                        while True:
                            try:
                                Points = int(input("Increase by how many points? (1 or 2): "))
                            except ValueError:
                                print("Sorry, not an integer. Try again.\n")
                                continue
                            if Points == "":
                                print("Sorry, input can't be empty. Try again.")
                                continue
                            if Points == 2 and Score == 2:
                                if Dex + Points > 20:
                                    print("Sorry, can't increase abilities past 20.")
                                    continue
                                Dex += Points
                                Score -= 2
                                print("Increased dexterity by 2.")
                                break

                            if Points == 1 and Score >= 1:
                                Dex += Points
                                Score -= 1
                                print("Increased dexterity by 1.")
                                break
                            else:
                                print("\nSorry, can't increase by more than 2, or you only had one increase left\n")
                                break
                        
                    if Ability == "con":
                        if Con >= 20:
                            print("Sorry, can't increase abilities past 20.")
                        while True:
                            try:
                                Points = int(input("Increase by how many points? (1 or 2): "))
                            except ValueError:
                                print("Sorry, not an integer. Try again.\n")
                                continue
                            if Points == "":
                                print("Sorry, input can't be empty. Try again.")
                                continue
                            if Points == 2 and Score == 2:
                                if Dex + Points > 20:
                                    print("Sorry, can't increase abilities past 20.")
                                    continue
                                Con += Points
                                Score -= 2
                                print("Increased constitution by 2.")
                                break

                            if Points == 1 and Score >= 1:
                                Con += Points
                                Score -= 1
                                print("Increased constitution by 1.")
                                break
                            else:
                                print("\nSorry, can't increase by more than 2, or you only had one increase left\n")
                                break
                        
                    if Ability == "int":
                        if Int >= 20:
                            print("Sorry, can't increase abilities past 20.")
                        while True:
                            try:
                                Points = int(input("Increase by how many points? (1 or 2): "))
                            except ValueError:
                                print("Sorry, not an integer. Try again.\n")
                                continue
                            if Points == "":
                                print("Sorry, input can't be empty. Try again.")
                                continue
                            if Points == 2 and Score == 2:
                                if Dex + Points > 20:
                                    print("Sorry, can't increase abilities past 20.")
                                    continue
                                Int += Points
                                Score -= 2
                                print("Increased intelligence by 2.")
                                break

                            if Points == 1 and Score >= 1:
                                Int += Points
                                Score -= 1
                                print("Increased intelligence by 1.")
                                break
                            else:
                                print("\nSorry, can't increase by more than 2, or you only had one increase left\n")
                                break
                    
                    if Ability == "wis":
                        if Wis >= 20:
                            print("Sorry, can't increase abilities past 20.")
                        while True:
                            try:
                                Points = int(input("Increase by how many points? (1 or 2): "))
                            except ValueError:
                                print("Sorry, not an integer. Try again.\n")
                                continue
                            if Points == "":
                                print("Sorry, input can't be empty. Try again.")
                                continue
                            if Points == 2 and Score == 2:
                                if Dex + Points > 20:
                                    print("Sorry, can't increase abilities past 20.")
                                    continue
                                Wis += Points
                                Score -= 2
                                print("Increased wisdom by 2.")
                                break

                            if Points == 1 and Score >= 1:
                                Wis += Points
                                Score -= 1
                                print("Increased wisdom by 1.")
                                break
                            else:
                                print("\nSorry, can't increase by more than 2, or you only had one increase left\n")
                                break

                    if Ability == "cha":
                        if Cha >= 20:
                            print("Sorry, can't increase abilities past 20.")
                        while True:
                            try:
                                Points = int(input("Increase by how many points? (1 or 2): "))
                            except ValueError:
                                print("Sorry, not an integer. Try again.\n")
                                continue
                            if Points == "":
                                print("Sorry, input can't be empty. Try again.")
                                continue
                            if Points == 2 and Score == 2:
                                if Dex + Points > 20:
                                    print("Sorry, can't increase abilities past 20.")
                                    continue
                                Cha += Points
                                Score -= 2
                                print("Increased charisma by 2.")
                                break

                            if Points == 1 and Score >= 1:
                                Cha += Points
                                Score -= 1
                                print("Increased charisma by 1.")
                                break
                            else:
                                print("\nSorry, can't increase by more than 2, or you only had one increase left\n")
                                break

            #Recalculates modifiers
            StrMod = math.floor((Str-10)/2)
            DexMod = math.floor((Dex-10)/2)
            ConMod = math.floor((Con-10)/2)
            IntMod = math.floor((Int-10)/2)
            WisMod = math.floor((Int-10)/2)
            ChaMod = math.floor((Cha-10)/2)

            print("\nYour new ability scores:")
            print(f"Strength: {Str}, modifier: {StrMod}\nDexterity: {Dex}, modifier: {DexMod}\nConstitution: {Con}, modifier: {ConMod}")
            print(f"Intelligence: {Int}, modifier: {IntMod}\nWisdom: {Wis}, modifier: {WisMod}\nCharisma: {Cha}, modifier: {ChaMod}")

        if FeatOrASI != "f" and FeatOrASI != "asi": #Go here if the user makes an invalid input in asking if they want a feat or ASI
            print("Sorry, not a valid input. Try again.")

#Following section defines classes used to store information about user's character. These also call the functions.
#Basic information about the character.
class Character():
    Name = ""
    Class = ""
    SubClass = ""
    Race = ""
    SubRace = ""
    Background = ""
    PersonalityTraits = ""
    Ideals = ""
    Bonds = ""
    Flaws = ""
    Alignment = ""
    Level = ""

Character = Character()
Character.Name = CharName()
Character.Class = CharClass()
Character.SubClass = CharSubClass()
Character.Race = CharRace()
Character.SubRace = CharSubRace()
Character.Background = CharBackground()
Character.Personality = CharPersonality()
Character.Ideals = CharIdeals()
Character.Bonds = CharBonds()
Character.Flaws = CharFlaws()
Character.Alignment = CharAlignment()
Character.Level = CharLevel()

class charStats():
    AbilityScores = ""
    HitDice = ""
    Hitpoints = ""
    ArmorClass = ""

Stats = charStats()
Stats.AbilityScores = CharAbilityScores()
Stats.HitDice = CharHitDice()
Stats.Hitpoints = CharHP()
Stats.ArmorClass = CharAC()

#Character's traits, proficiencies (from character's class and race) and languages.
class charTraitsLangsFeats():
    ClassFeatures = ""
    SubClassFeatures = ""
    RaceFeatures = ""
    SubRaceFeatures = ""
    ProfBonus = ""
    ClassProfs = ""
    RaceProfs = ""
    SubRaceProfs = ""
    RaceASI = ""
    SubRaceASI = ""
    RaceSpeed = ""
    RaceSizeWeight = ""
    RaceAge = ""
    Languages = ""
    Feats = ""

TraitsStuff = charTraitsLangsFeats()
TraitsStuff.ClassFeatures = CharClassFeats()
TraitsStuff.SubClassFeatures = CharSubClassFeats()
TraitsStuff.RaceFeatures = CharRaceFeats()
TraitsStuff.SubRaceFeatures = CharSubRaceFeats()
TraitsStuff.ProfBonus = CharProfBonus()
TraitsStuff.ClassProfs = CharClassProfs()
TraitsStuff.RaceProfs = CharRaceProfs()
TraitsStuff.SubRaceProfs = CharSubRaceProfs()
TraitsStuff.RaceASI = CharRaceASI()
TraitsStuff.SubRaceASI = CharSubRaceASI()
TraitsStuff.RaceSpeed = CharSpeed()
TraitsStuff.RaceSizeWeight = CharSizeWeight()
TraitsStuff.RaceAge = CharAge()
TraitsStuff.Languages = CharLangs()
TraitsStuff.Feats = CharLevelFeats()


#Dictionary for storing character's stats and skill checks
SkillChecks = {
    "Acrobatics": DexMod,
    "Animal Handling": WisMod,
    "Arcana": IntMod,
    "Athletics": StrMod,
    "Deception": ChaMod,
    "History": IntMod,
    "Insight": WisMod,
    "Intimidation": ChaMod,
    "Investigation": IntMod,
    "Medicine": WisMod,
    "Nature": IntMod,
    "Perception": WisMod,
    "Performance": ChaMod,
    "Persuasion": ChaMod,
    "Religion": IntMod,
    "Sleight of Hand": DexMod,
    "Stealth": DexMod,
    "Survival": WisMod
}

#Finally, a function for writing all data to a file.
def WriteToFile():
    global FeatsList
    print("----------Finishing up----------")
    print("\nThat's the entire character set.")
    print("There are a few things you'll have to do manually.")
    print("\n**After** writing to the file, consider taking a look at your character file")
    print("and see your equipment, potential ability score increases and proficiencies through your race and subrace,")
    print("and your background info for potential extra languages, proficiencies, features and items.\n")
    print("Select yes (y) if you wish to write character to file, select no (n)")
    print("if you wish to exit the program and lose your character.\n")
    Write = input("Write character to file? (y/n): ")
    if Write.lower() == "y":
        OpenFile = open(CharFilePath, "w")
        print("Writing to file...\n")
        OpenFile.write(Character.Name + "\n")
        OpenFile.write(Character.SubClass + " ")
        OpenFile.write(Character.Class + "\n")
        OpenFile.write(Character.SubRace + " ")
        OpenFile.write(Character.Race + "\n\n")
        OpenFile.write(Character.Background + "\n\n")
        OpenFile.write("\nLevel:")
        OpenFile.write(str(Character.Level))
        OpenFile.write("\n\nAbility scores:")
        OpenFile.write("\n\nStrength: ")
        OpenFile.write(str(Str))
        OpenFile.write(" Modifier: ")
        OpenFile.write(str(StrMod))
        OpenFile.write("\n\nDexterity: ")
        OpenFile.write(str(Dex))
        OpenFile.write(" Modifier: ")
        OpenFile.write(str(DexMod))
        OpenFile.write("\n\nConstitution: ")
        OpenFile.write(str(Con))
        OpenFile.write(" Modifier: ")
        OpenFile.write(str(ConMod))
        OpenFile.write("\n\nIntelligence: ")
        OpenFile.write(str(Int))
        OpenFile.write(" Modifier: ")
        OpenFile.write(str(IntMod))
        OpenFile.write("\n\nWisdom: ")
        OpenFile.write(str(Wis))
        OpenFile.write(" Modifier: ")
        OpenFile.write(str(WisMod))
        OpenFile.write("\n\nCharisma: ")
        OpenFile.write(str(Cha))
        OpenFile.write(" Modifier: ")
        OpenFile.write(str(ChaMod))
        OpenFile.write("\n\n\nHitpoints, Armor Class and Proficiency Bonus\n\nHit dice: ")
        OpenFile.write(str(Stats.HitDice))
        OpenFile.write("\nHitpoints: ")
        OpenFile.write(str(Stats.Hitpoints))
        OpenFile.write("\nArmor class: ")
        OpenFile.write(str(Stats.ArmorClass))
        OpenFile.write("\nProficiency bonus: ")
        OpenFile.write(str(TraitsStuff.ProfBonus))
        OpenFile.write("\n\n\nTraits (Class):\n")
        OpenFile.write(TraitsStuff.ClassFeatures)
        OpenFile.write("\n\n\nTraits (Subclass)\n")
        OpenFile.write(TraitsStuff.SubClassFeatures)
        OpenFile.write("\n\n\nTraits (Race)\n")
        OpenFile.write(TraitsStuff.RaceFeatures)
        OpenFile.write("\n\n\nTraits (Subrace)\n")
        OpenFile.write(TraitsStuff.SubRaceFeatures)
        OpenFile.write("\n\n\nProficiencies (Class)\n")
        OpenFile.write(TraitsStuff.ClassProfs)
        OpenFile.write("\n\n\nProficiencies (Race)\n")
        OpenFile.write(TraitsStuff.RaceProfs)
        OpenFile.write("\n\n\nProficiencies (subrace)\n")
        OpenFile.write(TraitsStuff.SubRaceProfs)
        OpenFile.write("\n\nLanguages\n")
        OpenFile.write(TraitsStuff.Languages)
        OpenFile.write("\n\nAbility score increase (Race)\n")
        OpenFile.write(TraitsStuff.RaceASI)
        OpenFile.write("\nAbility score increase (Subrace)\n")
        OpenFile.write(TraitsStuff.SubRaceASI)
        OpenFile.write("\n\nSpeed\n")
        OpenFile.write(TraitsStuff.RaceSpeed)
        OpenFile.write("\n\n\nSize and weight\n")
        OpenFile.write(TraitsStuff.RaceSizeWeight)
        OpenFile.write("\n\nAge\n")
        OpenFile.write(TraitsStuff.RaceAge)
        OpenFile.write("\n\nPersonality traits:\n")
        OpenFile.write(Character.Personality)
        OpenFile.write("\n\nIdeals:\n")
        OpenFile.write(Character.Ideals)
        OpenFile.write("\n\nBonds:\n")
        OpenFile.write(Character.Bonds)
        OpenFile.write("\n\nFlaws:\n")
        OpenFile.write(Character.Flaws)
        OpenFile.write("\n\nAlignment:\n")
        OpenFile.write(Character.Alignment + "\n")
        OpenFile.write("\n\nFeat(s) from levels:")
        OpenFile.write("".join(map(str, FeatsList)))
        print("\nFinished writing to file. Closing file and exiting program.")
        OpenFile.close()
        sys.exit()
WriteToFile()