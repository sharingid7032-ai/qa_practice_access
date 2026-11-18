from playwright.sync_api import Page, expect
from helpers import login, add_user, try_access


def test_acc01_access_allowed(page: Page):
    # 사전조건: 로그인, 연구동 그룹 사용자 홍길동 / A001 등록
    login(page)
    add_user(page, "홍길동", "A001", "연구동")

    # Step: A001로 인증, 연구동 문, 10:00에 출입 시도
    try_access(page, "A001", "연구동", "10:00")

    # 기대 결과: 출입 허용, 연구동 문 열림, 이벤트 로그 1건 (허용)
    expect(page.get_by_test_id("access-result")).to_have_text("출입 허용")
    expect(page.get_by_test_id("door-lab-status")).to_have_text("열림")
    expect(page.get_by_test_id("event-row")).to_have_count(1)
    expect(page.get_by_test_id("event-row")).to_contain_text("허용")
