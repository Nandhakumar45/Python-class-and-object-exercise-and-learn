"""How to find the web page images, text, and others by using inbuild playwright methods--
1. page.get_by_alt_text --> this in build method is used for how to find the images in web page
2. Page_get_by_text--> This in build method is used for how to find the text in web page
3. Page_get_by_role -> This is mostly used in to find the role in the web page, let say we have n number attributes is present
4. Label is noted, but an element present, let say we have a field called first name, last name and address, etc. on the place of the text we have test input filed those are called as label.
5. Page_get_by_label is a copy paste of step 4
6. Page_get_by_place holder, Place holder, it also like an element of attributes, in most of the web page search text box along with some button would be there.
7. page_get_by_title is mostly used to get the title of the page..





Like radio button, header, slider bar, those things are we can consider as a role in the web page"""

import re

from playwright.sync_api import Page, expect


def test_webpage_logo(page: Page):
    page.goto("https://eu.gymshark.com/")

    # Image by alt text
    logo = page.get_by_alt_text("Gymshark")
    expect(logo).to_be_visible()
    print("The value of the brand name is", logo.get_attribute("alt"))

    # get_by_text
    expect(page.get_by_text("POPULAR RIGHT NOW")).to_be_visible()
    expect(page.get_by_text("POPULAR", exact=False)).to_be_visible()
    expect(page.get_by_text(re.compile("POPULAR"))).to_be_visible()

    # get_by_role
    page.wait_for_timeout(5000)
    page.goto("https://auth.gymshark.com/u/login")
    page.wait_for_timeout(5000)
    expect(page.get_by_role("button", name="LOG IN")).to_be_visible()

    # get_by_label
    page.goto("https://auth.gymshark.com/u/signup")
    page.wait_for_timeout(5000)
    page.get_by_label("Email address *").fill("Nandhakumar")
    page.get_by_label("Password *").fill("Nandhakumar")


    # # get_by_placeholder
    # # get_by_placeholder (FIXED)
    # page.goto("https://getrawnutrition.com/")
    #
    # # Step 1: Click search icon / button
    # page.get_by_role("button", name="Search").click()
    #
    # # Step 2: Now the input exists and is visible
    # search_input = page.get_by_placeholder("Search for protein, creatine...")
    # expect(search_input).to_be_visible()
    # page.wait_for_timeout(5000)
    # # Step 3: Fill the input
    # search_input.fill("Preworkout")

    #get_by_title
    page.goto("https://getrawnutrition.com/")
    expect(page.get_by_title("RAW Nutrition – Get Raw Nutrition"))  #.to_have_text() when we use this method means, let say my page tit
    #is Hypertext markup language is mentioned in the page DOM structure but in the web page GUI, it would be in HTML,,
    page.close()
    #get_by_test_id
    # page.goto("https://getrawnutrition.com/")
    # page.get_by_test_id("shop-cart-sync-iframe")

