# ============================================================
#  paginas/pg_menu.py — Menu de Módulos por Empresa
# ============================================================

import json
from datetime import datetime
from config import MODULOS, FONT_URL, FONT_FAMILY
from utils  import css_base, html_header_simples


def gerar(empresa):
    mjs    = json.dumps(MODULOS, ensure_ascii=False)
    cor    = empresa["cor"]
    nome   = empresa["nome"]
    dsh    = empresa.get("vendas_arquivo","#")
    gerado = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>""" + nome + """ &mdash; PGV5</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest"></script>
<style>
""" + css_base(cor) + """
body{display:block;}
.mod-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:20px;margin-top:32px;}
.mod-card{background:#fff;border:1px solid #e8ecf4;border-radius:16px;padding:32px 24px;
  text-align:center;cursor:pointer;transition:all .3s;position:relative;overflow:hidden;
  box-shadow:0 1px 3px rgba(0,0,0,.05);text-decoration:none;display:block;}
.mod-card:hover{transform:translateY(-4px);box-shadow:0 12px 24px rgba(0,0,0,.12);border-color:""" + cor + """;}
.mod-card.inativo{opacity:0.4;cursor:not-allowed;}
.mod-card.inativo:hover{transform:none;box-shadow:0 1px 3px rgba(0,0,0,.05);}
.mod-icon{width:64px;height:64px;margin:0 auto 20px;border-radius:16px;
  display:flex;align-items:center;justify-content:center;background:""" + cor + """15;}
.mod-icon i{color:""" + cor + """;}
.mod-titulo{font-size:1.1rem;font-weight:800;color:#0f172a;letter-spacing:-.02em;text-transform:uppercase;}
.mod-badge{position:absolute;top:12px;right:12px;background:#f1f5f9;color:#94a3b8;
  font-size:.65rem;font-weight:700;padding:4px 10px;border-radius:20px;text-transform:uppercase;letter-spacing:.06em;}
@keyframes fadeIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.mod-card{animation:fadeIn .5s ease both;}
.mod-card:nth-child(1){animation-delay:0s;}
.mod-card:nth-child(2){animation-delay:.05s;}
.mod-card:nth-child(3){animation-delay:.1s;}
.mod-card:nth-child(4){animation-delay:.15s;}
.mod-card:nth-child(5){animation-delay:.2s;}
.mod-card:nth-child(6){animation-delay:.25s;}
.mod-card:nth-child(7){animation-delay:.3s;}
@media(max-width:900px){
  .mod-grid{grid-template-columns:repeat(2,1fr);gap:14px;}
}
</style>
</head>
<body>
""" + html_header_simples(empresa) + """
<main style="max-width:1000px;margin:0 auto;">
<h1 style="font-size:1.8rem;font-weight:900;color:#0f172a;letter-spacing:-.03em;margin-bottom:8px;">""" + nome + """</h1>
<p style="font-size:.85rem;color:#64748b;font-weight:500;">Selecione um módulo para começar</p>
<div class="mod-grid" id="mod-grid"></div>
</main>
<script>
var MODULOS = """ + mjs + """;
var dashUrl = '""" + dsh + """';

// Mapeamento de ícones Lucide por módulo
var iconMap = {
  'Vendas': 'trending-up',
  'Compras': 'shopping-cart',
  'A Receber': 'arrow-down-to-line',
  'A Pagar': 'arrow-up-from-line',
  'Históricos': 'history',
  'Indicadores': 'gauge',
  'Resultados': 'pie-chart'
};

document.getElementById('mod-grid').innerHTML = MODULOS.map(function(m){
  var ativo = m.label === 'Vendas';
  var url = ativo ? dashUrl : '#';
  var icon = iconMap[m.label] || 'box';
  
  return '<a href="'+url+'" class="mod-card'+(ativo?'':' inativo')+'" '+(ativo?'':'onclick="return false;"')+'>'+
    (ativo?'':'<span class="mod-badge">Em breve</span>')+
    '<div class="mod-icon"><i data-lucide="'+icon+'" style="width:48px;height:48px"></i></div>'+
    '<div class="mod-titulo">'+m.label+'</div>'+
    '</a>';
}).join('');

lucide.createIcons();
</script>
</body></html>"""
