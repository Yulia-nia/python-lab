class Singleton(type):
    sample = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.sample:
            cls.sample[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.sample[cls]
