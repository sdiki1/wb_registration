import time, logging, random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from DB import Accounts, engine
from sqlalchemy.orm import sessionmaker

from services.sms_api import get_code, get_number
from services import random_name
from services.solve_captcha import solve_captcha
import datetime

def generate_code():
  characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  code = random.choices(characters, k=8)
  code = ''.join(code)
  return code

def reg_account():
    try:
        url = 'https://www.wildberries.ru/security/login'
        with webdriver.Chrome() as browser:
            browser.get(url)
            time.sleep(20)
            data_number = get_number()
            browser.find_element(By.CLASS_NAME, 'input-item').send_keys(data_number['number'][2::])
            time.sleep(5)
            browser.find_element(By.ID, "requestCode").click()
            time.sleep(5)

            cpt_el = browser.find_element(By.CLASS_NAME, 'form-block__captcha-img')
            time.sleep(5)
            hash_name = generate_code()
            cpt_el.screenshot(f'captcha.png')
            res = solve_captcha(f'captcha.png')
            while res == -1:
                print('ERR capthca')
                res = solve_captcha(f'captcha.png')
                time.sleep(2)
            print(f'CAPTCHA {hash_name} - {res}')
            input_captcha_res = browser.find_element(By.ID, 'smsCaptchaCode').send_keys(res)
            time.sleep(25)

            code = get_code(data_number['tzid'])
            while code == -1:
                code = get_code(data_number['tzid'])
                print(code)
                time.sleep(2)
            print(code)
            # input_sms_code = browser.find_elements(By.CLASS_NAME, 'input-item')
            # print(input_sms_code)
            # print('\n\n\n')
            # time.sleep(10)
            # # print(input_sms_code)
            # input_sms_code[0].click()
            # print('button clicked)')
            actions = ActionChains(browser)
            res = actions.send_keys(code)
            print(res)
            actions.perform()
            time.sleep(6)
            browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[3]/a').click()
            # time.sleep(5)
            # browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div')

            cookies = browser.get_cookies()
            for i in cookies:
                if i['name'] == 'WILDAUTHNEW_V3':
                    auth_V3 = i['value']
            new_account = Accounts(
                AuthV3 = auth_V3,
                Date_active = datetime.datetime.now(),
                Is_using = False
            )
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(new_account)
            session.commit()
            account = session.query(Accounts).filter(Accounts.AuthV3 == auth_V3).first()
            session.close()
            print("END OF REGISTRATION")
            browser.close()
            return account.Id
    except Exception as E:
        print(f'ERROR - {E}')
        return reg_account()
            



def open_site(id_ac):

    Session = sessionmaker(bind=engine)
    session = Session()
    account = session.query(Accounts).filter(Accounts.Id == id_ac).first()
    account.Is_using = True
    session.commit()
    account = session.query(Accounts).filter(Accounts.Id == id_ac).first()
    session.close()
    
    with webdriver.Chrome() as browser:
        url = 'https://www.wildberries.ru'
        browser.get(url)

        print(account)
        cookie = {'name': 'WILDAUTHNEW_V3', 'value': account.AuthV3}
        browser.add_cookie(cookie)
        time.sleep(3)
        browser.refresh()
        time.sleep(2)
        name = random_name()
        print(name)
        time.sleep(8)
        browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[3]/a/span').click()
        time.sleep(10)
        browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/a').click()
        time.sleep(6)
        browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/div/div/button').click()
        time.sleep(1)
        inpt = browser.find_element(By.XPATH, '/html/body/div[1]/div/form/ul/li/input')
        inpt.clear()
        time.sleep(0.5)
        inpt.send_keys(name['name'])
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/form/div[1]/button').click()
        time.sleep(3)
        if name['is_man']:
            browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/ul/li[2]/div/label[1]/span[1]').click()
        else:
            browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/ul/li[2]/div/label[2]/span[1]').click()
        

        account.Is_man = name['is_man']
        account.Name = name['name']
        account.Is_using = False
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(account)
        session.commit()
        session.close()
        




