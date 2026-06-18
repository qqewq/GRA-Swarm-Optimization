import unittest
import numpy as np
from gra_swarm.optimization import RecursiveOptimizer
from gra_swarm.agent import GRAAgent


class TestRecursiveOptimizer(unittest.TestCase):
    def setUp(self):
        self.goal = "test_goal"
        self.space = np.random.randn(5, 3)
        self.agent = GRAAgent(0, self.goal, self.space)

    def test_optimize_with_errors(self):
        func = self.agent.optimize_godel_space
        errors = []
        result = RecursiveOptimizer.optimize_godel_space_with_errors(self.agent, func, errors)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
