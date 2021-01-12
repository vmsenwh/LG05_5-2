
from test_po.page.main_page import MainPage


class TestAddDept():

    def setup(self):
        self.mainpage = MainPage()

    def teardown(self):
        self.mainpage.driver.quit()

    def test_add_dept(self):
        result = self.mainpage.goto_contact().add_dept("super").get_dept()
        assert "super" in result

    def test_add_dept_fail(self):
        result = self.mainpage.goto_contact().add_dept_fail("super").get_dept()
        assert result[0]
