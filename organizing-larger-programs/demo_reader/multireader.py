class MultiReader:
    def __init__(self, filename):
        self.f = open(filename, 'rt')

    def read(self):
        return self.f.read()

    def close(self):
        self.f.close()
