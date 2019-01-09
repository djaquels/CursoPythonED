class MiError(Exception):
    def __init__(self,x):
        print("Este fue el valor",x)

try :
    raise MiError(999)
except MiError:
    print("Mi Error")