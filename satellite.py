
class Satellite:

    def __init__(self, id):
        self.id = id
        self.direct = []

    def addDirect(self, sat):
        self.direct.append(sat)

    def getDirect(self):
        return self.direct

    def getOrbiters(self):
        orbiters = []
        if not self.direct:
            return orbiters
        else:
            orbiters.append(self.direct)
            for i in self.direct:
                orbiters.append(i.getOrbiters())
        return orbiters

    