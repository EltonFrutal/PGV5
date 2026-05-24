# ============================================================
#  pg_vendas_lista.py — Listagem de Vendas
# ============================================================

from datetime import datetime
from utils import css_base, gerar_cabecalho, gerar_subnav, gerar_meta_icons

def gerar(emp, dados):
    """Listagem de vendas"""
    
    cor = emp.get("cor", "#0ea5e9")
    nome = emp.get("nome", "Organização")
    
    # Arquivos - SEM defaults incorretos
    menu_arq = emp.get('menu_arquivo', 'index.html')
    dash_arq = emp.get('vendas_arquivo', 'vendas_dash.html')
    lista_arq = emp.get('listagem_arquivo', 'vendas_lista.html')
    
    # Data de atualização
    data_atualizacao = dados.get('data_atualizacao', datetime.now().strftime('%d/%m/%Y %H:%M'))
    
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>""" + nome + """ &mdash; Vendas Listagem</title>
""" + gerar_meta_icons(path_raiz='../../') + """
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest"></script>
<style>
""" + css_base(cor) + """
body{display:block;}
</style>
</head>
<body>
""" + gerar_cabecalho(
    icone_empresa=emp.get('icone'),
    mostrar_trocar_org=True,
    path_raiz='../../'
) + gerar_subnav(
    pagina_ativa='lista',
    dash_arq=dash_arq,
    lista_arq=lista_arq
) + """
<main style="max-width:1400px;margin:0 auto;padding:40px;background:#f1f5f9;min-height:100vh;">
<h1 style="font-size:1.8rem;font-weight:900;color:#0f172a;letter-spacing:-.03em;margin-bottom:8px;">Listagem</h1>
<p style="font-size:.85rem;color:#64748b;font-weight:500;">Em desenvolvimento...</p>
</main>
<script>
lucide.createIcons();
</script>
</body></html>"""
