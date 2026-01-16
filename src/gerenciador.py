class GerenciadorTarefas:
    def __init__(self):
        # Lista para armazenar as tarefas (entregas)
        self.tarefas = []

    def adicionar_tarefa(self, descricao, prioridade="Normal"):
        """
        Adiciona uma nova tarefa de logística ao sistema.
        """
        if not descricao:
            return "Erro: Descrição não pode ser vazia."
        
        tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": "Pendente"
        }
        self.tarefas.append(tarefa)
        return "Sucesso"

    def listar_tarefas(self):
        """
        Retorna todas as tarefas cadastradas.
        """
        return self.tarefas

    def concluir_tarefa(self, id_tarefa):
        """
        Marca uma tarefa como concluída pelo ID.
        """
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["status"] = "Concluído"
                return True
        return False

# Exemplo de uso rápido para teste manual:
if __name__ == "__main__":
    app = GerenciadorTarefas()
    app.adicionar_tarefa("Entrega na Avenida Paulista", "Alta")
    print(app.listar_tarefas())