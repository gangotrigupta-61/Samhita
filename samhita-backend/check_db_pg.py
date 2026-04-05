import os
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine, text
from pprint import pprint
import json

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("NO DATABASE_URL found")
    exit(1)

# fix the pg connection issues seen in the application
# import socket
# from urllib.parse import urlparse
# _connect_args = {}
# try:
#     parsed = urlparse(DATABASE_URL)
#     if parsed.hostname:
#         resolved = socket.gethostbyname(parsed.hostname)
#         _connect_args["hostaddr"] = resolved
# except Exception as e:
#     pass



# engine = create_engine(DATABASE_URL, connect_args=_connect_args)
# with engine.connect() as conn:
#     # Get document 17
#     result = conn.execute(text("SELECT id, error_message, extracted_json FROM documents WHERE id = 17")).fetchone()
#     if not result:
#         print("Document 17 not found")
#         exit(0)
    
#     print("ID:", result[0])
#     print("Error:", result[1])
#     try:
#         d = json.loads(result[2])
#     except:
#         d = {}
#     print("Extracted Keys:", list(d.keys()))
#     print("Raw Text Length:", len(d.get("raw_text", "")))
#     print("Raw Text snippet:", repr(d.get("raw_text", "")[:200]))

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    connect_args={"sslmode": "require"}
)