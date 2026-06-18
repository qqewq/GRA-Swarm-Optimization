https://orcid.org/my-orcid?orcid=0009-0004-1872-1153
https://doi.org/10.5281/zenodo.20741609
-------------
Ниже готовый двуязычный README, можешь просто заменить им текущий `README.md` в репо.

***

# GRA-Swarm-Optimization  

**RU | EN**

Рой ИИ-агентов на основе GRA-Обнуленки для рекурсивной оптимизации Гёделевского пространства решений.  
A swarm of GRA-based AI agents for recursive optimization of the Gödel solution space.

***

## 🇷🇺 Описание проекта

`GRA-Swarm-Optimization` — это экспериментальная реализация роя ИИ-агентов, работающих поверх семейства библиотек **GRA / Обнуленка**.  
Каждый агент:

- стремится к *общей цели* (оптимизация Гёделевского пространства решений под конкретную задачу);
- анализирует решения и поведение *соседних агентов* и ищет **наиболее фундаментальные ошибки** в их подходах;
- использует принципы **GRA-Обнуленки, иерархической стабильности и мультиверсной согласованности** для улучшения всего роя.

Таким образом, сначала оптимизируется **Гёделевское пространство решений**, а затем — **сама процедура оптимизации** этого пространства (рекурсивная оптимизация оптимизации).

Проект опирается на экосистему GRA:

- `GRA-Hormonal-Explosion-Of-Subject`  
- `GRA-Living-Vaccine-Architecture`  
- `GRA-Core-Unified-Hierarchical-Stability-Library`  
- `gra-orchestra`  
- `Drone-War-Distributed-GRA`  
- `GRA-ASI-Metric-Space`  
- `GRA-Multiverse-Final`  
- `ALL-IN-BIT-The-Foamless-Landscape-of-Optimal-Rank-N`  
- `Hierarchical-Stability-Rank-N`  
- `GRA-Hierarchical-Stability`  
- `Love-Swarm-Nullification-Enhanced`  
- `GRA-Love-Oriented-Nullification`  
- `GRA-Swarm-Subject`  

Подробные материалы см. в каталоге `docs/` и примерах в `examples/`.

***

## 🇬🇧 Project description

`GRA-Swarm-Optimization` is an experimental implementation of a swarm of AI agents built on top of the **GRA / Nullification** framework.  
Each agent:

- pursues a *shared global goal* (optimizing the Gödel solution space for a given task);
- inspects the *neighboring agents* and searches for the **most fundamental errors** in their approaches;
- uses **GRA Nullification, hierarchical stability, and multiverse consistency** to improve the entire swarm.

This creates a recursive loop:

1. First, the **Gödel solution space** is optimized.  
2. Then, the **optimization procedure itself** is optimized (optimization of optimization).

The project relies on the GRA ecosystem:

- `GRA-Hormonal-Explosion-Of-Subject`  
- `GRA-Living-Vaccine-Architecture`  
- `GRA-Core-Unified-Hierarchical-Stability-Library`  
- `gra-orchestra`  
- `Drone-War-Distributed-GRA`  
- `GRA-ASI-Metric-Space`  
- `GRA-Multiverse-Final`  
- `ALL-IN-BIT-The-Foamless-Landscape-of-Optimal-Rank-N`  
- `Hierarchical-Stability-Rank-N`  
- `GRA-Hierarchical-Stability`  
- `Love-Swarm-Nullification-Enhanced`  
- `GRA-Love-Oriented-Nullification`  
- `GRA-Swarm-Subject`  

See `docs/` for detailed theory and `examples/` for runnable demos.

***

## 🇷🇺 Установка

```bash
git clone https://github.com/qqewq/GRA-Swarm-Optimization.git
cd GRA-Swarm-Optimization
pip install -r requirements.txt
```

(При необходимости установите также зависимости GRA-репозиториев, если они используются как git-submodule или отдельные пакеты.)

***

## 🇬🇧 Installation

```bash
git clone https://github.com/qqewq/GRA-Swarm-Optimization.git
cd GRA-Swarm-Optimization
pip install -r requirements.txt
```

(Additionally install any required GRA repositories if they are used as git submodules or separate packages.)

***

## 🇷🇺 Быстрый старт

Минимальный пример использования см. в `examples/`. Условно:

```python
from gra_swarm import Swarm, GRAAgent
from gra_swarm.godel_space import GodelSpace

# создаём Гёделевское пространство решений
godel_space = GodelSpace(initial_data=...)

# создаём рой агентов
swarm = Swarm(
    num_agents=16,
    goal="optimize_godel_space",
    godel_space=godel_space,
)

# запускаем рекурсивную оптимизацию
optimized_space = swarm.run_recursive_optimization(
    iterations=10
)
```

***

## 🇬🇧 Quick start

See `examples/` for runnable usage. Conceptually:

```python
from gra_swarm import Swarm, GRAAgent
from gra_swarm.godel_space import GodelSpace

# create Gödel solution space
godel_space = GodelSpace(initial_data=...)

# create a swarm of agents
swarm = Swarm(
    num_agents=16,
    goal="optimize_godel_space",
    godel_space=godel_space,
)

# run recursive optimization
optimized_space = swarm.run_recursive_optimization(
    iterations=10
)
```

***

## 🇷🇺 Основные идеи архитектуры

- **Рой агентов**: каждый агент имеет собственную субъектность (GRA-Subject), но работает на общую цель роя.  
- **Поиск фундаментальных ошибок**:  
  агент A анализирует агента B и пытается найти:
  - нарушения иерархической стабильности,
  - потерю субъектности,
  - сбои в механизмах обнуления (nullification),
  - несогласованности в мультиверсном представлении задач.  
- **Nullification / Обнуление**:  
  ошибки не просто фиксируются, а *обнуляются* через GRA-Love-Oriented / Love-Swarm механизмы.  
- **Рекурсия над оптимизацией**:  
  на верхнем уровне оптимизируется не только решение, но и сама **процедура поиска решения** (мета-оптимизация).

***

## 🇬🇧 Core architectural ideas

- **Swarm of agents**: each agent has its own subjectivity (GRA-Subject) but serves the shared swarm-level goal.  
- **Fundamental error search**:  
  agent A inspects agent B and tries to detect:
  - hierarchical stability violations,
  - subjectivity loss,
  - nullification failures,
  - multiverse inconsistencies in task representation.  
- **Nullification**:  
  errors are not only detected, but *nullified* using GRA-Love-Oriented / Love-Swarm mechanisms.  
- **Recursive optimization**:  
  at the meta-level, the system optimizes not only the solution but the **optimization process itself**.

***

## 🇷🇺 Документация

- `docs/` — теоретические материалы, схемы, формулы, описания протоколов роя.
- `examples/` — примеры:
  - простая оптимизация Гёделевского пространства,
  - рой агентов, критикующих друг друга,
  - рекурсивная мета-оптимизация.

***

## 🇬🇧 Documentation

- `docs/` — theoretical materials, diagrams, formulas, swarm protocols.
- `examples/` — examples:
  - basic Gödel space optimization,
  - a swarm of mutually critical agents,
  - recursive meta-optimization.

***

## 🇷🇺 Лицензия

Проект распространяется по лицензии **MIT**. См. файл `LICENSE`.

***

## 🇬🇧 License

This project is released under the **MIT** license. See `LICENSE` for details.
