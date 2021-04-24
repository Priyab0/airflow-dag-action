# Airflow-Dag-Validation-Action

Validate DAGs file, var and dependencies before deployment to Apache Airflow.

### Using Action Inputs
```yml
- name: 'Validate DAGs'
  uses: Priyab0/airflow-dag-action@v0.1
    with:
      requirementsFile: requirements.txt
      dagPaths: dags
      varFile: var.json
```
