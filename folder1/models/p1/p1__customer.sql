{{
  config({    
    "materialized": "table",
    "alias": "dummytable",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH demographics_unknown_format AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

)

SELECT *

FROM demographics_unknown_format
