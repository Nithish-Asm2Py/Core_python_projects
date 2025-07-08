import csv

# Function to clean a CSV file
def clean_csv(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)

            # Read the first row as headers
            headers = next(reader)

            # Clean headers: strip whitespace and make lowercase
            clean_headers = [h.strip().lower() for h in headers]

            # List to store clean rows
            cleaned_rows = []

            # Loop through each remaining row
            for row in reader:
                # Clean each cell: strip whitespace
                clean_row = [cell.strip() for cell in row]

                # Skip row if any cell is empty
                if "" in clean_row:
                    continue

                # Add the cleaned row to our list
                cleaned_rows.append(clean_row)

        # Write cleaned data to output file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)

            # Write cleaned headers first
            writer.writerow(clean_headers)

            # Then write each cleaned row
            writer.writerows(cleaned_rows)

        print(f"✅ Cleaned CSV saved as '{output_file}'")

    except FileNotFoundError:
        print("❌ Input file not found. Please check the file name.")
    except Exception as e:
        print("⚠️ An error occurred:", e)


# ----------------------------------------
# Run the function with user input
# ----------------------------------------
if __name__ == "__main__":
    # Ask user for input file name
    input_file = input("Enter input CSV file name (with .csv extension): ")

    # Ask user for output file name
    output_file = input("Enter output CSV file name: ")

    # Run the cleaner function
    clean_csv(input_file, output_file)
