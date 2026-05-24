# ============================================================
#  limpar_para_github.py — Preparar projeto para GitHub
# ============================================================

import os
import shutil
from pathlib import Path

# Pasta raiz do projeto
RAIZ = Path("C:/PGV5")

def limpar():
    """Remove arquivos desnecessários antes de subir para GitHub"""
    
    print("\n" + "=" * 60)
    print("🧹 LIMPANDO PROJETO PARA GITHUB")
    print("=" * 60)
    
    # ── ARQUIVOS PARA DELETAR ────────────────────────────────
    arquivos_deletar = [
        "python/IMPLEMENTACAO_LOGIN.md",
        "python/RESTAURACAO_VENDAS_DASH.md",
    ]
    
    for arquivo in arquivos_deletar:
        caminho = RAIZ / arquivo
        if caminho.exists():
            caminho.unlink()
            print(f"  ✓ Deletado: {arquivo}")
    
    # ── PASTAS PARA DELETAR ──────────────────────────────────
    pastas_deletar = [
        "python/__pycache__",
        "python/BKP",
        "python/paginas/__pycache__",
    ]
    
    for pasta in pastas_deletar:
        caminho = RAIZ / pasta
        if caminho.exists():
            shutil.rmtree(caminho)
            print(f"  ✓ Deletada: {pasta}")
    
    # ── OPCIONAL: LIMPAR HTMLs GERADOS ───────────────────────
    limpar_gerados = input("\n❓ Deletar HTMLs gerados (serão recriados com gerar_pgv5.py)? [s/N]: ")
    
    if limpar_gerados.lower() == 's':
        arquivos_gerados = [
            "index.html",
            "empresas.html",
            "permissoes.json",
            "manifest.json",
        ]
        
        for arquivo in arquivos_gerados:
            caminho = RAIZ / arquivo
            if caminho.exists():
                caminho.unlink()
                print(f"  ✓ Deletado: {arquivo}")
        
        # Deletar pasta empresa/
        pasta_empresa = RAIZ / "empresa"
        if pasta_empresa.exists():
            shutil.rmtree(pasta_empresa)
            print(f"  ✓ Deletada: empresa/")
    
    # ── RESUMO ───────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("✅ LIMPEZA CONCLUÍDA!")
    print("=" * 60)
    print("\n📁 ESTRUTURA FINAL:")
    print("""
C:\\PGV5\\
├── .gitignore          ← Configurado
├── README.md           ← Criar documentação
├── imagem/
│   ├── logos/          ← Logos das empresas
│   └── fotos/          ← Fotos dos usuários
└── python/
    ├── paginas/        ← Geradores de páginas
    ├── configuracao.xlsx  ← Dados do sistema
    ├── schema.py       ← Classes principais
    ├── gerar_pgv5.py   ← Gerador principal
    ├── servidor_rapido.py ← Servidor HTTP
    ├── utils.py        ← Funções reutilizáveis
    └── config.py       ← Configurações
    """)
    
    print("\n🚀 PRÓXIMOS PASSOS:")
    print("  1. Revisar arquivos")
    print("  2. git add .")
    print("  3. git commit -m 'Estrutura completa PGV5'")
    print("  4. git push origin main")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    try:
        limpar()
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        print("   Verifique se está executando de C:\\PGV5\\python\\")
