# tests/conftest.py
import sys
from pathlib import Path

# Agrega la carpeta raíz del proyecto (datamanager/) al sys.path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))