class Enigma():


    def __init__(self, Rotset):
        self.Rotset = Rotset
        self.Rot1 = "abcdefghijklmnopqrstuvwxyz"
        self.Rot2 = "abcdefghijklmnopqrstuvwxyz"
        self.Rot3 = "abcdefghijklmnopqrstuvwxyz"        
        

    def Rotdraaien(self):
        set= self.Rotset
        print(set)
        Rot1 =self.Rot1[set:26] + self.Rot1[0: set]
        return Rot1


enigma = Enigma(4)

print(Enigma.Rotdraaien(enigma))

