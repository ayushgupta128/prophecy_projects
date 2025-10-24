{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH empty_output AS (

  SELECT * 
  
  FROM {{ source('ayush_demos.demos', 'customer') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM empty_output AS in0

)

SELECT *

FROM Reformat_1
