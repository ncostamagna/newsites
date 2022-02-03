from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

search="cambio climatico"
year="2019"

driver = webdriver.Chrome()
driver.get("https://www.pagina12.com.ar/buscar?q={}".format(search))

try:
    b = driver.find_elements_by_class_name("read-more-loader")
    driver.implicitly_wait(30) # seconds
    time.sleep(3)
    for i in range(5):
        if len(b) > 0:
            b[0].click()
            driver.implicitly_wait(10) # seconds
            time.sleep(1)

    a = driver.find_elements_by_class_name("article-box__container")

    for aa in a:
        d = aa.find_elements_by_class_name("date-1")
        
        link = aa.find_element_by_tag_name('a')
        url = link.get_attribute('href')

        for dd in d:
            if dd.text[-4:] == year or year == "":
                print(dd.text[-4:])
                print(url)

except TypeError as err:
    print(err)
except:
    print(sys.exc_info())
finally:
    driver.quit()
