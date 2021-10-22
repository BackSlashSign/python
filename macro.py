from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
options.enable_mobile();
driver = webdriver.Chrome('chromedriver.exe', options=options)