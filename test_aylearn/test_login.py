from page.login import Login


class TestLogin:
    def setup_class(self):
        self.login = Login()

    def test_goto_myclass(self):
        self.login.goto_myclass('05132', 'CJ2938cj').select_class()



