{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH single_field_csv AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('p3', 'single_field_csv') }}

),

Filter_1 AS (

  SELECT * 
  
  FROM single_field_csv AS in0
  
  WHERE true

)

SELECT *

FROM Filter_1
