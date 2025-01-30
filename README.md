# Get_0050TW

This repository contains a Python script to **fetch the latest fifty shares** included in **0050.TW** from Yuanta's official website.

0050.TW is a **Taiwan Top 50 ETF** (Yuanta Taiwan 50 ETF), tracking the performance of the top 50 stocks on the Taiwan Stock Exchange. This script automates the process of retrieving its constituent stocks using **web scraping**.

---

## 🚀 **Features**
- **Automated data extraction** from Yuanta's official ETF website.
- Uses **Selenium** to simulate browser interactions.
- Runs in both **headless mode** (for Linux servers) and **GUI mode**.
- Handles dynamic content loaded via **Ajax**, which cannot be scraped using simple HTTP requests.

---

## 📋 **Requirements**

Before running the script, ensure that you have installed the following:

### **Python Packages:**
```bash
pip install selenium
```

### **WebDriver:**
The script requires **Google Chrome** and the **ChromeDriver** to function correctly.

1. Install Google Chrome:
   - Ubuntu:  
     ```bash
     sudo apt update
     sudo apt install google-chrome-stable
     ```
   - macOS (using Homebrew):  
     ```bash
     brew install --cask google-chrome
     ```

2. Install ChromeDriver:
   - Download ChromeDriver from: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
   - Ensure the ChromeDriver version matches your installed Chrome browser version.
   - Add the ChromeDriver executable to your system PATH.

---

## 📦 **How to Run**

Clone the repository and run the script:

```bash
git clone https://github.com/your-username/Get_0050TW.git
cd Get_0050TW
python get_0050TW.py
```

The script will:
- Visit Yuanta's official website for **0050.TW**.
- Expand the stock information section.
- Extract the **stock codes** from the dynamically loaded content.

If successful, the output will look like this:

```text
len(stock_list):  50
stock_list:  ['2330', '2317', '2454', '2308', '2412', ... ]
```

---

## 🛠 **Customizing the Script**

You can customize or modify the following options in the script:

1. **WebDriver Setup:**
   - Uncomment and use the `webdriver.Chrome()` line to run the script with a GUI browser.
   - Modify the `chrome_options` to adjust **headless mode** and browser behavior.

   Example (headless mode):
   ```python
   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
   driver = webdriver.Chrome(options=chrome_options)
   ```

2. **Wait Time:**
   - Adjust the **implicit** and **explicit wait times** to handle network latency and dynamic content loading.

   ```python
   wait = WebDriverWait(driver, 5)
   ```

3. **Target URL:**
   - The script currently targets **Yuanta’s ETF page for 0050.TW**.
   ```python
   driver.get("https://www.yuantaetfs.com/product/detail/0050/ratio")
   ```
   - To scrape other ETFs, modify this URL.

---

## 🔍 **Script Walkthrough**

### **Imports**
The script uses Selenium for web scraping:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

### **Function Definition**
```python
def get_TW0050_stock_list():
    # Setup headless browser options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the target URL
    driver.get("https://www.yuantaetfs.com/product/detail/0050/ratio")

    # Expand the stock list
    expand_button = driver.find_element(By.CSS_SELECTOR, ".moreBtn")
    expand_button.click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".each_table .tbody .tr")))

    # Extract stock codes
    TW0050_stock_list = []
    rows = driver.find_elements(By.CSS_SELECTOR, ".each_table .tbody .tr")
    for row in rows:
        td_elements = row.find_elements(By.CSS_SELECTOR, '.td')
        if td_elements:
            stock_code = td_elements[0].text.strip()
            if stock_code and stock_code.isdigit():
                TW0050_stock_list.append(stock_code)

    driver.quit()
    return TW0050_stock_list
```

### **Main Execution**
```python
if __name__ == '__main__':
    stock_list = get_TW0050_stock_list()
    print("len(stock_list): ", len(stock_list))
    print("stock_list: ", stock_list)
```

---

## 🐞 **Troubleshooting**

- **Error:** `selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH`
  - Ensure that **ChromeDriver** is installed and accessible in your system PATH.

- **Error:** `TimeoutException`
  - Increase the **explicit wait time** in the script to handle slow-loading content.
  ```python
  wait = WebDriverWait(driver, 10)
  ```

- **Error:** `Connection refused`
  - Check your internet connection and ensure that the target URL is accessible.

---

## 📜 **License**
This project is licensed under the [MIT License](LICENSE).

---

## 💬 **Contributing**
Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or improvements.

---

## 📞 **Contact**
For questions or support, please contact:
- **Author:** Your Name
- **Email:** your.email@example.com

