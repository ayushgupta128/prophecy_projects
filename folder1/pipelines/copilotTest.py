with DAG():
    copilotTest__reformat_customer_city = Task(
        task_id = "copilotTest__reformat_customer_city", 
        component = "Model", 
        modelName = "copilotTest__reformat_customer_city"
    )
