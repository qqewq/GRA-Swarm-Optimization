import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from gra_swarm import GRASwarm
from gra_swarm.utils import print_schema


def main():
    print_schema()

    # Определяем общую цель: максимизировать некоторую функцию
    goal = "Maximize profit in trading simulation"

    # Начальное Гёделевское пространство решений (случайные векторы)
    initial_space = np.random.randn(10, 5)  # 10 решений, каждое размерности 5

    # Создаём рой из 5 агентов
    swarm = GRASwarm(num_agents=5, goal=goal, initial_godel_space=initial_space)

    # Запускаем полную оптимизацию на 3 итерации (для демонстрации)
    swarm.run_full_optimization(iterations=3)

    # Выводим финальные оптимумы каждого агента
    for agent in swarm.agents:
        print(f"Agent {agent.agent_id} final optimal solution: {agent.godel_space.optimal}")


if __name__ == "__main__":
    main()
