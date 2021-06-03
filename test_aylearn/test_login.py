from page.login import Login


class TestLogin:
    def setup(self):
        self.login = Login()

    def test_register(self):
        self.login.goto_index('05132', 'CJ2938cj')

