class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.data[self.index]

    def Etc(self):
        print("Hello, Reverse")
        for e in [1, 2, 3]:
            print(e)

        for e in (1, 2, 3):
            print(e)

        for key, value in {"one": 1, "two": 2, "three": 3}.items():
            print(key, value, end="\n")

        for char in "123456789":
            print(char, end=" ")
        print()

        for line in open("file.txt"):
            print(line, end="")

        s = "abcdefg"

        it = iter(s)

        # print(next(it))

        for _ in range(s.__len__()):
            print(next(it))
