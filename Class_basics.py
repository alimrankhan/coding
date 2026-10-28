
print('hello world, from Notepad++ on my new laptop HP Elitebook 830 G6.')

class Human:
    def __init__(self, name): 
        self.name= name

    def character(self, details):
        self.details= details
        print(self.details)

### ABSTRACT FUNCTION
    def __dis(self): 
        return f"Name: {self.name}"

    def display(self):
        return self.__dis()

Name= input()

print(Name)

h1= Human(Name)

print(h1.display())

a=input()
