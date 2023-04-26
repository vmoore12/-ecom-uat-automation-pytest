
import os

class MainConfigs:

    URL_CONFIGS = {
        "dev": {
            "base_url": "http://dev.localhost.8888/quicksite/"
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
            env = os.environ.get('ENVIRONMENT', 'test')
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