# from selenium import webdriver
# from selenium.webdriver.common.by import By # New version selenium using this one
# from selenium.webdriver.chrome.service import Service # Then for login need to use this
# from selenium.webdriver.support.ui import WebDriverWait # define WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC # define EC


# s = Service(r'C:\Program Files\chromedriver.exe') # 利用selenium做爬蟲
# browser = webdriver.Chrome(service=s)
# browser.get("https://www.goopi.co/")

# browser.find_element(By.CLASS_NAME, 'menu-button.signin-signup-button.mobile-revamp-navigation').click()

# #search_Id = browser.find_element(By.NAME, 'mobile_phone_or_email') #找到輸入帳號的位置 並先記錄之後要input
# #search_Id.send_keys('skyfood123@yahoo.com.tw') #輸入帳號   (到時候可以考慮利用腳本輸入多個帳號
# #WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.NAME, 'password'))) #顯性等待 不然爬蟲跑太快了 抓不到元素
# ##search_password = browser.find_element(By.NAME, 'password') #找到輸入密碼的位置 並先記錄之後要input
# ##search_password = browser.find_element(By.CLASS_NAME, 'line-input.ng-pristine.ng-scope.ng-empty.ng-invalid.ng-invalid-required.ng-valid-minlength.ng-valid-maxlength.ng-touched')
# #search_password = browser.find_element(By.XPATH, value = '//input[@type="password"]')
# #search_password.send_keys('qwe123')
# #browser.find_element(By.ID, 'sign-in-recaptcha').click()
# ActionChains(driver)
# xpath = '//input[@type="password"]'
# try:
#     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
# except:
#     print("Click Error")
# # # 登入動作
# # browser.find_element_by_link_text("登入").click()
# # search_Id = browser.find_element_by_name('username') #找到輸入帳號的位置 並先記錄之後要input
# # search_Id.send_keys('iamaccount') #輸入帳號   (到時候可以考慮利用腳步輸入多個帳號
# # browser.find_element_by_id('login-signin').click()
# # WebDriverWait(browser, 20, 0.5).until(EC.presence_of_element_located((By.ID, 'login-passwd'))) #顯性等待 不然爬蟲跑太快了 抓不到元素
# # search_password = browser.find_element_by_id('login-passwd') 
# # search_password.send_keys('wearelose') #輸入密碼
# # browser.find_element_by_id('login-signin').click()

# -*- coding: utf-8 -*-
# 以下為ChatGPT修改後的內容
from selenium import webdriver
from selenium.webdriver.common.by import By # New version selenium using this one
from selenium.webdriver.chrome.service import Service # Then for login need to use this
from selenium.webdriver.support.ui import Select # import selector for selecting store
from selenium.webdriver.support.ui import WebDriverWait # define WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # define EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import tkinter as tk




def login_windows():
    # 建立視窗
    window = tk.Tk()
    window.title('Login')
    window.geometry('700x500')

    # 建立帳號標籤及文字方塊
    tk.Label(window, text='User name: ').place(x=50, y=50)
    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=160, y=50)

    # 建立密碼標籤及文字方塊
    tk.Label(window, text='Password: ').place(x=50, y=90)
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=160, y=90)


    # 建立標籤
    tk.Label(window, text='電話號碼：').place(x=50, y=130)
    tk.Label(window, text='信用卡號：').place(x=50, y=170)
    tk.Label(window, text='持卡人姓名：').place(x=50, y=210)
    tk.Label(window, text='有效時間：').place(x=50, y=240)
    tk.Label(window, text='安全碼：').place(x=50, y=270)
    tk.Label(window, text='要買的商品網頁連結').place(x=50, y=300)

    # 建立輸入框
    var_phone = tk.StringVar()
    var_card = tk.StringVar()
    var_name = tk.StringVar()
    var_time = tk.StringVar()
    var_code = tk.StringVar()
    var_website_link = tk.StringVar()


    entry_phone = tk.Entry(window, textvariable=var_phone)
    entry_phone.place(x=160, y=130)
    entry_card = tk.Entry(window, textvariable=var_card)
    entry_card.place(x=160, y=170)
    entry_name = tk.Entry(window, textvariable=var_name)
    entry_name.place(x=160, y=210)
    entry_time = tk.Entry(window, textvariable=var_time)
    entry_time.place(x=160, y=240)
    entry_code = tk.Entry(window, textvariable=var_code)
    entry_code.place(x=160, y=300)
    entry_website_link = tk.Entry(window, textvariable=var_website_link)
    entry_website_link.place(x=160, y=300)

    #建立登入按鈕
    def usr_login():
        record_input(entry_usr_name.get(), entry_usr_pwd.get(), entry_phone.get(), entry_card.get(), entry_name.get(), entry_time.get(), entry_code.get())
        window.destroy()

        

    btn_login = tk.Button(window, text='Login', command=usr_login)
    btn_login.place(x=170, y=330)
    window.mainloop()

def record_input(acc, pwd, ph, ccn, cn, ct, cs):
    global user_account, user_password, phone_number, credit_card_number, card_name, card_time, card_security
    user_account = acc
    user_password = pwd
    # 結帳資料填寫
    phone_number = ph
    credit_card_number = ccn
    card_name = cn
    card_time = ct
    card_security = cs



def goopi_login():
    # 輸入帳號密碼視窗
    login_windows()
    s = Service(r'C:\Users\forev\Downloads\chromedriver_win32 (1)\chromedriver') # 利用selenium做爬蟲
    browser = webdriver.Chrome(service=s)
    # browser.get("https://tw.buy.yahoo.com/") #此為switch產品網頁
    browser.get("https://www.goopi.co/")

    browser.find_element(By.CLASS_NAME, 'menu-button.signin-signup-button.mobile-revamp-navigation').click()
    # browser.find_element(By.CLASS_NAME, 'login-btn-label').click()

    search_Id = browser.find_element(By.NAME, 'mobile_phone_or_email') #找到輸入帳號的位置 並先記錄之後要input
    search_Id.send_keys(user_account) #輸入帳號   (到時候可以考慮利用腳步輸入多個帳號
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.NAME, 'password'))) #顯性等待 不然爬蟲跑太快了 抓不到元素
    search_password = browser.find_element(By.XPATH, value = '/html/body/div[10]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/form/div[2]/div/div/input') #找到輸入密碼的位置 並先記錄之後要input
    #search_password = browser.find_element(By.CLASS_NAME, 'line-input.ng-pristine.ng-scope.ng-empty.ng-invalid.ng-invalid-required.ng-valid-minlength.ng-valid-maxlength.ng-touched')
    #search_password = browser.find_element(By.XPATH, value = '//input[@type="password"]')
    search_password.send_keys(user_password)
    browser.find_element(By.XPATH, value = '//*[@id="sign-in-recaptcha"]').click()
    #browser.find_element(By.XPATH, value = '/html/body/div[10]/div[1]/nav/div[2]/div/div[2]/div/div/ul/li[1]/a').click()

    # ActionChains(driver).click(search_password).perform()

    # 商品的XPATH，也就是選擇商品
    browser.get('https://www.goopi.co/products/melsign-colour-matching-trousers-abyss')


    while 1:
        try:
            # 點擊購買按鍵， 顯性等待，直到出現可以購買後直接購買
            buy = WebDriverWait(browser, 1, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-buy-now.btn-purchase-action.btn-custom.ladda-button.form-control-inline.js-btn-main-buy-now.js-btn-show.js-btn-scroll')))
            buy.click()
            print('可以購買')
            # 跳到購買頁面後，點擊前往結帳按鈕
            print('準備前往購買頁面')
            go_buy = WebDriverWait(browser, 1, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-success.btn-block.btn-checkout')))
            go_buy.click()
            
            try:
                # 點擊搜尋門市按鈕
                browser.find_element(By.CLASS_NAME, 'btn.btn-color-primary.btn-block.btn-pick-store').click()
                time.sleep(1)
                ## 點擊門市名稱按鈕
                frame_content = browser._switch_to.frame(0)
                print(frame_content)
                select = Select(browser.find_element(By.XPATH, value = f'//*[@id="sel_area"]'))
                select.select_by_visible_text(u"桃園市")
                time.sleep(3)

                js = 'document.getElementById("road").style.display="Block";'
                browser.execute_script(js)
                #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="road_chosen"]')))
                # 選擇街道
                select_road = Select(browser.find_element(By.XPATH, value = f'//*[@id="road"]'))
                select_road.select_by_visible_text(u"松信路")
                time.sleep(3)
                #選擇店家
                select_store = browser.find_element(By.XPATH, value = f'//*[@id="ol_stores"]/li[1]')
                select_store.click()
                time.sleep(2)
                #門市確認
                # return to original frame, because changing to other frame that make selenium can not find the html content
                browser.switch_to.default_content() 
                map_mask = browser.find_element(By.ID, "mapMask")
                content = map_mask.get_attribute("innerHTML")
                # print(content) # checking search frame is correct
                browser.find_element(By.XPATH, value = f'//*[@id="sevenDataBtn"]').click()
                time.sleep(2)
                browser.find_element(By.XPATH, value = f'//*[@id="AcceptBtn"]').click()
                time.sleep(2)
                browser.find_element(By.XPATH, value = f'//*[@id="submit_butn"]').click()
                time.sleep(2)
                # 填寫資料
                # browser.find_element(By.XPATH, value = f'//*[@id="delivery-form-content"]/div[1]/label/input').click()
                # phone_number_data = browser.find_element(By.XPATH, value = f'//*[@id="order-customer-phone"]')
                # phone_number_data.send_keys(phone_number)
            except:
                print('無法選擇門市')

            
            break
        except:
            print('還不能購買! 重新整理')
            browser.refresh()


def customer_information(browser):
    # 填寫購買資訊
    ## 客戶資料
    
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.NAME, 'order[customer_phone]'))) #顯性等待 不然爬蟲跑太快了 抓不到元素
    customer_information_phone1 = browser.find_element(By.NAME, value = 'order[customer_phone]')
    customer_information_phone1.send_keys(phone_number)

    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'recipient-phone'))) #顯性等待 不然爬蟲跑太快了 抓不到元素
    customer_information_phone2 = browser.find_element(By.ID, value = 'recipient-phone')
    customer_information_phone2.send_keys(phone_number)

    # frame = browser.find_elements(By.TAG_NAME, value = 'iframe')[2]
    # print(frame.text)

def credit_card(browser):
    s = Service(r'C:\Users\forev\Downloads\chromedriver_win32 (1)\chromedriver') # 利用selenium做爬蟲
    browser = webdriver.Chrome(service=s)
    
    # card number
    browser._switch_to.frame(0)
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.ID, f'input-file')))
    customer_information_card = browser.find_element(By.ID, f'input-file')
    customer_information_card.click()
    print("This is credit card number", credit_card_number)
    customer_information_card.send_keys(credit_card_number)

    # Name for the card
    browser.switch_to.default_content() 
    browser._switch_to.frame(1)
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.ID, f'input-file')))
    customer_information_card = browser.find_element(By.ID, f'input-file')
    customer_information_card.click()
    print("This is credit card name", card_name)
    customer_information_card.send_keys(card_name)


    # MM/YY
    browser.switch_to.default_content() 
    browser._switch_to.frame(2)
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.ID, f'input-file')))
    customer_information_card = browser.find_element(By.ID, f'input-file')
    customer_information_card.click()
    print("This is credit card time", card_time)
    customer_information_card.send_keys(card_time)


    # security code
    browser.switch_to.default_content() 
    browser._switch_to.frame(3)
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.ID, f'input-file')))
    customer_information_card = browser.find_element(By.ID, f'input-file')
    customer_information_card.click()
    print("This is credit card security", card_security)
    customer_information_card.send_keys(card_security)

# ## 點擊收件人資料與顧客資料相同
# browser.find_element(By.XPATH, value = '//*[@id="delivery-form-content"]/div[1]/label/input').click()
# ## 點擊我同意網站服務條款擊隱私權政策按鈕
# browser.find_element(By.XPATH, value = '//*[@id="checkout-container"]/div/div[5]/div[1]/form/div/label/input')
time.sleep(10)


if __name__ == '__main__':
    



