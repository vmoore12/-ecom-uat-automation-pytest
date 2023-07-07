
from  ecom_uat_automation_pytest.automation.src.utilities.dbUtility import DBUtility
import random

class CustomersDAO:

    def __init__(self):
        self.db_helper = DBUtility()
        self.database = self.db_helper.database
        self.table_prefix = self.db_helper.table_prefix
        
    def get_customer_by_email(self, email):
        sql = f"""SELECT * FROM {self.database}.{self.table_prefix}users 
                  WHERE user_email = '{email}';"""

        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql


    def get_random_customer_from_db(self, qty=1):

        sql = f"""SELECT user_email FROM {self.database}.{self.table_prefix}users
                  ORDER BY RAND() LIMIT 100;"""
        
        rs_sql = self.db_helper.execute_select(sql) # gets a list of random customers from the database
        
        return random.sample(rs_sql, int(qty)) # selects and returns a random customer email from the db
    def get_all_customers_from_db(self):
        sql= f"""SELECT * FROM {self.database}.{self.table_prefix}users;"""

        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql
    

    