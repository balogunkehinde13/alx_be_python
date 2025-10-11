class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method — performs a simple addition
    @staticmethod
    def add(a, b):
        return a + b

    # Class method — performs multiplication and uses a class attribute
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
