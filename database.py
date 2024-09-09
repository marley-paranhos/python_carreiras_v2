from sqlalchemy import create_engine, text
import os

# String de conexão usando 'mysql+pymysql' para se conectar ao banco de dados MySQL na Railway
string_conexao = os.environ['db_conexao_string']

# Criação da engine com SSL ativado, sem necessidade de especificar um certificado
engine = create_engine(
    string_conexao,
    connect_args={
        'ssl_disabled': False  # Habilita SSL sem especificar um certificado manualmente
    }
)
# 

def carrega_vagas_db():
  # Conexão e execução da consulta
  with engine.connect() as conn:
      resultado = conn.execute(text("SELECT * FROM vagas"))

      # Inicializa uma lista vazia para armazenar os dicionários
      vagas = []

      # Itera sobre o resultado da consulta e transforma cada linha em dicionário
      for vaga in resultado.mappings():  # Usando .mappings() para mapear o resultado como dicionário
          vagas.append(dict(vaga))

      # Retorna a lista de dicionários
      return vagas


def carrega_vaga_db(id):
  # Conexão e execução da consulta
  with engine.connect() as conn:
      resultado = conn.execute(text(
        f'SELECT * FROM vagas WHERE id = :val'
      ),
        {'val': id}
      )

      registro = resultado.mappings().all()
      if len(registro) == 0:
        return None
      else:
        return dict(registro[0])
