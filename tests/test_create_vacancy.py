import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from pages.vacancies_page import VacanciesPage
from pages.add_vacancy_page import AddVacancyPage
import datetime
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_create_new_vacancy(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)
    recruitment = RecruitmentPage(driver)
    vacancies = VacanciesPage(driver)
    add_vacancy = AddVacancyPage(driver)

    # Step 1: Login
    login_page.login("Admin", "admin123")

    # Step 2: Go to Recruitment > Vacancies
    dashboard.go_to_recruitment()
    recruitment.go_to_vacancies()

    # Step 3: Click "+Add"
    vacancies.click_add()

    # Step 4+5: Fill Ad Vacancy Form
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    vacancy_name = f"Automation Tester For {today}"
    job_title = "Account Assistant"  # Giả sử đây là job title có sẵn
    description = "Automation Test Is Running"
    # hiring_manager = "Paul Collings"  # Giả sử tài khoản này đang đăng nhập
    num_positions = "1"
    active = False
    publish = True
    webpage = True
    add_vacancy.fill_vacancy_form(
        vacancy_name,
        job_title,
        description,
        # hiring_manager,
        num_positions,
        active,
        publish,
        webpage,
    )

    sleep(10)

    # Step 6: Click Save
    add_vacancy.click_save()

    # # Step 7: Verify Edit Vacancy displays (giả lập: check vacancy name xuất hiện)
    # assert vacancy_name in driver.page_source

    # # Step 8: Click Cancel
    # driver.find_element_by_xpath("//button[text()='Cancel']").click()

    # # Step 9: Verify Vacancies page lại hiển thị
    # assert "Vacancies" in driver.page_source

    # # Step 10: Search lại
    # # vacancies.search_vacancy(job_title, hiring_manager)

    # # Step 11: Verify có ít nhất 1 result
    # results = driver.find_elements_by_xpath(
    #     "//div[contains(text(), '{}')]".format(vacancy_name)
    # )
    # assert len(results) > 0

    # # Step 12: Verify data trùng khớp
    # assert any(vacancy_name in r.text for r in results)

    # # Step 13: Logout
    # driver.find_element_by_xpath("//span[@class='oxd-userdropdown-tab']").click()
    # driver.find_element_by_xpath("//a[text()='Logout']").click()
