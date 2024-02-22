
import os

class MainConfigs:

    URL_CONFIGS = {
        "dev": {
            "base_url": "http://localhost:8888/mysite1/"
        },
        "test": {
            "base_url": "http://demostore.supersqa.com/"

        },
        "staging": {},
        "prod": {}

    }

    DB_CONFIGS = {
        "dev": {},
        "test": {},
        "staging": {},
        "prod": {}
    }

    @staticmethod
    def get_base_url():
        base_url = os.environ.get('BASE_URL')
        if not base_url:
            env = os.environ.get('ENVIRONMENT', 'dev')
            return MainConfigs.URL_CONFIGS[env.lower()]['base_url']
        else:
            return base_url

    @staticmethod
    def get_coupon_code(filter):
        if filter.upper() == 'FREE_COUPON':
            return "ssqa100"
        elif filter.upper() == '50_OFF':
            return "JFOADIUFHADF"
        else:
            raise Exception(f"Unknown value for parameter 'filter'. filter={filter}")
        
    @staticmethod
    def get_db_configs():
        environment = os.environ.get('ENV', 'test')
        db_configs = MainConfigs.DB_CONFIGS[environment.lower()]
        DB_PORT_OVERRIDE = os.environ.get("DB_PORT_OVERRIDE")
        DB_HOST_OVERRIDE = os.environ.get("DB_HOST_OVERRIDE")
        DB_DATABASE_OVERRIDE = os.environ.get("DB_DATABASE_OVERRIDE")
        DB_TABLE_PREFIX_OVERRIDE = os.environ.get("DB_TABLE_PREFIX_OVERRIDE")

        if DB_PORT_OVERRIDE:
            db_configs['port'] = int(DB_PORT_OVERRIDE)
        if DB_HOST_OVERRIDE:
            db_configs['db_host'] = DB_HOST_OVERRIDE
        if DB_DATABASE_OVERRIDE:
            db_configs['database'] = DB_DATABASE_OVERRIDE
        if DB_TABLE_PREFIX_OVERRIDE:
            db_configs['table_prefix'] = DB_TABLE_PREFIX_OVERRIDE

        return db_configs
