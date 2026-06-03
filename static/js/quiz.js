async function submitAnswer() {
    const userAnswer = document.getElementById("user-answer").value;

    const response = await fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_answer: userAnswer
        })
    });

    const data = await response.json();
    console.log(data);

    // 얼굴 전체 공개
    document.getElementById("quiz-image").src = data.full_image;

    // 결과 표시
    const resultBox = document.getElementById("result-box");

    // -----------------------------
    // 코드네임 분리 처리
    // ex) Bourbon(버번)
    // -----------------------------
    let codeKo = "";
    let codeEn = "";

    if (data.code_name && data.code_name !== 'n') {

        if (data.code_name.includes("(")) {

            codeEn = data.code_name.split("(")[0].trim();

            codeKo = data.code_name
                .split("(")[1]
                .replace(")", "")
                .trim();
        }
    }

    // -----------------------------
    // 한글 정답
    // -----------------------------
    const koAnswer = codeKo && codeKo !== data.ko_name
        ? `${codeKo} ${data.ko_name}`
        : data.ko_name;

    // -----------------------------
    // 영어 정답
    // -----------------------------
    const enAnswer = codeEn && codeEn !== data.en_name
        ? `${codeEn} ${data.en_name}`
        : data.en_name;

    // -----------------------------
    // 최종 출력 문자열
    // -----------------------------
    const answerText = data.en_name
        ? `${koAnswer}<br>(${enAnswer})`
        : koAnswer;

    // -----------------------------
    // 정답 / 오답 표시
    // -----------------------------
    if (data.is_correct) {

        resultBox.innerHTML =
            `<h2 class="text-success fw-bold">정답입니다!</h2>`;

    } else {

        resultBox.innerHTML =
            `<h2 class="text-danger fw-bold">틀렸습니다!</h2>
            <p class="text-warning fs-5">
                정답: <strong>${answerText}</strong>
            </p>`;
    }

    // 제출 버튼 숨기기
    document.getElementById("submit-btn").style.display = "none";

    // 다음 버튼 표시
    document.getElementById("next-btn").style.display = "block";
}

async function nextQuiz() {

    const response = await fetch('/next_quiz');
    const data = await response.json();

    // 게임 종료
    if (data.game_end) {

        alert(`게임 종료!\n점수 : ${data.score}`);
        window.location.href = "/";
        return;
    }

    // 눈 사진 교체
    document.getElementById("quiz-image").src = data.eye_image;

    // 입력창 초기화
    document.getElementById("user-answer").value = "";

    // 결과창 초기화
    document.getElementById("result-box").innerHTML = "";

    // 버튼 상태 초기화
    document.getElementById("next-btn").style.display = "none";

    document.getElementById("submit-btn").style.display = "block";
}