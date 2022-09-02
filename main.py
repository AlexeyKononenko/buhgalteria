from application.salary import get_money
from application.db.people import get_workers
from datetime import datetime


if __name__ == '_main_':
    print(datetime.now())
    get_money()
    get_workers()