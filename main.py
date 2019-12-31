# todo pytest, make it easier to run by using args from command line, implement test plans, more explicit waits, do the By

import pytest
import logging

logging.basicConfig(filename='./logs/log.log',
                    filemode='w',
                    format="%(asctime)s | %(levelname)s | %(message)s",
                    level=logging.INFO)

pytest.main()
