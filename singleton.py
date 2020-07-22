class configValues:

    __instance = None

    @staticmethod
    def getInstance():
        if configValues.__instance == None:
            configValues()
        return configValues.__instance

    def __init__(self):
        """ Virtually private constructor """
        if configValues.__instance != None:
            raise Exception ("this class is a singleton")
        else:
            configValues.__instance = self

s = configValues.getInstance()
print(s)

s = configValues.getInstance()
print(s)
