def add(a, b):
    """
    Adds two numbers.
    
    :param a: First number (float or int)
    :param b: Second number (float or int)
    :return: A dictionary containing operation details and the result.
    """
    return {"operation": "add", "input_1": a, "input_2": b, "result": a + b}

def subtract(a, b):
    """
    Subtracts the second number from the first.
    
    :param a: First number (float or int)
    :param b: Second number (float or int)
    :return: A dictionary containing operation details and the result.
    """
    return {"operation": "subtract", "input_1": a, "input_2": b, "result": a - b}

def multiply(a, b):
    """
    Multiplies two numbers.
    
    :param a: First number (float or int)
    :param b: Second number (float or int)
    :return: A dictionary containing operation details and the result.
    """
    return {"operation": "multiply", "input_1": a, "input_2": b, "result": a * b}

def divide(a, b):
    """
    Divides the first number by the second.
    
    :param a: First number (float or int)
    :param b: Second number (float or int)
    :return: A dictionary containing operation details and the result, or an error message if division by zero occurs.
    """
    if b == 0:
        return {
            "operation": "divide",
            "input_1": a,
            "input_2": b,
            "result": None,
            "error": "Division by zero is not allowed."
        }
    return {"operation": "divide", "input_1": a, "input_2": b, "result": a / b}

if __name__ == "__main__":
    # Example usage
    print(add(5, 3))          # {'operation': 'add', 'input_1': 5, 'input_2': 3, 'result': 8}
    print(subtract(10, 4))    # {'operation': 'subtract', 'input_1': 10, 'input_2': 4, 'result': 6}
    print(multiply(7, 6))     # {'operation': 'multiply', 'input_1': 7, 'input_2': 6, 'result': 42}
    print(divide(8, 2))       # {'operation': 'divide', 'input_1': 8, 'input_2': 2, 'result': 4.0}
    print(divide(5, 0))       # {'operation': 'divide', 'input_1': 5, 'input_2': 0, 'result': None, 'error': 'Division by zero is not allowed.'}
