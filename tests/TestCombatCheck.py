import unittest
from config import config
from ok.test.TaskTestCase import TaskTestCase
from src.task.AutoCombatTask import AutoCombatTask

config['debug'] = True


class TestCombatCheck(TaskTestCase):
    task_class = AutoCombatTask
    config = config

    def test_in_combat_check(self):
        self.task.do_reset_to_false()
        self.set_image('tests/images/test1.png')
        in_combat = self.task.in_combat()
        print("[DEBUG] " + str(in_combat))

    def test_in_combat_check2(self):
        self.task.do_reset_to_false()
        self.set_image('tests/images/test2.png')
        in_combat = self.task.in_combat()
        print("[DEBUG] " + str(in_combat))

    def test_in_combat_check3(self):
        self.task.do_reset_to_false()
        self.set_image('tests/images/test3.png')
        in_combat = self.task.in_combat()
        print("[DEBUG] " + str(in_combat))
        self.logger.debug('in_combat_check task done')


if __name__ == '__main__':
    unittest.main()
