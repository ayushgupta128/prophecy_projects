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

Reformat_1 AS (

  SELECT * 
  
  FROM customer AS in0

),

Limit_1 AS (

  SELECT * 
  
  FROM Reformat_1 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
