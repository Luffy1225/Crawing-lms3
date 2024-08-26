import configparser
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


ini_filename = 'credentials.ini'

acc = ""
pwd = ""

# 檢查檔案是否存在
if not os.path.exists(ini_filename):
    print(f"檔案 {ini_filename} 不存在。使用手動輸入模式。")
    
    # 提示使用者輸入帳號和密碼
    acc = input("請輸入帳號: ")
    pwd = input("請輸入密碼: ")

    # 建立 ConfigParser 物件
    config = configparser.ConfigParser()
    
    # 添加 'credentials' 區塊並設定帳號密碼
    config['credentials'] = {
        'username': acc,
        'password': pwd
    }

    # 將資料寫入到 ini 檔案
    with open(ini_filename, 'w') as configfile:
        config.write(configfile)
    
    print(f"已創建檔案 {ini_filename} 並儲存帳號密碼。下次不需再輸入。")

else:
    # 建立 ConfigParser 物件
    config = configparser.ConfigParser()

    # 讀取 INI 檔案
    config.read('credentials.ini')

    # 取得帳號和密碼
    acc = config['credentials']['username']
    pwd = config['credentials']['password']

    print(f"Username: {acc}")
    print(f"Password: {pwd}")


# 設定 Chrome 為 headless 模式
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# 初始化瀏覽器
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 開啟指定的網址
url1 = "https://lms3.ntpu.edu.tw/login/index.php"

driver.get(url1)

# 找到帳號和密碼輸入框
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")



# 輸入帳號和密碼
username_input.send_keys(acc)
password_input.send_keys(pwd)

# 找到並點擊登入按鈕
login_button = driver.find_element(By.ID, "loginbtn")

login_button.click()

# 等待一段時間以便完成登入
time.sleep(5)

# 獲取頁面內容
page_source = driver.page_source


if(page_source.__contains__("登入無效，請重試")):
    print("登入無效，請重試")
elif(page_source.__contains__("曾柏碩")):
    print("登入成功")
else:
    print(page_source)


# 顯示頁面內容到終端機
# print(page_source)

# 關閉瀏覽器
driver.quit()
