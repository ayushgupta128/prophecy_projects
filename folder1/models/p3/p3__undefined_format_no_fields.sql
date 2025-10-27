{{
  config({    
    "materialized": "table",
    "alias": "complexdata",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH empty_output_1 AS (

  SELECT * 
  
  FROM {{ source('ayush_demos.demos', 'json_array_data') }}

)

SELECT *

FROM empty_output_1
