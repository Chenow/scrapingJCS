from launcher import *

if __name__ == "__main__":
    
    wb = initialisation_excel()
    browser = initialisation_launcher()

    time.sleep(2)
    page = 1
    while True:
        list_avis = get_list_avis(browser, page)
        if list_avis == []:
            break
        trier_avis(wb, list_avis)
        page +=1    
        time.sleep(3)

    print("test ok")
    browser.quit()

