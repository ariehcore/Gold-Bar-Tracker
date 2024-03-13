class Drop():

    @property
    def dropType(self):
        return self._dropType

    @property
    def image(self):
        return self._image

    @property
    def currentCount(self):
        return self._currentCount

    @property
    def beforeCount(self):
        return self._beforeCount
    
    @property
    def afterCount(self):
        return self._afterCount

    def __init__(self, dropType, image):
        self._dropType = dropType
        self._image = image
        self._beforeCount = 0 
        self._afterCount = 0 
        self._currentCount = 0