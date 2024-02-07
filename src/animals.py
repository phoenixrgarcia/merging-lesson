

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

# Add another animal below.  Come up with something unique
# Feel free to add functions or whatever you want.  If you don't feel
# confident in your python, you just copy and paste the bird and change
# the names or even just write a comment.  Just add something to the file.
