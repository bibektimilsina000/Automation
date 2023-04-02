
from webdriver import getWindowReady, goToWebsite, login, funcButtons, getAllActionButton, unfollow
from credentials import get_credentials
from constants import website as facebook
from install_requirements import install_requirements
from chromedriver_installer import install_chromedriver
from tk_installer import install_tkinter

def main():
    # install_chromedriver()
    install_tkinter()
    # install_requirements()
    cred =  get_credentials()
    driver = getWindowReady()
    goToWebsite(facebook, driver)
    login(cred[0], cred[1], driver)
    funcButtons(driver)
    allActionButtons = getAllActionButton(driver)
    unfollow(driver, allActionButtons)


if __name__ == '__main__':
    main()
