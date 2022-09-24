from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import lots_db

url1 = "https://www.avito.ru/samara/avtomobili?f=ASgBAQECAkTyCrCKAeC2DaSKNAJA5rYNZIjirhDAtyjCtyjKtyjMtyjQtyjwtg007rco8rco8LcoBEX4Ahh7ImZyb20iOjIwMzAzLCJ0byI6bnVsbH2MFBZ7ImZyb20iOjExMCwidG8iOm51bGx9vhUYeyJmcm9tIjpudWxsLCJ0byI6ODAwMDB9xpoMF3siZnJvbSI6MCwidG8iOjE2MDAwMDB9&localPriority=1"


def get_lots(url):
    driver = webdriver.Chrome(executable_path='C:\\Users\\ZZnote\\Downloads\\chromedriver_win32\\chromedriver')
    i = 0
    el = '1'
    lots = []
    old_lots = lots_db.select_all()

    while el:
        if i != 0:
            driver.get(url + '&p=' + str(i) + '&radius=100')
        else:
            driver.get(url + '&radius=100')

        el = driver.find_elements(By.CLASS_NAME, 'js-catalog-item-enum')

        for e in el:
            title = e.find_element(By.TAG_NAME, 'h3').text
            desc = e.find_element(By.CLASS_NAME, 'iva-item-text-Ge6dR').text
            price = e.find_element(By.CLASS_NAME, 'price-text-_YGDY').text
            link = e.find_element(By.CLASS_NAME, 'link-link-MbQDP').get_attribute('href')

            stitle = title.split(', ')
            sprice = ''
            for g in price.replace('₽', '').split():
                sprice += g
            sdesc = desc.split(', ')
            srun = ''
            for l in sdesc[0].replace('км', '').split():
                srun += l

            cdate = time.strftime('%x')
            age = stitle[1]
            sprice = int(sprice)
            prod = stitle[0].split()[0]
            mod = ''
            for t in stitle[0].split()[1:]:
                mod += t
            run = int(srun)
            lot = [cdate, age, sprice, link, prod, mod, run]
            print(lot)
            flag = True
            for lot1 in old_lots:
                if link == lot1[4]:
                    flag = False
            if flag:
                lots.append(lot)
        i += 1
        print('End parse page: ' + str(i))

    return lots
