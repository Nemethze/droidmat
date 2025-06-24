import os
from time import sleep
import uiautomator as u

# airplane mode be-ki kapcsolás !!!TSU installálása és ROOT legyen!!!
def airplaneMode(time):
    os.system("sudo settings put global airplane_mode_on 1")
    sleep(time)
    os.system("sudo settings put global airplane_mode_on 0")

# rákeres az adott keywordre
def search(keyword):
   search_url = f"https://www.google.com/search?q={keyword}"
   os.system(f'am start -n com.android.chrome/com.google.android.apps.chrome.Main -a android.intent.action.VIEW -d "{search_url}" --ez create_new_tab true --ez incognito true')

# próbacseresznye
airplaneMode(3)
search("lufi")