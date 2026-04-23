import csv

with open("two_months.csv", newline="") as infile, open("two_months_noFloor.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        location = row["Location"]

        for idx, val in enumerate(location):
            if val.isdigit():
                location = location[:idx]
        if location.find("First") != -1:
            id = location.find("First")
            location = location[:id]
        if location.find("Second") != -1:
            id = location.find("Second")
            location = location[:id]
        if location.find("Basement") != -1:
            id = location.find("Basement")
            location = location[:id]


        row["Location"] = location

        writer.writerow(row)
