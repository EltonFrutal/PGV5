# ============================================================
#  pg_modulos.py — Menu de Módulos (Com Cabeçalho Padrão)
# ============================================================

from utils import gerar_cabecalho

def gerar(empresa, permissoes):
    """Gera menu de módulos usando cabeçalho padrão"""
    
    nome_empresa = empresa.get('nome', 'Empresa')
    icone_empresa = empresa.get('icone', 'sistema')
    empresa_id = str(empresa.get('id', '0'))
    
    # Módulos disponíveis
    modulos = [
        {
            'id': 'vendas',
            'label': 'Vendas',
            'desc': 'Faturamento, pedidos e vendedores',
            'icon': 'trending-up',
            'cor': '#6366f1',
            'url': 'vendas_dash.html',
            'ativo': permissoes.get('exibevendas', 'não') == 'sim'
        },
        {
            'id': 'compras',
            'label': 'Compras',
            'desc': 'Entradas e fornecedores',
            'icon': 'shopping-cart',
            'cor': '#10b981',
            'url': 'compras_dash.html',
            'ativo': permissoes.get('exibecompras', 'não') == 'sim'
        },
        {
            'id': 'areceber',
            'label': 'A Receber',
            'desc': 'Títulos e inadimplência',
            'icon': 'arrow-down-to-line',
            'cor': '#f59e0b',
            'url': 'areceber_dash.html',
            'ativo': permissoes.get('exibeareceber', 'não') == 'sim'
        },
        {
            'id': 'apagar',
            'label': 'A Pagar',
            'desc': 'Obrigações e vencimentos',
            'icon': 'arrow-up-from-line',
            'cor': '#ef4444',
            'url': 'apagar_dash.html',
            'ativo': permissoes.get('exibeapagar', 'não') == 'sim'
        },
        {
            'id': 'historicos',
            'label': 'Históricos',
            'desc': 'Movimentos por período',
            'icon': 'history',
            'cor': '#8b5cf6',
            'url': 'historicos_dash.html',
            'ativo': permissoes.get('exibehistoricos', 'não') == 'sim'
        },
        {
            'id': 'indicadores',
            'label': 'Indicadores',
            'desc': 'KPIs e metas',
            'icon': 'gauge',
            'cor': '#06b6d4',
            'url': 'indicadores_dash.html',
            'ativo': permissoes.get('exibeindicadores', 'não') == 'sim'
        },
        {
            'id': 'resultados',
            'label': 'Resultados',
            'desc': 'DRE e resultado final',
            'icon': 'pie-chart',
            'cor': '#f97316',
            'url': 'resultados_dash.html',
            'ativo': permissoes.get('exiberesultados', 'não') == 'sim'
        }
    ]
    
    # Gerar cards de módulos
    modulos_html = ""
    for i, mod in enumerate(modulos):
        delay = i * 0.05
        
        modulos_html += f'''<a href="{mod['url']}" class="mod-card" style="animation-delay:{delay}s" data-modulo="{mod['id']}">
    <div class="mod-icon"><i data-lucide="{mod['icon']}" style="width:36px;height:36px"></i></div>
    <div class="mod-titulo">{mod['label']}</div>
  </a>
'''
    
    # Usar função de cabeçalho padrão
    cabecalho = gerar_cabecalho(
        icone_empresa=icone_empresa,  # Com ícone da empresa
        mostrar_trocar_org=True,      # Com botão trocar
        path_raiz='../../'            # Em html/empresa/, então usa ../../
    )
    
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>""" + nome_empresa + """ &mdash; PGV5</title>

<!-- Favicon e ícones -->
<link rel="icon" type="image/png" sizes="32x32" href="../imagem/logos/sistema.png">
<link rel="icon" type="image/png" sizes="16x16" href="../imagem/logos/sistema.png">
<link rel="apple-touch-icon" sizes="180x180" href="../imagem/logos/sistema.png">
<link rel="manifest" href="../manifest.json">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="PGV5">

<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0;}
html,body{height:100%;}
body{background:#e2e8f0;color:#1e293b;font-family:'Plus Jakarta Sans',sans-serif;min-height:100vh;display:block;}

/* Conteúdo */
main{padding:22px 28px 48px;max-width:1000px;margin:0 auto;}
.page-titulo{font-size:1.8rem;font-weight:900;color:#0f172a;letter-spacing:-.03em;margin-bottom:8px;}
.page-desc{font-size:.85rem;color:#64748b;font-weight:500;margin-bottom:32px;}

/* Grid de Módulos */
.mod-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:16px;}
.mod-card{background:#fff;border:1px solid #e8ecf4;border-radius:12px;padding:20px 16px;
  text-align:center;cursor:pointer;transition:all .3s;position:relative;overflow:hidden;
  box-shadow:0 1px 3px rgba(0,0,0,.05);text-decoration:none;display:block;}
.mod-card:hover{transform:translateY(-4px);box-shadow:0 12px 24px rgba(0,0,0,.12);border-color:#10b981;}
.mod-card.inativo{opacity:0.5;cursor:not-allowed;background:#f8fafc;}
.mod-card.inativo:hover{transform:none;box-shadow:0 1px 3px rgba(0,0,0,.05);}
.mod-icon{width:48px;height:48px;margin:0 auto 14px;border-radius:12px;
  display:flex;align-items:center;justify-content:center;background:#10b98115;}
.mod-icon i{color:#10b981;}
.mod-titulo{font-size:.95rem;font-weight:800;color:#0f172a;letter-spacing:-.02em;text-transform:uppercase;}
.mod-lock{position:absolute;top:10px;right:10px;width:28px;height:28px;
  background:rgba(239,68,68,0.1);border-radius:50%;display:flex;align-items:center;justify-content:center;
  color:#ef4444;}

/* Animações */
@keyframes fadeIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.mod-card{animation:fadeIn .5s ease both;}

/* Responsivo */
@media(max-width:900px){
  .mod-grid{grid-template-columns:repeat(2,1fr);gap:14px;}
  main{padding:16px;}
}
</style>
</head>
<body>

""" + cabecalho + """

<main>
  <h1 class="page-titulo">""" + nome_empresa + """</h1>
  <p class="page-desc">Selecione um módulo para começar</p>
  <div class="mod-grid" id="mod-grid">
""" + modulos_html + """
  </div>
</main>

<script>
// Carregar permissões dinamicamente
(async function(){
  var usuarioId = localStorage.getItem('pgv5_usuario_id');
  var empresaId = '""" + empresa_id + """';
  
  if(!usuarioId){
    window.location.href = '../index.html';
    return;
  }
  
  // Carregar permissões do JSON
  try {
    const response = await fetch('/permissoes.json');
    const permissoes = await response.json();
    const chave = usuarioId + '_' + empresaId;
    const userPerms = permissoes[chave];
    
    console.log('🔐 Permissões carregadas:');
    console.log('   Usuário ID:', usuarioId);
    console.log('   Empresa ID:', empresaId);
    console.log('   Chave:', chave);
    console.log('   Permissões:', userPerms);
    
    if(userPerms){
      // Aplicar permissões aos cards
      const modulos = [
        {id: 'vendas', perm: userPerms.exibevendas},
        {id: 'compras', perm: userPerms.exibecompras},
        {id: 'areceber', perm: userPerms.exibeareceber},
        {id: 'apagar', perm: userPerms.exibeapagar},
        {id: 'historicos', perm: userPerms.exibehistoricos},
        {id: 'indicadores', perm: userPerms.exibeindicadores},
        {id: 'resultados', perm: userPerms.exiberesultados}
      ];
      
      console.log('📋 Aplicando permissões aos módulos:');
      modulos.forEach(mod => {
        console.log(`   ${mod.id}: ${mod.perm}`);
        const cards = document.querySelectorAll('a[href*="' + mod.id + '"]');
        cards.forEach(card => {
          if(mod.perm === 'não'){
            console.log(`   🔒 Bloqueando módulo: ${mod.id}`);
            card.classList.add('inativo');
            card.onclick = function(e){ e.preventDefault(); return false; };
            
            // Adicionar cadeado
            if(!card.querySelector('.mod-lock')){
              const lock = document.createElement('div');
              lock.className = 'mod-lock';
              lock.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>`;
              card.appendChild(lock);
            }
          }
        });
      });
    } else {
      console.warn('⚠️  Permissões não encontradas para:', chave);
    }
  } catch(err){
    console.error('❌ Erro ao carregar permissões:', err);
  }
})();

lucide.createIcons();
</script>

</body>
</html>
"""
