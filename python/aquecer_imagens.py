#!/usr/bin/env python3
# ============================================================
#  aquecer_imagens.py — Força carregamento de todas imagens
# ============================================================

import os
from pathlib import Path

print("=" * 60)
print("  AQUECENDO IMAGENS")
print("=" * 60)

os.chdir('..')
pasta_imagem = Path('imagem')

if not pasta_imagem.exists():
    print("\n❌ Pasta imagem/ não existe!")
    exit(1)

print(f"\n📂 Carregando arquivos de: {pasta_imagem.absolute()}\n")

count = 0
for arquivo in pasta_imagem.rglob('*'):
    if arquivo.is_file():
        # Ler 1 byte força Windows carregar arquivo
        with open(arquivo, 'rb') as f:
            f.read(1)
        count += 1
        print(f"   ✅ {arquivo.relative_to(pasta_imagem)}")

print(f"\n✅ {count} arquivos carregados!")
print("=" * 60)
