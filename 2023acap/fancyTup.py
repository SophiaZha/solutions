class fancyTuple:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        self._first = value

    @property
    def second(self):
        if self.len() < 2:
            raise AttributeError
        else:
            return self._second

    @second.setter
    def second(self, value):
        self._second = value

    @property
    def third(self):
        if self.len() < 3:
            raise AttributeError
        else:
            return self._third

    @third.setter
    def third(self, value):
        self._third = value

    @property
    def fourth(self):
        if self.len() < 4:
            raise AttributeError
        else:
            return self._fourth

    @fourth.setter
    def fourth(self, value):
        self._fourth = value

    @property
    def fifth(self):
        if self.len() < 5:
            raise AttributeError
        else:
            return self._fifth

    @fifth.setter
    def fifth(self, value):
        self._fifth = value

    def __init__(self, *args):
        self.first = None
        self.second = None
        self.third = None
        self.fourth = None
        self.fifth = None
        self.animals = []
        for i, ani in enumerate(args):
            if i == 0 :
                self.first = ani
            elif i == 1:
                self.second = ani
            elif i == 2:
                self.third = ani
            elif i == 3:
                self.fourth = ani
            elif i == 4:
                self.filth = ani
            self.animals.append(ani)

    def __len__(self):
        return len(self.animals)


    def len(self):
        return len(self.animals)


print(fancyTuple("dog", "pig").first)
print(fancyTuple("dog", "pig").third)
print(fancyTuple("dog", "pig", "cat").third)
print(fancyTuple("dog", "pig", "cat", "rat", "bird").first)
print(fancyTuple("dog", "pig").second)
print( fancyTuple("dog", "pig").len() )
print(len(fancyTuple("dog", "pig")))




