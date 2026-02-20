# UI Test Automation — Demo Bank

Проект по автоматизации UI-тестирования демо-банковского веб-приложения.  
Демонстрирует практические навыки написания автотестов с использованием **Selenium**, **Pytest** и **Page Object Model**.

📊 **Allure-отчёт (GitHub Pages)**  
🔗 https://katerinamancova-lab.github.io/demokey-bank-ui-tests/

---

## 🧪 Стек технологий

- Python  
- Pytest  
- Selenium WebDriver  
- Page Object Model (POM)  
- Allure Reports  
- Git / GitHub  
- GitHub Actions (CI)

---

## ✅ Покрытие автотестами

- Авторизация пользователя (Login)
- Регистрация нового пользователя (Registration)
- Денежные переводы:
  - по имени пользователя
  - по номеру счёта
- Проверка позитивных и негативных сценариев
- Проверка сообщений об ошибках

---

## 🔁 CI / GitHub Actions

В проекте настроен CI с использованием GitHub Actions.

Workflow автоматически запускается при каждом push в ветку `main` и выполняет:
- установку зависимостей
- запуск тестов через pytest

⚠️ UI-тесты используют Selenium и требуют браузерного окружения.  
В headless-среде GitHub Actions тесты могут завершаться с ошибкой, что является ожидаемым поведением для UI-автоматизации.

CI используется для демонстрации навыков настройки пайплайна и автоматического запуска тестов.

Конфигурация CI находится в файле:

.github/workflows/tests.yml


> UI-тесты с браузером в основном запускаются локально.  
> CI используется для проверки стабильности проекта и автотестов.

---

## ▶ Запуск проекта локально

### Установка зависимостей

```bash
pip install -r requirements.txt
Запуск автотестов с генерацией Allure-результатов
pytest --alluredir=allure-results --clean-alluredir
Просмотр Allure-отчёта
allure generate allure-results -o allure-report --clean
allure serve allure-report
📌 Примечания
Проект создан в учебных и демонстрационных целях

Все тесты реализованы с использованием Page Object Model

Для отчётности используется Allure

CI настроен через GitHub Actions

👩‍💻 Автор
Екатерина Манькова
QA Automation Engineer (Junior)

🔗 GitHub:
https://github.com/katerinamancova-lab