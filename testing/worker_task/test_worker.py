import unittest
from worker import Worker


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Alexander', 150, 30)

    def test_worker_is_properly_initiated(self):
        self.assertEqual(self.worker.name, 'Alexander')
        self.assertEqual(self.worker.salary, 150)
        self.assertEqual(self.worker.energy, 30)

    def test_is_energy_is_increased_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    def test_worker_raises_exception_when_working_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_is_the_worker_money_is_increased(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_is_worker_energy_is_decreased(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - old_energy, -1)

    def test_is_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(info, 'Alexander has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
