{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH student_records AS (

  SELECT *
  
  FROM students

)

SELECT *

FROM student_records
