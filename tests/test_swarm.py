import unittest
import numpy as np
from gra_swarm.swarm import GRASwarm


class TestGRASwarm(unittest.TestCase):
    def setUp(self):
        self.goal = "test_goal"
        self.space = np.random.randn(5, 3)
        self.swarm = GRASwarm(num_agents=3, goal=self.goal, initial_godel_space=self.space)

    def test_swarm_creation(self):
        self.assertEqual(len(self.swarm.agents), 3)

    def test_swarm_iteration(self):
        self.swarm.run_swarm_iteration()
        self.assertEqual(self.swarm.current_iteration, 1)


if __name__ == '__main__':
    unittest.main()
