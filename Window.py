 from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import timeit
from array import *
import pyautogui
import mss
from PIL import Image
  
  def PillowScreenCap(self):
        with mss.mss() as sct:
            sct_img = sct.grab(self.monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            px = img.load()
            if self.noGuessing:
                self.searchStartClick(px)
            time.sleep(0.1)
            sct_img = sct.grab(self.monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            px = img.load()
            img.show()
