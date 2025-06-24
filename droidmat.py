import os
from time import sleep
import uiautomator2 as u
import random

d = u.connect()

# airplane mode be-ki kapcsolás !!!TSU installálása és ROOT legyen!!!
def airplaneMode(time):
    os.system("sudo settings put global airplane_mode_on 1")
    sleep(time)
    os.system("sudo settings put global airplane_mode_on 0")

# rákeres az adott keywordre
def search(keyword):
    d.app_start("com.android.chrome")

    # 3 pöttyre rányom
    if d(description="More options").exists:
       d(description="More options").click()

    # megnyit új inkognitó lapot
    if d(text="New incognito tab").exists:
       d(text="New incognito tab").click()
    
    address_bar = d(className="android.widget.EditText")

    if address_bar.exists:
        address_bar.click()
        d.send_keys(keyword)
     
def siteVisit():
    for i in range(random.randint(1,3)):
        for i in range(random.randint(1,3)):
            d(scrollable=True).scroll.vert.forward()
        for i in range(random.randint(1,3)):
            d(scrollable=True).scroll.vert.backward()
    d.press("back")
    
# próbacseresznye
airplaneMode(3)
search("lufi")