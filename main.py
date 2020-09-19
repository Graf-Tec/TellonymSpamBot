from selenium import webdriver
import time
import subprocess


def open(driver1, driver2, url):
    driver1.get(url)
    driver2.get(url)
    time.sleep(4.5)

    accept = driver1.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
    accept.click()

    accept1 = driver2.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
    accept1.click()


def sendMSG(driver2, driver22, url, msg):
    input_field = driver2.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea')
    input_field2 = driver22.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[1]/div/textarea')
    for x1 in msg:
        input_field.send_keys(x1)
        input_field2.send_keys(x1)
        time.sleep(0.4)
    time.sleep(2.5)

    submit_field = driver2.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[2]/form/button/div/div')
    submit_field.click()

    submit_field2 = driver22.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[5]/div/div/div[1]/div[2]/div/div[4]/div[3]/div/div[2]/form/button/div/div')
    submit_field2.click()

    time.sleep(1)
    driver2.get(url)
    driver22.get(url)
    time.sleep(1)


def clear():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()


if __name__ == '__main__':
    print("Bitte Tellonym Namen eingeben!")
    name = input()
    clear()
    print("Ist der Tellonym Namen: " + name + " korrekt? (Y für Ja und N für Nein)")
    correkt = input()
    if correkt in ['y', 'Y']:
        clear()
        print("Bitte Spam-Nachricht eingeben!")
        Nachricht = input()
        clear()
        print("Bitte Anzahl der Wiederholungen eingeben! (Alles wird ZWEI mal ausgeführt!)")
        wdh = input()
        try:
            aa = int(wdh)
        except ValueError:
            print('Falsche Eingabe!')
            exit(0)
        clear()
        print("Go? (Y für Ja und N für Nein)")
        test = input()
        if test in ['y', 'Y']:
            print()
            str1 = 'chromedriver.exe'
            Maindriver = webdriver.Chrome(str1)
            Maindriver2 = webdriver.Chrome(str1)
            tellonymURL = 'https://tellonym.me/' + name
            open(Maindriver, Maindriver2, tellonymURL)
            for x in range(aa):
                sendMSG(Maindriver, Maindriver2, tellonymURL, Nachricht)

            Maindriver.quit()
            Maindriver2.quit()
            allewdh = wdh * 2;
            subprocess.call('msg * /TIME:5 "Deine Nachricht wurde "' + allewdh + '" mal an "' + name + '" gesendet',
                            shell=True)
            print('Fertig!')
            exit(0)
        else:
            exit(0)
    else:
        exit(0)
