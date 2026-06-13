'''
tag id ----> Tag of the particular code line and look for the ID attribute. specify the # as the tag and id combination.
EX:
tag class ---> Tag of the particular code line and look for the class attribute.Specify the . as the tag and class combination.
Ex:
tag attributes--->
EX:
tag class attributes--->
'''


from playwright.sync_api import Page

def test_CSSLocator(page: Page):
    # #tag id combination
    # page.goto("https://demowebshop.tricentis.com")
    # #tag id combination
    # page.locator("input#small-searchterms").fill("T-shirt")
    # page.wait_for_timeout(500)



    # #tag.class combination
    # page.goto("https://demowebshop.tricentis.com")
    # page.locator("input.search-box-text").fill("Laptop")
    # page.wait_for_timeout(500)

    # # tag.attribute combination
    # page.goto("https://demowebshop.tricentis.com")
    # page.locator("input[name=q]").fill("Mobile")
    # page.wait_for_timeout(500)

    #tag.class and attribute
    page.goto("https://demowebshop.tricentis.com")
    page.locator("input.search-box-text[name=q]").fill("pant")
    page.wait_for_timeout(500)

















