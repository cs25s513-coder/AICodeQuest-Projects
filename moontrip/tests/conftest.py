# BASELINE — implemented by the study team. Do not modify for tasks M1-M12.
# Makes `logic` importable when pytest is run from the moontrip/ folder.
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
