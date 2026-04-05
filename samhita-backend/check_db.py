# import sqlite3
# import json

# try:
#     conn = sqlite3.connect("samhita.db") # wait, db might be in data/samhita.db? Let's check both
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, error_message, extracted_json, coded_json FROM documents WHERE id = 17")
#     row = cursor.fetchone()
#     print("ID:", row[0])
#     print("Error:", row[1])
#     d = json.loads(row[2]) if row[2] else {}
#     print("Extracted Keys:", list(d.keys()) if d else None)
#     print("Extracted Data:", str(d)[:500])
# except Exception as e:
#     import traceback
#     traceback.print_exc()

# import os
# print("Testing with data/samhita.db")
# try:
#     conn = sqlite3.connect("data/samhita.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, error_message, extracted_json, coded_json FROM documents WHERE id = 17")
#     row = cursor.fetchone()
#     print("ID:", row[0])
#     print("Error:", row[1])
#     d = json.loads(row[2]) if row[2] else {}
#     print("Extracted Keys:", list(d.keys()) if d else None)
#     print("Raw Text Snippet:", d.get('raw_text', '')[:100] if d else None)
# except Exception as e:
#     import traceback
#     traceback.print_exc()

