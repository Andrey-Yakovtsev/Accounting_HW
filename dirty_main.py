from datetime import datetime
from Application.salary import *
from Application.db.people import *


if __name__ == "__main__":

    print(datetime.now())
    calculate_salary()
    get_employees()