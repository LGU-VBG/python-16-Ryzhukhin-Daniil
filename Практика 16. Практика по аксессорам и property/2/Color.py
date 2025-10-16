class Color:
    def __init__(self, hexcode):
        self._hexcode = hexcode
        
    @property
    def r(self):
        return self._r    
        
    @property
    def g(self):
        return self._g    
    @property
    def b(self):
        return self._b    
    
    @property
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, value):
        self._hexcode = value
        self._r = int(value[0:2], 16)
        self._g = int(value[2:4], 16)
        self._b = int(value[4:6], 16)
        
        
color = Color('0000FF') 
 
print(color.hexcode) 
print(color.r) 
print(color.g) 
print(color.b)
