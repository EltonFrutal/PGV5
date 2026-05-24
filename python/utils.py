# ============================================================
#  utils.py — Funções Compartilhadas
#  CSS base, Header HTML, Git Push
# ============================================================

import hashlib, subprocess
from datetime import datetime
from config import REPO_PATH

# Constantes
FONT_FAMILY = "'Plus Jakarta Sans', sans-serif"


def gerar_meta_icons(path_raiz=''):
    """
    Gera meta tags para favicon e ícones mobile
    
    Args:
        path_raiz: Caminho relativo para raiz ('' ou '../')
    
    Returns:
        HTML das meta tags
    """
    return f"""
<!-- Favicon e ícones -->
<link rel="icon" type="image/png" sizes="32x32" href="{path_raiz}imagem/logos/sistema.png">
<link rel="icon" type="image/png" sizes="16x16" href="{path_raiz}imagem/logos/sistema.png">
<link rel="apple-touch-icon" sizes="180x180" href="{path_raiz}imagem/logos/sistema.png">
<link rel="manifest" href="{path_raiz}manifest.json">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="PGV5">
"""


def gerar_cabecalho(icone_empresa=None, mostrar_trocar_org=True, path_raiz=''):
    """
    Gera cabeçalho fixo padrão reutilizável
    
    Args:
        icone_empresa: Nome do ícone da empresa (ex: 'multicar') ou None
        mostrar_trocar_org: Se mostra botão trocar organização
        path_raiz: Caminho relativo para raiz ('' ou '../')
    
    Returns:
        HTML do cabeçalho completo com CSS e JavaScript
    """
    
    # CSS do cabeçalho
    css = """
.hdr-main{background:#000;border-bottom:1px solid #1e293b;padding:0 28px;height:58px;
  display:flex;align-items:center;justify-content:space-between;
  position:sticky;top:0;z-index:200;box-shadow:0 2px 8px rgba(0,0,0,.3);}
.hdr-left{display:flex;align-items:center;gap:16px;}
.hdr-menu-btn{background:transparent;border:1.5px solid #334155;border-radius:8px;color:#94a3b8;
  padding:8px;cursor:pointer;text-decoration:none;transition:all .2s;display:flex;align-items:center;
  justify-content:center;width:38px;height:38px;opacity:0.3;pointer-events:none;}
.hdr-logo{height:34px;}
.hdr-titulo{color:#fff;font-weight:700;font-size:1.1rem;letter-spacing:-.02em;}
.hdr-right{display:flex;align-items:center;gap:12px;}
.hdr-empresa-logo{height:32px;margin-right:8px;border:2px solid #fff;border-radius:8px;padding:2px;background:#fff;}
.hdr-avatar{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#8b5cf6);
  display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:800;color:#fff;overflow:hidden;
  border:2px solid #fff;}
.hdr-avatar img{width:100%;height:100%;object-fit:cover;border-radius:50%;}
.btn-trocar-org{background:transparent;border:1.5px solid #334155;border-radius:8px;color:#94a3b8;
  padding:8px;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center;
  width:38px;height:38px;text-decoration:none;}
.btn-trocar-org:hover{border-color:#fff;color:#fff;background:rgba(255,255,255,.1);}
.btn-trocar-org svg{display:block;}
.btn-logoff{background:transparent;border:1.5px solid #334155;border-radius:7px;color:#94a3b8;
  font-family:'Plus Jakarta Sans',sans-serif;font-size:.75rem;font-weight:600;padding:8px 12px;cursor:pointer;
  transition:all .2s;display:flex;align-items:center;}
.btn-logoff:hover{border-color:#ef4444;color:#ef4444;background:rgba(239,68,68,.1);}
.btn-logoff svg{display:block;}

@media(max-width:768px){
  .hdr-titulo{display:none !important;}
  .btn-logoff{width:36px;height:36px;padding:8px;}
  .btn-logoff span{display:none;}
  .btn-logoff svg{width:20px;height:20px;}
}
"""
    
    # Logo da empresa (se fornecido)
    logo_empresa = ''
    if icone_empresa:
        logo_empresa = f'<img src="{path_raiz}imagem/logos/{icone_empresa}.png" class="hdr-empresa-logo" onerror="this.style.display=' + "'none'" + '">'
    
    # Botão trocar organização
    btn_trocar = ''
    if mostrar_trocar_org:
        btn_trocar = f'''<a href="{path_raiz}empresas.html" class="btn-trocar-org" title="Trocar Organização">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"></path><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"></path><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"></path><path d="M10 6h4"></path><path d="M10 10h4"></path><path d="M10 14h4"></path><path d="M10 18h4"></path></svg>
    </a>'''
    
    # HTML do cabeçalho
    html = f"""
<style>
{css}
</style>

<header class="hdr-main">
  <div class="hdr-left">
    <button class="hdr-menu-btn">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
    </button>
    <img src="{path_raiz}imagem/logos/sistema.png" alt="PGV5" class="hdr-logo" onerror="this.style.display='none'">
    <span class="hdr-titulo">Painel Gerencial</span>
  </div>
  <div class="hdr-right">
    {logo_empresa}
    <div class="hdr-avatar" id="hdr-avatar">?</div>
    {btn_trocar}
    <button class="btn-logoff" onclick="sair()">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
      <span style="margin-left:6px">Sair</span>
    </button>
  </div>
</header>

<script>
// Carregar avatar do usuário
(function(){{
  var usuarioId = localStorage.getItem('pgv5_usuario_id');
  var usuarioNome = localStorage.getItem('pgv5_usuario_nome');
  var usuarioFoto = localStorage.getItem('pgv5_usuario_foto');
  
  if(!usuarioId){{
    window.location.href = '{path_raiz}index.html';
    return;
  }}
  
  var avatar = document.getElementById('hdr-avatar');
  if(usuarioFoto){{
    var img = document.createElement('img');
    img.src = '{path_raiz}' + usuarioFoto;
    img.style.width = '100%';
    img.style.height = '100%';
    img.style.objectFit = 'cover';
    img.style.borderRadius = '50%';
    img.onerror = function() {{
      avatar.textContent = usuarioNome ? usuarioNome.charAt(0).toUpperCase() : 'U';
    }};
    avatar.innerHTML = '';
    avatar.appendChild(img);
  }} else if(usuarioNome){{
    avatar.textContent = usuarioNome.charAt(0).toUpperCase();
  }}
}})();

function sair(){{
  localStorage.clear();
  window.location.href = '{path_raiz}index.html';
}}
</script>
"""
    
    return html


def gerar_subnav(pagina_ativa='dash', dash_arq='vendas_dash.html', lista_arq='vendas_lista.html', filtros_html=''):
    """
    Gera submenu de navegação (Dashboard/Listagem/Filtros)
    
    Args:
        pagina_ativa: 'dash' ou 'lista'
        dash_arq: Nome do arquivo dashboard
        lista_arq: Nome do arquivo listagem
        filtros_html: HTML dos filtros (opcional)
    
    Returns:
        HTML do submenu completo
    """
    ad = "active" if pagina_ativa == "dash" else ""
    al = "active" if pagina_ativa == "lista" else ""
    
    return f"""
<div class="hdr-sub">
  <a href="{dash_arq}" class="subnav-btn {ad}">Dashboard</a>
  <a href="{lista_arq}" class="subnav-btn {al}">Listagem</a>
  {filtros_html}
</div>
"""


def h(senha):
    """Hash SHA-256 de uma senha."""
    return hashlib.sha256(senha.encode()).hexdigest()


# ── CSS BASE (tema claro, compartilhado em todas as páginas) ─
def css_base(cor):
    return """
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;}
body{background:#e2e8f0;color:#1e293b;font-family:'Plus Jakarta Sans',sans-serif;min-height:100vh;}
.hdr-main{background:#000;border-bottom:1px solid #1e293b;padding:0 28px;height:58px;
  display:flex;align-items:center;justify-content:space-between;
  position:sticky;top:0;z-index:200;box-shadow:0 2px 8px rgba(0,0,0,.3);}
.hdr-menu-btn{background:transparent;border:1.5px solid #334155;border-radius:8px;color:#94a3b8;
  padding:8px;cursor:pointer;text-decoration:none;transition:all .2s;display:flex;align-items:center;
  justify-content:center;width:38px;height:38px;}
.hdr-menu-btn:hover{border-color:#fff;color:#fff;background:rgba(255,255,255,.1);}
.hdr-menu-btn svg{display:block;}
.hdr-right{display:flex;align-items:center;gap:12px;}
.hdr-avatar{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#8b5cf6);
  display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:800;color:#fff;overflow:hidden;}
.hdr-avatar img{max-width:36px !important;max-height:36px !important;}
.btn-trocar-org{background:transparent;border:1.5px solid #334155;border-radius:8px;color:#94a3b8;
  padding:8px;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center;
  width:38px;height:38px;text-decoration:none;}
.btn-trocar-org:hover{border-color:#fff;color:#fff;background:rgba(255,255,255,.1);}
.btn-trocar-org svg{display:block;}
.btn-logoff{background:transparent;border:1.5px solid #334155;border-radius:7px;color:#94a3b8;
  font-family:'Plus Jakarta Sans',sans-serif;font-size:.75rem;font-weight:600;padding:8px 12px;cursor:pointer;
  transition:all .2s;display:flex;align-items:center;}
.btn-logoff:hover{border-color:#ef4444;color:#ef4444;background:rgba(239,68,68,.1);}
.btn-logoff svg{display:block;}
.hdr-sub{background:#fff;border-bottom:1px solid #e2e8f0;padding:0 28px;height:50px;
  display:flex;align-items:center;gap:12px;box-shadow:0 1px 3px rgba(0,0,0,.04);}
.subnav-btn{background:transparent;border:none;font-family:'Plus Jakarta Sans',sans-serif;font-size:.82rem;
  font-weight:600;color:#64748b;padding:6px 14px;border-radius:6px;cursor:pointer;text-decoration:none;transition:all .2s;}
.subnav-btn:hover{background:#f1f5f9;color:#1e293b;}
.subnav-btn.active{background:COR15;color:COR;}
.sub-div{width:1px;height:20px;background:#e2e8f0;}
.filtro-wrap{display:flex;align-items:center;gap:8px;margin-left:auto;flex-wrap:wrap;}
.filtro-label{font-size:.7rem;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.06em;}
.filtro-select{background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:7px;color:#334155;
  font-family:'Plus Jakarta Sans',sans-serif;font-size:.82rem;font-weight:500;padding:5px 10px;outline:none;cursor:pointer;transition:border-color .2s;}
.filtro-select:focus{border-color:COR;}
.filtro-nav-btn{background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:6px;color:#475569;
  font-size:.78rem;font-weight:700;padding:5px 9px;cursor:pointer;transition:all .2s;font-family:'Plus Jakarta Sans',sans-serif;}
.filtro-nav-btn:hover{border-color:COR;color:COR;background:#fff;}
main{padding:22px 28px 48px;}
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px;}
.kpi-card{background:#fff;border:1px solid #e8ecf4;border-radius:14px;padding:6px 8px;
  position:relative;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.05);transition:box-shadow .2s;}
.kpi-card:hover{box-shadow:0 4px 16px rgba(0,0,0,.09);}
.kpi-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--kc,COR);}
.kpi-titulo{font-size:.72rem;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.07em;margin-bottom:10px;}
.kpi-valor{font-size:1.9rem;font-weight:800;color:#0f172a;letter-spacing:-.04em;line-height:1;margin-bottom:6px;}
.kpi-var{font-size:.8rem;font-weight:700;}
.kpi-footer{display:flex;justify-content:space-between;margin-top:10px;padding-top:10px;
  border-top:1px solid #f1f5f9;font-size:.7rem;color:#94a3b8;font-weight:500;}
.prog-bar{height:4px;background:#f1f5f9;border-radius:3px;margin-top:10px;overflow:hidden;}
.prog-fill{height:100%;border-radius:3px;}
.kpi-ph{background:#fff;border:2px dashed #e2e8f0;border-radius:14px;padding:18px 20px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;min-height:120px;}
.kpi-ph .ph-t{font-size:.72rem;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.07em;margin-bottom:6px;}
.kpi-ph .ph-m{font-size:.7rem;color:#cbd5e1;line-height:1.6;}
.chart-row{display:grid;grid-template-columns:1.4fr 1fr;gap:14px;margin-bottom:16px;}
.chart-card{background:#fff;border:1px solid #e8ecf4;border-radius:14px;padding:4px;box-shadow:0 1px 3px rgba(0,0,0,.05);}
.chart-titulo{font-size:.9rem;font-weight:800;color:#0f172a;letter-spacing:-.02em;}
.chart-sub{font-size:.7rem;color:#94a3b8;font-weight:500;margin-top:3px;}
.chart-hdr{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;}
.chart-leg{display:flex;gap:12px;flex-wrap:wrap;}
.leg-i{display:flex;align-items:center;gap:5px;font-size:.68rem;color:#64748b;font-weight:500;}
.leg-d{width:10px;height:10px;border-radius:2px;}
.chart-wrap{position:relative;height:220px;}
.kpi2-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;}
.kpi2-card{background:#fff;border:1px solid #e8ecf4;border-radius:14px;padding:6px 8px;box-shadow:0 1px 3px rgba(0,0,0,.05);}
.kpi2-titulo{font-size:.7rem;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.07em;margin-bottom:12px;}
.kpi2-vals{display:flex;align-items:flex-end;gap:14px;margin-bottom:6px;}
.kpi2-v{font-size:1.7rem;font-weight:800;letter-spacing:-.04em;}
.kpi2-v.sec{font-size:1.3rem;color:#94a3b8;}
.kpi2-vr{font-size:1rem;font-weight:800;}
.kpi2-labs{display:flex;gap:14px;font-size:.65rem;color:#94a3b8;font-weight:500;}
.kpi2-ph{background:#fff;border:2px dashed #e2e8f0;border-radius:14px;padding:18px 20px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.kpi-card,.kpi2-card,.chart-card,.kpi-ph,.kpi2-ph{animation:fadeUp .4s ease both;}
@media(max-width:900px){
  .kpi-row,.kpi2-row{grid-template-columns:repeat(2,1fr);}
  .chart-row{grid-template-columns:1fr;}
  main{padding:16px;}
  .hdr-main,.hdr-sub{padding:0 16px;}
}
@media(max-width:768px){
  .hdr-main > div:first-child > span{display:none !important;}
  .btn-logoff{width:36px;height:36px;padding:8px;}
  .btn-logoff span{display:none;}
  .btn-logoff svg{width:20px;height:20px;}
}
""".replace("COR", cor)


def js_utils():
    """Funções JavaScript utilitárias reutilizáveis"""
    return """
// ========== FUNÇÕES UTILITÁRIAS ==========

// Formatação de números (K, M, B)
function formatNum(valor) {
  if (valor >= 1000000000) {
    var v = (valor/1000000000).toFixed(1);
    return (v.endsWith('.0') ? v.slice(0, -2) : v.replace('.', ',')) + 'B';
  }
  if (valor >= 1000000) {
    var v = (valor/1000000).toFixed(1);
    return (v.endsWith('.0') ? v.slice(0, -2) : v.replace('.', ',')) + 'M';
  }
  if (valor >= 1000) {
    var v = (valor/1000).toFixed(1);
    return (v.endsWith('.0') ? v.slice(0, -2) : v.replace('.', ',')) + 'K';
  }
  return valor.toFixed(0);
}

// Cor do indicador baseado em direção e percentual
function getCorIndicador(percentual, direcao) {
  // direcao: 'up' = melhor para cima, 'down' = melhor para baixo
  if (direcao === 'up') {
    if (percentual >= 100) return 'verde';
    if (percentual >= 95) return 'amarelo';
    return 'vermelho';
  } else {
    if (percentual <= 100) return 'verde';
    if (percentual <= 105) return 'amarelo';
    return 'vermelho';
  }
}
"""


# ── HEADER HTML COMPARTILHADO ────────────────────────────────
def html_header_simples(empresa, menu_arq="index.html"):
    """Cabeçalho simples sem subnav (para página de menu)."""
    logo_org = empresa.get("logo", "")
    return (
        '<header class="hdr-main">'
        '<div style="display:flex;align-items:center;gap:16px;">'
        '<a href="' + menu_arq + '" class="hdr-menu-btn" title="Menu" style="opacity:0.3;pointer-events:none;">'
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
        '<line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line>'
        '</svg></a>'
        '<img src="imagem/logos/sistema.png" alt="PGV5" style="height:34px" onerror="this.style.display=\'none\'">'
        '<span style="color:#fff;font-weight:700;font-size:1.1rem;letter-spacing:-.02em">Painel Gerencial</span>'
        '</div>'
        '<div class="hdr-right">'
        + ('<img src="' + logo_org + '" style="height:32px;margin-right:8px" onerror="this.style.display=\'none\'">' if logo_org else '') +
        '<div class="hdr-avatar" id="hdr-avatar">?</div>'
        '<a href="index.html" class="btn-trocar-org" title="Trocar Organização">'
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"></path><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"></path><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"></path><path d="M10 6h4"></path><path d="M10 10h4"></path><path d="M10 14h4"></path><path d="M10 18h4"></path>'
        '</svg></a>'
        '<button class="btn-logoff" id="btn-logout">'
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line>'
        '</svg><span style="margin-left:6px">Sair</span></button>'
        '</div>'
        '</header>'
        '<script>'
        '(function(){'
        'var usuarioId=localStorage.getItem("pgv5_usuario_id");'
        'var usuarioNome=localStorage.getItem("pgv5_usuario_nome");'
        'var usuarioFoto=localStorage.getItem("pgv5_usuario_foto");'
        'if(!usuarioId){window.location="index.html";return;}'
        'var avatar=document.getElementById("hdr-avatar");'
        'if(usuarioFoto){avatar.innerHTML=\'<img src="\'+usuarioFoto+\'" style="width:100%;height:100%;object-fit:cover;border-radius:50%">\';}else{avatar.textContent=usuarioNome?usuarioNome.charAt(0).toUpperCase():"U";}'
        'document.getElementById("btn-logout").addEventListener("click",function(){'
        'localStorage.clear();window.location="index.html";});'
        '})();'
        '</script>'
    )


def html_header(empresa, pagina_ativa, cor, menu_arq, dash_arq, lista_arq, filtros_html="", data_atualizacao=None, path_raiz='../../'):
    nome = empresa["nome"]
    logo_org = empresa.get("logo", "")
    ad   = "active" if pagina_ativa == "dash"  else ""
    al   = "active" if pagina_ativa == "lista" else ""
    data_texto = f'<div style="display:flex;align-items:center;gap:6px;margin-left:12px;" title="Atualizado em {data_atualizacao}"><i data-lucide="clock" style="width:14px;height:14px;color:#94a3b8"></i><span style="color:#64748b;font-size:.75rem;font-weight:500;">{data_atualizacao}</span></div>' if data_atualizacao else ''
    return (
        '<header class="hdr-main">'
        '<div style="display:flex;align-items:center;gap:16px;">'
        '<a href="' + menu_arq + '" class="hdr-menu-btn" title="Menu">'
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'
        '<line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line>'
        '</svg></a>'
        '<img src="' + path_raiz + 'imagem/logos/sistema.png" alt="PGV5" style="height:34px" onerror="this.style.display=\'none\'">'
        '<span style="color:#fff;font-weight:700;font-size:1.1rem;letter-spacing:-.02em">Painel Gerencial</span>'
        + data_texto +
        '</div>'
        '<div class="hdr-right">'
        + ('<img src="' + logo_org + '" style="height:32px;margin-right:8px" onerror="this.style.display=\'none\'">' if logo_org else '') +
        '<div class="hdr-avatar" id="hdr-avatar">?</div>'
        '<a href="' + path_raiz + 'index.html" class="btn-trocar-org" title="Trocar Organização">'
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"></path><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"></path><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"></path><path d="M10 6h4"></path><path d="M10 10h4"></path><path d="M10 14h4"></path><path d="M10 18h4"></path>'
        '</svg></a>'
        '<button class="btn-logoff" id="btn-logout">'
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line>'
        '</svg><span style="margin-left:6px">Sair</span></button>'
        '</div>'
        '</header>'
        '<div class="hdr-sub">'
        '<a href="' + dash_arq  + '" class="subnav-btn ' + ad + '">Dashboard</a>'
        '<a href="' + lista_arq + '" class="subnav-btn ' + al + '">Listagem</a>'
        + filtros_html +
        '</div>'
        '<script>'
        '(function(){'
        'var usuarioId=localStorage.getItem("pgv5_usuario_id");'
        'var usuarioNome=localStorage.getItem("pgv5_usuario_nome");'
        'var usuarioFoto=localStorage.getItem("pgv5_usuario_foto");'
        'if(!usuarioId){window.location="' + path_raiz + 'index.html";return;}'
        'var avatar=document.getElementById("hdr-avatar");'
        'if(usuarioFoto){avatar.innerHTML=\'<img src="' + path_raiz + '\'+usuarioFoto+\'" style="width:100%;height:100%;object-fit:cover;border-radius:50%">\';}else{avatar.textContent=usuarioNome?usuarioNome.charAt(0).toUpperCase():"U";}'
        'document.getElementById("btn-logout").addEventListener("click",function(){'
        'localStorage.clear();window.location="' + path_raiz + 'index.html";});'
        '})();'
        '</script>'
    )


# ── FILTROS PERÍODO + EMPRESA (bloco HTML reutilizável) ──────
def html_filtros(onchange="filtrar()"):
    return (
        '<div class="filtro-wrap">'
        '<span class="filtro-label">Filial</span>'
        '<select class="filtro-select" id="f-empresa" onchange="' + onchange + '"><option value="">Todas</option></select>'
        '<span class="filtro-label">De</span>'
        '<button class="filtro-nav-btn" onclick="navD(\'ini\',-1)">&#9664;</button>'
        '<input type="date" class="filtro-select" id="f-ini" onchange="' + onchange + '">'
        '<button class="filtro-nav-btn" onclick="navD(\'ini\',1)">&#9654;</button>'
        '<span class="filtro-label">At&eacute;</span>'
        '<button class="filtro-nav-btn" onclick="navD(\'fim\',-1)">&#9664;</button>'
        '<input type="date" class="filtro-select" id="f-fim" onchange="' + onchange + '">'
        '<button class="filtro-nav-btn" onclick="navD(\'fim\',1)">&#9654;</button>'
        '</div>'
    )


# ── GIT PUSH AUTOMÁTICO ───────────────────────────────────────
def git_push():
    """Commit + Push para GitHub (Windows)."""
    try:
        print("      • Adicionando arquivos...")
        result = subprocess.run(["git", "-C", REPO_PATH, "add", "."], 
                              capture_output=True, text=True, check=True)
        
        print("      • Verificando status...")
        status = subprocess.run(["git", "-C", REPO_PATH, "status", "--short"], 
                              capture_output=True, text=True, check=True)
        if status.stdout:
            print(f"        Arquivos modificados:\n{status.stdout}")
        
        print("      • Fazendo commit...")
        msg = f"PGV5 - {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        subprocess.run(["git", "-C", REPO_PATH, "commit", "-m", msg], check=True)
        
        print("      • Enviando para GitHub...")
        subprocess.run(["git", "-C", REPO_PATH, "push"], check=True)
        print("      ✔ Enviado!")
    except subprocess.CalledProcessError as e:
        print(f"      AVISO: Git não enviado ({e})")


# ── FUNÇÕES FORMATAÇÃO ────────────────────────────────────────
def fmtv(v):
    """Formata número grande (ex: 1234567 → 1.23M)."""
    if not v: return "—"
    v = float(v)
    if v >= 1e9: return f"{v/1e9:.2f}B"
    if v >= 1e6: return f"{v/1e6:.2f}M"
    if v >= 1e3: return f"{v/1e3:.2f}K"
    return f"{v:.2f}"

def fmtpct(v):
    """Formata percentual (ex: 0.1234 → 12.3%)."""
    if v is None: return "—"
    return f"{float(v):.1f}%"

def fmt_k(v):
    """Formata número (7.85K, 78.5K, 785K, 7.85M)."""
    if not v: return "0"
    v = float(v)
    if v >= 1e9: return f"{v/1e9:.2f}B"
    if v >= 1e6: return f"{v/1e6:.2f}M"
    if v >= 1e3: return f"{v/1e3:.2f}K"
    return f"{v:.0f}"

def fmt_num(v):
    """Formata número com separador (ex: 1234567 → 1.234.567)."""
    if not v: return "0"
    return f"{int(v):,}".replace(",", ".")

def cor_var(var):
    """Retorna cor baseada em variação (positivo=verde, negativo=vermelho)."""
    if var is None or var == 0: return "#94a3b8"
    return "#10b981" if var > 0 else "#ef4444"

def seta(var):
    """Retorna seta baseada em variação (↑ ↓ →)."""
    if var is None or var == 0: return "→"
    return "↑" if var > 0 else "↓"
