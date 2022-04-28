from selenium import webdriver
import time
import os
from tqdm import TqdmExperimentalWarning
    



username = "translateturkei"
password = "H.steal3131"

scrool = 400

class Instagram():
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    
    def signIn(self):                                             #GİRİŞ YAPMA
        self.browser.get('https://www.instagram.com/?hl=tr')
        self.browser.maximize_window()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(6)
    
    def find_post(self):                                 #POSTA GİTME
        self.browser.get(post_url)
        time.sleep(4)
        self.browser.find_element_by_css_selector('#react-root > section > main > div > div.ltEKP > article > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div.eo2As > section.EDfFK.ygqzn > div > div > div > a > div').click()
        time.sleep(4)








    def scrollDown(self):                                 #SCROLL DOWN
        js = f"""
        page = document.querySelector("body > div.RnEpo.Yx5HN > div > div > div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div");
        page.scrollTo(0, {scrool});
        let pageEnd = {scrool};
        return pageEnd;
        """

        pageEnd = self.browser.execute_script(js)

        while True:
            end = pageEnd
            time.sleep(1)
            pageEnd = self.browser.execute_script(js)
            if end == pageEnd:
                break
        
        instagram.getFollower()


    def getFollower(self):  
          
        followersList = []
        followers = self.browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll')

        for follower in followers:
            followersList.append(follower.text)

        with open("data/photo_likes.txt", "a", encoding="UTF-8") as file: #Dosya acma islemlerine iyi bak
            for follower in followersList:
                file.write(follower + "\n")
    

    def nameControl(self):                                 #İSİM KONTROL
        filenamed = open("data/photo_likes.txt" , "r").readlines() #sayafadan çektiğimiz

        filecontrol = open("data/just_1_name.txt" , "a") #isim teke düşer
        count = 0
        Sadece1isim = []

        for line in filenamed :
            if line not in Sadece1isim:
                filecontrol.write(line)
                Sadece1isim.append(line)

    def folow(self):
        with open("data/just_1_name.txt","r") as FolowList:
            folows = FolowList.readlines()

            for folow in folows:
                self.browser.get("https://www.instagram.com/{}/".format(folow))
                time.sleep(4)
                try:
                    self.browser.find_element_by_class_name('.sqdOP.L3NKy.y3zKF').click()
                    time.sleep(3)
                except:
                    try:
                        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div').click()
                    except:
                        try:
                            self.browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.XBGH5 > div.qF0y9.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm.bPdm3 > div > div > button > div').click()       
                        except:
                            try:
                                self.browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.XBGH5 > div.qF0y9.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm.bPdm3 > div > div > button').click()
                            except:
                                try:
                                    self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
                                except:
                                    print(f"{folow} Hesabına istek atılamadı")

    def profile(self):
        self.browser.get('https://www.instagram.com/translateturkei/?hl=tr')
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()     
        time.sleep(4)

    def scrooldownUnf(self):
        jsunf = f"""
        page = document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.isgrP");
        page.scrollTo(0, {scrool});
        let pageEnd = {scrool};
        return pageEnd;
        """

        pageEnd = self.browser.execute_script(jsunf)

        while True:
            end = pageEnd
            time.sleep(1)
            pageEnd = self.browser.execute_script(jsunf)
            if end == pageEnd:
                break
        
        instagram.unflist()


    def unflist(self):
        
        unfList = []
        unfollowers = self.browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll')

        for unf in unfollowers:
            unfList.append(unf.text)   

        with open("data/unfollowers.txt", "a", encoding="UTF-8") as fileunf: 
            for unf in unfList:
                fileunf.write(unf + "\n")

    def namecontrolUnf(self):
        filenameunf = open("data/unfollowers.txt" , "r").readlines()

        filecontrolunf = open("data/just_1_name_unf.txt" , "a")

        Sadece1isimunf = []

        for line in filenameunf :
            if line not in Sadece1isimunf:
                filecontrolunf.write(line)
                Sadece1isimunf.append(line)

    def unf(self):
        with open("data/just_1_name_unf.txt","r") as UnfList:
            unfs = UnfList.readlines()

            for unf in unfs:
                self.browser.get("https://www.instagram.com/{}/".format(unf))
                time.sleep(5)

                try: 
                    self.browser.find_element_by_class_name('.vBF20._1OSdk').click()
                    time.sleep(3)
                    self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                    time.sleep(3)

                except:
                    try:
                        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]').click()
                        time.sleep(5)
                        self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                        time.sleep(2)
                    except:
                        try:
                            self.browser.find_element_by_class_name('._5f5mN.-fzfL._6VtSN.yZn4P').click()
                            time.sleep(5)
                            self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                            time.sleep(2)
                        except:
                            with open("data/log.txt", "a", encoding="UTF-8") as log: 
                                log.write(f"{unf} isimli hesaba unf atılamadı\n")
                            


            unf = UnfList.readlines()
            print("data/log.txt dosyasını kontrol edin!")

    def clean_file(self):
        folders = ["data/just_1_name.txt", "data/just_1_name_unf.txt", "data/unfollowers.txt", "data/log.txt", "data/photo_likes.txt"]
        for folder in folders:
            os.remove(folder)


################################################# FOR TERMİNAL ##############################################
        

choose = int(input("işlem seçin: \n1. Beğenenleri Takip Etme: \n2. UNF (15 den fazla kullanıcıyı takip etmelisiniz!): \n3. Çıkış: \nişlem: "))

if choose == 1:
    post_url = input("Post linki girin: ")
    instagram = Instagram(username, password)

    instagram.signIn()

    instagram.find_post()

    limit = 0
    while limit < 25:
        instagram.scrollDown()
        scrool += 300
        limit += 1


    instagram.nameControl()
    instagram.folow()

    reset = input("Uygulamayı sıfırlamak ister misiniz? (e/h): ")
    if reset == "e":
        instagram.clean_file()
    else:
        print("Data içindeki Txt Dosyalarını manuel temizleyiniz!")



elif choose == 2:
    print("Takip Ettiğiniz Kişi Sayısı 15 den az ise bu işlemi kullanmayın!")
    instagram = Instagram(username, password)
    instagram.signIn()
    instagram.profile()
    
    limit2 = 0
    while limit2 < 25:
        instagram.scrooldownUnf()
        scrool += 300
        limit2 += 1

    instagram.namecontrolUnf()
    instagram.unf()

    reset = input("Uygulamayı sıfırlamak ister misiniz? (e/h): ")
    if reset == "e":
        instagram.clean_file()
    else:
        print("Data İçindeki Txt Dosyalarını manuel temizleyiniz!")

elif choose == 3:
    print("Çıkılıyor...")

else:
    print("Yanlış işlem seçtiniz...")










    
