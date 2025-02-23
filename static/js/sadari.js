// 2025-02-23 오후 9시
let players = []; // 플레이어 입력 (변수 재선언 안되게 하려고 let 사용)
let results = []; // 결과값 입력
let horizontalLines = []; // 수평선 저장 배열 (수평선 = 사다리 가로줄)
const lineHeight = 8; // 수평선 높이
const verticalMargin = 30; // 세로줄 간격(공과 세로줄의 어색함을 지우기 위해 넣음)
const ballSpacing = 65; // 공 간격을 65픽셀로 설정

// 미리 정해진 색상 배열(빨,주,노,초,청,파,보,핑,검,흰)
const colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#7F00FF', '#FF00FF', '#000000', '#FFFFFF'];

// 사다리 생성 함수
function generateLadder() {
    const container = document.getElementById('ladder-container'); // 사다리 컨테이너 
    container.innerHTML = '';  // 이전 내용 초기화
    horizontalLines = []; // 수평선 배열 초기화

    const count = parseInt(document.getElementById('playerCount').value); // 참가자 수 가져오기
    if (count < 2 || count > 10) { // 범위 확인
        alert('2에서 10명까지 가능합니다.'); //경고 메세지 (try 써도 될듯..? 고려 사안)
        return;
    }
    // 게임 초기화 기능
    document.getElementById('names').innerHTML = ''; // 참가자 이름 입력
    document.getElementById('results').innerHTML = ''; // 결과 입력
    players = []; // 플레이어
    results = []; // 결과 배열

    // 참가자 이름 및 결과 입력 필드 생성
    for (let i = 0; i < count; i++) { 
        const nameInput = document.createElement('input'); // 이름 입력 (생성)
        nameInput.type = 'text'; 
        nameInput.placeholder = `참가자 ${i + 1}`; // 플레이어 자리 표시자
        nameInput.className = 'name-input'; // 클래스 이름
        document.getElementById('names').appendChild(nameInput); // 이름 입력 (추가) 

        const resultInput = document.createElement('input'); // 결과 입력 (생성)
        resultInput.type = 'text'; 
        resultInput.placeholder = `결과 ${i + 1}`; // 결과 자료 표시자
        resultInput.className = 'result-input'; // 클래스 이름
        document.getElementById('results').appendChild(resultInput); // 결과 입력 (추가)
    }

    // 세로줄 생성
    for (let i = 0; i < count; i++) {
        const line = document.createElement('div'); // 생성
        line.className = 'vertical-line'; // 이름 설정 (세로줄)
        container.appendChild(line); // 세로줄 추가
    }

    // 수평선 랜덤 생성 (가로줄)
    for (let i = 0; i < count - 1; i++) {
        const numLines = Math.floor(Math.random() * 3) + 1; // 1~3 사이 랜덤 생성
        for (let j = 0; j < numLines; j++) { 
            const position = Math.random() * (550 - (lineHeight * (count - 1) + 10 * (numLines - 1))) + (20 + (lineHeight * j) + 10 * j); // 수평선 위치 계산 (오류 방지를 위한 최소 간격 10px)
            const horizontal = document.createElement('div'); // 수평선 생성
            horizontal.className = 'horizontal-line'; // 클래스 이름
            horizontal.style.top = `${Math.floor(position)}px`; // 위치 설정

            // 3번째 가로줄부터 5픽셀 오른쪽으로 이동 (★위치 맞추려고 하고 있는데 수정 필요★)
            if (i >= 2) { 
                horizontal.style.left = `${65 + i * 60}px`; // 3번째부터 오른쪽으로 이동
            } else {
                horizontal.style.left = `${60 + i * 60}px`; // 기본 위치
            }
            
            container.appendChild(horizontal); // 수평선 추가 
            horizontalLines.push({ x: i, y: Math.floor(position) }); // 수평선 위치 저장
        }
    }
}
// 게임 시작 함수
function startGame() {
    const container = document.getElementById('ladder-container'); // 사다리 선택
    const count = parseInt(document.getElementById('playerCount').value); // 참가자 "수" 입력값 가져오기

    // 참가자 "이름", 결과 배열 생성
    players = Array.from(document.querySelectorAll('.name-input')).map(el => el.value || 'Player'); // 이름 배열
    results = Array.from(document.querySelectorAll('.result-input')).map(el => el.value || 'Result'); // 결과 배열 

    // 미리 정의된 색상을 사용하여 공 생성
    for (let i = 0; i < count; i++) {
        const ball = document.createElement('div'); // 공 생성
        ball.className = 'ball'; // 클래스 이름 설정 

        // 공의 위치를 세로줄에 맞게 조정
        ball.style.left = `${60 + i * ballSpacing}px`; // 공 간격을 65픽셀로 설정

        ball.style.backgroundColor = colors[i]; // 고유 색상 사용
        container.appendChild(ball); // 공 추가

        // 공의 시작 위치를 세로줄에 맞게 조정 (y=0 위치 시작)
        ball.style.top = `0px`; // 세로줄 위치에 맞춤
        moveBall(ball, i); // 공 이동 함수 호출
    }
}
// 공 이동 함수 
function moveBall(ball, index) {
    let x = index; // 현재 세로줄 인덱스
    let y = 0; // 현재 y 위치

    const interval = setInterval(() => {
        y += 5; // y 위치 증가시키기
        ball.style.top = `${y}px`; // 위치 업데이트(y)

        // 다음 수평선 확인
        const nextLineRight = horizontalLines.find(line => line.x === x && Math.abs(line.y - y) < 5); // 오른쪽
        const nextLineLeft = horizontalLines.find(line => line.x === x - 1 && Math.abs(line.y - y) < 5); // 왼쪽

        // 오른쪽, 왼쪽 이동
        if (nextLineRight) {
            x += 1; // 이동
            ball.style.left = `${60 + x * ballSpacing}px`; // 공 간격을 65픽셀로 설정
            } else if (nextLineLeft) {
            x -= 1; // 이동
            ball.style.left = `${60 + x * ballSpacing}px`; // 공 간격을 65픽셀로 설정
        }
        // 공 바닥으로 도달했으면
        if (y >= 600) { // 높이에 맞춰 조정
            clearInterval(interval);
            alert(`${players[index]}의 결과: ${results[x]}`); // 결과 호출 (★방식을 수정하는 방향도 고려★)
        }
    }, 100);
}
