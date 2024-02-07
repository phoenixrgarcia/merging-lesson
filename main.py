import src.animals as animals

# Don't worry about this.  It just gets all of the classes defined in the
# animals file and runs their "hi" function
def main():
    classes = filter(lambda x: not x.startswith("__") and not x == "Animal", animals.__dir__())
    for animal in classes:
        a = getattr(animals, animal)()
        if hasattr(a, "hi"):
            a.hi()

if __name__ == '__main__':
    main()
