class Vector:

    def __init__(self, *args):
        self.args = list(args)
        self.dimension = len(args)

    def __add__(self, other):
        if len(self.args) == len(other.args):
            result = tuple([first_value + second_value for first_value, second_value in zip(self.args, other.args)])
            return Vector(*result)
        else:
            return 'Different dimensions!'

    def __sub__(self, other_vector):
        if len(self.args) == len(other_vector.args):
            result = tuple([first_value - second_value for first_value, second_value in zip(self.args, other_vector.args)])
            return Vector(*result)
        else:
            return 'Different dimensions!'

    def __mul__(self, other_vector):
        if type(other_vector) == Vector:
            if len(self.args) == len(other_vector.args):
                result = tuple([first_value * second_value for first_value, second_value in zip(self.args, other_vector.args)])
                return Vector(*result)
            else:
                return 'Different dimensions!'
        else:
            result = tuple([other_vector * i for i in self.args])
            return Vector(*result)

    def __truediv__(self, other_vector):
        if type(other_vector) == Vector:
            if len(self.args) == len(other_vector.args):
                result = tuple(
                    [first_value / second_value for first_value, second_value in zip(self.args, other_vector.args)])
                return Vector(*result)
            else:
                return 'Different dimensions!'
        else:
            result = tuple([i / other_vector for i in self.args])
            return Vector(*result)

    def __len__(self):
        return self.dimension

    def __getitem__(self, index):
        if index >= self.dimension:
            raise IndexError("Index out of range")
        return self.args[index]

    def __eq__(self, other_vector):
        if len(self.args) == len(other_vector.args) and all([i == j for i, j in zip(self.args, other_vector)]):
            return True
        return False

    def __str__(self):
        return str(self.args)
