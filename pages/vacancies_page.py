from selenium.webdriver.common.by import By


class VacanciesPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()

    def search_vacancy(self, job_title, hiring_manager):
        self.driver.find_element(
            By.XPATH, "//label[text()='Job Title']/../following-sibling::div//input"
        ).send_keys(job_title)
        self.driver.find_element(
            By.XPATH,
            "//label[text()='Hiring Manager']/../following-sibling::div//input",
        ).send_keys(hiring_manager)
        self.driver.find_element(By.XPATH, "//button[text()='Search']").click()
