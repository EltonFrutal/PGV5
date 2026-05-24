# ============================================================
#  config.py — GERADO de Configuracao.xlsx
# ============================================================

REPO_PATH = r"G:\Meu Drive\Consys\PainelGerencial\PGV5"

# ── USUÁRIOS ─────────────────────────────────────────────────
USUARIOS = [
    {
        "email":    "elton@hotmail.com",
        "senha":    "123",
        "nome":     "Elton",
        "perfil":   "administrador",
        "empresas": ['Multicar', 'RS'],
        "foto":     "Imagem/fotos/elton@hotmail.com.jpg",
    },
    {
        "email":    "afonso@hotmail.com",
        "senha":    "123",
        "nome":     "Afonso",
        "perfil":   "consultor",
        "empresas": ['Multicar'],
        "foto":     "Imagem/fotos/afonso@hotmail.com.jpg",
    },
]

# ── EMPRESAS ─────────────────────────────────────────────────
EMPRESAS = [
    {
        "id":               "Multicar",
        "nome":             "Multicar",
        "arquivo":          "multicar.html",
        "cor":              "#10b981",
        "icone":            "🏪",
        "logo":             "Imagem/Logos/multicar.png",
        "base":             r"G:\Meu Drive\Consys\PainelGerencial\BaseDados\DadosConsys_Multicar.accdb",
        "vendas_arquivo":   "multicar_vendas_dash.html",
        "listagem_arquivo": "multicar_vendas_lista.html",
    },
    {
        "id":               "RS",
        "nome":             "RS",
        "arquivo":          "rs.html",
        "cor":              "#6366f1",
        "icone":            "🚗",
        "logo":             "Imagem/Logos/rs.png",
        "base":             r"G:\Meu Drive\Consys\PainelGerencial\BaseDados\DadosConsys_RSAutomotivo.accdb",
        "vendas_arquivo":   "rs_vendas_dash.html",
        "listagem_arquivo": "rs_vendas_lista.html",
    },
]

# ── MÓDULOS ──────────────────────────────────────────────────
MODULOS = [
    {"id":"vendas",      "label":"Vendas",      "desc":"Faturamento, pedidos e vendedores","cor":"#6366f1","pronto":True},
    {"id":"compras",     "label":"Compras",     "desc":"Entradas e fornecedores",          "cor":"#10b981","pronto":False},
    {"id":"a_receber",   "label":"A Receber",   "desc":"Títulos e inadimplência",          "cor":"#f59e0b","pronto":False},
    {"id":"a_pagar",     "label":"A Pagar",     "desc":"Obrigações e vencimentos",         "cor":"#ef4444","pronto":False},
    {"id":"historicos",  "label":"Históricos",  "desc":"Movimentos por período",           "cor":"#8b5cf6","pronto":False},
    {"id":"indicadores", "label":"Indicadores", "desc":"KPIs e metas",                     "cor":"#06b6d4","pronto":False},
    {"id":"resultados",  "label":"Resultados",  "desc":"DRE e resultado final",            "cor":"#f97316","pronto":False},
]

FONT_URL = "https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700;800&display=swap"
FONT_FAMILY = "'DM Sans', sans-serif"

FONT_URL_LISTA = "https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap"
FONT_FAMILY_LISTA = "'Nunito', sans-serif"
