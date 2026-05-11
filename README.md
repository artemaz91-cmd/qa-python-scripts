# QA Python Scripts

Мои учебные автотесты для тестирования API. Проект создан в рамках подготовки к Junior QA Engineer.

---

## 📁 Содержание

- `test_api.py` — первый автотест: отправляет GET-запрос к `httpbin.org` и проверяет статус 200 OK

---

## 🚀 Запуск

### 1. Установите Python
Скачайте с [официального сайта](www.python.org/downloads/) (версия 3.x). При установке **обязательно** поставьте галочку `Add Python to PATH`.

### 2. Установите библиотеку requests
Откройте командную строку (Win + R → `cmd`) и выполните:
```bash
pip install requests
```

3. Запустите тест

```bash
python test_api.py
```

Ожидаемый результат

```
Статус ответа: 200
✅ Тест пройден: статус 200 OK
Ответ сервера (первые 100 символов): {
"args": {},
"headers": {
"Accept": "*/*",
...
```

---

🛠️ Технологии

· Python 3.x
· Библиотека requests
· Git / GitHub

---

📬 Контакты

· Портфолио с баг-репортами: https://docs.google.com/document/d/1YPHoiAzl0lVpyHYyiDJK80LZquhR4sJLtOgKCxxAnFk/edit?tab=t.0
· Резюме: https://bryansk.hh.ru/resume/823c31f5ff105f5e860039ed1f644539366774,  https://talanto.work/auth/login?next=%2Faccount%2Fprofile%2F0972f967-404b-4ecb-8a49-e0c1eb1389eb%2Fedit
---

📝 О проекте

Этот проект — первый шаг в автоматизации тестирования.
Планирую расширять:

· добавить тесты на POST-запросы
· подключить pytest для структурирования тестов
· написать автотесты для Wildberries / Ozon (API)

---

Автор: Артем — начинающий QA Engineer
###Последнее обновление 11 мая 2026
