from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from datetime import datetime



class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.bet365.com/#/AVR/B24/R^1/")
        time.sleep(8)

    def get_data(self):
        self.driver.find_element_by_class_name('vr-ResultsNavBarButton').click()
        time.sleep(5)
        self.podiumPosition = self.driver.find_elements_by_class_name('vrr-PodiumPlace_Position')
        self.podiumPrice = self.driver.find_elements_by_class_name('vrr-Price')
        self.podiumRunner = self.driver.find_elements_by_class_name('vrr-ParticipantInfo_Runner')
        self.podiumResult = self.driver.find_elements_by_class_name('vrr-ResultParticipant_Text')
        Bot.toCSVAndKeepActualData()
    
    def toCSVAndKeepActualData(self):       
        df_old = pd.read_csv('bet365.csv')
        df_new = pd.DataFrame({
            'HourAndDate': [ Bot.getHourAndDate()],
            'Winner': [self.podiumPosition[0].text],
            'Price': [self.podiumPrice[0].text],
            'Runner': [self.podiumRunner[0].text],
            'Result': [self.podiumResult[1].text]
        })
        df_new.to_csv('bet365.csv', index=False)
        df_merged = df_old.append(df_new)
        df_merged.to_csv('bet365.csv', index=False)
        print('Data updated')
        self.driver.refresh()


    def getHourAndDate(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d/%m/%Y")
        return current_time + ' ' + current_date

    def initBot(self):
        while True:
            self.get_data()
            time.sleep(30)

Bot = Bot()
while True:
    Bot.get_data()
    time.sleep(190)



