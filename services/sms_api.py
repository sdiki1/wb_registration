import requests, json
from DB import engine, SMS
from sqlalchemy.orm import sessionmaker
import time
api_onlinesim = 'j6jtkkAAmqd1CUD-V47xWP69-8Xn8wUtX-RBf85Uv5-GcrLDd2V926b5Vn'


def get_number():
    data = {"service":"wildberries","country":7,"reject":[],"number":True}
    url = f'https://onlinesim.io/api/getNum.php?apikey={api_onlinesim}'
    response = requests.post(url=url, json=data)
    data = json.loads(response.text)

    js = {
        'tzid': data['tzid'], 
        'number': data['number']
    }

    new_sms = SMS(
        Phone =js['number'][1::],
        Tzid = js['tzid']
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(new_sms)
    session.commit()
    session.close()
    
    return js



def get_code(tzid):
    url = f'https://onlinesim.io/api/getState.php?apikey={api_onlinesim}'
    data = {
    "tzid": tzid,
    "message_to_code": 1,
    "orderby": "asc",
    "msg_list": 0,
    "clean": 1,
    "lang": "ru"
    }
    try:
        resp = requests.get(url=url, json=data)
        data = json.loads(resp.text)
        print(data)
        Session = sessionmaker(bind=engine)
        session = Session()
        sms = session.query(SMS).filter(SMS.Tzid == tzid).first()
        sms.Sms = data[0]['msg']
        session.commit()
        session.close()
        return data[0]['msg']
    except:
        return -1

