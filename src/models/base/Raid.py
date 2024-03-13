class Raid():

    @property
    def name(self):
        return self._name

    @property
    def drops(self):
        return self._drops
    
    @drops.setter
    def drops(self, drops):
        self._drops = drops
    
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, image):
        self._image = image
    
    @property
    def totalCount(self):
        return self._totalCount
    
    @totalCount.setter
    def totalCount(self, count):
        self._totalCount = count

    def __init__(self, name):
        self._name = name
        self._totalCount = 0
        self._blueCount = 0
