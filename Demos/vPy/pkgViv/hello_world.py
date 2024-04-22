class HelloWorld:
    def __init__(self, id, full_name, age):
        self.id = id
        self.full_name = full_name
        self.age = age

    def say(self):
        print(f"Hello {self.id} - {self.full_name} - {self.age}")
