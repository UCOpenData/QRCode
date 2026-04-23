import csv
from datetime import datetime

# ---- EDIT THESE ----
INPUT_FILE = "full_data.csv"
OUTPUT_FILE = "two_months.csv"
CUTOFF = datetime(2025, 12, 20, 23, 59, 59)  # keep rows with Timestamp <= this
# --------------------

TS_FMT = "%m/%d/%Y %H:%M:%S"

with open(INPUT_FILE, "r", newline="", encoding="utf-8-sig") as f_in, \
     open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f_out:

    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        ts = row.get("Timestamp", "")
        if not ts:
            continue
        if datetime.strptime(ts.strip(), TS_FMT) <= CUTOFF:
            writer.writerow(row)
