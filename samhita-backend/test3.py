import os
import traceback

with open("out2.txt", "w") as f:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        f.write("dotenv loaded\n")

        from services.vision import extract_from_image
        f.write("vision imported\n")

        f.write("running extraction...\n")
        res = extract_from_image("uploads/16/page_1.png")
        f.write("extraction success\n")
        f.write(str(list(res.keys())) + "\n")
    except Exception as e:
        f.write(f"Exception: {type(e).__name__}: {str(e)}\n")
        traceback.print_exc(file=f)
