from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_recruitment(self):
        self.driver.find_element(By.XPATH, "//span[text()='Recruitment']").click()
