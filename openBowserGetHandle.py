from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://www.baidu.com/")
# 获取当前操作界面的句柄
print (driver.current_window_handle)

driver.implicitly_wait(2)
driver.find_element_by_id("kw").send_keys("selenium")

#获取所有句柄
all_handles = driver.window_handles
print (all_handles)

driver.find_element_by_id("su").click()
driver.implicitly_wait(2)

# 电击后进入新窗口，新窗口有自己的句柄
driver.find_element_by_link_text("百度翻译").click()
driver.implicitly_wait(2)

#获取进入新窗口后所有的句柄
all_handles2 = driver.window_handles
print (all_handles2)
driver.implicitly_wait(2)

#拿到新窗口句柄 并切换到新窗口
newhandle = [handle for handle in all_handles2 if handle not in all_handles]
driver.switch_to.window(newhandle[0])

print (driver.title)
# 关闭当前窗口
driver.close()
driver.implicitly_wait(5)

#切换到原窗口
driver.switch_to.window(all_handles[0])
print (driver.title)
print (driver.current_window_handle)
driver.quit()

