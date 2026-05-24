# ============================================================
#  pg_vendas_dash.py — Dashboard de Vendas (COM CARD 1)
# ============================================================

from datetime import datetime
from utils import css_base, gerar_cabecalho, gerar_subnav, gerar_meta_icons

def gerar(emp, dados):
    """Dashboard com Card 1 completo"""
    
    cor = emp.get("cor", "#0ea5e9")
    nome = emp.get("nome", "Organização")
    
    # Arquivos
    menu_arq = emp.get('menu_arquivo', 'index.html')
    dash_arq = emp.get('vendas_arquivo', 'vendas_dash.html')
    lista_arq = emp.get('listagem_arquivo', 'vendas_lista.html')
    
    # Data de atualização
    data_atualizacao = dados.get('data_atualizacao', datetime.now().strftime('%d/%m/%Y %H:%M'))
    
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>""" + nome + """ &mdash; Vendas Dashboard</title>
""" + gerar_meta_icons(path_raiz='../../') + """
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0"></script>
<style>
""" + css_base(cor) + """
body{display:block;}

/* Cards KPI */
.kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:12px;}
.kpi-card-visual{background:#fff;border:1px solid #e8ecf4;border-radius:14px;padding:16px;
  box-shadow:0 1px 3px rgba(0,0,0,.05);min-height:120px;}

/* Grid de Gráficos */
.charts-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:12px;}
.chart-card-visual{background:#fff;border:1px solid #e8ecf4;border-radius:14px;padding:12px;
  box-shadow:0 1px 3px rgba(0,0,0,.05);min-height:280px;}

/* Cards Menores */
.small-cards-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}
.small-card-visual{background:#fff;border:1px solid #e8ecf4;border-radius:14px;padding:16px;
  box-shadow:0 1px 3px rgba(0,0,0,.05);min-height:60px;}

/* Estilos KPI */
.kpi-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;}
.kpi-nome{font-size:0.75rem;color:#64748b;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;}
.kpi-variacao{display:flex;align-items:center;gap:4px;font-size:0.85rem;font-weight:700;}
.kpi-realizado{font-size:1.8rem;font-weight:800;line-height:1;margin-bottom:12px;}
.kpi-meta-info{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;font-size:0.7rem;}
.kpi-meta-label{color:#64748b;font-weight:600;}
.kpi-atingido{font-weight:700;}
.kpi-barra{height:8px;background:#e2e8f0;border-radius:4px;overflow:hidden;}
.kpi-barra-fill{height:100%;border-radius:4px;transition:width 0.3s ease;}

/* Títulos */
.chart-titulo{font-size:1rem;font-weight:700;color:#0f172a;margin-bottom:16px;}

/* Cores Indicadores */
.cor-verde{color:#16a34a;}
.cor-amarelo{color:#f59e0b;}
.cor-vermelho{color:#dc2626;}
.bg-verde{background:#16a34a;}
.bg-amarelo{background:#f59e0b;}
.bg-vermelho{background:#dc2626;}

.small-variacao{display:inline-flex;align-items:center;gap:3px;}
.small-realizado{}

/* Responsive */
@media(max-width:1200px){
  .kpi-grid{grid-template-columns:repeat(2,1fr);}
  .charts-grid{grid-template-columns:1fr;}
  .small-cards-grid{grid-template-columns:repeat(2,1fr);}
}

@media(max-width:768px){
  .kpi-grid{grid-template-columns:1fr;}
  .small-cards-grid{grid-template-columns:1fr;}
  
  /* Esconder título "Painel Gerencial" no mobile */
  .hdr-main > div:first-child > span{display:none !important;}
  
  /* Botão sair: só ícone no mobile */
  .btn-logoff{width:36px;height:36px;padding:8px;}
  .btn-logoff span{display:none;}
  .btn-logoff svg{width:20px;height:20px;}
}
</style>
</head>
<body>
""" + gerar_cabecalho(
    icone_empresa=emp.get('icone'),
    mostrar_trocar_org=True,
    path_raiz='../../'
) + gerar_subnav(
    pagina_ativa='dash',
    dash_arq=dash_arq,
    lista_arq=lista_arq,
    filtros_html=''
) + """
<main style="max-width:1400px;margin:0 auto;padding:16px;background:#e2e8f0;min-height:100vh;">

<!-- 4 CARDS SUPERIORES (KPIs) -->
<div class="kpi-grid">
  
  <!-- CARD 1 - VENDAS -->
  <div class="kpi-card-visual" id="card1">
    <div class="kpi-header">
      <div>
        <div class="kpi-nome">Vendas maio-26</div>
        <div style="display:flex;align-items:center;gap:3px;margin-top:2px;">
          <i data-lucide="arrow-up-right" style="width:10px;height:10px;color:#94a3b8;"></i>
          <span style="font-size:0.65rem;color:#94a3b8;font-weight:600;">melhor</span>
        </div>
      </div>
      <div class="kpi-variacao" id="var1">
        <i data-lucide="arrow-up" style="width:16px;height:16px;"></i>
        <span>+10%</span>
      </div>
    </div>
    <div class="kpi-realizado" id="real1">110K</div>
    <div class="kpi-meta-info">
      <span class="kpi-meta-label">Meta: <strong>100K</strong></span>
      <span class="kpi-atingido" id="ating1">110%</span>
    </div>
    <div class="kpi-barra">
      <div class="kpi-barra-fill" id="barra1" style="width:100%"></div>
    </div>
  </div>

  <!-- CARD 2 - INADIMPLÊNCIA (AMARELO) -->
  <div class="kpi-card-visual" id="card2">
    <div class="kpi-header">
      <div>
        <div class="kpi-nome">Inadimplência maio-26</div>
        <div style="display:flex;align-items:center;gap:3px;margin-top:2px;">
          <i data-lucide="arrow-down-right" style="width:10px;height:10px;color:#94a3b8;"></i>
          <span style="font-size:0.65rem;color:#94a3b8;font-weight:600;">melhor</span>
        </div>
      </div>
      <div class="kpi-variacao" id="var2">
        <i data-lucide="arrow-up" style="width:16px;height:16px;"></i>
        <span>+3,3%</span>
      </div>
    </div>
    <div class="kpi-realizado" id="real2">3,1%</div>
    <div class="kpi-meta-info">
      <span class="kpi-meta-label">Meta: <strong>3%</strong></span>
      <span class="kpi-atingido" id="ating2">103%</span>
    </div>
    <div class="kpi-barra">
      <div class="kpi-barra-fill" id="barra2" style="width:103%"></div>
    </div>
  </div>

  <!-- CARD 3 - MARGEM (VERMELHO) -->
  <div class="kpi-card-visual" id="card3">
    <div class="kpi-header">
      <div>
        <div class="kpi-nome">Margem maio-26</div>
        <div style="display:flex;align-items:center;gap:3px;margin-top:2px;">
          <i data-lucide="arrow-up-right" style="width:10px;height:10px;color:#94a3b8;"></i>
          <span style="font-size:0.65rem;color:#94a3b8;font-weight:600;">melhor</span>
        </div>
      </div>
      <div class="kpi-variacao" id="var3">
        <i data-lucide="arrow-down" style="width:16px;height:16px;"></i>
        <span>-10%</span>
      </div>
    </div>
    <div class="kpi-realizado" id="real3">18%</div>
    <div class="kpi-meta-info">
      <span class="kpi-meta-label">Meta: <strong>20%</strong></span>
      <span class="kpi-atingido" id="ating3">90%</span>
    </div>
    <div class="kpi-barra">
      <div class="kpi-barra-fill" id="barra3" style="width:90%"></div>
    </div>
  </div>

  <!-- CARD 4 -->
  <div class="kpi-card-visual">
    <div class="kpi-header">
      <div class="kpi-nome">Card KPI 4</div>
    </div>
    <div style="font-size:1.8rem;font-weight:800;">--</div>
  </div>

</div>

<!-- 2 GRÁFICOS (Grid) -->
<div class="charts-grid">
  <div class="chart-card-visual">
    <div class="chart-titulo">Vendas Mensais 2025 vs 2026</div>
    <div style="height:240px;">
      <canvas id="chartVendas"></canvas>
    </div>
  </div>
  <div class="chart-card-visual">
    <div class="chart-titulo">Gráfico 2</div>
    <div style="height:240px;display:flex;align-items:center;justify-content:center;color:#94a3b8;">
      Área do gráfico
    </div>
  </div>
</div>

<!-- 4 CARDS MENORES -->
<div class="small-cards-grid">
  <div class="small-card-visual" id="small1">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;">
      <div style="display:flex;align-items:center;gap:6px;">
        <i data-lucide="package" style="width:16px;height:16px;color:#64748b;"></i>
        <span style="font-size:0.7rem;color:#64748b;font-weight:700;text-transform:uppercase;">Pedidos</span>
      </div>
      <span class="small-variacao" id="smallvar1" style="font-size:0.75rem;font-weight:700;">+6,3%</span>
    </div>
    <div style="display:flex;align-items:flex-end;gap:16px;">
      <div style="display:flex;flex-direction:column;">
        <span class="small-realizado" id="smallreal1" style="font-size:1.3rem;font-weight:800;line-height:1;">3,4K</span>
        <span style="font-size:0.65rem;color:#94a3b8;font-weight:600;margin-top:3px;">2026</span>
      </div>
      <div style="display:flex;flex-direction:column;">
        <span style="font-size:1.1rem;color:#94a3b8;font-weight:700;line-height:1;">3,2K</span>
        <span style="font-size:0.65rem;color:#94a3b8;font-weight:600;margin-top:3px;">2025</span>
      </div>
    </div>
  </div>
  <div class="small-card-visual">
    <div style="font-size:0.7rem;color:#64748b;font-weight:600;">Card Menor 2</div>
  </div>
  <div class="small-card-visual">
    <div style="font-size:0.7rem;color:#64748b;font-weight:600;">Card Menor 3</div>
  </div>
  <div class="small-card-visual">
    <div style="font-size:0.7rem;color:#64748b;font-weight:600;">Card Menor 4</div>
  </div>
</div>

</main>

<script>
// Função para calcular cor baseada em direção e percentual
function getCorIndicador(percentual, direcao) {
  // direcao: 'up' = melhor para cima, 'down' = melhor para baixo
  
  if (direcao === 'up') {
    // Melhor para cima: quanto maior melhor
    if (percentual >= 100) return 'verde';
    if (percentual >= 95) return 'amarelo';
    return 'vermelho';
  } else {
    // Melhor para baixo: quanto menor melhor
    if (percentual <= 100) return 'verde';
    if (percentual <= 105) return 'amarelo';
    return 'vermelho';
  }
}

// Aplicar cores no Card 1 (VERDE - melhor para cima, 110%)
(function(){
  var percentual = 110;
  var direcao = 'up';
  var cor = getCorIndicador(percentual, direcao);
  document.getElementById('var1').className = 'kpi-variacao cor-' + cor;
  document.getElementById('real1').className = 'kpi-realizado cor-' + cor;
  document.getElementById('ating1').className = 'kpi-atingido cor-' + cor;
  document.getElementById('barra1').className = 'kpi-barra-fill bg-' + cor;
})();

// Aplicar cores no Card 2 (AMARELO - melhor para baixo, 103%)
(function(){
  var percentual = 103; // 3.1/3 * 100 = 103.3%
  var direcao = 'down'; // inadimplência: quanto menor melhor
  var cor = getCorIndicador(percentual, direcao);
  document.getElementById('var2').className = 'kpi-variacao cor-' + cor;
  document.getElementById('real2').className = 'kpi-realizado cor-' + cor;
  document.getElementById('ating2').className = 'kpi-atingido cor-' + cor;
  document.getElementById('barra2').className = 'kpi-barra-fill bg-' + cor;
})();

// Aplicar cores no Card 3 (VERMELHO - melhor para cima, 90%)
(function(){
  var percentual = 90; // 18/20 * 100 = 90%
  var direcao = 'up'; // margem: quanto maior melhor
  var cor = getCorIndicador(percentual, direcao);
  document.getElementById('var3').className = 'kpi-variacao cor-' + cor;
  document.getElementById('real3').className = 'kpi-realizado cor-' + cor;
  document.getElementById('ating3').className = 'kpi-atingido cor-' + cor;
  document.getElementById('barra3').className = 'kpi-barra-fill bg-' + cor;
})();

// Card Menor 1 - Pedidos (VERDE)
(function(){
  var realizado = 3400;
  var comparativo = 3200;
  var percentual = (realizado / comparativo) * 100; // 106.25%
  var direcao = 'up'; // melhor para cima
  var cor = getCorIndicador(percentual, direcao);
  
  document.getElementById('smallvar1').className = 'small-variacao cor-' + cor;
  document.getElementById('smallreal1').className = 'small-realizado cor-' + cor;
})();

// Gráfico de Vendas Mensais
(function(){
  var ctx = document.getElementById('chartVendas');
  if (!ctx) return;
  
  // Dados simulados
  var meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
  var vendas2025 = [85, 92, 88, 95, 90, 98, 93, 97, 91, 99, 94, 102];
  var vendas2026 = [92, 98, 95, 102, 97, 105, 100, 104, 98, 106, 101, 110];
  var metas = [90, 90, 90, 95, 95, 100, 100, 100, 95, 100, 100, 105];
  
  // Detectar mobile e rotação
  var isMobile = window.innerWidth <= 768;
  var numDatasets = 2; // 2025 + 2026 (barras)
  var numPontos = meses.length;
  var temMeta = true;
  var rotulosInferiores = numDatasets === 2 && temMeta && numPontos >= 12; // true
  
  // Plugin de rótulos (só desktop, na parte inferior)
  var labelPlugin = {
    id: 'chartLabels',
    afterDatasetsDraw: function(chart) {
      if (isMobile) return;
      
      var ctx = chart.ctx;
      chart.data.datasets.forEach(function(dataset, i) {
        if (dataset.type === 'line') return;
        
        var meta = chart.getDatasetMeta(i);
        if (!meta.hidden) {
          meta.data.forEach(function(bar, index) {
            var valor = dataset.data[index];
            if (valor == null) return;
            
            ctx.save();
            ctx.font = '700 10px "Plus Jakarta Sans", sans-serif';
            
            // Rótulos na parte INFERIOR (branco para contraste)
            ctx.textAlign = 'center';
            ctx.textBaseline = 'top';
            ctx.fillStyle = '#fff';
            ctx.fillText(valor, bar.x, bar.y + 8);
            
            ctx.restore();
          });
        }
      });
    }
  };
  
  new Chart(ctx, {
    type: 'bar',
    plugins: [isMobile ? null : labelPlugin].filter(Boolean),
    data: {
      labels: meses,
      datasets: [
        {
          label: '2025',
          data: vendas2025,
          backgroundColor: '#ff6600',
          borderColor: '#ff6600',
          borderWidth: 0,
          borderRadius: 3
        },
        {
          label: '2026',
          data: vendas2026,
          backgroundColor: '#00a8ff',
          borderColor: '#00a8ff',
          borderWidth: 0,
          borderRadius: 3
        },
        {
          label: 'Meta',
          data: metas,
          type: 'line',
          borderColor: '#ffd700',
          backgroundColor: 'transparent',
          borderWidth: 3,
          pointRadius: 5,
          pointHoverRadius: 7,
          pointBackgroundColor: '#ffd700',
          pointBorderColor: '#fff',
          pointBorderWidth: 2,
          tension: 0.4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          position: 'bottom',
          labels: {
            color: '#64748b',
            font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' },
            padding: 12,
            usePointStyle: true,
            pointStyle: 'circle',
            boxWidth: 6,
            boxHeight: 6
          }
        },
        tooltip: {
          backgroundColor: '#1e293b',
          titleColor: '#fff',
          bodyColor: '#fff',
          padding: 12,
          cornerRadius: 8
        }
      },
      scales: {
        x: {
          display: false,
          grid: { display: false },
          border: { display: false }
        },
        y: {
          display: false,
          grid: { display: false },
          border: { display: false }
        }
      }
    }
  });
})();

lucide.createIcons();
</script>
</body></html>"""


def gerar_listagem(emp, dados):
    """Chama arquivo separado"""
    from paginas.pg_vendas_lista import gerar as gerar_lista
    return gerar_lista(emp, dados)
