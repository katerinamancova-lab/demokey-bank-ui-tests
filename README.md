# UI автотесты демо-банка (demoqa.ru)

## 📊 Allure Report (GitHub Pages)
🔗 https://katerinamancova-lab.github.io/demokey-bank-ui-tests/

## 🧪 Стек
- Python
- Pytest
- Selenium
- Page Object Model
- Allure

## ✅ Что покрыто
- Login
- Registration
- Transfer by name
- Transfer by account

## ▶️ Как запустить проект локально
```bash
pip install -r requirements.txt
pytest --alluredir=allure-results --clean-alluredir
allure generate allure-results -o allure-report --clean
allure serve allure-report
