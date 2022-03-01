from abstract_classes import DataModel

class File(DataModel):

    def __init__(self, name):
        super(File, self).__init__(name)
        self._name = name
        self._type = "file"
