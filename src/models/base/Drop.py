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

    def setImage(self, image):
        self.image = image

    def incrementCount(countType):
        countType += 1

    def decrementCount(countType):
        countType -= 1

    def __init__(self, dropType):
        self.dropType = dropType
        self.beforeCount, self.afterCount, self.currentCount = 0