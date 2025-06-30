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
INSERT INTO pointReason (no, reason, value, type) VALUES (202, '교복 착용 상태 불량 빛 임의 변형', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (203, '교복(교복 규정) 미착용', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (204, '슬리퍼, 굽 높은 신발 착용', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (205, '신체에 피어싱한 경우', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (206, '보행 중 음식물 취식 및 교실(실습실) 반입 행위', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (207, '학교 게시물을 고의로 훼손하거나 학교 기물을 파손한 학생', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (208, '교사의 주의에도 불구하고 실내에서 소란스런 행동을 한 경우', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (209, '쓰레기 투기 및 껌과 가래침을 뱉는 행위', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (210, '청소 활동에 참여하지 않는 경우', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (211, '지나친 욕설과 불손한 언행을 하는 경우', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (212, '불량만화, 잡지, 영상물을 소지하거나 보는 행위', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (213, '사행성 물품을 소지하거나 사행성 오락 및 도박을 한 학생', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (214, '월당 행위(교문 외 다른 곳으로 등,하교 한 학생)', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (215, '학교 단체 행사에 미인정 또는 고의로 참가하지 않는 경우', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (216, '수업 태도가 불량하거나, 면학 분위기를 저해하는 행위', -4, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (217, '지속해서 수업 준비 및 태도가 불량한 학생', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (218, '주의에도 불구하고 수업 또는 타인의 학생을 방해한 학생', -4, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (219, '학교 시설물 등에 낙서하는 행위', -4, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (220, '경고 행위 적발 시 타인의 이름을 도용하거나 도주한 경우', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (221, '불건전한 이성 교제 및 신체 접촉 등으로 풍기를 문란하게 한 학생', -3, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (222, '흉기와 학생 금지 물품을 소지한 경우', -10, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (223, '사이버 통신예절을 지키지 않아 다른 학생에게 피해를 준 학생', -4, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (224, '실습 시간 및 교실에서 컴퓨터 사용 시 교육 외의 목적으로 이용한 학생', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (225, '학생에서 통신매체를 이용하여 사행성 프로그램에 접속하였거나 도박을 한 학생', -10, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (226, '교내에서 도색잡지 소지 및 음란 사이트 접속하거나 배포한 학생', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (227, '인원(출석) 점검 시 대리로 대답한 학생', -10, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (228, '황당한 이유 없이 미인정 지각한 경우', -1, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (229, '미인정으로 조퇴, 결과, 외출한 경우', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (230, '합당한 이유 없이 미인정 결석한 경우', -2, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (231, '학생 생활 규정에 따른 교사의 정당한 지도에 불응한 학생', -10, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (232, '라이터 또는 담배(전자담배), 주류를 소지한 경우', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (233, '학교 내에서 흡연하였거나, 흡연한 증거가 확실한 경우', -10, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (234, '학교 내에서 음주하였거나, 음주한 증거가 확실한 경우', -10, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (235, '학교 외에서 흡연하였거나, 흡연한 증거가 확실한 경우', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (236, '학교 외에서 음주하였거나, 음주한 증거가 확실한 경우', -5, 'penalty');
INSERT INTO pointReason (no, reason, value, type) VALUES (237, '위 항목 외 학생 생활 규정의 훈계에 해당한 경우', -3, 'penalty');

DELETE FROM pointReason WHERE type = 'penalty';

commit;
