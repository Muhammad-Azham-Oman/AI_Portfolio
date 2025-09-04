class m():
    a = 8
    @classmethod
    def b(cls):
        print(f"This is the value: {cls.a}")


c = m()
c.b()