#https://www.cryptool.org/en/cto-ciphers/enigma

Start1 = 3 
Start2 = 4
Start3 = 5
tekst = "test"

class Enigma():

    def __init__(self, Rotset1, Rotset2, Rotset3, Tekst):
        self.Rotset1 = Rotset1
        self.Rotset2 = Rotset2
        self.Rotset3 = Rotset3
        #De originele enigma rotors zaten niet alledrie op alphabetvolgorde maar op deze manier:
        #We kunnen aan het eind dus nog iets er inschrijven dat je de verschillende rotoren kan plaatsen...
        self.Rot1 = "ekmflgdqvzntowyhxuspaibrcj"
        self.Rot2 = "ajdksiruxblhwtmcqgznpyfvoe"
        self.Rot3 = "fvpjiaoyedrzxwgctkuqsbnmhl"       
        self.Tekst = Tekst 
        
    #functie die de rotoren aan het begin klaarzet, deze kunnen we gebruiken voor recursie dan hoeven we alleen maar de rotorsettings op te hogen!
    def Rotset(self):
        print(set)
        Rot1 =self.Rot1[self.Rotset1:26] + self.Rot1[0: self.Rotset1]
        Rot2 =self.Rot2[self.Rotset2:26] + self.Rot2[0: self.Rotset2]
        Rot3 =self.Rot3[self.Rotset3:26] + self.Rot2[0: self.Rotset3]
        return Rot1, Rot2, Rot3
    
    def Encrypt(self):
        Enigma().Rotset()
        return

enigma = Enigma(Start1, Start2, Start3, tekst)

print(Enigma.Rotset(enigma))

