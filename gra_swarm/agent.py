import numpy as np
from .gra_core import GRACore
from .godel_space import GodelSpace


class GRAAgent:
    """
    ИИ-агент в рое.
    Каждый агент:
    - имеет цель (общую для роя)
    - имеет субъективность (собственное восприятие)
    - может критиковать соседа, находя его фундаментальные ошибки
    - может оптимизировать Гёделевское пространство
    - может рекурсивно оптимизировать саму оптимизацию
    """

    def __init__(self, agent_id, goal, initial_godel_space):
        self.agent_id = agent_id
        self.goal = goal
        self.gra_core = GRACore()
        self.godel_space = GodelSpace(initial_godel_space)
        self.subjectivity = np.random.randn(10)  # пример субъективности
        self.hierarchy = [1, 2, 3, 5]  # уровни иерархии
        self.neighbor = None
        self.errors_found = []

    def set_neighbor(self, neighbor_agent):
        self.neighbor = neighbor_agent

    def find_fundamental_errors(self):
        """
        Ищет фундаментальные ошибки у соседнего агента.
        Возвращает список ошибок.
        """
        if self.neighbor is None:
            return []

        errors = []
        neighbor = self.neighbor

        # 1. Проверка Hierarchical Stability
        err = self.gra_core.check_stability_violation(neighbor.hierarchy)
        if err:
            errors.append({
                'type': 'HIERARCHICAL_STABILITY_VIOLATION',
                'severity': 'FUNDAMENTAL',
                'description': err,
                'source_agent': neighbor.agent_id
            })

        # 2. Проверка Subjectivity
        subj_val = np.mean(neighbor.subjectivity)  # упрощённо
        err = self.gra_core.check_subjectivity_loss(subj_val)
        if err:
            errors.append({
                'type': 'SUBJECTIVITY_LOSS',
                'severity': 'CRITICAL',
                'description': err,
                'source_agent': neighbor.agent_id
            })

        # 3. Проверка Nullification
        err = self.gra_core.check_nullification_failure(neighbor.gra_core)
        if err:
            errors.append({
                'type': 'NULLIFICATION_FAILURE',
                'severity': 'FUNDAMENTAL',
                'description': err,
                'source_agent': neighbor.agent_id
            })

        # 4. Проверка Multiverse
        err = self.gra_core.check_multiverse_inconsistency(neighbor.goal)
        if err:
            errors.append({
                'type': 'MULTIVERSE_INCONSISTENCY',
                'severity': 'CRITICAL',
                'description': err,
                'source_agent': neighbor.agent_id
            })

        self.errors_found = errors
        return errors

    def optimize_godel_space(self):
        """Оптимизирует Гёделевское пространство с учётом своих параметров"""
        hs = self.gra_core.hs
        subj = self.gra_core.subj
        null = self.gra_core.null

        # Оптимизация через GRA-Core
        space = self.godel_space.space
        space = self.gra_core.optimize_hierarchical_stability(space)
        space = self.gra_core.optimize_subjectivity(space, self.subjectivity)
        space = self.gra_core.optimize_nullification(space)
        space = self.gra_core.optimize_multiverse(space)

        # Обновляем пространство
        self.godel_space.space = space

        # Находим оптимальное решение
        optimal = self.godel_space.optimize(hs, subj, null)
        return optimal

    def optimize_optimization(self, optimization_function):
        """
        Рекурсивная оптимизация: оптимизирует саму функцию оптимизации.
        """
        # Находим ошибки в текущей оптимизационной функции
        # (упрощённо: считаем, что функция имеет параметры, которые можно настроить)
        # Для примера, будем корректировать параметры на основе ошибок соседа
        errors = self.find_fundamental_errors()
        corrected_func = self.gra_core.correct_optimization(optimization_function, errors)

        # Применяем исправленную функцию к пространству
        new_space = corrected_func(self.godel_space.space)
        self.godel_space.space = new_space

        # Повторно оптимизируем
        return self.optimize_godel_space()
