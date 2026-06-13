""" This is first programming in playwright how launch the web using playwright. and whatever the web we launched that is correct or not"""

# commend to run the code in cmd prompt "python -m pytest "Playwright_WEB/test_URL launch.py" -s -v"
# they are two mode of execution is available in execute the automation test case 1. Headless and headed.. Headless means to UI will in running state, it is kind of only background will take a part of this.. Headed means UI interaction it is possible to see the UI runs when execute the script..
# The commend for execute the headed execution "python -m pytest "Playwright_WEB/test_URL launch.py" -s -v --headed"


from playwright.sync_api import Page, expect


def test_url(page: Page):
    page.goto("https://eu.gymshark.com/")
    expect(page).to_have_url("https://eu.gymshark.com/")



