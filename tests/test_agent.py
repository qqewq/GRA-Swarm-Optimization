import unittest
import numpy as np
from gra_swarm.agent import GRAAgent


class TestGRAAgent(unittest.TestCase):
    def setUp(self):
        self.goal = "test_goal"
        self.space = np.random.randn(5, 3)
        self.agent1 = GRAAgent(0, self.goal, self.space)
        self.agent2 = GRAAgent(1, self.goal, self.space)
        self.agent1.set_neighbor(self.agent2)
        self.agent2.set_neighbor(self.agent1)

    def test_find_errors(self):
        errors = self.agent1.find_fundamental_errors()
        self.assertIsInstance(errors, list)

    def test_optimize_godel(self):
        opt = self.agent1.optimize_godel_space()
        self.assertIsNotNone(opt)

    def test_optimize_optimization(self):
        func = self.agent1.optimize_godel_space
        result = self.agent1.optimize_optimization(func)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
