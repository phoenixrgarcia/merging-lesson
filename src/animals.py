

class Animal:
    noise = ""
    def hi(self):
        # Don't worry too much about this part
        print(f"Hi, I am a {type(self).__name__}.  {self.noise}")


# An example class representing a bird
class Bird(Animal):
    noise = "TWEET"

    def fly(self):
        pass

class Crow(Bird):
    noise = "CAW"

class Dog(Animal):
    noise = "BARK"

    def fetch(self):
        pass


class Phoenix:
    noise = "RAAR CAWCAW"
    def breath_fire():
        print("SNAP SNAP CRACKLE")


class Jack(Animal):
    noise = "GIT CLONE <USERNAME> MERGE LESSON"

    def fetch(self):
        pass

# Add another animal below.  Come up with something unique
# Feel free to add functions or whatever you want.  If you don't feel
# confident in your python, you just copy and paste the bird and change
# the names or even just write a comment.  Just add something to the file.
