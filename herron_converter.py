# Herron Temperature Scale Converter
# Converts between Herron (H), Fahrenheit (F), and Celsius (C)
# Aug 07, 2025

def h_to_f(h):
    """Convert Herron to Fahrenheit"""
    return (2/3) * h + 32

def f_to_h(f):
    """Convert Fahrenheit to Herron"""
    return (3/2) * (f - 32)

def h_to_c(h):
    """Convert Herron to Celsius"""
    return (10/27) * h

def c_to_h(c):
    """Convert Celsius to Herron"""
    return (27/10) * c

def main():
    print("Herron Temperature Scale Converter")
    print("Enter a number to see conversions (or 'q' to quit)")
    print("-" * 40)

    while True:
        user_input = input("\nEnter a temperature value: ").strip()

        # Check for quit command
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("\nGoodbye!\n")
            break

        try:
            # Convert input to float
            x = float(user_input)

            # Print conversions
            print(f"\n{x} H = {h_to_f(x):.2f} F")
            print(f"{x} F = {f_to_h(x):.2f} H")
            print(f"{x} H = {h_to_c(x):.2f} C")
            print(f"{x} C = {c_to_h(x):.2f} H")

        except ValueError:
            print("Please enter a valid number (or 'q' to quit)")

if __name__ == "__main__":
    main()
