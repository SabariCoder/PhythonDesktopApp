class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_hello():
        """
        Prints a greeting message 'Hello' to the console.

        This function does not take any arguments and simply outputs
        the string "Hello" when called.

        Returns:
            None
        """
        print("Hello")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    #def display():
    #    print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def square(self, number):
            return number * number

# Example usage
if __name__ == "__main__":
    person = Person("Alice", 30)
    #person.display()
    result = person.square(5)
    print(f"The square of 5 is {result}.")
    person.greet()
    Person.display_hello()