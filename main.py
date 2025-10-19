import csv
import re
from pprint import pprint

# === Читаем CSV ===
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# === 1. Приводим ФИО к правильному виду ===
new_contacts = []
for contact in contacts_list:
    fio = " ".join(contact[:3]).split()
    while len(fio) < 3:
        fio.append('')
    contact[:3] = fio[:3]
    new_contacts.append(contact)

# === 2. Приводим телефоны к единому формату ===
pattern = re.compile(
    r'(\+7|8)?\s*\(?([0-9]{3})\)?[\s\-]*([0-9]{3})[\s\-]*([0-9]{2})[\s\-]*([0-9]{2})(?:\s*\(?(доб.)\s*(\d+)\)?)?'
)
substitution = r'+7(\2)\3-\4-\5\6\7'

for contact in new_contacts:
    contact[5] = re.sub(pattern, substitution, contact[5]).replace('доб.', ' доб.')

# === 3. Объединяем дубли ===
contacts_dict = {}
for contact in new_contacts:
    lastname, firstname = contact[0], contact[1]
    key = (lastname, firstname)
    if key not in contacts_dict:
        contacts_dict[key] = contact
    else:
        existing = contacts_dict[key]
        for i in range(len(contact)):
            if not existing[i]:
                existing[i] = contact[i]

final_contacts = list(contacts_dict.values())

# === 4. Сохраняем результат ===
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(final_contacts)

pprint(final_contacts)
print("✅ Готово! Файл phonebook.csv сохранён.")
