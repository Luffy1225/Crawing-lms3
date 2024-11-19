# Crawing-lms3 (自動化網站登入腳本)

這是一個使用 Python 和 Selenium 的自動化腳本，用於自動登入 臺北大學數位系統3.0 。

## 簡單開始

```bash
   git clone https://github.com/Luffy1225/Crawing-lms3.git
   cd Crawing-lms3
   pip install -r requirements.txt
   python main.py
```
## Install

1. 安裝：

   ```bash
   git clone https://github.com/Luffy1225/Crawing-lms3.git
   cd Crawing-lms3
   ```

1. 安裝必要的 Python 套件：

    ```bash
    pip install -r requirements.txt
    ```

3. 將 `credentials.ini` 檔案放置於與腳本相同的目錄中，或者第一次執行時根據提示輸入您的帳號和密碼。

## 使用方式
執行腳本：

```bash
python main.py
```

如果 `credentials.ini` 不存在，您將被提示輸入帳號和密碼，並且這些資訊將儲存於 `credentials.ini` 中。
如果 `credentials.ini` 存在，腳本將讀取此檔案以獲取帳號和密碼。
腳本將使用提供的帳號與密碼自動登入數位學院3.0網站。


## 常見問題
### ChromeDriver 版本不匹配
如果您遇到 `ChromeDriver` 版本不匹配的錯誤，請下載與您安裝的 Chrome 瀏覽器版本相對應的 `ChromeDriver`，或者使用 `webdriver-manager` 自動安裝適當的版本。

### 無法啟動 Chrome 瀏覽器
確保您已正確安裝 Chrome 瀏覽器並且它可以在您的系統上運行。

