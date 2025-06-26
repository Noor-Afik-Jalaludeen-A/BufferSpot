# convert_to_utf8.py

input_file = "db_backup.json"
output_file = "db_backup_utf8.json"

with open(input_file, "r", encoding="windows-1252") as source_file:
    content = source_file.read()

with open(output_file, "w", encoding="utf-8") as target_file:
    target_file.write(content)

print("✅ File converted to UTF-8 and saved as db_backup_utf8.json")
