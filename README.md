# Crawing-lms3 (自動化網站登入腳本)

這是一個使用 Python 和 Selenium 的自動化腳本，用於自動登入 臺北大學數位系統3.0 。

## 簡單開始(Yuniko)

```bash
   git clone https://github.com/Luffy1225/Crawing-lms3.git
   cd Crawing-lms3
   python Yuniko_ver.py
```


## 簡單開始

```bash
   git clone https://github.com/Luffy1225/Crawing-lms3.git
   cd Crawing-lms3
   pip install -r requirements.txt
   python main.py
```

## Requirements

在開始之前，請確保您已安裝以下工具和庫：

- Python 3.x
- pip (Python 的套件管理工具)
- Chrome 瀏覽器
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (必須與您安裝的 Chrome 版本相符)

## Install

1. 克隆此存儲庫到您的本地機器：

   ```bash
   git clone https://github.com/Luffy1225/Crawing-lms3.git
   cd Crawing-lms3
   ```

1. 安裝必要的 Python 套件：

    ```bash
    pip install -r requirements.txt
    ```

    `requirements.txt` 應包含以下內容：
    ```txt
    selenium
    webdriver-manager
    ```

3. 將 `credentials.ini` 檔案放置於與腳本相同的目錄中，或者第一次運行時根據提示輸入您的帳號和密碼。

## 使用方式
執行腳本：

```bash
python main.py
```

如果 `credentials.ini` 不存在，您將被提示輸入帳號和密碼，並且這些資訊將儲存於 `credentials.ini` 中。
如果 `credentials.ini` 存在，腳本將讀取此檔案以獲取帳號和密碼。
腳本將使用提供的憑證自動登入指定的網站。


## 常見問題
### ChromeDriver 版本不匹配
如果您遇到 `ChromeDriver` 版本不匹配的錯誤，請下載與您安裝的 Chrome 瀏覽器版本相對應的 `ChromeDriver`，或者使用 `webdriver-manager` 自動安裝適當的版本。

### 無法啟動 Chrome 瀏覽器
確保您已正確安裝 Chrome 瀏覽器並且它可以在您的系統上運行。

