import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    # Thiết lập ChromeOptions nếu cần (ví dụ: headless, disable notifications, ...)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Bật dòng này nếu muốn chạy headless
    options.add_argument("--window-size=1920,1080")
    # Khởi tạo WebDriver
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Chờ tối đa 10s cho các phần tử xuất hiện

    yield driver

    # Đóng browser sau khi chạy xong test
    driver.quit()


@pytest.fixture(scope="session")
def credentials():
    # Thông tin đăng nhập demo OrangeHRM (hoặc dùng biến môi trường cho thực tế)
    return {"username": "Admin", "password": "admin123"}
