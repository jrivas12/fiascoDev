class Language:
    # define class attributes
    Grammar = "a set of rules that describe how words and phrases are arranged in a language"
    Languages = {
        "Python": {
            "Field": "General-purpose",
            "Recognizing_Automaton": "Python virtual machine",
            "Production_rules": "Python syntax and semantics",
            "Examples": ["print('Hello, world!')", "x = 5 + 3", "import math"]
        },
        "Java": {
            "Field": "General-purpose",
            "Recognizing_Automaton": "Java Virtual Machine (JVM)",
            "Production_rules": "Java syntax and semantics",
            "Examples": ["System.out.println('Hello, world!');", "int x = 5 + 3;", "import java.util.*;"]
        },
        "C": {
            "Field": "Systems programming",
            "Recognizing_Automaton": "C compiler",
            "Production_rules": "C syntax and semantics",
            "Examples": ["printf('Hello, world!');", "int x = 5 + 3;", "#include <stdio.h>"]
        },
        "Fortran": {
            "Field": "Scientific computing",
            "Recognizing_Automaton": "Fortran compiler",
            "Production_rules": "Fortran syntax and semantics",
            "Examples": ["WRITE(*,*) 'Hello, world!'", "REAL :: x = 5.0 + 3.0", "USE math_module"]
        },
        "Ruby": {
            "Field": "Web development",
            "Recognizing_Automaton": "Ruby interpreter",
            "Production_rules": "Ruby syntax and semantics",
            "Examples": ["puts 'Hello, world!'", "x = 5 + 3", "require 'math'"]
        }
        # Add more programming languages and their attributes here...
    }

    def __init__(self, name):
        # define instance attribute
        self.name = name

    def __str__(self):
        # return a string representation of the instance
        return f"This is an instance of the Language class with the name {self.name}"

    @classmethod
    def recognize(cls, language_name):
        if language_name in cls.Languages:
            language = cls(language_name)
            print(f"Recognized language: {language.name}")
            print(f"Field of implementation: {cls.Languages[language.name]['Field']}")
            print(f"Grammar: {cls.Grammar}")
            print(f"Recognizing Automaton: {cls.Languages[language.name]['Recognizing_Automaton']}")
            print(f"Production Rules (Constraints): {cls.Languages[language.name]['Production_rules']}")
            print(f"Examples using {language.name}:")
            for example in cls.Languages[language.name]['Examples']:
                print(f"- {example}")
        else:
            print("Language not recognized.")

def recognize_programming_language():
    print("Welcome to the Programming Language Recognition System!")
    print("This system can provide information about various programming languages.")
    print("Here are the available languages:")
    print(list(Language.Languages.keys()))
    
    while True:
        language_name = input("Enter the name of a programming language or 'exit' to quit: ")
        if language_name.lower() == "exit":
            print("Thank you for using the Programming Language Recognition System. Goodbye!")
            break
        else:
            Language.recognize(language_name)
            print()

# Example usage:
recognize_programming_language()
