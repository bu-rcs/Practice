def fibonacci(n):
    """
    Compute the nth Fibonacci number.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


if __name__ == "__main__":
    # Example usage
    print("Fibonacci sequence (first 10 numbers):")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
