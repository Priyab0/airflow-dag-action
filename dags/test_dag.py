from datetime import datetime
from airflow.models import Variable, DAG
from airflow.operators.python_operator import PythonOperator

def test_import_module():
    import prettyprint
    return True

def test_access_var():
    my_var = Variable.get("hsfjskdfjhk")
    print("my var message : {}".format(my_var))
    return ("Access Var Success!")

with DAG('test_dag',
         description='sample dag',
         schedule_interval=None,
         start_date=datetime('2021-04-01')) as dag:
    access_var = PythonOperator(
        task_id='test_access_var',
        python_callable=test_access_var,
        dag=dag
    )
    import_module = PythonOperator(
        task_id='test_import_module',
        python_callable=test_import_module,
        dag=dag
    )

    access_var >> import_module
