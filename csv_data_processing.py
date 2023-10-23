import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

def process_csv_file(file_path):
    processed_data = []

    with open(file_path, "r") as input_file:
        reader = csv.DictReader(input_file)

        for row in reader:
            product = row['product']
            raw_price = row['price']
            quantity = row['quantity']
            transaction_date = row['date']
            region = row['region']

            if product == "pink morsel":
                price = float(raw_price[1:])  # Remove '$' and convert to float
                sale = price * int(quantity)

                processed_data.append({'sales': sale, 'date': transaction_date, 'region': region})

    return processed_data

def main():
    header = ["sales", "date", "region"]
    with open(OUTPUT_FILE_PATH, "w", newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=header)
        writer.writeheader()

        for file_name in os.listdir(DATA_DIRECTORY):
            file_path = os.path.join(DATA_DIRECTORY, file_name)
            processed_data = process_csv_file(file_path)
            writer.writerows(processed_data)

if __name__ == "__main__":
    main()
