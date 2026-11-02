import csv


# function to read the csv file
def read_csv_file(file_name):
    website_list = []
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            website_list.append(row)
    return website_list

# function to write new rows which the user has entered from the menu at the end of the file
def write_csv_file(file_name, website_list,mode):
    with open(file_name, mode=mode, newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in website_list:
            writer.writerow(row)
