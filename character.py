class Character:
    def __init__(self):
        self._firstName = ''
        self._lastName = ''
        self._pic = ''
        self._position = ''
        self._bio = ''

    @property
    def firstName(self):
        return self._firstName
    @property
    def lastName(self):
        return self._lastName

    @property
    def pic(self):
        return self._pic
    
    @property
    def position(self):
        return self._position
    
    @property
    def bio(self):
        return self._bio
    
    def setCharacter(self, firstName, lastName, pic, position, bio):
        self._firstName = firstName
        self._lastName = lastName
        self._pic = pic
        self._position = position
        self._bio = bio

    def printCharacter(self):
        print('info:' + self._firstName + ' ' 
            + self._lastName + ' ' + self._pic + ' '+ self._position + ' '+ self._bio) 

    def __str__(self):
        print('info:' + self._firstName + ' ' 
            + self._lastName + ' ' + self._pic + ' '+ self._position + ' '+ self._bio) 
        return self._firstName + ' ' + self._lastName