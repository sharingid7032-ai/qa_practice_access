from pathlib import Path
from playwright.sync_api import Page

APP_URL = (Path(__file__).parent / "practice_app.html").resolve().as_uri()


def login(page: Page):
    page.goto(APP_URL)
    page.get_by_test_id("login-id").fill("admin")
    page.get_by_test_id("login-pw").fill("Test1234!")
    page.get_by_test_id("login-btn").click()


def add_user(page: Page, name, no, group="정문"):
    page.get_by_test_id("user-name").fill(name)
    page.get_by_test_id("user-no").fill(no)
    page.get_by_test_id("user-group").select_option(group)
    page.get_by_test_id("save-btn").click()


def try_access(page: Page, no, door, time):
    page.get_by_test_id("access-user-no").fill(no)
    page.get_by_test_id("access-door").select_option(door)
    page.get_by_test_id("access-time").fill(time)
    page.get_by_test_id("access-btn").click()
