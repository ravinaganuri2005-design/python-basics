
#GETTER AND SETTER WITH SOME EXAMPLES
class rectangel:
    def __init__(self,width,height):
        self.width = width
        self.height =height
    
    @property   #getter
    def width(self):
        return self._width
    
    @width.setter   #setter
    def width(self,values):
        if values <=0:
            print("width must be positive")
        else:
            self._width = values
    
    @property  #getter
    def height(self):
        return self._height
    
    @height.setter  #setter
    def height(self,values):
        if values <= 0:
            print("hieght must be positive")
        else: 
         self._height = values
     
    @property  #ONLY READ THE VALUE NO SETTER
    def area(self):
        return self._width * self.height
    
    @property # ONLY GETTER NO SETTER
    def perimater(self):
          return 2 * (self._width + self._height)
    
r = rectangel(4,5)
    
print(r.width)# READ
print(r.height)
print(r.area)
print(r.perimater)

r.width =23  # CHANGE THE VALUE
print(r.width)

r.height = -77  # NO CHANGE BECOUSE IT IS NAGETIVE
print(r.height)
