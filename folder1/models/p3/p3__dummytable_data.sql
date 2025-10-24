{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH dummytable_data AS (

  SELECT *
  
  FROM ayush_demos.demos.dummytable

)

SELECT *

FROM dummytable_data
