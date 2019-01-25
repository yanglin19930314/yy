import allure

class Test_001:
    @allure.step(title='第一个测试步骤')
    def test_001(self):
        print('---test_001')
        assert True

    @allure.step(title='第二个测试步骤')
    def test_002(self):
        print('---test_002')
        assert False