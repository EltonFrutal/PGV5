# ============================================================
#  reset_e_push.py — Limpa GitHub e sobe versão nova
# ============================================================

import subprocess
import os

REPO_PATH = "C:/PGV5"
REPO_URL = "https://github.com/EltonFrutal/PGV5"

def cmd(comando, descricao):
    """Executa comando git"""
    print(f"\n  • {descricao}...")
    try:
        result = subprocess.run(
            comando,
            cwd=REPO_PATH,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout:
            print(f"    ✓ {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"    ❌ {e.stderr}")
        return False

print("\n" + "=" * 60)
print("🔥 RESET COMPLETO + PUSH LIMPO")
print("=" * 60)
print("\n⚠️  ATENÇÃO: Isso vai DELETAR TUDO no GitHub e subir versão nova!")
print(f"   Repositório: {REPO_URL}")

confirma = input("\n   Continuar? Digite 'SIM' para confirmar: ")

if confirma != 'SIM':
    print("\n   Cancelado.")
    exit()

print("\n🚀 INICIANDO...\n")

# 1. Deletar pasta .git local (reset completo)
print("  • Removendo .git local...")
import shutil
git_folder = os.path.join(REPO_PATH, ".git")
if os.path.exists(git_folder):
    shutil.rmtree(git_folder)
    print("    ✓ Removido")

# 2. Inicializar git novo
cmd("git init", "Inicializando Git novo")

# 3. Adicionar remote
cmd(f"git remote add origin {REPO_URL}", "Conectando ao GitHub")

# 4. Adicionar todos arquivos
cmd("git add .", "Adicionando arquivos")

# 5. Commit
cmd('git commit -m "PGV5 - Sistema completo reorganizado"', "Fazendo commit")

# 6. Branch main
cmd("git branch -M main", "Configurando branch main")

# 7. Force push (SUBSTITUI TUDO no GitHub)
print("\n🔥 FORCE PUSH - SUBSTITUINDO TUDO NO GITHUB...")
cmd("git push -u origin main --force", "Enviando (force)")

print("\n" + "=" * 60)
print("✅ CONCLUÍDO!")
print("=" * 60)
print(f"\n🔗 Acesse: {REPO_URL}")
print("\n✨ GitHub limpo com versão nova do projeto!")
print("=" * 60 + "\n")
