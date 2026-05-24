# ============================================================
#  gerar_pgv5.py — Gerador Completo com Login e Autenticação
# ============================================================

import os
from datetime import datetime
from schema import ler_configuracao, obter_empresas_usuario, obter_permissoes_usuario
from paginas import pg_login, pg_empresas, pg_modulos, pg_vendas_dash, pg_vendas_lista


def salvar(caminho, conteudo):
    """Salva arquivo HTML"""
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    print(f"      ✔ {caminho}")


def main():
    print("=" * 60)
    print("  PGV5 — Gerador Completo com Autenticação")
    print("=" * 60)
    
    # ── 1. LER CONFIGURAÇÃO ────────────────────────────────
    print("\n[1/6] Lendo configuração...")
    config = ler_configuracao('configuracao.xlsx')
    
    print(f"      ✔ {len(config['usuarios'])} usuários")
    print(f"      ✔ {len(config['empresas'])} empresas cadastradas")
    
    # Filtrar empresas ativas
    empresas_ativas = [e for e in config['empresas'] if e.is_ativa()]
    print(f"      ✔ {len(empresas_ativas)} empresas ativas")
    
    # ── 2. GERAR LOGIN ─────────────────────────────────────
    print("\n[2/6] Gerando página de login...")
    
    # DEBUG: Ver qual usuário está sendo usado
    print(f"\n   🔍 DEBUG - Usuários carregados:")
    for i, u in enumerate(config['usuarios']):
        print(f"      [{i}] ID={u.id}, Nome={u.nome}")
    
    print(f"\n   🔍 Usando config['usuarios'][0]:")
    usuario = config['usuarios'][0]
    print(f"      ID={usuario.id}, Nome={usuario.nome}")
    
    salvar("../index.html", pg_login.gerar())
    
    # ── 2.1. GERAR MANIFEST.JSON ───────────────────────────
    print("\n[2.1/6] Gerando manifest.json...")
    manifest = {
        "name": "Painel Gerencial",
        "short_name": "Painel Gerencial",
        "description": "Sistema de Gestão Empresarial",
        "start_url": "./index.html",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#000000",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "./imagem/logos/sistema.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any"
            },
            {
                "src": "./imagem/logos/sistema.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "maskable"
            }
        ]
    }
    import json
    with open("../manifest.json", 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"      ✔ ../manifest.json")
    
    # ── 3. GERAR SELEÇÃO DE EMPRESAS ───────────────────────
    print("\n[3/6] Gerando página de empresas...")
    
    # Para cada usuário, gerar empresas.html com suas empresas
    # Por enquanto vamos gerar para o primeiro usuário
    usuario = config['usuarios'][0]
    empresas_usuario = obter_empresas_usuario(usuario.id, config)
    
    # Preparar dados para página
    empresas_data = [
        {
            'id': emp.id,
            'nome': emp.empresa,
            'icone': emp.icone
        }
        for emp in empresas_usuario
    ]
    
    usuario_data = {
        'id': usuario.id,
        'nome': usuario.nome,
        'perfil': usuario.perfil
    }
    
    salvar("../empresas.html", pg_empresas.gerar(usuario_data, empresas_data))
    
    # ── 4. CRIAR PASTAS POR EMPRESA ────────────────────────
    print("\n[4/6] Criando estrutura de pastas...")
    
    for empresa in empresas_ativas:
        pasta = f"../empresa/{empresa.icone}"  # ../empresa/multicar, ../empresa/cocacafe
        os.makedirs(pasta, exist_ok=True)
        print(f"      ✔ {pasta}/")
    
    # ── 5. GERAR MENU DE MÓDULOS ───────────────────────────
    print("\n[5/6] Gerando menus de módulos...")
    
    # Gerar JSON com todas as permissões
    import json
    permissoes_json = {}
    
    print("\n      📋 Lendo permissões do Excel:")
    for usu in config['usuarios']:  # Renomeado de 'usuario' para 'usu'
        for empresa in empresas_ativas:
            permissoes = obter_permissoes_usuario(usu.id, empresa.id, config)
            if permissoes:
                chave = f"{usu.id}_{empresa.id}"
                permissoes_json[chave] = {
                    'exibevendas': permissoes.exibevendas,
                    'exibecompras': permissoes.exibecompras,
                    'exibeareceber': permissoes.exibeareceber,
                    'exibeapagar': permissoes.exibeapagar,
                    'exibehistoricos': permissoes.exibehistoricos,
                    'exibeindicadores': permissoes.exibeindicadores,
                    'exiberesultados': permissoes.exiberesultados
                }
                # Debug - mostrar permissões
                print(f"      • {usu.nome} @ {empresa.empresa}:")
                print(f"        Compras: {permissoes.exibecompras}")
                if permissoes.exibecompras == 'não':
                    print(f"        ⚠️  SEM PERMISSÃO PARA COMPRAS")
    
    # Salvar JSON de permissões
    with open('../permissoes.json', 'w', encoding='utf-8') as f:
        json.dump(permissoes_json, f, ensure_ascii=False, indent=2)
    print(f"      ✔ ../permissoes.json")
    
    # Gerar menu.html para cada empresa (dinâmico)
    for empresa in empresas_ativas:
        empresa_data = {
            'id': empresa.id,
            'nome': empresa.empresa,
            'icone': empresa.icone
        }
        
        # Passar permissões vazias - será carregado via JavaScript
        permissoes_data = {
            'exibevendas': 'sim',
            'exibecompras': 'sim',
            'exibeareceber': 'sim',
            'exibeapagar': 'sim',
            'exibehistoricos': 'sim',
            'exibeindicadores': 'sim',
            'exiberesultados': 'sim'
        }
        
        caminho = f"../empresa/{empresa.icone}/menu.html"
        salvar(caminho, pg_modulos.gerar(empresa_data, permissoes_data))
    
    # ── 6. GERAR PÁGINAS DE VENDAS ─────────────────────────
    print("\n[6/6] Gerando páginas de vendas (dados fictícios)...")
    
    for empresa in empresas_ativas:
        print(f"\n   Processando {empresa.empresa} (ID={empresa.id})...")
        print(f"      🔍 Chamando: obter_permissoes_usuario({usuario.id}, {empresa.id}, config)")
        
        # Verificar se usuário tem acesso a vendas
        permissoes = obter_permissoes_usuario(usuario.id, empresa.id, config)
        
        print(f"      🔍 Retorno: {permissoes}")
        print(f"      🔍 Tipo: {type(permissoes)}")
        
        if permissoes:
            print(f"      Permissões encontradas: exibevendas={permissoes.exibevendas}")
            print(f"      🔍 tem_permissao('vendas'): {permissoes.tem_permissao('vendas')}")
        else:
            print(f"      ❌ SEM permissões!")
            continue
        
        if permissoes.tem_permissao('vendas'):
            print(f"      ✅ Gerando vendas...")
            
            # Preparar dados fictícios
            dados_ficticios = {
                'data_atualizacao': datetime.now().strftime('%d/%m/%Y %H:%M')
            }
            
            emp_config = {
                'id': empresa.id,
                'nome': empresa.empresa,
                'icone': empresa.icone,
                'logo': f'../../imagem/logos/{empresa.icone}.png',
                'cor': '#0ea5e9',  # Cor padrão
                'menu_arquivo': 'menu.html',
                'vendas_arquivo': 'vendas_dash.html',
                'listagem_arquivo': 'vendas_lista.html'
            }
            
            # Gerar dashboard
            caminho_dash = f"../empresa/{empresa.icone}/vendas_dash.html"
            salvar(caminho_dash, pg_vendas_dash.gerar(emp_config, dados_ficticios))
            
            # Gerar listagem
            caminho_lista = f"../empresa/{empresa.icone}/vendas_lista.html"
            salvar(caminho_lista, pg_vendas_lista.gerar(emp_config, dados_ficticios))
        else:
            print(f"      ⚠️  Sem permissão de vendas (exibevendas={permissoes.exibevendas})")
    
    # ── RESUMO ─────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("✅ GERAÇÃO CONCLUÍDA!")
    print("=" * 60)
    print(f"\nArquivos gerados:")
    print(f"  • index.html (login)")
    print(f"  • empresas.html (seleção de empresa)")
    
    for empresa in empresas_ativas:
        print(f"  • {empresa.icone}/")
        print(f"      - menu.html")
        
        permissoes = obter_permissoes_usuario(usuario.id, empresa.id, config)
        if permissoes and permissoes.tem_permissao('vendas'):
            print(f"      - vendas_dash.html")
            print(f"      - vendas_lista.html")
    
    print(f"\n📊 Total: {len(empresas_ativas)} empresas geradas")
    print(f"\n🌐 Acesse: index.html")
    print(f"   Login: {usuario.nome}")
    print(f"   Senha: {usuario.senha}")
    

if __name__ == '__main__':
    main()
