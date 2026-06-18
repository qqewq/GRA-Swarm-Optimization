import random
from .agent import GRAAgent


class GRASwarm:
    """
    Рой ИИ-агентов.
    Управляет агентами, организует взаимную критику и рекурсивную оптимизацию.
    """
    def __init__(self, num_agents, goal, initial_godel_space):
        self.agents = []
        for i in range(num_agents):
            agent = GRAAgent(i, goal, initial_godel_space)
            self.agents.append(agent)

        # Назначаем соседей (кольцевая топология)
        for i in range(num_agents):
            neighbor = self.agents[(i + 1) % num_agents]
            self.agents[i].set_neighbor(neighbor)

        self.current_iteration = 0

    def run_swarm_iteration(self):
        """
        Одна итерация роя:
        1. Каждый агент критикует соседа, находит ошибки.
        2. Каждый агент оптимизирует своё Гёделевское пространство.
        3. Каждый агент оптимизирует свою оптимизацию (рекурсия).
        """
        print(f"--- Swarm iteration {self.current_iteration} ---")

        # Шаг 1: Поиск ошибок
        for agent in self.agents:
            errors = agent.find_fundamental_errors()
            if errors:
                print(f"Agent {agent.agent_id} found errors in neighbor {agent.neighbor.agent_id}: {len(errors)} errors")
                for err in errors:
                    print(f"  {err['type']}: {err['description']}")

        # Шаг 2: Оптимизация Гёделевского пространства (каждый агент)
        for agent in self.agents:
            optimal = agent.optimize_godel_space()
            print(f"Agent {agent.agent_id} optimized space, optimal solution: {optimal}")

        # Шаг 3: Рекурсивная оптимизация (оптимизация оптимизации)
        # Используем функцию из gra_core для демонстрации
        for agent in self.agents:
            # Возьмём функцию оптимизации, например, optimize_godel_space
            func = agent.optimize_godel_space
            better_opt = agent.optimize_optimization(func)
            print(f"Agent {agent.agent_id} recursively optimized optimization, new optimum: {better_opt}")

        self.current_iteration += 1

    def run_full_optimization(self, iterations=10):
        """Запускает полный процесс рекурсивной оптимизации"""
        for _ in range(iterations):
            self.run_swarm_iteration()
        print("Full optimization complete.")
