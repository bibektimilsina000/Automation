from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def getWindowReady():
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    return driver


def goToWebsite(WebsiteUrl, driver):
    driver.get(WebsiteUrl)
    driver.implicitly_wait(3)


def login(email, password, driver):
    emailField = driver.find_element(By.ID, "email")
    emailField.clear()
    emailField.send_keys(email)

    passwordField = driver.find_element(By.ID, "pass")
    passwordField.clear()
    passwordField.send_keys(password)

    passwordField.send_keys(Keys.RETURN)


def unfollowSelectedItem(driver):
    followBtn = driver.find_element(
        By.XPATH, '//div[@role="menuitem"][.//span[text()="Follow settings"]]')
    followBtn.click()

    checkbox = driver.find_element(
        By.XPATH, '//input[@aria-label="Unfollow"]')

    driver.execute_script("arguments[0].scrollIntoView();", checkbox)

    checkbox.click()

    updateButton = driver.find_element(
        By.XPATH, "//div[@aria-label='Update']")
    updateButton.click()


def funcButtons(driver):
    pageBtn = driver.find_element(By.XPATH, "//a[.//span[text()='Pages']]")
    pageBtn.click()

    likeButton = driver.find_element(
        By.XPATH, "//a[.//span[text()='Liked Pages']]")
    likeButton.click()


def getAllActionButton(driver):
    moreActionButtons = driver.find_elements(
        By.XPATH, "//div[@aria-label='More actions']")

    return moreActionButtons


def refreshBrowser(driver):
    driver.refresh()


def unfollow(driver, allActionButtons):
    for actionButton in allActionButtons:
        actionButton.click()
        try:
            unfollowSelectedItem(driver)
        except:
            refreshBrowser(driver)
            allActionButtons = getAllActionButton(driver)
            unfollow(driver, allActionButtons)
