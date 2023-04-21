import os
from unittest import TestCase


class Test(TestCase):
    def test_on_ready(self):

        # 断言文件路径中存在userInfo.csv
        self.assertTrue(os.path.exists('userInfo.csv'))
