init_select_queries = '''
select product_id
from products final
where brand_id = 77;
'''


# init_select_queries = '''
# select product_id
# from products final
#          join remainders final using (product_id)
# where updated = today() and date = today()-1;
# '''

my_select_queries = '''
select product_id
from products
where product_id IN (
select product_id 
from remainders 
where date = yesterday;
) 
where updated = today();
'''
'''
1) Для первой причины достаточно базового знания чистого SQL (алгоритм фильтрации)


2) Для второй причины достаточно знания отличия SQL JOIN от IN  

Каждый раз для выполнения запроса с одинаковым JOIN, подзапрос выполняется заново — результат не кэшируется. правая 
    таблица читается заново при каждом запросе. Поэтому используем вложенный запрос и IN
    
3)  Для третьей причины требуется прочитать про ReplacingMergeTree и про final (15 минут чтения официальной документации
 по Clickhouse)
 
Запросы, которые используют FINAL выполняются немного медленее, чем аналогичные запросы без него, потому что:

Данные мёржатся во время выполнения запроса в памяти, и это не приводит к физическому мёржу кусков на дисках.
Запросы с модификатором FINAL читают столбцы первичного ключа в дополнение к столбцам, используемым в запросе.
В большинстве случаев избегайте использования FINAL.
 
'''
