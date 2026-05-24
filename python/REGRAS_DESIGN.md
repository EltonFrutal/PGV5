# REGRAS DE DESIGN PGV5
## Aplicar SEMPRE em todos os componentes

---

## 1. TIPOGRAFIA

### Fonte Padrão
**Plus Jakarta Sans**
- Import: `https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap`
- CSS: `font-family: 'Plus Jakarta Sans', sans-serif;`
- Pesos: 300, 400, 500, 600, 700, 800

**Nunca usar outras fontes!**

---

## 2. GRÁFICOS (Chart.js)

### Configuração Padrão de Escalas
```javascript
scales: {
  x: {
    display: false,  // SEMPRE false - esconder eixo X
    grid: { display: false },
    border: { display: false }
  },
  y: {
    display: false,  // SEMPRE false - esconder eixo Y
    grid: { display: false },
    border: { display: false }
  }
}
```

### Rótulos (Labels)
- **Desktop (>768px)**: Mostrar rótulos nos gráficos
- **Mobile (≤768px)**: NÃO mostrar rótulos nos gráficos

**Regras de Posicionamento:**
1. **2 séries + meta mensal** (≥12 pontos): Rótulos na **PARTE INFERIOR** das barras
2. **Até 2 datasets**: Rótulos ACIMA das barras
3. **3+ datasets + Mensal** (≥12 pontos): Rótulos a **90 graus**

**Implementação:**
```javascript
// Detectar mobile
var isMobile = window.innerWidth <= 768;

// Detectar características do gráfico
var numDatasets = chart.data.datasets.filter(d => d.type !== 'line').length;
var numPontos = chart.data.labels.length;
var temMeta = chart.data.datasets.some(d => d.type === 'line');

// Definir posicionamento
var rotulos90graus = numDatasets >= 3 && numPontos >= 12;
var rotulosInferiores = numDatasets === 2 && temMeta && numPontos >= 12;

// Plugin de rótulos (só desktop)
var labelPlugin = {
  id: 'chartLabels',
  afterDatasetsDraw: function(chart) {
    if (isMobile) return;  // Sem rótulos no mobile
    
    var ctx = chart.ctx;
    chart.data.datasets.forEach(function(dataset, i) {
      if (dataset.type === 'line') return;  // Pular linhas
      
      var meta = chart.getDatasetMeta(i);
      if (!meta.hidden) {
        meta.data.forEach(function(bar, index) {
          var valor = dataset.data[index];
          if (valor == null) return;
          
          ctx.save();
          ctx.font = '700 10px "Plus Jakarta Sans", sans-serif';
          ctx.fillStyle = '#1e293b';
          
          if (rotulos90graus) {
            // Rotação 90 graus
            ctx.translate(bar.x, bar.y - 8);
            ctx.rotate(-Math.PI / 2);
            ctx.textAlign = 'right';
            ctx.textBaseline = 'middle';
            ctx.fillText(formatNum ? formatNum(valor) : valor, 0, 0);
          } else if (rotulosInferiores) {
            // Rótulos na parte INFERIOR (2 séries + meta mensal)
            ctx.textAlign = 'center';
            ctx.textBaseline = 'top';
            ctx.fillStyle = '#fff';  // Branco para contraste
            ctx.fillText(formatNum ? formatNum(valor) : valor, bar.x, bar.y + 8);
          } else {
            // Rótulos acima (padrão)
            ctx.textAlign = 'center';
            ctx.textBaseline = 'bottom';
            ctx.fillText(formatNum ? formatNum(valor) : valor, bar.x, bar.y - 4);
          }
          
          ctx.restore();
        });
      }
    });
  }
};

// Configurar plugin de rótulos
plugins: [
  isMobile ? null : labelPlugin  // só ativa no desktop
].filter(Boolean)
```

### Sem Linhas de Grade
```javascript
grid: { display: false }
```

### Legendas
**Círculos SEMPRE pequenos:**
```javascript
legend: {
  display: true,
  position: 'bottom',
  labels: {
    color: '#64748b',
    font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' },
    padding: 12,
    usePointStyle: true,
    pointStyle: 'circle',
    boxWidth: 6,      // SEMPRE 6px - círculo pequeno
    boxHeight: 6      // SEMPRE 6px - círculo pequeno
  }
}
```

### Template Completo
```javascript
new Chart(ctx, {
  type: 'bar',
  data: { ... },
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
          boxWidth: 6,      // SEMPRE 6px
          boxHeight: 6      // SEMPRE 6px
        }
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
```

---

## 3. PWA / MOBILE

### Logo Tela Inicial
```html
<!-- Favicon padrão -->
<link rel="icon" type="image/png" href="imagem/logos/sistema.png">

<!-- Apple Touch Icon (iOS) -->
<link rel="apple-touch-icon" href="imagem/logos/sistema.png">

<!-- Android PWA -->
<link rel="icon" sizes="192x192" href="imagem/logos/sistema.png">
<link rel="icon" sizes="512x512" href="imagem/logos/sistema.png">

<!-- Meta tags -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="apple-mobile-web-app-title" content="PGV5">
```

### Mobile - Esconder Título Cabeçalho
```css
@media(max-width:768px){
  /* Menu e outras páginas */
  .hdr-main > div:first-child > span{
    display:none !important;
  }
}
```

---

## 4. FORMATAÇÃO DE NÚMEROS

### Função formatNum()
```javascript
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
```

---

## 5. CORES

### Sistema de Cores para Indicadores
```javascript
function getCorIndicador(percentual, direcao) {
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
```

### Paleta
- Verde: `#16a34a`
- Amarelo: `#f59e0b`
- Vermelho: `#dc2626`
- Cinza fundo: `#e2e8f0`
- Cinza texto: `#64748b`, `#94a3b8`

### Cores Gráficos (Vibrantes + Degradê)

**Barras com Degradê:**
```javascript
// Dataset 1 - Azul Ciano Vibrante
{
  backgroundColor: function(context) {
    var ctx = context.chart.ctx;
    var gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, '#06b6d4');    // Cyan 500
    gradient.addColorStop(1, '#0891b2');    // Cyan 600
    return gradient;
  },
  borderColor: '#0891b2',
  borderWidth: 2
}

// Dataset 2 - Laranja Vibrante
{
  backgroundColor: function(context) {
    var ctx = context.chart.ctx;
    var gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, '#fb923c');    // Orange 400
    gradient.addColorStop(1, '#f97316');    // Orange 500
    return gradient;
  },
  borderColor: '#f97316',
  borderWidth: 2
}

// Dataset 3 - Roxo Vibrante (alternativa)
{
  backgroundColor: function(context) {
    var ctx = context.chart.ctx;
    var gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, '#a78bfa');    // Violet 400
    gradient.addColorStop(1, '#8b5cf6');    // Violet 500
    return gradient;
  },
  borderColor: '#8b5cf6',
  borderWidth: 2
}
```

**Linhas (Metas):**
```javascript
// Meta - Amarelo Vibrante
{
  type: 'line',
  borderColor: '#facc15',           // Yellow 400
  backgroundColor: 'transparent',
  borderWidth: 3,
  pointBackgroundColor: '#facc15',
  pointBorderColor: '#fff',
  pointBorderWidth: 2,
  pointRadius: 5,
  pointHoverRadius: 7
}
```

**Paleta Completa:**
- 🟠 **Laranja Vivo** (ano anterior): `#ff7043` → `#ff5722`
- 🔵 **Azul Ciano Vivo** (ano atual): `#00d4ff` → `#0099cc`
- 🟢 **Verde**: `#3b7d23` → `#326a1d`
- ⚪ **Cinza** (dados anteriores): `#94a3b8` → `#64748b`
- 🟡 **Amarelo** (linha meta): `#facc15`

**Degradês Suaves:**
- Laranja: Diferença de 15% (suave e vibrante)
- Azul: Diferença de 20% (suave e brilhante)

**Exemplo Completo (3 anos + meta):**
```javascript
datasets: [
  {
    label: '2024',
    data: dados2024,
    backgroundColor: function(context) {
      var ctx = context.chart.ctx;
      var gradient = ctx.createLinearGradient(0, 0, 0, context.chart.height);
      gradient.addColorStop(0, '#94a3b8');  // Cinza claro
      gradient.addColorStop(1, '#64748b');  // Cinza escuro
      return gradient;
    },
    borderColor: '#64748b',
    borderWidth: 2,
    borderRadius: 8
  },
  {
    label: '2025',
    data: dados2025,
    backgroundColor: function(context) {
      var ctx = context.chart.ctx;
      var gradient = ctx.createLinearGradient(0, 0, 0, context.chart.height);
      gradient.addColorStop(0, '#ff7043');  // Laranja vivo claro
      gradient.addColorStop(1, '#ff5722');  // Laranja vivo escuro
      return gradient;
    },
    borderColor: '#ff5722',
    borderWidth: 2,
    borderRadius: 8
  },
  {
    label: '2026',
    data: dados2026,
    backgroundColor: function(context) {
      var ctx = context.chart.ctx;
      var gradient = ctx.createLinearGradient(0, 0, 0, context.chart.height);
      gradient.addColorStop(0, '#00d4ff');  // Azul ciano vivo claro
      gradient.addColorStop(1, '#0099cc');  // Azul ciano vivo escuro
      return gradient;
    },
    borderColor: '#0099cc',
    borderWidth: 2,
    borderRadius: 8
  },
  {
    label: 'Meta',
    data: metas,
    type: 'line',
    borderColor: '#facc15',
    borderWidth: 3,
    pointBackgroundColor: '#facc15',
    pointBorderColor: '#fff',
    pointBorderWidth: 2,
    pointRadius: 5
  }
]
```

---

## CHECKLIST PRÉ-DEPLOY

- [ ] Fonte: Plus Jakarta Sans em todos CSS
- [ ] Gráficos: scales.x.display = false
- [ ] Gráficos: scales.y.display = false
- [ ] Gráficos: grid.display = false
- [ ] Legendas: boxWidth = 6, boxHeight = 6
- [ ] Rótulos: condicionais desktop/mobile
- [ ] PWA: apple-touch-icon configurado
- [ ] Mobile: título cabeçalho escondido
