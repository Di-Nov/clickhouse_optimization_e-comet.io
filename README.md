# <img src="https://hh.ru/employer-logo/3910308.png" style="object-fit: cover; width:3%;" > [e-Comet](https://e-comet.io/ "ссылка на сайт")

> Тестовое задание для компании "e-Comet"

## Содержание

* [Тестовое задание](#test)
* [Технологии](#teh)
* [Использование](#use)
* [Установка](#t)
* [Выводы](#conclusions)
* [Feedback](#feedback)
* [Команда проекта](#team)

## <h3 id="test">Тестовое задание</h3>

1) Python. Функция трансформации T(n: int) -> int выполняется 5 минут. N - список типа int. Требуется вернуть список
   положительных трансформированных значений N. Предложи решение, которое удовлетворяет следующим критериям:

- в одну строчку
- эффективно с точки зрения времени выполнения
- не использует map()

2) Clickhouse - это крутая высокопроизводительная БД для анализа больших данных. С ней имеет смысл познакомиться, даже
   если
   ты про нее ранее не слышал.

Даны две таблицы в Clickhouse, в каждой из которых по 100 млн+ строк и возможны дубликаты. Каждый день обновляется около
1 млн продуктов (то есть на 2 порядка меньше, чем строк в таблице).

``` SQL
CREATE TABLE (
    product_id   Int32,
    product_name String,
    brand_id     Int32,
    seller_id    Int32,
    updated      Date
)
    ENGINE = ReplacingMergeTree
    ORDER BY product_id;
```

``` SQL
CREATE TABLE    (
    date       Date,
    product_id Int32,
    remainder  Int32,
    price      Int32,
    discount   Int32,
    pics       Int32,
    rating     Int32,
    reviews    Int32,
    new        Bool
)
    ENGINE = ReplacingMergeTree
    ORDER BY (date, product_id);
```

Напиши 3 причины, по которым следующий запрос выполняется медленно (5 секунд) и предложи быструю версию запроса (<0.1
секунды :), без изменений архитектуры таблиц (не надо предлагать "добавить индексы") и дающую такой же результат (без
дубликатов):

``` SQL
SELECT product_id
FROM products FINAL 
JOIN remainders FINAL USING(product_id) 
WHERE updated=today() AND date=today()-1
```

Несколько хинтов:

1. Для первой причины достаточно базового знания чистого SQL (алгоритм фильтрации)
2. Для второй причины достаточно знания отличия SQL JOIN от IN
3. Для третьей причины требуется прочитать про ReplacingMergeTree и про final (15 минут чтения официальной документации
   по Clickhouse)
4. Нейронка или авто-оптимизаторы SQL тут не помогут. Мы хотим проверить НЕ навык промт-энжиниринга, а твою способность
   думать и разбираться в новых вещах. Не словом ("Могу быстро разобраться с чем угодно... но не сейчас"), а делом ;)

## <h3 id="teh">Технологии</h3>

+ docker
+ clickhouse
+ python = 3.11
+ python-dotenv = 1.0.1
+ faker = 25.9.1
+ clickhouse-driver = 0.2.8

## <h3 id="use">Использование</h3>

1) В пакете [python_script_to_first_task](python_script_to_first_task) можно посмотреть и запустить решение для первого
   задания. Надеюсь задание понял верно.
2) В пакете [optimization_sql_for_clickhouse](optimization_sql_for_clickhouse) можно посмотреть и запустить решение для
   пторого задания. При помощи контейнеров докер мы запускаем СУБД clickhouse и после его запуска, запусускается
   контейнер load_data, который создаст таблицы products и remainders.
   После создания таблиц load_data создаст тестовые данные и загрузит их в эти таблицы. Нужно подождать окончания
   создания и загрузки данных. Для остановки загрузки данных нажмите CTRL+C

## <h3 id="t">Установка</h3>

* Скопировать приложение к себе локально git clone https://github.com/Di-Nov/clickhouse_optimization_e-comet.io-.git
* Замените файлы .env.template и .env.dockerfile на .env, изменив переменные окружения
* Запустить `make up-ch` (Данной командой запускется база clickhouse)
* Запустить `make up-ld` (создаются таблицы и загружаются тестовые данные)
* Джем окончания загрузки тестовых данных 4 минуты (load_data exited with code 0)
* Прописать в терминале  `docker exec -it clickhouse clickhouse-client` (Заходим в контейнер clickhouse)
* Выполнить базовый запрос в терминале:

``` SQL
SELECT product_id
FROM products FINAL 
JOIN remainders FINAL USING(product_id) 
WHERE updated=today() AND date=today()-1
```

У меня получился такой результат, у Вас может быть другой, так как тестовые данные разные.
![img.png](optimization_sql_for_clickhouse/images/img2.png)

* Выполняем оптимизированный запрос:

``` SQL
SELECT product_id
FROM products FINAL
WHERE product_id IN (
    SELECT product_id
    FROM remainders
    WHERE date = yesterday()
) AND updated = today();
```

Запрос выполнился значительно быстрее. При бо'льших объемах данных разница в скорости выполнения увеличивается.
![img.png](optimization_sql_for_clickhouse/images/img3.png)

## <h3 id="conclusions">Выводы</h3>

#### Функция трансормации.

Предположу что тут можно использовать list comprehension. На примере
приложения [func.py](python_script_to_first_task%2Ffunc.py) можно увидеть что данное решение выполняется быстрее
встроенной фильтрации filter и преобразования map, при использовании lambda функции

![img.png](optimization_sql_for_clickhouse/images/img.png)

#### Оптимизация SQL в clickhouse.

1) при выполнении запроса происходит полное объединение таблиц по product_id, а затем фильтрация результатов.
   Значит при большом количестве строк, все они будут объединяться до фильтрации

2) Каждый раз для выполнения запроса с одинаковым JOIN, подзапрос выполняется заново — результат не кэшируется. правая
   таблица читается заново при каждом запросе. Поэтому используем вложенный запрос и IN.
   Так как clickhouse столбцовая СУБД, нам не нужна информация из других столбцов, достаточно только product_id

3) По информации из документации, запросы, которые используют FINAL выполняются немного медленнее, чем аналогичные
   запросы без него, потому что:

Данные мёржатся во время выполнения запроса в памяти, и это не приводит к физическому мёржу кусков на дисках.
Запросы с модификатором FINAL читают столбцы первичного ключа в дополнение к столбцам, используемым в запросе.
В большинстве случаев избегайте использования FINAL.

- Данные мёржатся во время выполнения запроса в памяти, и это не приводит к физическому мёржу кусков на дисках.
- Запросы с модификатором FINAL читают столбцы первичного ключа в дополнение к столбцам, используемым в запросе.
  В большинстве случаев следует избегать использования FINAL. На тестовой БД запрос выполнился значительно быстрее

## <h3 id="feedback">Обратная связь</h3>

Вы можете дать обратную связь, если у вас будут предложение по улучшению проекта или информация по его дополнению.
Связь по почте novozhilov812@gmail.com или рассмотреть
мою [анкету на hh](https://spb.hh.ru/resume/470b7c08ff0be7838d0039ed1f594f75313234 "ссылка на HH")

## <h3 id="team">Команда проекта</h3>

Новожилов Дмитрий — Backend Developer <br>
novozhilov812@gmail.com
