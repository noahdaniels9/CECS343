import csv

category_list = []


def read_from_database(filename):
    """Read all category information from the database into memory"""
    with open(filename, 'r') as fp:
        for line in fp:
            category_list.append(line.strip())


def write_to_database(filename):
    """Write all category information from memory into the database"""
    with open(filename, 'w') as fp:
        writer = csv.writer(fp)
        for category in category_list:
            writer.writerow([category])


