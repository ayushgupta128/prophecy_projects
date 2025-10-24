{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH customer AS (

  SELECT * 
  
  FROM {{ source('ayush_demos.demos', 'customer') }}

),

reformat_customer_city AS (

  SELECT 
    customer_id AS CUSTOMER_ID,
    city AS CITY
  
  FROM customer

)

SELECT *

FROM reformat_customer_city
