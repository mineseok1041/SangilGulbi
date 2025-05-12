-- 상점 항목 (bonus)
INSERT INTO pointReason (no, reason, value, type) VALUES (101, '솔선하여 휴지를 줍는 행위', 1, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (102, '분실된 교구, 분실물을 습득하여 타의 모범이 된 학생', 2, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (103, '솔선하여 청소를 하거나 복도 교실주변의 껌을 제거한 학생', 2, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (104, '특별실 관리 및 학교 학급활동에 모범이 되어 담당교사의 추천을 받은 학생', 3, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (105, '수업에서 교재 교구 기자재 관리 및 안전관리에 모범적인 행동을 한 학생', 3, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (106, '학습 준비물을 철저히 준비하여 수업 보조도구로 활용되도록 한 학생', 4, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (107, '방과 후 업무 보조 및 환경정화 활동을 적극적으로 한 학생', 3, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (108, '방과 후 업무 보조 및 환경정화 활동을 적극적으로 한 학생', 4, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (109, '학교의 명예를 높인 학생 (경중에 따라 상벌점 운영소위원회에서 심의 후 부여)', 3, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (110, '학교의 명예를 높인 학생 (경중에 따라 상벌점 운영소위원회에서 심의 후 부여)', 4, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (111, '학교의 명예를 높인 학생 (경중에 따라 상벌점 운영소위원회에서 심의 후 부여)', 5, 'bonus');
INSERT INTO pointReason (no, reason, value, type) VALUES (112, '선행 효행 단체활동 불우이웃돕기 일손 돕기 등의 봉사활동을 하여 공인된 외부 기관에서 모범표창을 받았거나 이와 상응한 경우', 5, 'bonus');

-- 벌점 항목 (penalty)
INSERT INTO pointReason (no, reason, value, type) VALUES (201, '명찰 미착용', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (202, '교복 착용상태 불량 및 임의 변형', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (203, '미인정결석 및 미인정조퇴 행위', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (204, '미인정 지각 및 미인정결과 행위', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (205, '보행 중 음식물 취식 및 교실 반입 행위', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (206, '등·하굣길 통행 위반한 행위', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (207, '실내에서 소란스런 행동을 한 경우', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (208, '쓰레기 무단투기 및 껌과 가래침을 실내에서 뱉는 행위', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (209, '청소 활동에 참여하지 않은 경우', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (210, 'SNS, 메신저 등을 이용하여 협박, 허위 사실 등을 유포하거나 타인 또는 학교의 명예를 훼손한 학생', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (211, '불온 문서(불법 동영상 등 포함)를 은닉, 탐독, 제작, 게시 또는 유포한 학생', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (212, '월담 행위', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (213, '학교 단체 행사에 무단 또는 고의적으로 참가하지 않는 경우', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (214, '수업시간 중에 무단으로 교문 출입행위', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (215, '위 항목 외 선도규정의 훈계에 해당한 경우', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (216, '수업 태도가 불령하거나, 면학 분위기를 저해하는 행위(수업 중 스마트폰 사용 등)', -4, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (217, '학교 시설물 등에 낙서하거나 훼손하는 행위', -4, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (218, '라이터, 담배 또는 흉기를 소지한 경우', -4, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (219, '무단으로 현장실습 업체에서 이탈하거나 결근한 경우', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (220, '경고 행위 적발 시 타인의 이름을 도용하거나 도주한 경우', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (221, '교사의 정당한 지시에 따르지 않는 경우', -7, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (222, '학교 내·외에서 음주 및 흡연을 하였거나, 증거가 확실한 경우', -10, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (223, '몸의 일부에 문신을 한 경우', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (224, '규정위반으로 처벌 기간 중 미인정 결석 및 결과 한 경우', -4, 'penalty');

commit;
