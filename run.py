import time
from services.sms_api import get_number, get_code
from silenuem.main2 import reg_account
from threading import Thread as th

def run_one():
    id_acc = reg_account()
    print('REG is ready')

def run_all():
    for i in range(30):
        th(target=reg_account).start()
        time.sleep(120)
reg_account()
# run_all()