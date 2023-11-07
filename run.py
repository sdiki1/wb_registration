import time
from services.sms_api import get_number, get_code
from silenuem.main import reg_account, open_site
from threading import Thread as th

def run_one():
    id_acc = reg_account()
    open_site(id_acc)
    print('REG is ready')

def run_all():
    for j in range(10):
        for i in range(3):
            th(target=run_one).start()
            print(f'{i} - run')
            time.sleep(50)
        time.sleep(500)
    
run_all()