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
    sleep(3)
    for i in range(random.randint(1,3)):
        for i in range(random.randint(1,3)):
            d(scrollable=True).scroll.vert.forward()
        for i in range(random.randint(1,3)):
            d(scrollable=True).scroll.vert.backward()
    d.press("back")
    
def openAd(maxAds):
    for _ in range(maxAds):
        all_ads = d.xpath('//*[contains(@text, "Shop now")]').all()
        for ad in all_ads:
            ad_text = ad.xpath('..').get_text()
            if not any(b in ad_text for b in blacklist):
                ad_coords = ad.center()
                d.long_click(ad_coords[0], ad_coords[1], duration=1.5)
                d.xpath('//*[@text="Open in new tab"]').click_exists(timeout=2)
                siteVisit()
        d.swipe(500, 1500, 500, 500)
        
def close():
    d.press("home")
    d.shell("am force-stop com.android.chrome")

def readinFile():

# próbacseresznye

blacklist = []

for i in range(3):
    airplaneMode(3)
    search("lufi")
    openAd(10)
    close()