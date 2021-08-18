# from selenium import webdriver
import time 
import random
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
import json
import functools
from seleniumwire import webdriver

#Ссылки на раскрутку
urls = [
    'https://kwork.ru/website-repair/414488/dorabotayu-sayt-na-1s-bitriks',
    'https://kwork.ru/website-repair/170786/opencart-ocstore-dorabotka-i-ispravlenie',
    'https://kwork.ru/website-repair/5137308/dorabotka-sayta-na-1s-bitriks'
]

useragent = UserAgent(verify_ssl=False)
options = webdriver.ChromeOptions()

#------------Selenium mods------------

#User agent mode
options.add_argument(f"user-agent={useragent.random}")

#disable webdriver mode
options.add_argument('--disable-blink-features=AutomationControlled')

#headless mode
# options.add_argument('--headless')

#add proxy

login = 'optikremont7602'
password = '5c1a8d'

proxy_options = {
    "proxy": {
        'https': f'https://{login}:{password}@109.248.7.211:10407'
    }
}

#------------Selenium mods------------

#Рандомные имена для регистрации
names = [
    'Andrey',
    'Pavel',
    'Anton',
    'Evgeniy',
    'Artem',
    'Denis',
    'Kostya',
    'Lev',
    'Kirill',
    'Boris',
    'Vladimir',
    'Anatoliy',
    'Roman',
    'Mihail',
    'Petr',
    'Ilya',
    'Aleksey',
    'Ivan',
    'Egor'
]

#Генератор случайных чисел
def generate_num(num):
    randomlist = []
    for i in range(0, int(num)):
        n = random.randint(1,30)
        randomlist.append(str(n))

    randomstr = "".join(randomlist)

    return randomstr

def register_account(num, num2):
    
    driver = webdriver.Chrome(
        executable_path='/Users/user/Desktop/any_python_scripts/Kwork_autoreg/chromedriver', 
        options= options, seleniumwire_options= proxy_options)

    try:

        driver.get('https://kwork.ru/')
        time.sleep(random.randint(1,5))
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div[4]/ul/li[2]/a').click()
        time.sleep(random.randint(1,5))

        email = f'{random.choice(names)}{generate_num(4)}@gmail.com'
        login = f'{random.choice(names)}{generate_num(3)}'
        password = f'{random.choice(names)}{generate_num(3)}'

        #Ввод почты 
        user_email_input = driver.find_element_by_name('user_email')
        user_email_input.clear()
        user_email_input.send_keys(email)

        user_email_input.send_keys(Keys.ENTER)
        time.sleep(random.randint(1,5))

        #Ввод логина
        user_username_input = driver.find_element_by_name('user_username')
        user_username_input.clear()  
        user_username_input.send_keys(login) 
        time.sleep(random.randint(1,5))

        #Ввод пороля
        user_password_input = driver.find_element_by_name('user_password')
        user_password_input.clear()  
        user_password_input.send_keys(password)

        user_password_input.send_keys(Keys.ENTER)
        
        time.sleep(random.randint(1,5))

        with open(f'{num2}-account.txt', 'a') as f:
            f.write(email + ',' + password + '\n')
        
        print(f'{num} Зарегестрирован')

    except Exception as ex:
        print(ex)
        pass

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    amount = input ('Введите количество аккаунтов для регестрации: ')
    amount_list = [str(x) for x in range(1, int(amount) + 1)]

    #Количество окон
    p = Pool(processes=2)

    p.map(functools.partial(register_account, num2=amount), amount_list)
