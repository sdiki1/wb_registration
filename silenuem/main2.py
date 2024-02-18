import time, logging, random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from DB import Accounts, engine, modems
from sqlalchemy.orm import sessionmaker
import undetected_chromedriver as uc
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
    print('try to get proxy')
    while True:
        Session = sessionmaker()
        session = Session(bind=engine)
        proxies = session.query(modems).filter(modems.Is_using.is_(False)).filter(modems.To_reboot.is_(False)).all()
        print(proxies)
        if proxies == []:
            time.sleep(10)
            continue
        prox = proxies[random.randint(0, len(proxies)-1)]
        print('done')
        prox.Is_using = True
        proxy_id = prox.Id
        proxy_ip = prox.Ip
        session.add(prox)
        session.commit()
        session.close()
        break
    print('proxy geted, wait 30sec')
    time.sleep(30)
    try:
        url = 'https://www.wildberries.ru/security/login'
        print(proxy_ip)
        print(proxy_id)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=socks5://' + proxy_ip)
        print('lol')
        with uc.Chrome(options=chrome_options) as browser:
            browser.get(url)
            time.sleep(20)
            data_number = get_number()
            browser.find_element(By.CLASS_NAME, 'input-item').send_keys(data_number['number'][2::])
            time.sleep(5)
            browser.find_element(By.ID, "requestCode").click()
            time.sleep(15)

            cpt_el = browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/form/div/div[3]/div/img')
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
            print('captcha solved')
            code = get_code(data_number['tzid'])
            while code == -1:
                code = get_code(data_number['tzid'])
                print(code)
                time.sleep(2)
            print(code)
            actions = ActionChains(browser)
            res = actions.send_keys(code)
            print(res)
            actions.perform()
            time.sleep(10)
            print('code performed')
            time.sleep(25)
            
            print("END OF REGISTRATION")
            browser.refresh()
            time.sleep(2)
            name = random_name()
            print(name)
            time.sleep(8)
            browser.find_element(By.XPATH, '//*[@id="basketContent"]/div[3]').click() # - button with personal accoumt menu
            print('open profile')
            time.sleep(8)
            browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div' ).click() # open profile menu
            time.sleep(6)
            browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/section[1]/div/div/button').click() #button to edit profile
            time.sleep(1)
            inpt = browser.find_element(By.XPATH, '//*[@id="Item.FirstName"]')
            inpt.clear()
            time.sleep(0.5)
            inpt.send_keys(name['name'])
            time.sleep(2)
            browser.find_element(By.XPATH, '/html/body/div[1]/div/form/div[1]/button').click()
            time.sleep(3)
            if name['is_man']:
                browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/ul/li[3]/div/label[1]/span[1]').click()
            else:
                browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/ul/li[3]/div/label[2]/span[3]').click()
            print("DONNE")
            time.sleep(15)
            browser.refresh()
            time.sleep(10)
            cookies = browser.get_cookies()
            print(cookies)
            print('try to get cookie wildauth')
            try:
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
                account.Is_man = name['is_man']
                account.Name = name['name']
                account.Is_using = False
                Session = sessionmaker(bind=engine)
                session = Session()
                session.add(account)
                session.commit()
                session.close()
            except Exception as E:
                print("Error with adding data to db")
    except Exception as E:
        print(f'ERROR - {E}')
        try:
            Session = sessionmaker()
            account.Is_using = False
            account.Date_active = datetime.datetime.today()
            session = Session(bind=engine)
            proxy = session.query(modems).filter(modems.Id == proxy_id).first()
            proxy.Is_using = False
            proxy.To_reboot = True
            session.add(account)
            session.add(proxy)
            session.commit()
            session.close()
        except Exception as E:
            print('error with tatata', E)
        return -1
    try:
        Session = sessionmaker()
        account.Is_using = False
        account.Date_active = datetime.datetime.today()
        session = Session(bind=engine)
        proxy = session.query(modems).filter(modems.Id == proxy_id).first()
        proxy.Is_using = False
        proxy.To_reboot = True
        session.add(account)
        session.add(proxy)
        session.commit()
        session.close()
    except Exception as E:
        print('error with tatata', E)
    print("end!")
        



# def open_site(id_ac):

#     Session = sessionmaker(bind=engine)
#     session = Session()
#     account = session.query(Accounts).filter(Accounts.Id == id_ac).first()
#     account.Is_using = True
#     session.commit()
#     account = session.query(Accounts).filter(Accounts.Id == id_ac).first()
#     session.close()
    
#     print('try to get proxy')
#     while True:
#         Session = sessionmaker()
#         session = Session(bind=engine)
#         proxies = session.query(modems).filter(modems.Is_using.is_(False)).filter(modems.To_reboot.is_(False)).all()
#         print(proxies)
#         if proxies == []:
#             time.sleep(10)
#             continue
#         prox = proxies[random.randint(0, len(proxies)-1)]
#         print('done')
#         prox.Is_using = True
#         proxy_id = prox.Id
#         proxy_ip = prox.Ip
#         session.add(prox)
#         session.commit()
#         session.close()
#         break
#     time.sleep(20)
#     try:
#         print(proxy_ip)
#         print(proxy_id)
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=socks5://' + proxy_ip)
#         print('lol')
#         with uc.Chrome(options=chrome_options) as browser:
#             url = 'https://www.wildberries.ru'
#             browser.get(url)

#             print(account)
#             cookie = {'name': 'WILDAUTHNEW_V3', 'value': account.AuthV3}
#             browser.add_cookie(cookie)
#             time.sleep(3)
#             browser.refresh()
#             time.sleep(2)
#             name = random_name()
#             print(name)
#             time.sleep(8)
#             browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[3]/a/span').click()
#             time.sleep(10)
#             browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/a').click()
#             time.sleep(6)
#             browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/div/div/button').click()
#             time.sleep(1)
#             inpt = browser.find_element(By.XPATH, '/html/body/div[1]/div/form/ul/li/input')
#             inpt.clear()
#             time.sleep(0.5)
#             inpt.send_keys(name['name'])
#             time.sleep(2)
#             browser.find_element(By.XPATH, '/html/body/div[1]/div/form/div[1]/button').click()
#             time.sleep(3)
#             if name['is_man']:
#                 browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/ul/li[2]/div/label[1]/span[1]').click()
#             else:
#                 browser.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div/section[1]/ul/li[2]/div/label[2]/span[1]').click()
            

#             account.Is_man = name['is_man']
#             account.Name = name['name']
#             account.Is_using = False
#             Session = sessionmaker(bind=engine)
#             session = Session()
#             session.add(account)
#             session.commit()
#             session.close()
#     except:
#         return open_site(id_ac=id_ac)
#     finally:
#         try:
#             Session = sessionmaker()
#             account.Is_using = False
#             account.Date_active = datetime.datetime.today()
#             session = Session(bind=engine)
#             proxy = session.query(modems).filter(modems.Id == proxy_id).first()
#             proxy.Is_using = False
#             proxy.To_reboot = True
#             session.add(account)
#             session.add(proxy)
#             session.commit()
#             session.close()
#         except Exception as E:
#             print('error with tatata', E)
#     print("end!")
        




