class Enigma():


    def __init__(self, Rotset):
        self.Rotset = Rotset
        self.Rot1 = "abcdefghijklmnopqrstuvwxyz"
        self.Rot2 = "abcdefghijklmnopqrstuvwxyz"
        self.Rot3 = "abcdefghijklmnopqrstuvwxyz"        
        

    def EersteRotset(self):
        set = str(self.Rotset)
        print(set)
        Rot1 =self.Rot1[int(set[0]):26] + self.Rot1[0: int(set[0])]
        Rot2 =self.Rot2[int(set[1]):26] + self.Rot2[0: int(set[1])]
        Rot3 =self.Rot3[int(set[2]):26] + self.Rot2[0: int(set[2])]
        return Rot1, Rot2, Rot3


enigma = Enigma(423)

print(Enigma.EersteRotset(enigma))

