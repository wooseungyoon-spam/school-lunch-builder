# 🍱 AI 학교 급식 예측 & 평가 리포트 웹앱 (School Lunch Review Builder)

> 오늘 먹은 학교 급식 메뉴와 한줄평을 입력하면 Google Gemini AI가 재치 있는 유머 요약(Prompt A) 또는 영양사 선생님의 전문 영양 분석(Prompt B) 리포트를 자동으로 생성해 주는 Flask 기반 웹 애플리케이션입니다.

---

## 📌 주요 기능 (Key Features)

1. **급식 정보 입력 폼**: 학년/반, 오늘 날짜, 급식 메뉴, 나만의 한줄평/소감 입력
2. **다양한 생성 방식 (프롬프트 선택)**:
   - **🎉 Prompt A (유머 만발)**: 3줄 유머 요약, Best vs 아쉬운 메뉴 선정, AI 찰떡 답글, 급식 만족도 등급
   - **👩‍🍳 Prompt B (영양사 톤)**: 탄단지 영양 균형 분석, 영양사 피드백, 추천 저녁/간식 팁, 종합 평점
3. **Google Gemini API 연동**: 최신 `gemini-3.1-flash-lite` AI 모델 활용
4. **결과 활용 기능**:
   - **📋 원클릭 결과 복사**: 생성된 리포트 마크다운 결과를 클립보드로 복사
   - **📥 Markdown 파일 다운로드**: `급식_평가_리포트_날짜.md` 파일 저장
5. **안전한 보안 관리**: `.env` 파일과 `.gitignore`를 활용한 API Key 유출 방지
6. **유효성 검사 및 에러 처리**: 프런트엔드와 백엔드 양방향 입력값 검증 및 상세 로깅
7. **모던 UX/UI**: 상큼한 급식 테마 디자인, 로딩 스피너 애니메이션, 실시간 마크다운 HTML 렌더링

---

## 📁 프로젝트 파일 구조 (File Structure)

```text
school-lunch-builder/
├── app.py                  # Flask 백엔드 서버 & Gemini API 호출 로직
├── requirements.txt        # 필요한 Python 패키지 목록
├── .env                    # 비밀 Gemini API Key 보관 (Git 제외)
├── .env.example            # 환경변수 예시 템플릿
├── .gitignore              # Git 무시 파일 목록 (.env, venv 등)
├── README.md               # 프로젝트 안내 문서
├── templates/
│   └── index.html          # 급식 리뷰 메인 HTML 화면
└── static/
    ├── css/
    │   └── style.css       # 급식 앱 디자인 스타일시트
    └── js/
        └── app.js          # 비동기 API 요청 및 UI 제어 JavaScript
```

---

## 🛠️ 기술 스택 (Tech Stack)

- **Backend**: Python 3.14+, Flask, python-dotenv
- **AI Engine**: Google Gemini API (`google-genai` SDK, `gemini-3.1-flash-lite`)
- **Frontend**: HTML5, Vanilla CSS3, JavaScript (ES6+), Marked.js

---

## 🚀 실행 방법 (Getting Started)

1. **가상환경 생성 및 활성화**:
   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **필요 패키지 설치**:
   ```powershell
   py -m pip install -r requirements.txt
   ```

3. **환경변수 설정 (`.env`)**:
   - `.env` 파일을 생성하고 발급받은 Gemini API Key를 입력합니다.
   ```text
   GEMINI_API_KEY=your_actual_gemini_api_key
   ```

4. **Flask 웹 서버 실행**:
   ```powershell
   py app.py
   ```
   - 브라우저에서 `http://127.0.0.1:5000` 으로 접속합니다.
