from playwright.sync_api import Page, expect
from helpers import login, add_user, try_access

def test_acc03_time_boundary(page: Page):
    # 사전조건:
    login(page)
    add_user(page, "홍길동", "A001", "연구동")
    # Step 1: 18:00 출입 시도
    try_access(page, "A001", "연구동", "18:00")

    # 기대 결과 ①: 출입 허용, 연구동 문 열림, 이벤트 로그 1건 (허용)
    expect(page.get_by_test_id("access-result")).to_have_text("출입 허용")
    expect(page.get_by_test_id("door-lab-status")).to_have_text("열림")
    expect(page.get_by_test_id("event-row")).to_have_count(1)
    expect(page.get_by_test_id("event-row")).to_contain_text("허용")

    # Step 2: 18:01 출입 시도
    try_access(page, "A001", "연구동", "18:01")
    # 기대 결과 ②: 출입 거부, 연구동 문 잠김, 이벤트 로그 2건 (거부)
    expect(page.get_by_test_id("access-result")).to_have_text("E-003 출입 허용 시간이 아닙니다")
    expect(page.get_by_test_id("door-lab-status")).to_have_text("잠김")
    expect(page.get_by_test_id("event-row").first).to_contain_text("E-003")
    # 기대 결과 ③: 로그 이벤트 로그 2건 (거부)
    expect(page.get_by_test_id("event-row")).to_have_count(2)