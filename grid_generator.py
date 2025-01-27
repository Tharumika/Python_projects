import random
from prettytable import PrettyTable
import sys
import datetime

def create_grid(rows, columns):
    # Initialize an empty grid
    grid = []

    # Loop through each row
    for _ in range(rows):
        # Create a row with 'columns' number of elements
        row = []
        for _ in range(columns):
            # Randomly create an empty box
            if random.random() < 0.15:  
                row.append('  ')  
            else:
                # Randomly creating two-digit numbers
                row.append(random.randint(10, 99))
        # Append the row to the grid
        grid.append(row)

    return grid

def print_grid(grid): 
    # Create a pretty table
    table = PrettyTable()

    # Add numbers of the grid above each column
    for col in range(len(grid[0])):
        numbers_in_column = [grid[row][col] for row in range(len(grid))]
        table.add_column(f"Column {col+1}", numbers_in_column)
    
    # Add "Yes" or "No" if there are empty boxes in each column 
    empty_boxes = []
    for col in range(len(grid[0])):
        has_empty = any(grid[row][col] == '  ' for row in range(len(grid)))
        if has_empty:
            empty_boxes.append("No")
        else:
            empty_boxes.append("Yes")
    table.add_row(empty_boxes)

    # Print the pretty table
    print(table)
    return str(table)

def main():
    # Check if command-line are provided rows and columns
    if len(sys.argv) == 3:
        try:
            rows = int(sys.argv[1])
            columns = int(sys.argv[2])
        except ValueError:
            print("Invalid input. Please enter integer values for rows and columns.")
            sys.exit(1)
    else:
        rows = 5
        columns = 5

    # Validate rows and columns
    if rows < 3 or rows > 9 or columns < 3 or columns > 9:
        print("Please enter dimensions between 3x3 and 9x9")
        sys.exit(1)

    # Create the grid
    grid = create_grid(rows, columns)

    # Print the grid 
    output_text = print_grid(grid)

    # Today date
    today_date = datetime.date.today().strftime("%Y_%m_%d_")

    # Generate 4-digit random number
    random_number = str(random.randint(1000, 9999))

    # Save as text file
    text_filename = f"{today_date}_{random_number}.txt"
    with open(text_filename, "w") as text_file:
        text_file.write(output_text)

    # Save as HTML file
    html_filename = f"{today_date}_{random_number}.html"
    with open(html_filename, "w") as html_file:
        html_content = f"<html><body><pre>{output_text}</pre></body></html>"
        html_file.write(html_content)

    print(f"Output saved as text file and HTML file")

if __name__ == "__main__":
    main()
