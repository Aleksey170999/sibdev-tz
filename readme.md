## Установка и запуск проекта:

1. Склонируйте код из репозитория к себе на компьютер
```
    git clone https://github.com/Aleksey170999/sibdev-tz.git
    
```
2. Перейдите в папку со скачанным проектом выполните команду(убедитесь, что у вас установлен docker):
```
    docker-compose up --build
```
Данная команда полностью запустит проект и выполнит миграции внутри контейнера, соберет статические файлы, запустит wsgi сервер,  а также создаст учетную запись администратора 
 на странице 127.0.0.1:8000/admin/


Данные для входа в админ-панель: admin:admin123

### Взаимодействие с API
Для отправки запросов вы можете воспользоваться библиотекой requests:
```bash
pip install requests
```


Чтобы отправить файл на обработку, сделайте post запрос c файлом в теле запроса на эндпоинт http://127.0.0.1:8000/api/v1/file/
```python
import requests

file = {'deals': open('deals.csv', 'rb')}

r = requests.post(url='http://127.0.0.1:8000/api/v1/file/', file=file)
```
Чтобы получить  5 клиентов, потративших наибольшую сумму за весь период, отправьте на тот же эндпоинт get запрос
```python
import requests

r = requests.get(url='http://127.0.0.1:8000/api/v1/file/')
print(r.json())
```
В ответ вы должны получить список клиентов подобный такому:
```json
{
   "response":[
      {
         "username":"resplendent",
         "spent_money":451731,
         "gems":[
            "Сапфир",
            "Бирюза",
            "Танзанит",
            "Жемчуг",
            "Рубин"
         ]
      },
      {
         "username":"bellwether",
         "spent_money":217794,
         "gems":[
            "Сапфир",
            "Кварц",
            "Петерсит",
            "Цаворит",
            "Опал"
         ]
      },
      {
         "username":"uvulaperfly117",
         "spent_money":120419,
         "gems":[
            "Петерсит",
            "Аметрин",
            "Танзанит",
            "Яшма",
            "Марганит"
         ]
      },
      {
         "username":"braggadocio",
         "spent_money":108957,
         "gems":[
            "Изумруд",
            "Лунный камень"
         ]
      },
      {
         "username":"turophile",
         "spent_money":100132,
         "gems":[
            "Изумруд",
            "Рубин"
         ]
      }
   ]
}
```

