import pytest
from gerenciador import GerenciadorTarefas

def test_adicionar_tarefa_sucesso():
    """Testa se uma tarefa é adicionada corretamente"""
    sistema = GerenciadorTarefas()
    resultado = sistema.adicionar_tarefa("Entrega na Av. Paulista", "Alta")
    
    assert resultado == "Sucesso"
    assert len(sistema.listar_tarefas()) == 1
    assert sistema.listar_tarefas()[0]["descricao"] == "Entrega na Av. Paulista"

def test_adicionar_tarefa_invalida():
    """Testa se o sistema recusa tarefa sem descrição"""
    sistema = GerenciadorTarefas()
    resultado = sistema.adicionar_tarefa("", "Normal")
    
    assert "Erro" in resultado
    assert len(sistema.listar_tarefas()) == 0

def test_concluir_tarefa():
    """Testa a mudança de status de uma tarefa"""
    sistema = GerenciadorTarefas()
    sistema.adicionar_tarefa("Entrega em Alphaville")
    
    # O ID da primeira tarefa será 1
    sucesso = sistema.concluir_tarefa(1)
    
    assert sucesso is True
    assert sistema.listar_tarefas()[0]["status"] == "Concluído"

def test_concluir_tarefa_inexistente():
    """Testa se o sistema lida com ID que não existe"""
    sistema = GerenciadorTarefas()
    sucesso = sistema.concluir_tarefa(999)
    
    assert sucesso is False