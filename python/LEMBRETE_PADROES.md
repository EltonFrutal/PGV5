# 📋 LEMBRETE: PADRÕES DO PROJETO

## ⚠️ SEMPRE USAR EM NOVAS PÁGINAS:

### **1. TÍTULO DA ABA:**
```python
from utils import TITULO_PADRAO

<title>{TITULO_PADRAO}</title>
```
**Resultado:** `Painel Gerencial` (em TODAS as abas)

---

### **2. FAVICON:**
```python
from utils import gerar_meta_icons

{gerar_meta_icons(path_raiz='../../')}
```
**Resultado:** Logo `sistema.png` em todas páginas

---

### **3. CABEÇALHO:**
```python
from utils import gerar_cabecalho

{gerar_cabecalho(
    icone_empresa='multicar',
    mostrar_trocar_org=True,
    path_raiz='../../'
)}
```

---

### **4. SUBMENU:**
```python
from utils import gerar_subnav

{gerar_subnav(
    pagina_ativa='dash',
    dash_arq='vendas_dash.html',
    lista_arq='vendas_lista.html'
)}
```

---

## 📝 TEMPLATE COMPLETO:

```python
from utils import (
    css_base, 
    gerar_meta_icons, 
    gerar_cabecalho, 
    gerar_subnav, 
    TITULO_PADRAO  # ← NÃO ESQUECER!
)

def gerar_nova_pagina(emp, dados):
    cor = emp.get('cor', '#0ea5e9')
    icone = emp.get('icone', 'multicar')
    
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{TITULO_PADRAO}</title>
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
    pagina_ativa='dash',
    dash_arq='dash.html',
    lista_arq='lista.html'
)}
<main>
  <!-- Seu conteúdo aqui -->
</main>
</body>
</html>"""
```

---

## ✅ CHECKLIST NOVA PÁGINA:

- [ ] Importar `TITULO_PADRAO` do utils
- [ ] Usar `<title>{TITULO_PADRAO}</title>`
- [ ] Usar `gerar_meta_icons(path_raiz='../../')`
- [ ] Usar `gerar_cabecalho()` com icone da empresa
- [ ] Usar `gerar_subnav()` se tiver submenu
- [ ] Verificar caminhos relativos (`../../`)

---

**SEMPRE CONSULTE ESTE ARQUIVO AO CRIAR NOVAS PÁGINAS!** 📖
