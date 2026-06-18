# Использование GRA-Swarm-Optimization

## Быстрый старт

```python
import numpy as np
from gra_swarm import GRASwarm

# Определяем цель
goal = "Maximize profit in trading simulation"

# Создаём начальное Гёделевское пространство
initial_space = np.random.randn(10, 5)

# Создаём рой из 5 агентов
swarm = GRASwarm(num_agents=5, goal=goal, initial_godel_space=initial_space)

# Запускаем оптимизацию
swarm.run_full_optimization(iterations=3)
```

## Настройка агентов

Каждый агент имеет:
- `subjectivity` – вектор субъективности
- `hierarchy` – уровни иерархии
- `goal` – общая цель роя

## Расширение

Для добавления новых типов ошибок расширьте метод `find_fundamental_errors()` в `GRAAgent`.
