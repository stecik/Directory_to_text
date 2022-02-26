class Directory:

    def __init__(self, name):
        self._name = name
        self._type = "directory"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    def __repr__(self):
        return self._name

    def __str__(self):
        return self._name