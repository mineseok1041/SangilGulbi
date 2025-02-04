let notes = [];
let lanes = [100, 200, 300, 400]; // A, S, D, F 키의 x 좌표
let noteSpeed = 5; // 기본 속도 (2~10 조절 가능)
let score = 0;
let combo = 0;
let missCount = 0;
let maxMisses = 10;
let threshold = 0.25;
let lastNoteTime = 0;
let musicLoaded = false;
let audioPlayer;
let audioContext, analyser, dataArray;
let lastJudgment = "";
let judgmentTime = 0;
let judgmentEffects = [];
let startScreen = true;
let gameOverScreen = false;
let highScore = 0; // 최고 점수 저장 변수

function setup() {
  createCanvas(600, 800);
  textAlign(LEFT, TOP);
  audioPlayer = document.getElementById("audioPlayer");
  document.getElementById("audioFile").addEventListener("change", handleFile);
  initAudioAnalysis();

  // 속도 조정 버튼 추가
  let speedUpBtn = createButton("+ Speed");
  speedUpBtn.position(width - 90, 100); // 우측 상단 배경 위
  speedUpBtn.style("background-color", "#333"); // 검정 배경과 어울리도록
  speedUpBtn.style("color", "white");
  speedUpBtn.style("border", "none");
  speedUpBtn.style("padding", "5px 10px");
  speedUpBtn.mousePressed(increaseSpeed);

  let speedDownBtn = createButton("- Speed");
  speedDownBtn.position(width - 180, 100); // 우측 상단 배경 위
  speedDownBtn.style("background-color", "#333");
  speedDownBtn.style("color", "white");
  speedDownBtn.style("border", "none");
  speedDownBtn.style("padding", "5px 10px");
  speedDownBtn.mousePressed(decreaseSpeed);
}

function increaseSpeed() {
  if (noteSpeed < 10) {
    noteSpeed += 1;
  }
}

function decreaseSpeed() {
  if (noteSpeed > 2) {
    noteSpeed -= 1;
  }
}

function initAudioAnalysis() {
  audioContext = new (window.AudioContext || window.webkitAudioContext)();
  let source = audioContext.createMediaElementSource(audioPlayer);
  analyser = audioContext.createAnalyser();
  analyser.fftSize = 512;
  source.connect(analyser);
  analyser.connect(audioContext.destination);
  dataArray = new Uint8Array(analyser.frequencyBinCount);
}

function handleFile(event) {
  let file = event.target.files[0];
  if (file) {
    let fileURL = URL.createObjectURL(file);
    audioPlayer.src = fileURL;
    audioPlayer.play();
    musicLoaded = true;
    startScreen = false;
    if (audioContext.state === "suspended") {
      audioContext.resume();
    }
  }
}

class Note {
  constructor(lane) {
    this.x = lanes[lane];
    this.y = 0;
    this.hit = false;
    this.missEffect = 0;
  }

  move() {
    if (!this.hit) {
      this.y += noteSpeed; // 노트 속도 적용
    }
  }

  display() {
    if (this.missEffect > 0) {
      fill(255, 0, 0, this.missEffect);
      this.missEffect -= 10;
    } else {
      fill(random(100, 255), random(100, 255), random(100, 255));
    }
    rect(this.x, this.y, 80, 20);
  }
}

function draw() {
  background(0);

  if (startScreen) {
    fill(255);
    textSize(32);
    textAlign(CENTER, CENTER);
    text("Press SPACE to Start", width / 2, height / 2);
    return;
  }

  if (gameOverScreen) {
    if (score > highScore) {
      highScore = score;
    }
    fill(255, 0, 0);
    textSize(32);
    textAlign(CENTER, CENTER);
    text("Game Over!", width / 2, height / 2 - 50);
    textSize(24);
    text("Final Score: " + score, width / 2, height / 2);
    text("High Score: " + highScore, width / 2, height / 2 + 30); // 최고 점수 표시
    text("Press R to Restart", width / 2, height / 2 + 50);
    return;
  }

  fill(255);
  textSize(24);
  textAlign(LEFT, TOP);
  text("Score: " + score, 20, 20);
  text("Combo: " + combo, 20, 50);
  text("Miss: " + missCount + " / " + maxMisses, 20, 80);
  text("Speed: " + noteSpeed, 20, 140); // 현재 속도 표시
  text("High Score: " + highScore, 20, 170); // 최고 점수 항상 표시

  // 🟢 판정 바 복구 (항상 표시)
  fill(255);
  for (let i = 0; i < lanes.length; i++) {
    rect(lanes[i], 750, 80, 10);
  }

  // 🟢 판정 이펙트 복구
  for (let i = judgmentEffects.length - 1; i >= 0; i--) {
    let effect = judgmentEffects[i];
    fill(effect.color);
    ellipse(effect.x, effect.y, effect.size);
    effect.x += effect.vx;
    effect.y += effect.vy;
    effect.size *= 0.95;
    effect.alpha -= 5;
    if (effect.alpha <= 0) {
      judgmentEffects.splice(i, 1);
    }
  }

  analyser.getByteFrequencyData(dataArray);
  let volume = getAverageVolume(dataArray);

  if (volume > threshold * 255 && millis() - lastNoteTime > 300) {
    let laneIndex = floor(random(0, 4));
    notes.push(new Note(laneIndex));
    lastNoteTime = millis();
  }

  for (let i = notes.length - 1; i >= 0; i--) {
    notes[i].move();
    notes[i].display();
    if (notes[i].y > 770 && !notes[i].hit) {
      notes[i].missEffect = 255;
      score -= 10;
      combo = 0;
      missCount++; // Miss 카운트 증가
      lastJudgment = "Miss";
      judgmentTime = 45;

      if (missCount >= maxMisses) {
        gameOverScreen = true;
      }

      notes[i].hit = true;
    }

    if (
      (notes[i].missEffect <= 0 && notes[i].hit) ||
      notes[i].y > height + 50
    ) {
      notes.splice(i, 1);
    }
  }
}

function getAverageVolume(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }
  return sum / array.length;
}

function keyPressed() {
  if (startScreen && keyCode === 32) {
    startScreen = false;
    return;
  }

  if (gameOverScreen && keyCode === 82) {
    score = 0;
    combo = 0;
    missCount = 0;
    notes = [];
    gameOverScreen = false;
    return;
  }

  let keyMap = {
    65: 0,
    83: 1,
    68: 2,
    70: 3,
  };

  if (keyMap[keyCode] !== undefined) {
    let laneIndex = keyMap[keyCode];

    for (let i = 0; i < notes.length; i++) {
      if (notes[i].x === lanes[laneIndex] && !notes[i].hit) {
        let noteY = notes[i].y;

        if (noteY >= 730 && noteY <= 770) {
          score += 100;
          combo++;
          lastJudgment = "Perfect";
        } else if (noteY >= 710 && noteY <= 790) {
          score += 50;
          combo++;
          lastJudgment = "Good";
        } else {
          continue;
        }

        for (let j = 0; j < 10; j++) {
          judgmentEffects.push({
            x: notes[i].x + 40,
            y: 750,
            size: random(10, 20),
            vx: random(-2, 2),
            vy: random(-3, -1),
            alpha: 255,
            color: color(
              random(100, 255),
              random(100, 255),
              random(100, 255),
              255
            ),
          });
        }

        judgmentTime = 45;
        notes[i].hit = true;
        notes.splice(i, 1);
        break;
      }
    }
  }
}
