""" They are two type of mode of execution is present in one is synchronous mode of execution and asynchronous mode of execution.
Synchronous means let we have 10 line of code to execute, The programme it starts from the frist line and line by line it execute, For the first line
 It perform a set of action and second line it perform a set of action, and it goes on. This is called as synchronous mode of execution.
Asynchronous mode of execution means It parallel execute 10 line of code at same time which means, if it executes the first line, and it will not wait for the
task to complete. Parallelly it run the second line of code execution."""

'''It will wait still the code to execute and full the promise, we need to add await for the execution. Typescript and javascript are used for the async mode, 
python has sync and async mode. For api testing we need async.
'''
''' How to run the test case is different browser at same time, python -m pytest "Playwright_WEB/test_async_method_execution.py" -s -v --headed --browser --chromium --browser --firefox'''
''' How to run two browser at same time~ python -m pytest "Playwright_WEB/test_async_method_execution.py" -s -v --headed -n=2 or  --numprocesses 2 or --numprocesses=2 '''


import pytest
from playwright.async_api import async_playwright, Page, expect


@pytest.mark.asyncio
async def test_url():
    # write our own stuff for the async mode
    async with async_playwright() as p:
        # async_playwright is user defined function and p is alias
        browser = await p.chromium.launch(headless=False)
        # browser is a variable and await is the keyword, p is a variable name, chromium is Google Chrome background engine
        page: Page = await browser.new_page()
        # my page is a variable and await is a keyword, new page is a function to open the page.
        await page.goto("https://eu.gymshark.com/")
        await expect(page).to_have_url("https://eu.gymshark.com/")
        await browser.close()

@pytest.mark.asyncio
async def test_webpage_title():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page: Page = await browser.new_page()
        await page.goto("https://eu.gymshark.com/")
        Title = await page.title()
        print("The web page title is", Title)
