# UI Test Automation — Demo Bank

UI автотесты для демо-банковского приложения (demoqa.ru).
Проект демонстрирует навыки автоматизации UI-тестирования с использованием Selenium и Pytest.

📊 Allure Report (GitHub Pages)  
🔗 https://katerinamancova-lab.github.io/demokey-bank-ui-tests/

---

## 🧪 Tech Stack
- Python
- Pytest
- Selenium
- Page Object Model (POM)
- Allure

---

## ✅ Test Coverage
- Login
- Registration
- Transfer by user name
- Transfer by account number

---

## ▶ Run tests locally

Install dependencies:
```bash
pip install -r requirements.txt

Run tests:

pytest --alluredir=allure-results --clean-alluredir

Generate Allure report:

allure generate allure-results -o allure-report --clean
allure serve allure-report

📌 Notes

The project is built for demonstration and learning purposes.
All tests are written using Page Object Model and include reporting via Allure.