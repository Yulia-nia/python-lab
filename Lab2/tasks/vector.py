class Vector:

    def __init__(self, *args):
        self.args = args
        self.dimension = len(args)

    def __add__(self, other):
        if len(self) == len(other):
            result = tuple([first_value + second_value for first_value, second_value in zip(self, other)])
            return Vector(*result)
        else:
            raise ValueError("Dimensions don't match")

    def __sub__(self, other_vector):
        if len(self) == len(other_vector):
            result = tuple([first_value - second_value for first_value, second_value in zip(self, other_vector)])
            return Vector(*result)
        else:
            raise ValueError("Dimensions don't match")

    def __mul__(self, other_vector):
        if type(other_vector) == Vector:
            if len(self) == len(other_vector):
                result = tuple([first_value * second_value for first_value, second_value in zip(self, other_vector)])
                return Vector(*result)
            else:
                raise ValueError("Dimensions don't match")
        else:
            result = tuple([other_vector * i for i in self])
            return Vector(*result)

    def __truediv__(self, other_vector):
        if type(other_vector) == Vector:
            if len(self) == len(other_vector):
                result = tuple(
                    [first_value / second_value for first_value, second_value in zip(self, other_vector)])
                return Vector(*result)
            else:
                raise ValueError("Dimensions don't match")
        else:
            result = tuple([i / other_vector for i in self])
            return Vector(*result)

    def __len__(self):
        return len(self.args)

    def __getitem__(self, index):
        return self.args[index]

    def __eq__(self, other_vector):
        if len(self) == len(other_vector) and all([i == j for i, j in zip(self, other_vector)]):
            return True
        return False

    def __str__(self):
        return str(self.args)
