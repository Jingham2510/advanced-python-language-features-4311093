# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolour":
            return(self.red, self.green, self.blue)
        elif attr == "hexcolour":
            return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"
        else:
            raise AttributeError(f"{attr} is not valid")

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
         
        if attr == "rgbcolour":
            self.red = val[0]
            self.green = val[1]
            self.red = val[2]
        else:
            super().__setattr__(attr, val)
        

    # TODO: use dir to list the available properties
    def __dir__(self):
        return("rgbcolour", "hexcolour", "red", "green", "blue")
    


# create an instance of myColor
cls1 = MyColor()
# TODO: print the value of a computed attribute
print(cls1.rgbcolour)
print(cls1.hexcolour)
# TODO: set the value of a computed attribute
cls1.rgbcolour = (125, 200, 92)
print(cls1.rgbcolour)
print(cls1.hexcolour)
# TODO: access a regular attribute
print(cls1.red)
# TODO: list the available attributes
print(dir(cls1))
