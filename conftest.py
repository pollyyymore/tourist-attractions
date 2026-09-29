"""conftest.py — файл нужен, чтобы pytest заработал, тк выдавал ошибку."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
