{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [],
   "source": [
    "#web automation using python and selenium\n",
    "#task: order a product from snapdeal.com  \n",
    "from selenium import webdriver\n",
    "browser = webdriver.Chrome('G:\\coding society\\chromedriver.exe')  #using a chrome webdriver\n",
    "browser.get(\"https://www.snapdeal.com/\")   #url of a snapdeal\n",
    "\n",
    "            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "········\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "search_element = browser.find_element_by_id('inputValEnter')  #accessing the search bar \n",
    "search_element.send_keys('bluetooth speaker') #writing to search bar\n",
    "time.sleep(3)\n",
    "browser.find_element_by_xpath('//*[@id=\"sdHeader\"]/div[4]/div[2]/div/div[2]/button').click()\n",
    "time.sleep(5)\n",
    "browser.find_element_by_id('648314636646').click()\n",
    "window_after = browser.window_handles[1]  #switching to the new windows \n",
    "browser.switch_to.window(window_after)\n",
    "time.sleep(3)\n",
    "browser.find_element_by_id('buy-button-id').click()\n",
    "time.sleep(3)\n",
    "username_element = browser.find_element_by_id('username') #login to the snapdeal.com\n",
    "username_element.send_keys('ns.nikhilaks@gmail.com')\n",
    "browser.find_element_by_id('login-continue').click()\n",
    "time.sleep(5)\n",
    "password_element = browser.find_element_by_id('w_password')\n",
    "\n",
    "from getpass import getpass   # for taking the password\n",
    "password_element.send_keys(getpass())\n",
    "browser.find_element_by_id('login-done').click()\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
