-- E-Commerce Return Intelligence
-- SQL Analysis


-- 1. Total number of orders

SELECT COUNT(*) AS total_orders
FROM ecommerce_data;


-- 2. Total returned orders

SELECT COUNT(returned) AS returned_order
FROM ecommerce_data
WHERE returned = 1;


-- 3. Overall return rate

SELECT AVG(returned) * 100 AS return_rate
FROM ecommerce_data;


-- 4. Return rate by product category

SELECT 
    product_category,
    AVG(returned) * 100 AS return_rate
FROM ecommerce_data
GROUP BY product_category;


-- 5. Orders and return rate by product category

SELECT 
    product_category,
    COUNT(*) AS total_orders,
    AVG(returned) * 100 AS return_rate
FROM ecommerce_data
GROUP BY product_category;


-- 6. Return rate by past purchase count

SELECT 
    past_purchase_count,
    AVG(returned) * 100 AS return_rate,
    COUNT(*) AS total_orders
FROM ecommerce_data
GROUP BY past_purchase_count;


-- 7. Return rate by shipping method

SELECT 
    shipping_method,
    AVG(returned) * 100 AS return_rate
FROM ecommerce_data
GROUP BY shipping_method;


-- 8. Return rate by payment method

SELECT 
    payment_method,
    AVG(returned) * 100 AS return_rate
FROM ecommerce_data
GROUP BY payment_method;


-- 9. Return rate by coupon usage

SELECT 
    used_coupon,
    AVG(returned) * 100 AS return_rate
FROM ecommerce_data
GROUP BY used_coupon;


-- 10. Return rate by delivery condition

SELECT
    COUNT(*) AS total_orders,
    AVG(returned) * 100 AS return_rate,
    CASE
        WHEN delivery_delay_days < 0 THEN 'early_delivery'
        WHEN delivery_delay_days = 0 THEN 'on_time'
        WHEN delivery_delay_days > 0 THEN 'late_delivery'
    END AS delivery_condition
FROM ecommerce_data
GROUP BY
    CASE
        WHEN delivery_delay_days < 0 THEN 'early_delivery'
        WHEN delivery_delay_days = 0 THEN 'on_time'
        WHEN delivery_delay_days > 0 THEN 'late_delivery'
    END;


-- 11. Average product price for returned and non-returned orders

SELECT 
    AVG(product_price) AS average_product_price,
    returned
FROM ecommerce_data
GROUP BY returned;


-- 12. Average product price by category

SELECT 
    AVG(product_price) AS average_product_price,
    product_category
FROM ecommerce_data
GROUP BY product_category;


-- 13. Highest average product price by payment method

SELECT 
    AVG(product_price) AS average_product_price,
    payment_method
FROM ecommerce_data
GROUP BY payment_method
ORDER BY average_product_price DESC;


-- 14. Create price groups

SELECT
    CASE
        WHEN product_price < 25 THEN 'low_price'
        WHEN product_price >= 25 AND product_price < 100 THEN 'medium_price'
        WHEN product_price >= 100 THEN 'high_price'
    END AS price_group,
    COUNT(*) AS total_orders
FROM ecommerce_data
GROUP BY
    CASE
        WHEN product_price < 25 THEN 'low_price'
        WHEN product_price >= 25 AND product_price < 100 THEN 'medium_price'
        WHEN product_price >= 100 THEN 'high_price'
    END;


-- 15. Orders between age 18 and 25 who used a coupon

SELECT COUNT(*) AS total_order
FROM ecommerce_data
WHERE customer_age > 18
AND customer_age < 25
AND used_coupon = 1;


-- 16. Number of different product categories

SELECT COUNT(DISTINCT product_category) AS total_product
FROM ecommerce_data;


-- 17. Check missing product prices

SELECT COUNT(*) AS missing_product_price
FROM ecommerce_data
WHERE product_price IS NULL;


-- 18. Check negative product prices

SELECT COUNT(*)
FROM ecommerce_data
WHERE product_price < 0;


-- 19. Replace invalid negative product prices with NULL

UPDATE ecommerce_data
SET product_price = NULL
WHERE product_price < 0;


-- 20. Category-wise orders, returned orders and return rate

SELECT 
    product_category,
    COUNT(*) AS total_orders,
    SUM(returned) AS returned_order,
    AVG(returned) * 100 AS return_rate
FROM ecommerce_data
GROUP BY product_category;
