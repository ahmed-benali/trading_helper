from selenium import webdriver
PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://finance.yahoo.com/most-active")

symbols_list = []

for index in range(5):
    index = index + 1
    symbols = driver.find_element_by_xpath(
        "//tr[contains(@class, 'simpTblRow')]{}/td[contains(@class, 'Va(m) Ta(start)')][1]"
        .format("[{}]".format(index) if index else ""))
    symbols_list.append(str(symbols.text))

driver.quit()
    ##print(str(symbols.text))

