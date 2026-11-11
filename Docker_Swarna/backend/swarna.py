def get_names():
    with open("names.txt") as f:
        names = f.read()
        name = names.split()
        return name
