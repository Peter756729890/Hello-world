#!/usr/bin/env python3.4.3
#coding:utf-8  
#form http://blog.csdn.net/mypc2010/article/details/72934092 at 2017-08-19  
from selenium import webdriver  
import selenium.webdriver.support.ui as ui  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver import ActionChains  
import time  
#ffbrowser = webdriver.Chrome()
ffbrowser = webdriver.Firefox()
wait = ui.WebDriverWait(ffbrowser,3)
def LoginWeibo(username,password,url):#验证码输入未完成
    #print(username, password)
    try:  
        ffbrowser.get(url)#读取session中数据
        euser=ffbrowser.find_element_by_css_selector("div.input_wrap>input")
        ''' 
        euser=ffbrowser.find_element_by_id("loginname").send_keys(username)
        if not euser:
            print("euser is null")
        euser=ffbrowser.find_element_by_name("username").send_keys(username)
        if not euser:
            print("euser is null")
        euser=ffbrowser.find_element_by_class_name("W_input").send_keys(username)
        '''
        clr_user=ffbrowser.find_element_by_css_selector("div.input_wrap")  
        clr_user.click()#避免user含有提示信息 
        #print(ffbrowser)
        if not euser:
            print("euser is null")
        else:
            euser.send_keys(Keys.ENTER)  
            euser.send_keys(username)  
 
        epwd=ffbrowser.find_element_by_css_selector("[name='password']")
        if not epwd:
            print("epwd is null")
        else:
            epwd.send_keys(Keys.ENTER)  
            epwd.send_keys(password)  
  
        # 为防止报：Firefox 中的不安全密码警示这个错误，因此点击下密码框附件的区域  
        eunsafe=ffbrowser.find_element_by_css_selector("[class='info_list auto_login clearfix']")  
        eunsafe.click()  
        #点击登录按钮
        '''
        esubmit=ffbrowser.find_element_by_xpath("//a[@action-type='btn_submit']")  
        esubmit.click()  
        time.sleep(6)  
        eweibo=ffbrowser.find_element_by_css_selector("li>a[bpfilter='page_frame']")  
        eweibo.click()
        '''
        ffbrowser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
        time.sleep(3)  
    except Exception as e:
        print(e)
        return False
    finally:
        return True
        pass  

def DeleteWeibo():  
    try:  
        time.sleep(6)  
        elists=ffbrowser.find_elements_by_css_selector(".W_ficon.ficon_arrow_down.S_ficon")  
        for e in elists[1:]:  
            e.click()  
            time.sleep(1)  
            ees=ffbrowser.find_elements_by_css_selector(".screen_box>.layer_menu_list>ul>li[2]>a")
            #Message: Given css selector expression ".screen_box>.layer_menu_list>ul>li[2]>a" is invalid: 
            #SyntaxError: '.screen_box>.layer_menu_list>ul>li[2]>a' is not a valid selector            
            #ees=ffbrowser.find_element_by_xpath(".screen_box>.layer_menu_list>ul>li[2]>a")  
            print(ees[0].text)  
            ees[0].click()  
            time.sleep(1)  
            eenter=ffbrowser.find_element_by_css_selector(".W_btn_a>span")  
            eenter.click()  
            time.sleep(1)
            '''
            try:  
                time.sleep(1)  
                eclose=ffbrowser.find_element_by_css_selector(".W_ficon.ficon_close.S_ficon")  
                eclose.click()  
                time.sleep(2)
            except:  
                pass  
            '''
  
    except Exception as e:  
        print(e)
        return False
    finally:  
        pass
        return True
def QuitWeibo():
    ffbrowser.quit()
    
def LoginWeibo_Echo(username, password, url):
    ffbrowser.get(url)#读取session中数据
    #sign in the username 
    uid_xpath='//*[@id="loginname"]'
    try:
        browser.find_element_by_xpath('//*[@id="loginname"]').send_keys(username)
        print('user success!')
    except:
        print('user error!')
    time.sleep(1)
    #sign in the pasword
    pwd_xpath='//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input'
    try:
        browser.find_element_by_xpath(pwd_xpath).send_keys(password)
        print('pwd success!')
    except:
        print('pwd error!')
    time.sleep(1)
    #click to login
    click_xpath='//*[@id="pl_login_form"]/div/div[3]/div[6]/a'
    try:
        browser.find_element_by_xpath(click_xpath).click()
        print('click success!')
    except:
        print('click error!')
    time.sleep(30)

if __name__ == '__main__':
    your_usr="18589080511"#微博账户
    your_pwd="170725Young"#微博密码
    your_url="https://weibo.com/login.php"  
    print("开始登录微博,稍等")  
    flag=LoginWeibo(your_usr,your_pwd,your_url)
    #flag=LoginWeibo_Echo(your_usr, your_pwd, your_url)
    if flag:
        print("登录成功")
    else:
        print("failed")
        #QuitWeibo()
    
    i=1  
    while flag:  
        print("开始第"+str(i)+"轮删除")  
        time.sleep(6)  
        flag=DeleteWeibo()  
        i+=1
    if not flag:
        print("err")
        #QuitWeibo()
