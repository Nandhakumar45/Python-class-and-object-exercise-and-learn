from playwright.sync_api import Page, expect


def test_Orangeweb(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_placeholder("username").fill("Admin")
    page.get_by_placeholder("password").fill("admin123")
    page.get_by_role("button", name=" Login ").click()

    dashboard_heading = page.get_by_role("heading", name="Dashboard")

    expect.dashboard_heading = page.get_by_role("heading", name="Dashboard").to_be_visible()

    # Assertion
    expect(dashboard_heading).to_be_visible()

    # Get text
    a = dashboard_heading.text_content()

    print("The answer is:", a)

    assert a == "Dashboard"
