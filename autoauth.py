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
    'https://kwork.ru/website-repair/5137308/dorabotka-sayta-na-1s-bitriks',
    'https://kwork.ru/website-repair/14367911/dorabotka-saytov',
    'https://kwork.ru/website-repair/1541177/dorabotka-sayta-wordpress',
    'https://kwork.ru/website-repair/1869119/dorabotka-wordpress-lyubie-pravki-i-reshenie-problem-sayta',
    'https://kwork.ru/website-repair/4386/lyubaya-pravka-sayta',
    'https://kwork.ru/website-repair/121689/raboty-na-vashem-sayte',
    'https://kwork.ru/website-repair/215833/ispravlyu-ili-dorabotayu-rasshireniya-dlya-joomla-3-kh',
    'https://kwork.ru/website-repair/5934118/opencart-dorabotki-ispravlenie-oshibok'
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

login = ''
password = ''

proxy_options = {
    "proxy": {
        'https': f'https://{login}:{password}@109.248.7.211:10407'
    }
}

#------------Selenium mods------------


def auth_account(user_data):
    
    user_data = user_data.split(',')

    driver = webdriver.Chrome(
        executable_path='/Users/user/Desktop/any_python_scripts/Kwork_autoreg/chromedriver', 
        seleniumwire_options=proxy_options, options = options)

    try:

        driver.get('https://kwork.ru/')
        time.sleep(random.randint(1,5))
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div[4]/ul/li[1]/a').click()
        time.sleep(random.randint(1,5))


        #Ввод почты 
        user_email_input = driver.find_element_by_name('l_username')
        user_email_input.clear()
        user_email_input.send_keys(user_data[0])

        time.sleep(random.randint(1,5))

        #Ввод пороля
        user_password_input = driver.find_element_by_name('l_password')
        user_password_input.clear()
        user_password_input.send_keys(user_data[1])

        user_password_input.send_keys(Keys.ENTER)
        
        for i in urls:
            driver.get(i)
            time.sleep(random.randint(1,5))

        print(type(user_data))

    except Exception as ex:
        print(ex)
        pass

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    file_name = input ('Введите название файла: ')

    with open(file_name, 'r') as f:
        user_list = [x.rstrip() for x in f.readlines()]

    #Количество окон
    p = Pool(processes=2)
    p.map(auth_account, user_list)

