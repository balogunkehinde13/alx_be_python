def safe_divide(numerator, denominator):
    """Safely divide two numbers with error handling."""
    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Handle division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handles non-numeric inputs
        return "Error: Please enter numeric values only."
