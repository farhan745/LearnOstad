class father():
    def __init__(self):
        print("father")

class son(father):

    def __init__(self):
        print("Son")
        super().__init__()

obj = son()
