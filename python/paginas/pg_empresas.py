# ============================================================
#  pg_empresas.py — Seleção de Empresas (Com Cabeçalho Padrão)
# ============================================================

from utils import gerar_cabecalho

def gerar(usuario, empresas):
    """Gera página de seleção de empresas usando cabeçalho padrão"""
    
    # Gerar cards de empresas
    empresas_html = ""
    for i, emp in enumerate(empresas):
        delay = i * 0.08
        empresas_html += f"""
  <a class="emp-card" href="empresa/{emp['icone']}/menu.html" style="animation-delay:{delay}s">
    <div class="emp-icone">
      <img src="imagem/logos/{emp['icone']}.png" alt="{emp['nome']}" onerror="this.outerHTML='<div style=\\'font-size:2rem\\'>🏢</div>'">
    </div>
    <div class="emp-nome-card">{emp['nome']}</div>
  </a>
"""
    
    # Usar função de cabeçalho padrão
    cabecalho = gerar_cabecalho(
        icone_empresa=None,          # Sem ícone de empresa
        mostrar_trocar_org=False,    # Sem botão trocar (já está aqui)
        path_raiz=''                 # Na raiz
    )
    
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Painel Gerencial</title>

<!-- Favicon e ícones -->
<link rel="icon" type="image/png" sizes="32x32" href="imagem/logos/sistema.png">
<link rel="icon" type="image/png" sizes="16x16" href="imagem/logos/sistema.png">
<link rel="apple-touch-icon" sizes="180x180" href="imagem/logos/sistema.png">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="PGV5">

<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;margin:0;}
body{background:#e2e8f0;color:#1e293b;font-family:'Plus Jakarta Sans',sans-serif;min-height:100vh;}

/* Conteúdo */
.main-content{padding:28px;}
.sec-titulo{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#94a3b8;margin-bottom:16px;}
.emp-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:20px;max-width:1000px;}
.emp-card{background:#fff;border:1.5px solid #f1f5f9;border-radius:16px;padding:32px 20px;cursor:pointer;text-decoration:none;display:flex;flex-direction:column;align-items:center;text-align:center;transition:all .25s;box-shadow:0 1px 3px rgba(0,0,0,.06);}
.emp-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(0,0,0,.1);}
.emp-icone{width:64px;height:64px;border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:16px;background:#f1f5f9;}
.emp-icone img{width:100%;height:100%;object-fit:contain;}
.emp-nome-card{font-size:.9rem;font-weight:700;color:#1e293b;}

@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.emp-card{animation:fadeUp .4s ease both;}
</style>
</head>
<body>

""" + cabecalho + """

<div class="main-content">
  <div class="sec-titulo">Selecione a Organização</div>
  <div class="emp-grid">
""" + empresas_html + """
  </div>
</div>

</body>
</html>
"""
