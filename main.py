from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import random
import string



harfler = list(string.ascii_lowercase)
sayilar = [str(i) for i in range(1, 10)]

# genel_liste = harfler + sayilar
genel_liste = harfler + sayilar


def login(username, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-browser-side-navigation")
    
    # Eklenen argümanlar
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--log-level=3")  # 0: DEBUG, 1: INFO, 2: WARNING, 3: ERROR, 4: FATAL

    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://www.instagram.com/")
    time.sleep(3)

    username_input = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    username_input.send_keys(username)

    password_input = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    password_input.send_keys(password)
    time.sleep(1)

    login_button = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()
    time.sleep(10)

    return browser


def get_following_list(browser):
    browser.get("https://www.instagram.com/mr.programmer.exe/following/")
    index = 0
    following_list = []
    time.sleep(4)
    while index <= 1:
        try:
            search_bar = browser.find_element(By.CSS_SELECTOR,
                                               '.x1lugfcp.x19g9edo.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x5n08af.x5yr21d.x1a2a7pz.xyqdw3p.x1pi30zi.xg8j3zb.x1swvt13.x1yc453h.xh8yej3.xhtitgo.xs3hnx8.xoy4bel.x7xwk5j.xvs91rp.xp001vz')
            search_bar.clear()
            search_bar.send_keys(genel_liste[index])

            js_command = """
            followers = document.querySelector("._aano");
            followers.scrollTo(0, followers.scrollHeight);
            var lenOfPage = followers.scrollHeight;
            return lenOfPage
            """

            len_of_page = browser.execute_script(js_command)
            match = False

            while not match:
                last_count = len_of_page
                time.sleep(5)
                len_of_page = browser.execute_script(js_command)

                if last_count == len_of_page:
                    match = True

            time.sleep(5)

            takipci_elements = browser.find_elements(By.CSS_SELECTOR,
                                                     '.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd')

            for takipci in takipci_elements:
                following_list.append(takipci.text)

            print(f"Following list: {following_list}")
            index += 1

        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Hata durumunda döngüyü sonlandır

    return following_list


def find_unfollowers(browser, username, following_list):
    unfollowers_file = open("takip_etmiyor.txt", "w", encoding="utf-8")
    for following_user in following_list:
        browser.get(f"https://www.instagram.com/{following_user}/following/")
        time.sleep(5)
        following_elements = browser.find_elements(By.CSS_SELECTOR,
                                                   '.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd')

        aranan_user = username
        aranan_kelimeler = []

        for following_element in following_elements:
            aranan_kelimeler.append(following_element.text)

        if aranan_user not in aranan_kelimeler and following_user in following_list:
            print(f"{following_user} bizi takip etmiyor.")
            unfollowers_file.write(f"{following_user}\n")

    unfollowers_file.close()

class Bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'



def logo():
    print(Bcolors.RED + Bcolors.BOLD)
    logo = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠀⠀⠀⠀⠉⠙⠶⠦⣀⡀⠀⠀⠀⣀⣠⠴⠶⠞⠛⠛⠶⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠞⠁⠀⠀⠀⠀⠀⣀⣠⡤⠤⠤⠤⣤⣄⡀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⢠⠶⠛⠉⠁⠀⠀⠀⠀⠀⠈⠙⠓⠦⢤⣿⠤⠖⠒⠒⠒⠒⠒⠚⠒⠓⠲⠾⢧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⠤⠤⠤⠤⣭⣳⣤⡀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣬⣙⣳⣦⣄⠀⠀
⠀⠀⠀⠀⢀⣀⣿⣷⣦⣤⣄⣀⡀⠀⣀⣀⣤⣤⣤⣶⣯⣭⣥⣶⣶⣯⣭⣽⣶⣶⣬⣭⣙⣴⢖⣫⣭⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣷⣤
⠀⠀⠀⣤⠛⢹⡇⠈⠉⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡿⣿⣿⣿⣿
⠀⢀⡞⠁⠀⠸⠇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡣⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿
⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⣀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣉⣩⡭⠿⠛⠉⠁⠀⠀⠀⠀⠀⠙⠛⢿⡒⠛⠛⠛⠋⠻⡭⡉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⠉⠉⠉⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⣀⠀⠀⠀⠉⠙⠳⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣇⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡄⠀⠈⠉⠛⠢⢤⣤⣀⠀⠀⠈⠉⠉⠑⠒⠒⠒⠢⠤⢤⣤⣤⣤⣤⣄⣠⣤⣤⡤⠔⠚⠋⠁⢀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢦⣄⡀⠀⠀⠀⠈⠉⠙⠓⠒⠦⢦⣤⣤⣄⣀⣀⣀⣀⣀⣀⠀⠀⠈⠁⠀⢀⣀⣀⣠⣤⠖⠉⠀⠀
⠛⣻⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠲⢤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠁⠀⠈⠀⠉⠀⠉⠉⠉⠉⠉⣉⣉⣤⣥⣷⠾⠓⢲⣚⡟
⠈⣞⣷⣴⣌⣽⣫⣿⠷⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠷⠶⠶⠶⠶⢶⢦⣤⣤⣴⢿⣯⡉⠉⣁⣞⠗⢂⠹⡝⠅
⠀⣻⣿⣷⢪⣿⣋⠀⠀⢀⡈⣽⡛⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⣛⣍⣿⢷⡆⣈⣻⣮⠀⣻⣧⢿⣷⣶⠾
⠿⣿⣿⠾⠿⣿⡿⣵⣿⡏⣿⠹⣿⣞⢷⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⠟⡾⣿⣹⣿⣿⢷⡽⣏⠛⠓⠒⠛⠛⠛⠛⠛
⡼⢭⠥⣴⠬⣿⠿⢯⡿⢥⡿⢧⡿⢿⡿⢯⠭⢭⡿⢿⡿⢿⡿⢶⡶⢶⡾⢾⡿⢿⡭⢿⣿⠼⣧⠍⣭⠭⣥⠬⣷⢻⣆⣀⣦⣀⣴⣀⣀⠀
⢱⡿⠶⠿⠶⠾⠶⠾⠶⠾⠷⠾⠶⠾⠷⠾⠶⠾⠷⠾⠷⠾⠷⠾⠷⠾⠟⠛⠻⠞⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⡀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇

    # v1.0.0 #
       >> InstaDetective <<
       >> 17/12/2023 <<
       >> https://github.com/SOFTWAREPOLAT <<

    """
    print(logo)
    print(Bcolors.ENDC)

def main():
    username = input(Bcolors.GREEN +"Enter your Instagram username: " + Bcolors.ENDC)
    password = input(Bcolors.GREEN + "Enter your Instagram password: " + Bcolors.ENDC)

    browser = login(username, password)
    following_list = get_following_list(browser)
    find_unfollowers(browser, username, following_list)

    browser.close()


if __name__ == "__main__":
    logo()
    main()