with DAG():
    new_table = Task(
        task_id = "new_table", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "new_table", "sourceType" : "Table", "sourceName" : "ayush_demos.demos", "alias" : ""}
    )
    newtable = Task(
        task_id = "newtable", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "newtable", "sourceType" : "Table", "sourceName" : "ayush_demos.demos", "alias" : ""}
    )
    customer = Task(
        task_id = "customer", 
        component = "Dataset", 
        table = {"name" : "customer", "sourceType" : "Table", "sourceName" : "ayush_demos.demos"}
    )
    initial_table = Task(
        task_id = "initial_table", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "initial_table", "sourceType" : "Table", "sourceName" : "ayush_demos.demos", "alias" : ""}
    )
