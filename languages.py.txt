class Language:
    # define class attributes
    Grammar = "a set of rules that describe how words and phrases are arranged in a language"
    Languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese"]
    Recognizing_Automaton = "a mathematical model of computation that can recognize strings belonging to a language"
    Production_rules = {
        "Regular Grammar": "describes regular languages that can be recognized by finite automata",
        "Context-Free Grammar": "describes context-free languages that can be recognized by pushdown automata",
        "Context-Sensitive Grammar": "describes context-sensitive languages that can be recognized by linear-bounded automata",
        "Unrestricted Grammar": "describes recursively enumerable languages that can be recognized by Turing machines"
    }
    Examples = {
        "English": ["Hello, World!", "How are you?", "I love programming"],
        "Spanish": ["¡Hola, mundo!", "¿Cómo estás?", "Me encanta programar"],
        "French": ["Bonjour le monde!", "Comment ça va?", "J'adore programmer"],
        "German": ["Hallo, Welt!", "Wie geht es dir?", "Ich liebe programmieren"],
        "Chinese": ["你好，世界！", "你好吗？", "我喜欢编程"],
        "Japanese": ["こんにちは、世界！", "元気ですか？", "プログラミングが大好きです"]
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
            print(f"Grammar: {cls.Grammar}")
            print(f"Recognizing Automaton: {cls.Recognizing_Automaton}")
            print(f"Production Rules (Constraints):")
            for rule, description in cls.Production_rules.items():
                print(f"- {rule}: {description}")
            print(f"Examples using {language.name}:")
            for example in cls.Examples[language.name]:
                print(f"- {example}")
        else:
            print("Language not recognized.")

def recognize_programming_language():
    print("Welcome to the Programming Language Recognition System!")
    print("This system can provide information about various programming languages.")
    print("Here are the available languages:")
    print(Language.Languages)
    
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
