
import re

def convert_to_sql(natural_query):
    patterns = {
        r"total sales for last month": "SELECT SUM(sales) AS total_sales FROM transactions",
        r"sales by product": "SELECT product, SUM(sales) AS total_sales FROM transactions GROUP BY product",
        r"latest sales transactions": "SELECT * FROM transactions ORDER BY date"
    }
    for pattern, sql in patterns.items():
        if re.search(pattern, natural_query, re.IGNORECASE):
            return sql
    return None
