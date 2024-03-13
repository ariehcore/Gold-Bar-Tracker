class Raid():

    @property
    def name(self):
        return self._name

    @property
    def drops(self):
        return self._drops
    
    @property
    def image(self):
        return self._image
    
    @property
    def totalCount(self):
        return self._totalCount
    
    @property
    def blueCount(self):
        return self._blueCount

    # array of Drops
    def setDrops(self, drops):
        self._drops = drops
    
    def incrementCount(self):
        self.totalCount += 1

    def decrementCount(self):
        self.totalCount -= 1

    def __init__(self, name):
        self.name = name
        self.totalCount = 0
        self.blueCount = 0
