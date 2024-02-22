

from automation.src.utilities.dbUtility import DBUtility
import random
import logging as logger

class ProductsDAO:

    def __init__(self):
        self.db_helper = DBUtility()
        self.database = self.db_helper.database
        self.table_prefix = self.db_helper.table_prefix


    def get_random_product_from_db(self, qty=1):
        """
        Gets a random product from db.
        :param qty: number of products to get
        :return:
        """

        logger.info(f"Getting random products from db. qty= {qty}")
        sql = f"""SELECT ID, post_title, post_name FROM {self.database}.{self.table_prefix}posts 
        WHERE post_type = 'product' LIMIT 500;"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_random_onsale_product_from_db(self, qty=3):
        """
        Gets a random product that is onsale from db.
        :param qty: number of products to get
        :return:
        """

        logger.info(f"Getting random products from db. qty= {qty}")
        sql = f"""SELECT product_id, onsale FROM {self.database}.{self.table_prefix}wc_product_meta_lookup
        WHERE onsale = 1 LIMIT 100;"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))
