#!/usr/bin/env python3
# ============================================================
#  limpar_cache.py — Limpar cache Python
# ============================================================

import os
import shutil
from pathlib import Path

print("=" * 60)
print("  LIMPAR CACHE PYTHON")
print("=" * 60)

# Encontrar e deletar __pycache__
for pycache in Path('.').rglob('__pycache__'):
    print(f"🗑️  Deletando: {pycache}")
    shutil.rmtree(pycache)

# Deletar .pyc
for pyc in Path('.').rglob('*.pyc'):
    print(f"🗑️  Deletando: {pyc}")
    pyc.unlink()

print("\n✅ Cache limpo!")
print("=" * 60)
