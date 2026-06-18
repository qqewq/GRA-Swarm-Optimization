import numpy as np


class Subjectivity:
    """Реализация субъективности (\mathcal{S})"""

    def compute(self, agent_dist, env_dist):
        """
        \mathcal{S} = \int \rho(x) * log(\rho(x)/\mu(x)) dx (дивергенция Кульбака-Лейблера)
        """
        # Упрощённо: дискретное приближение
        # Предполагаем, что agent_dist и env_dist – массивы вероятностей
        if len(agent_dist) != len(env_dist):
            raise ValueError("Distributions must have same length")
        # Избегаем log(0)
        eps = 1e-10
        agent_dist = np.clip(agent_dist, eps, 1)
        env_dist = np.clip(env_dist, eps, 1)
        kl = np.sum(agent_dist * np.log(agent_dist / env_dist))
        return kl

    def check_loss(self, agent_subjectivity):
        if agent_subjectivity <= 0:
            return "Subjectivity loss: \mathcal{S} <= 0"
        return None

    def optimize(self, space, subjectivity):
        # Пример: добавляем субъективность как регуляризатор
        return space + subjectivity * 0.01
