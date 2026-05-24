# 📊 PGV5 - Painel Gerencial V5

Sistema web de gestão empresarial multi-empresa com autenticação e permissões dinâmicas.

---

## 🎯 Funcionalidades

✅ **Autenticação Multi-Usuário**
- Login com email e senha
- Fotos de usuários
- Logout seguro

✅ **Multi-Empresa**
- Seleção de empresas por usuário
- Logos personalizados
- Configuração via Excel

✅ **Permissões Dinâmicas**
- Controle granular por módulo
- Cadeados visuais em módulos bloqueados
- Carregamento via JSON

✅ **Dashboards Modernos**
- Design premium com animações
- Gráficos interativos (Chart.js)
- Responsivo para mobile

✅ **Módulos Disponíveis**
- 📈 Vendas (Dashboard + Listagem)
- 🛒 Compras
- 💰 A Receber
- 💸 A Pagar
- 📋 Históricos
- 📊 Indicadores
- 📈 Resultados

---

## 🏗️ Estrutura do Projeto

```
PGV5/
├── imagem/
│   ├── logos/              # Logos do sistema e empresas
│   └── fotos/              # Fotos dos usuários
├── empresa/                # HTMLs gerados por empresa
│   ├── multicar/
│   │   ├── menu.html
│   │   ├── vendas_dash.html
│   │   └── vendas_lista.html
│   └── cocacafe/
│       └── ...
├── python/
│   ├── paginas/            # Geradores de páginas
│   │   ├── pg_login.py
│   │   ├── pg_empresas.py
│   │   ├── pg_modulos.py
│   │   ├── pg_vendas_dash.py
│   │   └── pg_vendas_lista.py
│   ├── configuracao.xlsx   # Configuração do sistema
│   ├── schema.py           # Classes e funções principais
│   ├── gerar_pgv5.py       # Gerador principal
│   ├── servidor_rapido.py  # Servidor HTTP local
│   ├── utils.py            # Funções reutilizáveis
│   └── config.py           # Configurações do projeto
├── index.html              # Página de login
├── empresas.html           # Seleção de empresas
├── permissoes.json         # Permissões por usuário/empresa
└── manifest.json           # PWA manifest
```

---

## 🚀 Como Usar

### **1. Configurar dados**

Edite `python/configuracao.xlsx`:

- **Aba `usuario`**: Cadastro de usuários (id, nome, email, senha, perfil, foto)
- **Aba `empresa`**: Cadastro de empresas (id, empresa, Ativo, pasta, icone)
- **Aba `usuarioempresa`**: Vínculos e permissões (exibevendas, exibecompras, etc.)

### **2. Gerar arquivos HTML**

```bash
cd C:\PGV5\python
python gerar_pgv5.py
```

### **3. Iniciar servidor**

```bash
python servidor_rapido.py
```

### **4. Acessar sistema**

Abra o navegador:
```
http://localhost:8000/index.html
```

**Logins de teste:**
- `elton@hotmail.com` / `123` - Acesso completo
- `afonso@hotmail.com` / `123` - Acesso parcial (Compras bloqueado)

---

## 🔧 Tecnologias

**Backend (Geração):**
- Python 3.x
- openpyxl (leitura Excel)
- hashlib (criptografia senhas)

**Frontend:**
- HTML5 + CSS3
- JavaScript Vanilla
- Chart.js (gráficos)
- Lucide Icons
- localStorage (sessões)

**Servidor:**
- http.server (Python)
- Threading (requisições paralelas)
- Cache inteligente

---

## 🎨 Design System

**Paleta de Cores:**
- 🟠 Laranja: `#ff6600` (principal)
- 🔵 Azul: `#00a8ff` (secundária)
- 🟡 Amarelo: `#ffd700` (destaque)
- ⚫ Preto: `#000000` (header)

**Fonte:**
- Plus Jakarta Sans (Google Fonts)

**Estilo:**
- Glassmorphism
- Animações suaves
- Cards com sombras
- Gradientes sutis

---

## 📚 Arquivos de Referência

### **Funções Reutilizáveis (utils.py)**

```python
from utils import gerar_cabecalho, gerar_subnav, gerar_meta_icons

# Cabeçalho padrão
gerar_cabecalho(
    icone_empresa='multicar',
    mostrar_trocar_org=True,
    path_raiz='../../'
)

# Submenu Dashboard/Listagem
gerar_subnav(
    pagina_ativa='dash',
    dash_arq='vendas_dash.html',
    lista_arq='vendas_lista.html'
)
```

Consulte `EXEMPLO_CABECALHO_PADRAO.py` para mais detalhes.

---

## 🔐 Segurança

⚠️ **IMPORTANTE:** 

- Senhas são hashadas com SHA-256
- **NÃO use em produção sem HTTPS!**
- Dados salvos em localStorage (navegador)
- Sistema para uso **LOCAL/INTERNO**

---

## 📝 TODO / Roadmap

- [ ] Implementar módulos Compras, A Receber, A Pagar
- [ ] Dashboard com dados reais (integração banco)
- [ ] Filtros por data e empresa
- [ ] Exportação Excel/PDF
- [ ] Modo escuro
- [ ] PWA offline
- [ ] Deploy em servidor

---

## 👨‍💻 Autor

**Elton Frutal**
- GitHub: [@EltonFrutal](https://github.com/EltonFrutal)

---

## 📄 Licença

Este projeto é proprietário e de uso interno.

---

## 🆘 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação em `EXEMPLO_CABECALHO_PADRAO.py`
2. Execute `python gerar_pgv5.py` para regenerar arquivos
3. Limpe cache com `python limpar_cache.py`

---

**Desenvolvido com ❤️ para gestão empresarial eficiente!**
