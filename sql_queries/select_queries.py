init_select_queries = '''
select product_id
from products final
         join remainders final using (product_id)
where updated = today() and date = today()-1;
'''