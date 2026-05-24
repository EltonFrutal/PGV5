# ============================================================
#  schema.py — Estruturas de Dados (Configuração)
# ============================================================
"""
Define as estruturas de dados lidas de configuracao.xlsx
"""

from dataclasses import dataclass
from typing import List, Optional
import pandas as pd


# ── CLASSES DE DADOS ────────────────────────────────────────

@dataclass
class Usuario:
    """Usuário do sistema"""
    id: int
    nome: str           # Email do usuário
    senha: str
    perfil: str         # Administrador, Consultor, etc
    permissao: str      # Nível de permissão
    foto: str           # Nome do arquivo da foto


@dataclass
class Empresa:
    """Empresa cadastrada"""
    id: int
    empresa: str        # Nome da empresa
    ativo: str          # "Sim" ou "Não"
    pasta: str          # Caminho dos dados (ex: multicar-000061)
    icone: str          # Nome do ícone (ex: multicar)
    
    def is_ativa(self) -> bool:
        """Verifica se empresa está ativa"""
        return self.ativo.lower() == 'sim'


@dataclass
class UsuarioEmpresa:
    """Vínculo usuário x empresa + permissões"""
    usuario: int
    usuarionome: str
    empresa: int
    empresanome: str
    exibevendas: str
    exibecompras: str
    exibeareceber: str
    exibeapagar: str
    exibehistoricos: str
    exibeindicadores: str
    exiberesultados: str
    
    def tem_permissao(self, modulo: str) -> bool:
        """Verifica se tem permissão para o módulo"""
        campo = f'exibe{modulo.lower()}'
        valor = getattr(self, campo, 'não')
        return valor.lower() == 'sim'


# ── FUNÇÕES DE LEITURA ─────────────────────────────────────

def ler_configuracao(caminho_excel: str = 'configuracao.xlsx'):
    """
    Lê arquivo de configuração e retorna dicionário com dados
    
    Returns:
        dict com chaves: usuarios, empresas, usuario_empresa
    """
    # Ler todas as abas
    usuarios_df = pd.read_excel(caminho_excel, sheet_name='usuario')
    empresas_df = pd.read_excel(caminho_excel, sheet_name='empresa')
    usuario_empresa_df = pd.read_excel(caminho_excel, sheet_name='usuarioempresa')
    
    # Converter para objetos
    usuarios = [
        Usuario(
            id=int(row['id']),
            nome=str(row['nome']),
            senha=str(row['senha']),
            perfil=str(row['perfil']),
            permissao=str(row['permissao']),
            foto=str(row['foto'])
        )
        for _, row in usuarios_df.iterrows()
    ]
    
    empresas = [
        Empresa(
            id=int(row['id']),
            empresa=str(row['empresa']),
            ativo=str(row['Ativo']),
            pasta=str(row['pasta']),
            icone=str(row['icone'])
        )
        for _, row in empresas_df.iterrows()
    ]
    
    usuario_empresa = [
        UsuarioEmpresa(
            usuario=int(row['usuario']),
            usuarionome=str(row['usuarionome']),
            empresa=int(row['empresa']),
            empresanome=str(row['empresanome']),
            exibevendas=str(row['exibevendas']),
            exibecompras=str(row['exibecompras']),
            exibeareceber=str(row['exibeareceber']),
            exibeapagar=str(row['exibeapagar']),
            exibehistoricos=str(row['exibehistoricos']),
            exibeindicadores=str(row['exibeindicadores']),
            exiberesultados=str(row['exiberesultados'])
        )
        for _, row in usuario_empresa_df.iterrows()
    ]
    
    return {
        'usuarios': usuarios,
        'empresas': empresas,
        'usuario_empresa': usuario_empresa
    }


def autenticar_usuario(email: str, senha: str, config: dict) -> Optional[Usuario]:
    """
    Autentica usuário
    
    Returns:
        Usuario se credenciais válidas, None caso contrário
    """
    for usuario in config['usuarios']:
        if usuario.nome == email and usuario.senha == senha:
            return usuario
    return None


def obter_empresas_usuario(usuario_id: int, config: dict) -> List[Empresa]:
    """
    Retorna empresas ativas vinculadas ao usuário
    """
    # Buscar vínculos do usuário
    vinculos = [
        v for v in config['usuario_empresa']
        if v.usuario == usuario_id
    ]
    
    # IDs das empresas vinculadas
    empresa_ids = [v.empresa for v in vinculos]
    
    # Retornar empresas ativas
    empresas = [
        e for e in config['empresas']
        if e.id in empresa_ids and e.is_ativa()
    ]
    
    return empresas


def obter_permissoes_usuario(usuario_id: int, empresa_id: int, config: dict) -> Optional[UsuarioEmpresa]:
    """
    Retorna permissões do usuário na empresa
    """
    for vinculo in config['usuario_empresa']:
        if vinculo.usuario == usuario_id and vinculo.empresa == empresa_id:
            return vinculo
    return None
