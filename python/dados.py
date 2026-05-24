# ============================================================
#  dados.py — Leitura da Base Access
#  Usa schema.py para os nomes de tabelas e campos
# ============================================================

import pyodbc
from schema import JOINS, T, C


def conectar(base):
    return pyodbc.connect(
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + base + ";"
    )


def query(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    cols = [c[0] for c in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def ler_dados(base):
    conn = conectar(base)

    # ── Empresas ──────────────────────────────────────────────
    try:
        empresas = query(conn, f"""
            SELECT {C('empresas','id')}, {C('empresas','nome_fantasia')} as nome
            FROM {T('empresas')}
            ORDER BY {C('empresas','nome_fantasia')}
        """)
        # Filtrar empresa 999 programaticamente
        empresas = [e for e in empresas if e.get('id') != '61']
    except Exception as e:
        print(f"      Aviso: não leu empresas ({e})")
        empresas = []

    # ── Mensal agregado ───────────────────────────────────────
    mensal = query(conn, f"""
        SELECT Format(p.{C('pedidos','data')},'yyyy-mm')  AS ano_mes,
               Sum(pp.{C('pedido_produto','valor_total')}) AS faturamento,
               Sum(pp.{C('pedido_produto','custo_total')}) AS custo,
               Count(pp.{C('pedido_produto','pedido_id')}) AS qtd_pedidos
        FROM {JOINS['pedidos_produtos']}
        WHERE Format(p.{C('pedidos','data')},'yyyy') IN ('2025','2026')
          AND Format(p.{C('pedidos','data')},'yyyy-mm') >= '2025-01'
          AND p.{C('pedidos','empresa_id')} <> '999'
        GROUP BY Format(p.{C('pedidos','data')},'yyyy-mm')
        ORDER BY Format(p.{C('pedidos','data')},'yyyy-mm')
    """)
    for d in mensal:
        d['faturamento'] = round(float(d['faturamento'] or 0), 2)
        d['custo']       = round(float(d['custo'] or 0), 2)
        d['margem']      = round(d['faturamento'] - d['custo'], 2)
        d['margem_pct']  = round(d['margem'] / d['faturamento'] * 100, 1) if d['faturamento'] else 0
        d['qtd_pedidos'] = int(d['qtd_pedidos'] or 0)

    # ── Anual ─────────────────────────────────────────────────
    anual = query(conn, f"""
        SELECT Format(p.{C('pedidos','data')},'yyyy')     AS ano,
               Sum(pp.{C('pedido_produto','valor_total')}) AS faturamento,
               Sum(pp.{C('pedido_produto','custo_total')}) AS custo,
               Count(pp.{C('pedido_produto','pedido_id')}) AS qtd_pedidos
        FROM {JOINS['pedidos_produtos']}
        WHERE Format(p.{C('pedidos','data')},'yyyy') >= '2023'
          AND p.{C('pedidos','empresa_id')} <> '999'
        GROUP BY Format(p.{C('pedidos','data')},'yyyy')
        ORDER BY Format(p.{C('pedidos','data')},'yyyy')
    """)
    for d in anual:
        d['faturamento'] = round(float(d['faturamento'] or 0), 2)
        d['custo']       = round(float(d['custo'] or 0), 2)
        d['margem']      = round(d['faturamento'] - d['custo'], 2)
        d['margem_pct']  = round(d['margem'] / d['faturamento'] * 100, 1) if d['faturamento'] else 0
        d['qtd_pedidos'] = int(d['qtd_pedidos'] or 0)

    # ── Anual por Período (até dia/mês da data de atualização) ───
    max_data_query = query(conn, f"""
        SELECT MAX({C('pedidos','atualizado_em')}) as max_data
        FROM {T('pedidos')}
        WHERE {C('pedidos','empresa_id')} <> '999'
    """)
    
    anual_periodo = []
    if max_data_query and max_data_query[0].get('max_data'):
        max_data = max_data_query[0]['max_data']
        dia_limite = max_data.day
        mes_limite = max_data.month
        
        anual_periodo = query(conn, f"""
            SELECT Format(p.{C('pedidos','data')},'yyyy')     AS ano,
                   Sum(pp.{C('pedido_produto','valor_total')}) AS faturamento,
                   Sum(pp.{C('pedido_produto','custo_total')}) AS custo
            FROM {JOINS['pedidos_produtos']}
            WHERE Format(p.{C('pedidos','data')},'yyyy') >= '2023'
              AND p.{C('pedidos','empresa_id')} <> '999'
              AND (Month(p.{C('pedidos','data')}) < {mes_limite} 
                   OR (Month(p.{C('pedidos','data')}) = {mes_limite} AND Day(p.{C('pedidos','data')}) <= {dia_limite}))
            GROUP BY Format(p.{C('pedidos','data')},'yyyy')
            ORDER BY Format(p.{C('pedidos','data')},'yyyy')
        """)
        
        for d in anual_periodo:
            d['faturamento'] = round(float(d['faturamento'] or 0), 2)
            d['custo']       = round(float(d['custo'] or 0), 2)
            d['margem']      = round(d['faturamento'] - d['custo'], 2)

    # ── Listagem detalhada ────────────────────────────────────
    listagem = query(conn, f"""
        SELECT Format(p.{C('pedidos','data')},'yyyy')        AS ano,
               Format(p.{C('pedidos','data')},'mm')          AS mes,
               Format(p.{C('pedidos','data')},'dd')          AS dia,
               Format(p.{C('pedidos','data')},'yyyy-mm-dd')  AS data_full,
               p.{C('pedidos','empresa_id')}                 AS empresa_id,
               p.{C('pedidos','cupom')}                      AS cupom,
               p.{C('pedidos','cliente_id')}                 AS cliente,
               pp.{C('pedido_produto','produto_id')}          AS produto,
               Sum(pp.{C('pedido_produto','valor_total')})    AS venda,
               Sum(pp.{C('pedido_produto','custo_total')})    AS custo,
               Sum(pp.{C('pedido_produto','valor_total')})
                 - Sum(pp.{C('pedido_produto','custo_total')}) AS margem
        FROM {JOINS['pedidos_produtos']}
        WHERE Format(p.{C('pedidos','data')},'yyyy') >= '2025'
          AND p.{C('pedidos','empresa_id')} <> '999'
        GROUP BY Format(p.{C('pedidos','data')},'yyyy'),
                 Format(p.{C('pedidos','data')},'mm'),
                 Format(p.{C('pedidos','data')},'dd'),
                 Format(p.{C('pedidos','data')},'yyyy-mm-dd'),
                 p.{C('pedidos','empresa_id')},
                 p.{C('pedidos','cupom')},
                 p.{C('pedidos','cliente_id')},
                 pp.{C('pedido_produto','produto_id')}
        ORDER BY Format(p.{C('pedidos','data')},'yyyy-mm-dd') DESC
    """)
    for d in listagem:
        d['venda']      = round(float(d['venda']  or 0), 2)
        d['custo']      = round(float(d['custo']  or 0), 2)
        d['margem']     = round(float(d['margem'] or 0), 2)
        d['cliente']    = str(d['cliente']    or '')
        d['produto']    = str(d['produto']    or '')
        d['cupom']      = str(d['cupom']      or '')
        d['empresa_id'] = str(d['empresa_id'] or '')
        d['data_full']  = str(d['data_full']  or '')

    # ── Orçamento mensal (VENDAS) ────────────────────────────
    orcamento_vendas = query(conn, f"""
        SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-01' AS ano_mes, [{C('orcamentos','mes_01')}] AS valor FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-02', [{C('orcamentos','mes_02')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-03', [{C('orcamentos','mes_03')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-04', [{C('orcamentos','mes_04')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-05', [{C('orcamentos','mes_05')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-06', [{C('orcamentos','mes_06')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-07', [{C('orcamentos','mes_07')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-08', [{C('orcamentos','mes_08')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-09', [{C('orcamentos','mes_09')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-10', [{C('orcamentos','mes_10')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-11', [{C('orcamentos','mes_11')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-12', [{C('orcamentos','mes_12')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'VENDAS_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        ORDER BY ano_mes
    """)
    
    # ── Orçamento mensal (CMV) ────────────────────────────────
    orcamento_cmv = query(conn, f"""
        SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-01' AS ano_mes, [{C('orcamentos','mes_01')}] AS valor FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-02', [{C('orcamentos','mes_02')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-03', [{C('orcamentos','mes_03')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-04', [{C('orcamentos','mes_04')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-05', [{C('orcamentos','mes_05')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-06', [{C('orcamentos','mes_06')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-07', [{C('orcamentos','mes_07')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-08', [{C('orcamentos','mes_08')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-09', [{C('orcamentos','mes_09')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-10', [{C('orcamentos','mes_10')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-11', [{C('orcamentos','mes_11')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        UNION ALL SELECT {C('orcamentos','empresa_id')}, {C('orcamentos','ano')} & '-12', [{C('orcamentos','mes_12')}] FROM {T('orcamentos')} WHERE {C('orcamentos','tipo')} = 'CMV_ORCADO' AND {C('orcamentos','empresa_id')} <> '999'
        ORDER BY ano_mes
    """)
    
    # ── Parse e merge VENDAS + CMV ───────────────────────────
    # IMPORTANTE: Access pode retornar valores de 2 formas:
    #   1) Decimal/float direto: Decimal('610000.0000')
    #   2) String formatada BR: "R$ 610.000,00"
    # Detectamos o tipo e tratamos adequadamente para evitar erros.
    
    from decimal import Decimal
    
    def parse_valor(valor_original):
        """Helper para converter valor do Access"""
        # Caso 1: Já é número (Decimal, float, int) → converter direto
        if isinstance(valor_original, (Decimal, float, int)):
            return float(valor_original)
        
        # Caso 2: String com formato brasileiro "R$ 610.000,00"
        valor_str = str(valor_original).strip()
        valor_str = valor_str.replace('R$', '').replace('R', '').strip()
        
        # Formato BR: 610.000,00 (ponto = milhares, vírgula = decimal)
        if ',' in valor_str:
            partes = valor_str.split(',')
            inteiro = partes[0].replace('.', '').replace(' ', '')
            decimal = partes[1] if len(partes) > 1 else '00'
            valor_str = f"{inteiro}.{decimal}"
        else:
            valor_str = valor_str.replace('.', '').replace(' ', '')
        
        try:
            return float(valor_str)
        except:
            return 0.0
    
    # Parse vendas
    vendas_map = {}  # {ano_mes+empresa_id: valor}
    for d in orcamento_vendas:
        key = str(d.get('ano_mes', '')) + '|' + str(d.get('empresa_id', ''))
        vendas_map[key] = parse_valor(d.get('valor', 0))
    
    # Parse CMV
    cmv_map = {}  # {ano_mes+empresa_id: valor}
    for d in orcamento_cmv:
        key = str(d.get('ano_mes', '')) + '|' + str(d.get('empresa_id', ''))
        cmv_map[key] = parse_valor(d.get('valor', 0))
    
    # Merge e calcular margem
    orcamento = []
    all_keys = set(vendas_map.keys()) | set(cmv_map.keys())
    
    for key in sorted(all_keys):
        ano_mes, empresa_id = key.split('|')
        vendas_val = vendas_map.get(key, 0)
        cmv_val = cmv_map.get(key, 0)  # CMV é negativo
        
        # Cálculo: margem = (vendas + cmv) / vendas * 100
        # Como CMV é negativo: (1000 + (-300)) / 1000 = 0.70 = 70%
        margem_pct = 0.0
        if vendas_val > 0:
            margem_pct = ((vendas_val + cmv_val) / vendas_val) * 100
        
        orcamento.append({
            'empresa_id': empresa_id,
            'ano_mes': ano_mes,
            'orcamento': vendas_val,  # Valor de vendas orçado
            'cmv': cmv_val,           # Valor de CMV orçado (negativo)
            'margem_pct': margem_pct  # Margem % orçada
        })

    # ── Vendas por Carteira (todas) ─────────────────────────
    # Query com JOIN para pegar nome da carteira
    carteiras_raw = query(conn, f"""
        SELECT 
            cr.{C('contasrecer','data_emissao')},
            cr.{C('contasrecer','valor_titulo')},
            cart.{C('carteirareceb','tipo')} AS carteira_nome
        FROM {T('contasrecer')} AS cr
        LEFT JOIN {T('carteirareceb')} AS cart 
            ON cr.{C('contasrecer','carteira_recebimento_id')} = cart.{C('carteirareceb','id')}
        WHERE cr.{C('contasrecer','empresa_id')} <> '999'
        ORDER BY cr.{C('contasrecer','data_emissao')}
    """)
    
    # Processar e agrupar por carteira, ano e mês
    from collections import defaultdict
    from decimal import Decimal
    import re
    
    def parse_valor_br(valor_str):
        """Converte 'R$ 225,08' para float"""
        if isinstance(valor_str, (int, float, Decimal)):
            return float(valor_str)
        s = str(valor_str).replace('R$', '').replace('R', '').strip()
        if ',' in s:
            partes = s.split(',')
            inteiro = partes[0].replace('.', '').replace(' ', '')
            decimal = partes[1] if len(partes) > 1 else '00'
            s = f"{inteiro}.{decimal}"
        else:
            s = s.replace('.', '').replace(' ', '')
        try:
            return float(s)
        except:
            return 0.0
    
    # Agrupar: {(ano, mes, carteira): valor}
    agrupado = defaultdict(float)
    for row in carteiras_raw:
        data = row.get('data_emissao')
        carteira = str(row.get('carteira_nome', '') or 'SEM CARTEIRA').strip()
        if not data or not carteira:
            continue
        
        # Extrair ano e mês
        if hasattr(data, 'year'):  # datetime object
            ano = str(data.year)
            mes = str(data.month).zfill(2)
        else:  # string
            import datetime
            try:
                dt = datetime.datetime.strptime(str(data).split()[0], '%d/%m/%Y')
                ano = str(dt.year)
                mes = str(dt.month).zfill(2)
            except:
                continue
        
        valor = parse_valor_br(row.get('valor_titulo', 0))
        agrupado[(ano, mes, carteira)] += valor
    
    # Converter para formato final
    carteiras = []
    for (ano, mes, carteira), valor in sorted(agrupado.items()):
        carteiras.append({
            'ano_mes': f"{ano}-{mes}",
            'ano': ano,
            'mes': mes,
            'carteira': carteira,
            'valor': valor
        })
    
    # ── Quantidade de Pedidos (ano base vs ano anterior, mesmo período) ──
    # Obter maior data de emissão
    max_data_query = query(conn, f"""
        SELECT MAX({C('pedidos','atualizado_em')}) as max_data
        FROM {T('pedidos')}
        WHERE {C('pedidos','empresa_id')} <> '999'
    """)
    
    if max_data_query and max_data_query[0].get('max_data'):
        max_data = max_data_query[0]['max_data']
        
        # Extrair ano, mês e dia
        if hasattr(max_data, 'year'):
            ano_base = max_data.year
            mes_max = max_data.month
            dia_max = max_data.day
        else:
            # Parse string
            import datetime
            dt = datetime.datetime.strptime(str(max_data).split()[0], '%d/%m/%Y')
            ano_base = dt.year
            mes_max = dt.month
            dia_max = dt.day
        
        ano_anterior = ano_base - 1
        
        # Contar pedidos ano base (01/01 até data máxima)
        qtd_base = query(conn, f"""
            SELECT COUNT(*) as qtd
            FROM {T('pedidos')}
            WHERE {C('pedidos','empresa_id')} <> '999'
              AND {C('pedidos','data')} >= #{ano_base}-01-01#
              AND {C('pedidos','data')} <= #{ano_base}-{mes_max:02d}-{dia_max:02d}#
        """)
        
        # Contar pedidos ano anterior (mesmo período)
        qtd_anterior = query(conn, f"""
            SELECT COUNT(*) as qtd
            FROM {T('pedidos')}
            WHERE {C('pedidos','empresa_id')} <> '999'
              AND {C('pedidos','data')} >= #{ano_anterior}-01-01#
              AND {C('pedidos','data')} <= #{ano_anterior}-{mes_max:02d}-{dia_max:02d}#
        """)
        
        qtd_pedidos_base = qtd_base[0].get('qtd', 0) if qtd_base else 0
        qtd_pedidos_anterior = qtd_anterior[0].get('qtd', 0) if qtd_anterior else 0
    else:
        qtd_pedidos_base = 0
        qtd_pedidos_anterior = 0
    
    # ── Quantidade de Clientes (ano base vs ano anterior, mesmo período) ──
    if max_data_query and max_data_query[0].get('max_data'):
        # Já temos ano_base, mes_max, dia_max, ano_anterior da query anterior
        
        # Contar clientes únicos ano base (01/01 até data máxima)
        # Access não suporta COUNT(DISTINCT), usar subquery
        qtd_cli_base = query(conn, f"""
            SELECT COUNT(*) as qtd
            FROM (
                SELECT DISTINCT {C('pedidos','cliente_id')}
                FROM {T('pedidos')}
                WHERE {C('pedidos','empresa_id')} <> '999'
                  AND {C('pedidos','cliente_id')} IS NOT NULL
                  AND {C('pedidos','data')} >= #{ano_base}-01-01#
                  AND {C('pedidos','data')} <= #{ano_base}-{mes_max:02d}-{dia_max:02d}#
            )
        """)
        
        # Contar clientes únicos ano anterior (mesmo período)
        qtd_cli_anterior = query(conn, f"""
            SELECT COUNT(*) as qtd
            FROM (
                SELECT DISTINCT {C('pedidos','cliente_id')}
                FROM {T('pedidos')}
                WHERE {C('pedidos','empresa_id')} <> '999'
                  AND {C('pedidos','cliente_id')} IS NOT NULL
                  AND {C('pedidos','data')} >= #{ano_anterior}-01-01#
                  AND {C('pedidos','data')} <= #{ano_anterior}-{mes_max:02d}-{dia_max:02d}#
            )
        """)
        
        qtd_clientes_base = qtd_cli_base[0].get('qtd', 0) if qtd_cli_base else 0
        qtd_clientes_anterior = qtd_cli_anterior[0].get('qtd', 0) if qtd_cli_anterior else 0
    else:
        qtd_clientes_base = 0
        qtd_clientes_anterior = 0
    
    # ── Clientes Mensais (para o modal) ──────────────────────
    # Access não suporta COUNT(DISTINCT) em GROUP BY, então vamos usar subquery
    clientes_mensal_raw = query(conn, f"""
        SELECT Format(p.{C('pedidos','data')},'yyyy-mm') AS ano_mes,
               COUNT(*) AS qtd_clientes
        FROM (
            SELECT DISTINCT p.{C('pedidos','data')}, p.{C('pedidos','cliente_id')}
            FROM {T('pedidos')} AS p
            WHERE p.{C('pedidos','empresa_id')} <> '999'
              AND p.{C('pedidos','cliente_id')} IS NOT NULL
              AND Format(p.{C('pedidos','data')},'yyyy') >= '2022'
        ) AS subq
        INNER JOIN {T('pedidos')} AS p ON subq.{C('pedidos','data')} = p.{C('pedidos','data')}
                                       AND subq.{C('pedidos','cliente_id')} = p.{C('pedidos','cliente_id')}
        GROUP BY Format(p.{C('pedidos','data')},'yyyy-mm')
        ORDER BY Format(p.{C('pedidos','data')},'yyyy-mm')
    """)
    
    # Processar contagens mensais de clientes
    clientes_mensal = []
    for row in clientes_mensal_raw:
        ano_mes = row.get('ano_mes')
        if ano_mes:
            # Contar clientes únicos neste mês
            # A query já fez isso, mas vamos garantir
            clientes_no_mes = query(conn, f"""
                SELECT COUNT(*) AS qtd
                FROM (
                    SELECT DISTINCT {C('pedidos','cliente_id')}
                    FROM {T('pedidos')}
                    WHERE Format({C('pedidos','data')},'yyyy-mm') = '{ano_mes}'
                      AND {C('pedidos','empresa_id')} <> '999'
                      AND {C('pedidos','cliente_id')} IS NOT NULL
                )
            """)
            qtd = clientes_no_mes[0].get('qtd', 0) if clientes_no_mes else 0
            clientes_mensal.append({
                'ano_mes': ano_mes,
                'qtd_clientes': qtd
            })

    # ── Índice de Recebimento (últimos 5 anos) ────────────────
    # Para anos anteriores: recebimentos do ano (data_emissao) independente de quando foi pago
    indice_receb = []
    
    # Pegar últimos 5 anos de anual (já temos vendas)
    anos_vendas = {}
    for d in anual:
        anos_vendas[d['ano']] = d['faturamento']
    
    anos_ordenados = sorted(anos_vendas.keys())[-5:]
    
    for ano in anos_ordenados:
        vendas_ano = anos_vendas.get(ano, 0)
        
        # Recebimentos: baixas cuja data_emissao foi neste ano
        receb_query = query(conn, f"""
            SELECT SUM(b.{C('contasrecebaixas','valor_titulo')}) AS total_recebido
            FROM {T('contasrecebaixas')} AS b
            INNER JOIN {T('contasrecer')} AS cr ON cr.{C('contasrecer','id')} = b.{C('contasrecebaixas','contas_receber_id')}
            WHERE Format(cr.{C('contasrecer','data_emissao')},'yyyy') = '{ano}'
              AND cr.{C('contasrecer','empresa_id')} <> '999'
        """)
        
        total_recebido = 0
        if receb_query and receb_query[0].get('total_recebido'):
            val = receb_query[0]['total_recebido']
            # Pode vir como Decimal ou string formatada
            from decimal import Decimal
            if isinstance(val, (Decimal, float, int)):
                total_recebido = float(val)
            else:
                # Parse formato BR
                s = str(val).replace('R$', '').replace('R', '').strip()
                if ',' in s:
                    partes = s.split(',')
                    inteiro = partes[0].replace('.', '').replace(' ', '')
                    decimal = partes[1] if len(partes) > 1 else '00'
                    s = f"{inteiro}.{decimal}"
                else:
                    s = s.replace('.', '').replace(' ', '')
                try:
                    total_recebido = float(s)
                except:
                    total_recebido = 0
        
        indice_pct = round((total_recebido / vendas_ano * 100), 1) if vendas_ano > 0 else 0
        
        indice_receb.append({
            'ano': ano,
            'vendas': vendas_ano,
            'recebido': total_recebido,
            'indice_pct': indice_pct
        })

    conn.close()
    return {
        "mensal":    mensal,
        "anual":     anual,
        "anual_periodo": anual_periodo,
        "listagem":  listagem,
        "empresas":  empresas,
        "orcamento": orcamento,
        "carteiras": carteiras,
        "qtd_pedidos_base": qtd_pedidos_base,
        "qtd_pedidos_anterior": qtd_pedidos_anterior,
        "qtd_clientes_base": qtd_clientes_base,
        "qtd_clientes_anterior": qtd_clientes_anterior,
        "clientes_mensal": clientes_mensal,
        "indice_receb": indice_receb,
        "data_atualizacao": max_data.strftime("%d/%m/%Y %H:%M") if max_data else None,
    }
