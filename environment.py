from selenium import webdriver

def before_scenario(context, scenario):
    if 'browser' in context:
        context.browser.quit()
    context.browser = webdriver.Safari()

def after_scenario(context, scenario):
    if 'browser' in context:
        context.browser.quit()