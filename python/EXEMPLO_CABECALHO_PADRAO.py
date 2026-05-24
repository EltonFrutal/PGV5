# ============================================================
#  EXEMPLO: Como criar páginas com cabeçalho padrão
# ============================================================

"""
FUNÇÕES REUTILIZÁVEIS NO UTILS.PY:

1. gerar_meta_icons(path_raiz='')
   → Meta tags para favicon e ícones mobile

2. gerar_cabecalho(icone_empresa=None, mostrar_trocar_org=True, path_raiz='')
   → Cabeçalho completo com logo, avatar, botão sair
   
3. gerar_subnav(pagina_ativa='dash', dash_arq='', lista_arq='', filtros_html='')
   → Submenu (Dashboard/Listagem/Filtros)
"""

# ============================================================
#  EXEMPLO 1: Página de Dashboard
# ============================================================

from utils import css_base, gerar_meta_icons, gerar_cabecalho, gerar_subnav

def gerar_compras_dash(emp, dados):
    """Exemplo: Dashboard de Compras"""
    
    cor = emp.get('cor', '#0ea5e9')
    nome = emp.get('nome', 'Organização')
    icone = emp.get('icone', 'multicar')
    
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{nome} — Compras Dashboard</title>
{gerar_meta_icons(path_raiz='../../')}
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest"></script>
<style>
{css_base(cor)}
body{{display:block;}}
/* Seus estilos customizados aqui */
</style>
</head>
<body>
{gerar_cabecalho(
    icone_empresa=icone,
    mostrar_trocar_org=True,
    path_raiz='../../'
)}
{gerar_subnav(
    pagina_ativa='dash',
    dash_arq='compras_dash.html',
    lista_arq='compras_lista.html'
)}
<main style="max-width:1400px;margin:0 auto;padding:16px;">
  <h1>Dashboard de Compras</h1>
  <!-- Seu conteúdo aqui -->
</main>
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
<script>lucide.createIcons();</script>
</body>
</html>"""


# ============================================================
#  EXEMPLO 2: Página de Listagem
# ============================================================

def gerar_compras_lista(emp, dados):
    """Exemplo: Listagem de Compras"""
    
    cor = emp.get('cor', '#0ea5e9')
    nome = emp.get('nome', 'Organização')
    icone = emp.get('icone', 'multicar')
    
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{nome} — Compras Listagem</title>
{gerar_meta_icons(path_raiz='../../')}
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{css_base(cor)}
body{{display:block;}}
</style>
</head>
<body>
{gerar_cabecalho(
    icone_empresa=icone,
    mostrar_trocar_org=True,
    path_raiz='../../'
)}
{gerar_subnav(
    pagina_ativa='lista',
    dash_arq='compras_dash.html',
    lista_arq='compras_lista.html'
)}
<main style="max-width:1400px;margin:0 auto;padding:16px;">
  <h1>Listagem de Compras</h1>
  <!-- Sua tabela/listagem aqui -->
</main>
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
<script>lucide.createIcons();</script>
</body>
</html>"""


# ============================================================
#  EXEMPLO 3: Página sem subnav (ex: página de menu)
# ============================================================

def gerar_pagina_simples(emp, dados):
    """Exemplo: Página sem submenu"""
    
    cor = emp.get('cor', '#0ea5e9')
    nome = emp.get('nome', 'Organização')
    icone = emp.get('icone', 'multicar')
    
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{nome} — Menu</title>
{gerar_meta_icons(path_raiz='../../')}
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{css_base(cor)}
body{{display:block;}}
</style>
</head>
<body>
{gerar_cabecalho(
    icone_empresa=icone,
    mostrar_trocar_org=True,
    path_raiz='../../'
)}
<!-- SEM SUBNAV -->
<main style="max-width:1400px;margin:0 auto;padding:16px;">
  <h1>Menu Principal</h1>
  <!-- Cards de módulos aqui -->
</main>
</body>
</html>"""


# ============================================================
#  RESUMO DAS VANTAGENS:
# ============================================================

"""
✅ CÓDIGO REUTILIZÁVEL:
   - Cabeçalho, meta tags e subnav prontos
   - Não precisa reescrever HTML/CSS
   - Manutenção centralizada

✅ PADRÃO VISUAL CONSISTENTE:
   - Logo empresa sempre aparece
   - Avatar do usuário sempre carrega
   - Botões e layout idênticos

✅ CAMINHOS CORRETOS:
   - path_raiz ajusta automaticamente
   - Funciona em qualquer nível de pasta

✅ FÁCIL CRIAR NOVAS PÁGINAS:
   - 3 linhas: gerar_meta_icons + gerar_cabecalho + gerar_subnav
   - Copia/cola de exemplo acima
"""
