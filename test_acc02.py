from playwright.sync_api import Page, expect
from helpers import login, add_user, try_access

def test_acc02_access_denied(page: Page):
    # 사전조건
    login(page)
    add_user(page, "홍길동", "A001", "정문")
    # Step: A001로 인증, 연구동 문, 10:00에 출입 시도
    try_access(page, "A001", "연구동", "10:00")
    # 기대 결과: 출입 거부, 연구동 문 잠김, 이벤트 로그 1건 (거부)
    expect(page.get_by_test_id("access-result")).to_have_text("E-002 출입 권한이 없습니다")
    expect(page.get_by_test_id("door-lab-status")).to_have_text("잠김")
    expect(page.get_by_test_id("event-row")).to_have_count(1)
    expect(page.get_by_test_id("event-row")).to_contain_text("E-002")