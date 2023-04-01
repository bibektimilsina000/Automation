
from webdriver import getWindowReady, goToWebsite, login, funcButtons, getAllActionButton, unfollow
from credentials import getCred
from constants import website as facebook
from install_requirements import install_requirements
from chromedriver_installer import install_chromedriver

def main():
    install_chromedriver()
    install_requirements()
    cred = getCred()
    driver = getWindowReady()
    goToWebsite(facebook, driver)
    login(cred[0], cred[1], driver)
    funcButtons(driver)
    allActionButtons = getAllActionButton(driver)
    unfollow(driver, allActionButtons)


if __name__ == '__main__':
    main()
