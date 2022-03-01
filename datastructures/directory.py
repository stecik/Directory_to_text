from abstract_classes import DataModel

class Directory(DataModel):

    def __init__(self, name):
        super(Directory, self).__init__(name)
        self._name = name
        self._type = "directory"
