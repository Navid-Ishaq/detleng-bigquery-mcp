from bigquery_client import BigQueryClient

client = BigQueryClient()

sql = """
SELECT COUNT(*) AS total_customers
FROM `detleng-case-studies.cs003_olist_analytics.dim_customers`
"""

result = client.execute_query(sql)

for row in result:
    print(row.total_customers)
