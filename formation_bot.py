from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from openpyxl import Workbook 



option = webdriver.ChromeOptions()
option.add_argument("--incognito") # Navigation privée
option.add_argument("--start-maximized") #"kiosk" sur mac
#prefs={"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
#option.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(executable_path=r"/home/chenow/Documents/JCS/formation scraping/chromedriver_linux64/chromedriver", options=option)
#à télécharger sur internet
plat="Tarte aux fraises"
print('Recette : '+plat)


browser.get('https://www.marmiton.org/')


button = browser.find_element_by_id("didomi-notice-agree-button")
button.click()


barre_recherche = browser.find_element_by_xpath('//*[@id="header"]/header/div/div[1]/div[2]/div/div/input')
 

barre_recherche.send_keys(plat)
barre_recherche.send_keys(Keys.RETURN) 
"""
# # Autre manière de faire la recherche, c'est plus rapide
plat_separe=plat.lower().split(' ')
print(plat_separe)
plat_tiret=""
for plat_i in plat_separe:
        plat_tiret+=plat_i+'-'
plat_tiret=plat_tiret[:-1]

browser.get('https://www.marmiton.org/recettes/recherche.aspx?aqt='+plat_tiret)
"""

recette=browser.find_element_by_xpath('//*[@id="__next"]/div[3]/main/div/div[2]/div[1]/div[1]/div[3]/a[1]')
lien_recette=recette.get_attribute('href')

browser.get(lien_recette)

time.sleep(3) # en secondes evite le DDOS

temps=browser.find_element_by_xpath('//*[@id="__next"]/div[3]/main/div/div/div[1]/div[1]/div[5]/div[1]/span/p').text
print('Temps de préparation total : '+temps)


try :
    liste_ingredients1=browser.find_elements_by_xpath('//*[@id="simple-tabpanel-0"]/div[2]/div/div/div[1]/div[2]/div/div/span/span/div[2]/span/span[2]')
    for ingredient in liste_ingredients1:
        print(ingredient.text)
#//*[@id="simple-tabpanel-0"]/div[2]/div/div/div[1]/div[2]/div[1]/div/span/span/div[2]/span/span[2]
#//*[@id="simple-tabpanel-0"]/div[2]/div/div/div[1]/div[2]/div[2]/div/span/span/div[2]/span/span[2]
# on copie-colle, et on voit ce qu'ils ont en commun
except :
    None


wb=Workbook() #création du classeur 
ws=wb.active #création de la feuille
ws.title="recette" #titre de la feuille

# on set le "curseur"
column=1
row=1
for ingredient in liste_ingredients1:
        ws.cell(row,column).value=ingredient.text # assigne la valeur info à la cellule en ligne(row) et en colonne (column)
        column+=1  # sur une ligne on change de colonne

try :
    wb.save("recette"+".xlsx")  #on sauve l'excel sous la forme xls.

except : 
    wb.save("LeNomAPasMarche.xlsx")

browser.quit()

#faire un projet avec analyse, du style cb de farine il me faut pour faire toutes les tartes aux fraises. Projet libre à la créativité. L'effort est valorisé, 