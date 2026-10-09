from csv_loader import load_csv
from conversion import convert
import sys

def main():

    #load the csv file
    if len(sys.argv) > 2:
        print("Please use : python main.py OR python main.py <csv_file>")
        return

    csv_file = sys.argv[1] if len(sys.argv) == 2 else "units.csv"

    try:
        conversion_graph = load_csv(csv_file)

    except (FileNotFoundError, ValueError, KeyError) as e:
        print(f"Error loading CSV: {e}")
        return

    #request user for input : Quantity, source and target
    try:
        quantity = float(input("Quantity: "))
        
    except ValueError:
        print("Invalid quantity. Please enter a number")
        return
    
    source = input("Source unit: ").strip().lower()
    target = input("Target unit: ").strip().lower()

    try: #we want to catch the Value Error that would be raised by convert()
        result = convert(conversion_graph, quantity, source, target)

        print(f"{quantity} {source} = {result} {target}")

    except ValueError as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()

