from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_vacancies(self):
        wait = WebDriverWait(self.driver, 10)
        vacancies_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Vacancies']"))
        )
        vacancies_tab.click()
