from abstract_classes import DataModel

class Data(DataModel):
    def __init__(self, name, type):
        super(Data, self).__init__(name, type)