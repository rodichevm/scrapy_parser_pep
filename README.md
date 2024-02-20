# Парсинг PEP

Проект создан на основе фреймворка Scrapy.
- Проект проводит парсинг страницы "https://peps.python.org/". 
- Сохраняет список документов PEP.
- Собирает данные о количестве и статусе документов PEP. 
- Результаты работы парсера сохраняется в csv-файлы в папку _/results_

## Технологии:
- [Python](https://www.python.org/);
- [Scrapy](https://scrapy.org/);

## Как запустить проект:

- Клонировать репозиторий
```
git clone git@github.com:rodichevm/scrapy_parser_pep.git
```

- Перейти в корневую директорию проекта /scrapy_parser_pep
```
cd scrapy_parser_pep
```

- Создать и активировать виртуальное окружение и установить зависимости
```
python -m venv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```


## Запуск парсера:

```
scrapy crawl pep
```

Автор:
[Михаил Родичев](https://github.com/rodichevm)