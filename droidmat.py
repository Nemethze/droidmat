import os
from time import sleep
import uiautomator as u


# airplane mode be-ki kapcsolás !!!TSU installálása és ROOT legyen!!!
def airplaneMode(time):
    os.system("sudo settings put global airplane_mode_on 1")
    os.system("sudo am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true")
    sleep(time)
    os.system("sudo settings put global airplane_mode_off 1")
    os.system("sudo am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false")

# def search(keyword):
#     os.

airplaneMode(3)