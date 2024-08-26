import configparser
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class LMS3_0_User:
    def __init__(self, ini_filename="credentials.ini"):
        self.ini_filename = ini_filename
        self.Acc_Pwd_Setup()

    def Acc_Pwd_Setup(self):
        if not os.path.exists(self.ini_filename):
            print(f"檔案 {self.ini_filename} 不存在。使用手動輸入模式。")
            
            # 提示使用者輸入帳號和密碼
            self.username = input("請輸入帳號: ")
            self.password = input("請輸入密碼: ")

            config = configparser.ConfigParser()
            
            # 添加 'credentials' 區塊並 裝入帳號密碼
            config['credentials'] = {
                'username': self.username,
                'password': self.password
            }

            # 將資料寫入到 ini 檔案
            with open(self.ini_filename, 'w') as configfile:
                config.write(configfile)
            
            print(f"已創建檔案 {self.ini_filename} 並儲存帳號密碼。下次不需再輸入。")

        else:
            config = configparser.ConfigParser()

            # 讀取 INI 檔案
            config.read(self.ini_filename)

            self.username = config['credentials']['username']
            self.password = config['credentials']['password']

            print(f"Username: {self.username}")
            print(f"Password: {self.password}")

class LMS_Course:

    def __init__(self, category = "",course_name="", teacher = ""):
        self.Category = category
        self.Course_Name = course_name
        self.Teacher = teacher

    def update_teacher(self, new_teacher):
        self.Teacher = new_teacher

    def __str__(self):
        return (f"Course Name: {self.Course_Name}\n"
                f"Subject: {self.Subject}\n"
                f"Teacher: {self.Teacher}")

   

class LMS3_0:

    def __init__(self, noHead: bool, LMS_User : LMS3_0_User):  #noHead 是要不要顯示出web  # User 是關於帳號密碼的
        self.User = LMS_User
        
        self.NoHead = noHead
        self.Driver = None
        self.Chrome_options = Options()
        self.Service = None
        self.Courses = []
        self.LoginPass = False

        self.SeleniumSetup()

        

    def SeleniumSetup(self):
        if self.NoHead:
            self.Chrome_options.add_argument("--headless")
            self.Chrome_options.add_argument("--disable-gpu")
            self.Chrome_options.add_argument("--no-sandbox")

        # 初始化網頁
        self.Service = Service(ChromeDriverManager().install())
        self.Driver = webdriver.Chrome(service=self.Service, options=self.Chrome_options)    

    def OpenLMSHome(self):
        # 開啟數位學院3.0
        url = "https://lms3.ntpu.edu.tw/login/index.php"
        self.Driver.get(url)

    def Login(self):
        self.OpenLMSHome()

        # 帳號密碼輸入框
        username_input = self.Driver.find_element(By.ID, "username")
        password_input = self.Driver.find_element(By.ID, "password")

        # 輸入帳號和密碼
        username_input.send_keys(self.User.username)
        password_input.send_keys(self.User.password)

        # 點擊登入按鈕
        login_button = self.Driver.find_element(By.ID, "loginbtn")
        login_button.click()
        time.sleep(5)

    def LoginCheck(self):
        page_source = self.Driver.page_source

        if "登入無效，請重試" in page_source:
            print("登入無效，請重試")
            return False
        elif "我的課程" in page_source:
            print("登入成功")
            self.LoginPass = True
            return True
        else:
            print(page_source)
            return False

    def Print_All_Course(self):
        # self.OpenLMSHome()

        # 找到我的課程 div
        div = self.Driver.find_elements(By.CSS_SELECTOR, 'div[data-region="course-view-content"]')
        text = div[0].text

        # 將文本根據 字串\n切割 
        lines = text.split('\n')
        self._parse_course_data(lines)
        self.Print_Courses()


    def _parse_course_data(self,lines): # 把 課程字串 轉換成 LMS_Course 物件

        """ 文字格式 :
        'Course image'
        'Course category'
        "開課學系"
        'Course name'
        "課程名稱"
        教師: 教師名稱
        """

        # 從字串解析課程資料
        for i in range(0, len(lines), 6):  # 每六行一組資料
            if i + 5 < len(lines):
                category = lines[i + 2]       # 開課學系
                course_name = lines[i + 4]    # 課程名稱
                teacher = lines[i + 5].replace('教師: ', '')
                course = LMS_Course(category, course_name, teacher)
                self.Courses.append(course)
                

    def Print_Courses(self):
        for course in self.Courses:
            print(f"Category: {course.Category}\nCourse Name: {course.Course_Name}\nTeacher: {course.Teacher}\n")




def main():
    user = LMS3_0_User()  
    lms = LMS3_0(noHead=False, LMS_User=user)  
    lms.Login()
    lms.LoginCheck()
    lms.Print_All_Course()
    input("按 Enter 鍵以關閉瀏覽器...")
    lms.Driver.quit()


if __name__ == "__main__":
    main()
    



