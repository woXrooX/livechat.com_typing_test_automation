import time
from selenium import webdriver

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.livechat.com/typing-speed-test/#/")

# w8 till page loads / in my case 1s is enough
time.sleep(1)

# bigger is slower
typing_speed = 1.3

while True:
    time.sleep(typing_speed)

    word = browser.find_element_by_css_selector("#app > div > div.o-container > div:nth-child(2) > div > span > div.u-Py-lg.md\\:u-Py-xl > span > div > div.tst-input > div:nth-child(2) > span:nth-child(1)").text
    browser.find_element_by_css_selector("#test-input").send_keys(word+" ")

    try:
        browser.find_element_by_css_selector("#app > div > div.o-container > span > div > div > div > div")
        break
    except Exception as e:
        pass


input("Enter anything to quit: ")
browser.quit()
