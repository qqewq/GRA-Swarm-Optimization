import numpy as np


class HierarchicalStability:
    """Реализация Hierarchical Stability (S_h)"""

    def __init__(self, threshold=0.8, lambda_coeff=0.1):
        self.threshold = threshold
        self.lambda_coeff = lambda_coeff

    def compute(self, hierarchy_levels):
        """
        S_h = \prod (H_i / H_{i-1}) * exp(-\lambda * \Delta H_i)
        """
        if len(hierarchy_levels) < 2:
            return 1.0
        product = 1.0
        for i in range(1, len(hierarchy_levels)):
            H_prev = hierarchy_levels[i-1]
            H_curr = hierarchy_levels[i]
            if H_prev == 0:
                continue
            ratio = H_curr / H_prev
            delta = H_curr - H_prev
            product *= ratio * np.exp(-self.lambda_coeff * abs(delta))
        return product

    def check_violation(self, hierarchy):
        S = self.compute(hierarchy)
        if S < self.threshold:
            return f"Hierarchical Stability violation: S={S:.3f} < threshold={self.threshold}"
        return None

    def optimize(self, space):
        """Упрощённая оптимизация: повышаем стабильность иерархии"""
        # В реальности здесь сложная оптимизация, здесь пример
        return np.clip(space, 0, 1)
