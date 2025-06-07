# utils.py
import csv, os
from config import CSV_FILE

def enregistrer_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nom", "Prénom", "Email", "Service", "Date", "Heure"])
        writer.writerow(data)
