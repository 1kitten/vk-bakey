# Кондитерская "Bakey"
🤖 VK Бот для сообщества Кондитерской.

# Команды бота

* <code>Начать/Старт</code> - Вывод списка разделов кондитерской.

После вывода списка разделов, пользователю будет доступна клавиатура с наименованием конкретного раздела. <br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/112726662/218732533-5efe61e7-33b8-4d32-a9df-f6ea551972b5.png"/>
</div>

В каждом разделе находится по 2 товара. Просмотреть которые можно по нажатию кнопки с наименованием раздела. <br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/112726662/218733781-8498179b-70ce-4f1e-ae76-e9ea2453f52a.png" />
</div>

После вывода товаров в нужном разделе. Пользователю будет доступна кнопка "Назад" для возврата к меню со списком разделов.

<div align="center">
  <img src="https://user-images.githubusercontent.com/112726662/218745169-8f2a0708-8176-4eed-a4e6-9ea67a52d898.png" />
</div>

# Установка и запуск

Создайте файл <code>.env</code> и заполните в нём переменные окружения.<br>
Пример заполнения находится в файле <code>.env_template</code>

Запустить бота можно как через Docker-контейнер, так и вручную<br>
Для запуска через Docker. Необходимо создать docker image командой:
```bash
docker build -t vk_bot .
```
После чего запустить контейнер командой:
```bash
docker run vk_bot
```

# Запуск вручную

Если по какой-то причине нет возможности запустить бота через Docker-контейнер. Можно воспользоваться ручным запуском.<br>
Для этого необходимо создать новое виртуальное окружение в папке проекта командой: <br>
<b>Windows:</b>
```bash
python -m venv venv
```
<b>macOS/Linux:</b>
```bash
python3 -m virtualenv -p python3 venv
```

Активировать виртуальное окружение командой:<br>
<b>Windows:</b>
```bash
.\venv\Scripts\activate
```
<b>macOS/Linux</b>
```bash
source venv/bin/activate
```

Установить все зависимости командой:
```bash
pip install -r requirements.txt
```

Запустить бота командой
```bash
python vk_bot/bot.py
```

# Использованный стек

vkwave, python 3.10
