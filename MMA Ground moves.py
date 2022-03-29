class Takedown:
    Phrase = " goes for a takedown!"
    Type = "Wrestling"
    WinPhrase = " gets it!"
    FailPhrase = " gets stopped!"
    def __init__(self):
        self.Type = Type
        self.Phrase = Phrase
        self.WinPhrase = WinPhrase
        self.FailPhrase = FailPhrase
    def GetOutcome(OffensiveFighterSkills,DefensiveFighterSkills):
        RandomNumber = random.randint(1,10)
        PlusMinus = ["+","-"]
        Chooser = random.choice(PlusMinus)
        if Chooser == "+":
            OffensiveFighterSkillsRandomised = OffensiveFighterSkills + RandomNumber
        elif Chooser == "-":
            OffensiveFighterSkillsRandomised = OffensiveFighterSkills - RandomNumber
        if OffensiveFighterSkillsRandomised > DefensiveFighterSkills:
            worked = True
        if OffensiveFighterSkillsRandomised < DefensiveFighterSkills:
            worked = False
        if OffensiveFighterSkillsRandomised == DefensiveFighterSkills:
            worked = False
        return worked
    def GetType():
        Type2 = Takedown.Type
        return Type2
    def GetPhrase():
        Phrase2 = Takedown.Phrase
        return Phrase2
    def GetWinPhrase():
        Phrase2 = Takedown.WinPhrase
        return Phrase2
    def GetFailPhrase():
        Phrase2 = Takedown.FailPhrase
        return Phrase2