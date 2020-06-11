# Web_automation_snapdeal.com
Web automation using Python and selenium
In this project i just order a product from snapdeal.com using web automation using python and selenium tool
<br>
step1 - install selenium
<br>
pip install selenium
<br>
step 2 - install the webdriver in my case i use chrome web driver link -https://chromedriver.chromium.org/downloads
<br>
step 3 - to start a browser session-:
<br>
from selenium import webdriver
<br>
browser = webdriver.chrome()
<br>
step 4 : to open a webpage
<br>
browser.get('url')
<br>
step 5 : to select an element by id 
<br>
browser.find_element_by_id(/id)
<br>
if id is not given then use xpath
<br>
browser.find_element_by_xpath(/xpath)
<br>
step 6: input value in element
<br>
element.sendkeys()
<br>
step 7: click on any element
<br>
element.click()
<br>
so in this project you will order your product from snapdeal.com using python script without any single click on a website fully automated
<br>
#thank you 



