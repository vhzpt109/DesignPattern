class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        else:
            pass
        return cls.instance


if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    if singleton1 == singleton2:
        print("same instance")
    else:
        print("not same")
