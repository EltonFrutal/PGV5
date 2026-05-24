#!/usr/bin/env python3
# ============================================================
#  limpar_repo.py — Limpar repositório Git e recomeçar
# ============================================================

import os
import shutil
from datetime import datetime

print("=" * 60)
print("  LIMPAR REPOSITÓRIO GIT")
print("=" * 60)

# Pasta do repositório
repo_path = r'C:\Users\elton\OneDrive\Backup_Sistemas\Elton\Projetos\PGWeb\pgv5'

if not os.path.exists(repo_path):
    print(f"\n❌ Pasta não encontrada: {repo_path}")
    exit(1)

# 1. Fazer backup
print("\n[1/4] Fazendo backup...")
backup_name = f"pgv5_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
backup_path = os.path.join(os.path.dirname(repo_path), backup_name)

try:
    shutil.copytree(repo_path, backup_path)
    print(f"  ✔ Backup criado: {backup_path}")
except Exception as e:
    print(f"  ⚠️  Erro no backup: {e}")
    print("  Continuando mesmo assim...")

# 2. Entrar na pasta do repositório
os.chdir(repo_path)

# 3. Remover todos os arquivos (exceto .git)
print("\n[2/4] Removendo arquivos antigos...")
removidos = 0
for item in os.listdir('.'):
    if item == '.git':
        continue
    
    item_path = os.path.join('.', item)
    try:
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)
        removidos += 1
        print(f"  ✔ Removido: {item}")
    except Exception as e:
        print(f"  ⚠️  Erro ao remover {item}: {e}")

print(f"\n  Total removido: {removidos} itens")

# 4. Listar o que sobrou
print("\n[3/4] Verificando pasta...")
items = os.listdir('.')
print(f"  Itens restantes: {len(items)}")
for item in items:
    print(f"    • {item}")

print("\n[4/4] Status do Git...")
import subprocess
result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
print(result.stdout if result.stdout else "  (vazio)")

print("\n" + "=" * 60)
print("✅ REPOSITÓRIO LIMPO!")
print("=" * 60)
print("\n📋 PRÓXIMOS PASSOS:\n")
print("1. Copiar arquivos novos para:")
print(f"   {repo_path}\n")
print("2. Adicionar e commitar:")
print("   cd " + repo_path)
print("   git add .")
print('   git commit -m "Versão inicial completa - Sistema PGV5"\n')
print("3. Push para GitHub:")
print("   git push origin main\n")
