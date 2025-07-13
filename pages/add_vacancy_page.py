from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class AddVacancyPage:
    def __init__(self, driver):
        self.driver = driver

    def select_job_title(self, job_title):
        wait = WebDriverWait(self.driver, 10)

        # B1: Click dropdown
        dropdown = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//label[contains(text(),'Job Title')]/following::div[contains(@class,'oxd-select-text')][1]",
                )
            )
        )
        dropdown.click()
        # B2: Click option cần chọn

        self.driver.implicitly_wait(10)

        option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@role='option' and normalize-space()='{job_title}']")
            )
        )
        option.click()

    def slow_action(self, sec=6):
        import time

        time.sleep(sec)

    def input_hiring_manager_with_wait(self):
        wait = WebDriverWait(self.driver, 10)
        # 1. Tìm input
        hiring_input = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='Hiring Manager']/following::input[1]")
            )
        )
        hiring_input.clear()
        actions = ActionChains(self.driver)
        actions.move_to_element(hiring_input).click().send_keys("user").perform()
        # 2. Đợi tối đa 10s để dropdown suggest xuất hiện
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'oxd-autocomplete-dropdown')]")
            )
        )
        time.sleep(1)  # Cho bạn nhìn thấy dropdown hiện ra, có thể bỏ nếu muốn nhanh
        # 3. Arrow down để chọn suggest đầu tiên
        actions = ActionChains(self.driver)  # Tạo lại để đảm bảo focus
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(1)  # Cho bạn nhìn thấy đã chọn xong

    def fill_hiring_manager(self):
        from time import sleep

        current_user_name = "name"

        hiring_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='Hiring Manager']/following::input[1]")
            )
        )
        hiring_input.clear()

        hiring_input.send_keys(current_user_name)  # Gõ vài ký tự đầu
        sleep(10)

        # 3️⃣ Dùng ActionChains để move, select recommend
        actions = ActionChains(self.driver)
        actions.move_to_element(hiring_input)  # Di chuột tới field
        actions.click()  # Click để focus
        actions.send_keys(Keys.ARROW_DOWN)  # Chọn dòng recommend đầu tiên
        actions.send_keys(Keys.ENTER)  # Confirm chọn
        actions.perform()

        print(f"[INFO] Đã chọn Hiring Manager: {current_user_name}")

    def fill_vacancy_form(
        self,
        vacancy_name,
        job_title,
        description,
        # hiring_manager,
        num_positions,
        active,
        publish,
        webpage,
    ):
        self.driver.find_element(
            By.XPATH, "//label[text()='Vacancy Name']/following::input[1]"
        ).send_keys(vacancy_name)

        self.select_job_title(job_title)

        self.driver.find_element(
            By.XPATH, "//label[text()='Description']/following::textarea[1]"
        ).send_keys(description)

        self.fill_hiring_manager()

        self.driver.find_element(
            By.XPATH, "//label[text()='Number of Positions']/following::input[1]"
        ).clear()
        self.driver.find_element(
            By.XPATH, "//label[text()='Number of Positions']/following::input[1]"
        ).send_keys(num_positions)

        active_switch = self.driver.find_element(
            By.XPATH,
            "//p[text()='Active']/following::span[contains(@class, 'oxd-switch-input')][1]",
        )
        active_switch.click()

        publish_switch = self.driver.find_element(
            By.XPATH,
            "//p[text()='Publish in RSS Feed and Web Page']/following::span[contains(@class, 'oxd-switch-input')][1]",
        )
        publish_switch.click()

    def click_save(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
