# 從元大官網爬蟲爬取 0050 的成分股
# 因為資料不是直接附加在 HTML，而是使用 Ajax，所以不能直接用 request 來讀取網頁資料
# 需要使用 Selenium 來模擬瀏覽器，才能讀取到我們要的資料
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def get_TW0050_stock_list():
    # ------------------ 設置 WebDriver，在有 GUI 的情況下使用 ------------------
    # driver = webdriver.Chrome()  # 使用 Chrome，也可以設定別的瀏覽器

    # ------------------ 設置在 headless 模式下瀏覽網站，這樣才可以在 Linux 純文字模式下爬蟲 ------------------
    chrome_options = Options()
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    # chrome_options.add_argument(f'user-agent={user_agent}') # 有些網站安保級別比較高，會偵測如果是 headless 模式拜訪網站就會封鎖你，可以使用 agent 騙過
    chrome_options.add_argument("window-size=1920,1080") # 設置網頁解析度，以防有些東西拿不到
    chrome_options.add_argument("--no-sandbox")  # 在無頭模式下運行時需要，網路上有人說要放在第一行，放在 --headless 下面就會出錯
    chrome_options.add_argument("--headless")  # 啟用無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    driver = webdriver.Chrome(options=chrome_options)

    # 設定要拜訪的網站
    driver.get("https://www.yuantaetfs.com/product/detail/0050/ratio")

    # 設置一個隱式等待對象
    # driver.implicitly_wait(10) # 在整個網頁等待 10 秒鐘

    # 截圖確認有爬到網站
    # driver.get_screenshot_as_file("screenshot.png") 

    # 設置一個顯示等待對象
    wait = WebDriverWait(driver, 5)

    # 展開所有股票信息
    try:
        # 這個叫做 .moreBtn 的按鈕是網頁上"展開"的按鍵，按了才可以看到所有 0050 成分股
        expand_button = driver.find_element(By.CSS_SELECTOR, ".moreBtn")
        expand_button.click()
        # 等待及確認我們有加載到這個放置成分股的 table，他叫做 each_table
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".each_table .tbody .tr")))
    except Exception as e:
        print("Error while expanding stock information or waiting for elements: ", e)
        driver.quit()
        return []

    
    TW0050_stock_list = []
    # 提取股票代碼
    rows = driver.find_elements(By.CSS_SELECTOR, ".each_table .tbody .tr")
    for row in rows:
        td_elements = row.find_elements(By.CSS_SELECTOR, '.td')
        if td_elements:
            stock_code = td_elements[0].text.strip()
            if stock_code and stock_code.isdigit():  # 確保提取到的是數字型的股票代碼
                TW0050_stock_list.append(stock_code)

    # 關閉瀏覽器
    driver.quit()

    return TW0050_stock_list

if __name__ == '__main__':
    # 使用函數
    stock_list = get_TW0050_stock_list()
    print("len(stock_list): ", len(stock_list))
    print("stock_list: ", stock_list)

