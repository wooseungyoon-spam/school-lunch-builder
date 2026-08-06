 document.addEventListener("DOMContentLoaded", () => {
        // 1. 급식 평가용 HTML 요소 가져오기
        const lunchForm = document.getElementById("lunchForm");
        const gradeClassInput = document.getElementById("gradeClass");
        const dateInput = document.getElementById("date");
        const menuInput = document.getElementById("menu");
        const commentInput = document.getElementById("comment");
        const submitBtn = document.getElementById("submitBtn");

        const errorMessage = document.getElementById("errorMessage");
        const loadingArea = document.getElementById("loadingArea");
        const resultArea = document.getElementById("resultArea");
        const resultContent = document.getElementById("resultContent");

        const copyBtn = document.getElementById("copyBtn");
        const downloadBtn = document.getElementById("downloadBtn");

        let rawResultText = "";

        // 오늘 날짜 자동 입력
        if (dateInput && !dateInput.value) {
            const today = new Date().toISOString().split("T")[0];
            dateInput.value = today;
        }

        // 2. 폼 제출 이벤트 처리
        lunchForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            hideError();
            resultArea.classList.add("hidden");

            const gradeClass = gradeClassInput.value.trim();
            const date = dateInput.value.trim();
            const menu = menuInput.value.trim();
            const comment = commentInput.value.trim();

            const promptTypeRadio = document.querySelector('input[name="prompt_type"]:checked');
            const promptType = promptTypeRadio ? promptTypeRadio.value : "A";

            // [급식 앱 전용 입력 검증]
            if (!gradeClass) {
                showError("학년/반을 입력해 주세요.");
                gradeClassInput.focus();
                return;
            }

            if (!date) {
                showError("오늘 날짜를 입력해 주세요.");
                dateInput.focus();
                return;
            }

            if (!menu) {
                showError("오늘의 급식 메뉴를 입력해 주세요.");
                menuInput.focus();
                return;
            }

            showLoading(true);

            try {
                const response = await fetch("/generate", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        grade_class: gradeClass,
                        date: date,
                        menu: menu,
                        comment: comment,
                        prompt_type: promptType
                    }),
                });

                const data = await response.json();

                if (!response.ok || data.error) {
                    throw new Error(data.error || "서버 응답 오류가 발생했습니다.");
                }

                rawResultText = data.result;

                if (typeof marked !== "undefined") {
                    resultContent.innerHTML = marked.parse(rawResultText);
                } else {
                    resultContent.innerText = rawResultText;
                }

                resultArea.classList.remove("hidden");
                resultArea.scrollIntoView({ behavior: "smooth" });

            } catch (error) {
                console.error("오류:", error);
                showError(error.message || "서버 요청 처리 중 에러가 발생했습니다.");
            } finally {
                showLoading(false);
            }
        });

        // 3. 복사 버튼
        copyBtn.addEventListener("click", () => {
            if (!rawResultText) return;
            navigator.clipboard.writeText(rawResultText)
                .then(() => {
                    const orig = copyBtn.innerText;
                    copyBtn.innerText = "✅ 복사 완료!";
                    setTimeout(() => { copyBtn.innerText = orig; }, 2000);
                })
                .catch(() => alert("복사에 실패했습니다."));
        });

        // 4. 마크다운 다운로드 버튼
        downloadBtn.addEventListener("click", () => {
            if (!rawResultText) return;
            const blob = new Blob([rawResultText], { type: "text/markdown;charset=utf-8;" });
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = url;
            link.setAttribute("download", `급식_평가_리포트_${dateInput.value || "today"}.md`);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        });

        function showError(msg) {
            errorMessage.innerText = `⚠️ ${msg}`;
            errorMessage.classList.remove("hidden");
        }

        function hideError() {
            errorMessage.innerText = "";
            errorMessage.classList.add("hidden");
        }

        function showLoading(isLoading) {
            if (isLoading) {
                loadingArea.classList.remove("hidden");
                submitBtn.disabled = true;
            } else {
                loadingArea.classList.add("hidden");
                submitBtn.disabled = false;
            }
        }
    });