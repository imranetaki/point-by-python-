class point : 
    def _init_(self, abcisse = 0, ordonne = 0):
        self.abcisse = abcisse
        self.ordonne = ordonne 
    
    def get_abcisse(self):
        return self.abcisse 
    
    def set_abcsisse(self, value):
        self.abcisse = value 
    
    def get_ordonne(self):
        return self.ordonne
    
    def set_ordonne(self, value):
        self.ordonne  = value

    def distance(self, point):
        d =  ((self.abcisse - point.abcisse) ** 2 + (self.ordonne - point.ordonne ) ** 2) ** 0.5
        return d
    
    def Norm(self):
        n = (self.abcisse ** 2 + self.ordonne ** 2) ** (1/2)
        return n
    
#exemple of usage 
pts1 = point(4, 3)
print("distance est :", pts1.distance(point(0, 0)))
print("Norm :", pts1.Norm())
