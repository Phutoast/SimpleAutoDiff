from .baseNumber import BaseNumber

class Constant(BaseNumber):
    """
    Constant can't be change after initialized.
    """

    def __init__(self, value):
        super().__init__(value)
        if not (type(value) == int or type(value) == float):
            raise TypeError("Constant has to be int or float!!")