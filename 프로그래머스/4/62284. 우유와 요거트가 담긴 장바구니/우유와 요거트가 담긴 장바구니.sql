-- 코드를 입력하세요
SELECT DISTINCT cart_id
from cart_products
where name = 'Milk' AND
    cart_id IN
(
    select cart_id
    from cart_products
    where name = 'Yogurt'
)
order by cart_id