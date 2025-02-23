// 2025-02-23 오후 11시
// 참가자 목록을 저장할 배열
let participants = [];

// 캔버스와 텍스트 가져오기(텍스트는 중간에 배치)
const canvas = document.getElementById('wheelCanvas');
const ctx = canvas.getContext('2d');
const centerX = canvas.width / 2; // 캔버스 중심 X 
const centerY = canvas.height / 2; // 캔버스 중심 Y
const outerRadius = Math.min(centerX, centerY) - 10; // 돌림판 반지름 계산 

// 룰렛 기본 설정
let startAngle = 0; // 시작 각도
let spinTimeout = null; // 회전 타이머
let spinAngleStart = 0; // 회전 시작 각도
let spinTime = 0; // 회전 시간
let spinTimeTotal = 0; // 총 회전 시간

// 색상 배열
const colors = [
    "#FF5733", "#33FF57", "#3357FF",
    "#FF33A1", "#A133FF", "#33FFF3",
    "#FF8F33", "#8FFF33", "#FF3333",
    "#33FF8F", "#8F33FF", "#33A1FF"
];

// 참가자 추가 함수
function addParticipants() {
    const input = document.getElementById('participantInput').value; // 입력값 가져오기
    if (input.trim() === "") {
        alert("참가자나 항목을 입력해주세요."); // 경고 메세지
        return;
    }
    // 쉼표로 배열 구분하고 저장(입력값)
    participants = input.split(',').map(item => item.trim()).filter(item => item !== "");
    drawWheel(); // 돌림판 그리기 호출
}

// 돌림판 그리기 함수
function drawWheel() {
    if (participants.length === 0) return; // 참가자 없으면 종료
    const arc = Math.PI * 2 / participants.length; // 각도 계산 (인원에 따른 배분)

    // 캔버스 초기화
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 각 섹션 그리기
    for(let i = 0; i < participants.length; i++) { 
        const angle = startAngle + i * arc; // 각도 계산
        ctx.fillStyle = colors[i % colors.length]; // 색상 설정
        ctx.beginPath(); // 경로 시작
        ctx.moveTo(centerX, centerY); // 중심 이동
        ctx.arc(centerX, centerY, outerRadius, angle, angle + arc, false); // 그리기(섹션)
        ctx.lineTo(centerX, centerY); // 중심에 선 연결
        ctx.fill(); // 채우기

        // 텍스트 그리기 (중간에 위치)
        ctx.save(); // 상태 저장
        ctx.translate(centerX, centerY); // 중심 이동 (입력값)
        ctx.rotate(angle + arc / 2); // 텍스트 각도 조정
        ctx.textAlign = "center"; // 가운데 정렬
        ctx.fillStyle = "#ffffff"; // 색상(검정)
        ctx.font = "20px Arial"; // 폰트(★좀 더 크게해도 나쁘진 않을듯★)
        ctx.fillText(participants[i], outerRadius / 2, 10); // 텍스트 위치 조정
        ctx.restore(); // 상태 복원
    }

    // 포인터 그리기(화살표)
    ctx.fillStyle = "#000000"; // 포인터 색상
    ctx.beginPath(); // 경로 시작
    ctx.moveTo(centerX - 10, centerY - (outerRadius + 20)); // 포인터 시작점
    ctx.lineTo(centerX + 10, centerY - (outerRadius + 20)); // 포인터 끝 점
    ctx.lineTo(centerX, centerY - (outerRadius - 10)); // 두번째 포인터 끝 점
    ctx.closePath(); // 경로 
    ctx.fill(); // 포인터 채우기 
}

// 스핀 시작 함수
function spinWheel() {
    if (participants.length === 0) {
        alert("참가자를 추가해주세요."); // 경고 메세지
        return;
    }
    spinAngleStart = Math.random() * 10 + 10; // 랜덤한 회전 시작 각도
    spinTime = 0; // 회전 시간 초기화
    spinTimeTotal = 7000; // 7초로 변경(1000당 1초)
    rotateWheel(); // 회전 시작
}

// 회전 애니메이션 함수
function rotateWheel() {
    spinTime += 30; // 회전 시간 증가
    if(spinTime >= spinTimeTotal){ // 끝나면
        stopRotateWheel(); // 회전 멈추기
        return; 
    }
    const spinAngle = spinAngleStart - easeOut(spinTime, 0, spinAngleStart, spinTimeTotal); // 현재 회전 각도 계산
    startAngle += (spinAngle * Math.PI / 180); // 시작 각도 업데이트 
    drawWheel(); // 돌림판 다시 그리기
    spinTimeout = setTimeout(rotateWheel, 30); // 프레임 설정 
}

// 회전 멈춤 함수
function stopRotateWheel() {
    clearTimeout(spinTimeout); // 타이머 중지 (돌아가기)
    const degrees = startAngle * 180 / Math.PI + 90; // 도 단위로 변환(각도)
    const arcd = 360 / participants.length; // 각도 계산
    const index = Math.floor((360 - (degrees % 360)) / arcd); // 선택된 인덱스 계산(플레이어)
    showResult(participants[index]); // 결과 표시
}

// 이징 함수
function easeOut(t, b, c, d) {
    t /= d; // 시간 비율 계산
    t--;
    return c * (t*t*t + 1) + b;  // 이징 효과 적용
}

// 결과 표시 함수
function showResult(selected) {
    document.getElementById('resultDisplay').innerText = `선택된 항목: ${selected}`; // 결과 텍스트 업데이트
}

// 이벤트 리스너 추가
document.getElementById('addParticipantsButton').addEventListener('click', addParticipants); // 참가자 추가 버튼 클릭 시
document.getElementById('spinButton').addEventListener('click', spinWheel); // 돌리기 버튼 클릭 시
 