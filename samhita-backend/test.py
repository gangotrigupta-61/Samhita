from dotenv import load_dotenv
load_dotenv()
from services.vision import extract_from_image
try:
    res = extract_from_image("uploads/16/page_1.png")
    print("SUCCESS")
    print("KEYS:", res.keys())
    print("Entities / Text snippet:")
    print(res.get("raw_text", "")[:400])
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"FAILED: {e}")
