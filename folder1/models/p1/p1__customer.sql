{{
  config({    
    "materialized": "table",
    "alias": "test",
    "database": "ayush_demos",
    "schema": "demos_demos"
  })
}}

WITH demographics_unknown_format AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

)

SELECT *

FROM demographics_unknown_format
