from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
text = """
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class (Inheritance)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Another class showing encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Remaining balance: {self.__balance}"
        else:
            return "Insufficient funds!"

# Using the classes
dog = Dog("Tommy")
cat = Cat("Kitty")

print(dog.speak())   # Tommy says Woof!
print(cat.speak())   # Kitty says Meow!

account = BankAccount("Shobhit", 1000)
print(account.deposit(500))   # Deposited 500. New balance: 1500
print(account.withdraw(700))  # Withdrew 700. Remaining balance: 800
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=190,
    chunk_overlap=0
)
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks[2])