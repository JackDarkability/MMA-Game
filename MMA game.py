import random
from MMAGround import *
from MMAStandup import *






class Fighter:
    def __init__(self,FirstName,LastName,BoxingSkills,KarateSkills,MuayThaiSkills,BJJSkills,WrestlingSkills,HeadHealth,BodyHealth):
        self.FirstName = FirstName
        self.LastName = LastName
        self.BoxingSkills = BoxingSkills
        self.KarateSkills = KarateSkills
        self.MuayThaiSkills = MuayThaiSkills
        self.BJJSkills = BJJSkills
        self.WrestlingSkills = WrestlingSkills
        self.HeadHealth = HeadHealth
        self.BodyHealth = BodyHealth
        self.GeneralisedPosition = "Standup"
        self.Position = "Far"
    def Standup(self,OtherClass):
        AllMoves = [DoNothing,TryToStandUp,Takedown,Jab,Hook,PostureUp,PosturedPunchHead,HalfGuard,FullGuard,SideControl,PostureDown,Mount,ButterflyGuard]
        CurrentMovePossibilities = []
        for i in AllMoves:
            if ((i.Name == "Posture Up") and (self.GeneralisedPosition == "Ground") and ("Postured Up" not in self.Position) and ("Top" in self.Position)):
                CurrentMovePossibilities.append(i)
            if ((i.Name == "Posture Down") and (self.GeneralisedPosition == "Ground") and ("Postured Up" in self.Position) and ("Top" in self.Position)):
                CurrentMovePossibilities.append(i)
            if ((i.Name == "Do Nothing") and (i not in CurrentMovePossibilities)):
                CurrentMovePossibilities.append(i)
            if ((i.Name == "Stand Up") and (("Top" in self.Position) or (self.Position in TryToStandUp.SweepingPositions))):
                print("Hello")
                CurrentMovePossibilities.append(i)
            if self.Position in i.PreviousPosition:
                CurrentMovePossibilities.append(i)

        Choices = ""
        for i in CurrentMovePossibilities:
            index = CurrentMovePossibilities.index(i)
            Choices = Choices + "\nNumber "+str(index) +": " +i.Name

        print(Choices)
        Number = int(input("Input the number"))
        # Get rid of randomiser later


        Move = CurrentMovePossibilities[Number]
        GetPhrase = Move.GetPhrase()
        print(self.LastName + GetPhrase)
        self.WinOfOutcome(OtherClass,Move)
    def WinOfOutcome(self,OtherClass,Move):
        if Move.GetType() == "Boxing":
            Working = Move.GetOutcome(self.BoxingSkills,OtherClass.BoxingSkills)
        if Move.GetType() == "Karate":
            Working = Move.GetOutcome(self.KarateSkills,OtherClass.KarateSkills)
        if Move.GetType() == "Muay Thai":
            Working = Move.GetOutcome(self.MuayThaiSkills,OtherClass.MuayThaiSkills)
        if Move.GetType() == "BJJ":
            Working = Move.GetOutcome(self.BJJSkills,OtherClass.BJJSkills)
        if Move.GetType() == "Wrestling":
            Working = Move.GetOutcome(self.WrestlingSkills,OtherClass.WrestlingSkills)







        if Working == True:
            # True means win, False means lose
            GetWinPhrase = Move.GetWinPhrase()
            print(self.LastName + GetWinPhrase)
            if Move.GetDamage() == "Head":
                OtherClass.HeadHealth = OtherClass.HeadHealth - Move.GetAmountOfDamage()
            if Move.GetDamage() == "Body":
                OtherClass.BodyHealth = OtherClass.BodyHealth - Move.GetAmountOfDamage()
            self.Position = Move.GetOffensiveEndPosition(self)
            self.GeneralisedPosition = Move.GetGeneralisedEndPosition()
            OtherClass.Position = Move.GetDefensiveEndPosition(OtherClass)
            OtherClass.GeneralisedPosition = Move.GetGeneralisedEndPosition()
        if Working == False:
            GetFailPhrase = Move.GetFailPhrase()
            print(self.LastName + GetFailPhrase)


def FullFight(Class1,Class2):
    Randomiser = random.randint(1,2)
    if Randomiser == 1:
        print(Class1.LastName + "'s turn")
        Class1.Standup(Class2)
    if Randomiser == 2:
        print(Class2.LastName + "'s turn")
        Class2.Standup(Class1)


Fighter1 = Fighter("John","Johnson",46,56,66,87,98,200,200)
Fighter2 = Fighter("James","Jameson",46,88,42,96,98,150,300)
while True:
    FullFight(Fighter1,Fighter2)
