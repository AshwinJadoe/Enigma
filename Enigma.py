class Enigma():


    def __init__(self, Rotset1, Rotset2, Rotset3, Tekst):
        self.Rotset1 = Rotset1
        self.Rotset2 = Rotset2
        self.Rotset3 = Rotset3
        self.Rot1 = "abcdefghijklmnopqrstuvwxyz"
        self.Rot2 = "abcdefghijklmnopqrstuvwxyz"
        self.Rot3 = "abcdefghijklmnopqrstuvwxyz"        
        

    def Rotset(self):
        print(set)
        Rot1 =self.Rot1[self.Rotset1:26] + self.Rot1[0: self.Rotset1]
        Rot2 =self.Rot2[self.Rotset2:26] + self.Rot2[0: self.Rotset2]
        Rot3 =self.Rot3[self.Rotset3:26] + self.Rot2[0: self.Rotset3]
        return Rot1, Rot2, Rot3

    def encrypt(self):
        return

enigma = Enigma(4,2,3, "test")

print(Enigma.Rotset(enigma))

