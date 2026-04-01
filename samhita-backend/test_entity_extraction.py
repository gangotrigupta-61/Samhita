"""Quick test: extract entities from demo discharge summary via Groq NLP."""
import os
import sys
import json
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

from services.nlp import extract_entities

# Read demo discharge summary
with open("demo_data/case1_cardiac_surgery.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print(f"Input text length: {len(raw_text)} chars")
print("=" * 60)
print("Calling Groq NLP entity extraction...")
print("=" * 60)

entities = extract_entities(raw_text)

print(f"\nExtracted {len(entities)} entities:\n")
for i, e in enumerate(entities, 1):
    conf = e.get("confidence", 0)
    neg = " [NEGATED]" if e.get("negated") else ""
    print(f"  {i:2d}. [{e.get('entity_type', '?'):12s}] {e.get('entity_text', '')}{neg}")
    print(f"      Normalized: {e.get('normalized_value', '')}")
    print(f"      Confidence: {conf:.0%}")
    if e.get("temporal_context"):
        print(f"      Temporal: {e.get('temporal_context')}")
    print()

print(f"Total: {len(entities)} entities extracted")
if entities:
    avg_conf = sum(e.get("confidence", 0) for e in entities) / len(entities)
    print(f"Average confidence: {avg_conf:.0%}")
