# ✨ AI Resume & Portfolio Builder

> 사용자의 정보(이름, 지원 직무, 경력, 프로젝트, Tone)를 바탕으로 Google Gemini AI가 이력서와 포트폴리오 초안을 자동으로 생성해 주는 웹 애플리케이션입니다.

---

## 📌 주요 기능 (Key Features)

1. **사용자 정보 입력 폼**: 이름, 지원 직무, 상세 경력 사항, 주요 프로젝트, 톤앤매너 설정
2. **다양한 생성 방식 (프롬프트 선택)**:
   - **Prompt A (일반 모드)**: 정갈하고 가독성 높은 표준 이력서 & 포트폴리오
   - **Prompt B (전문가 STAR 모드)**: 수치, 성과 및 문제 해결 과정 중심의 임팩트 있는 전문 문서
3. **Google Gemini API 연동**: 최신 `gemini-3.1-flash-lite` 모델 활용
4. **결과 활용 기능**:
   - **📋 원클릭 결과 복사**: 생성된 마크다운 결과를 클립보드로 직접 복사
   - **📥 Markdown 파일 다운로드**: `홍길동_이력서_포트폴리오.md` 파일 저장
5. **안전한 보안 관리**: `.env` 파일과 `.gitignore`를 활용한 API Key 유출 방지
6. **유효성 검사 및 에러 처리**: 프론트엔드와 백엔드 양방향 입력값 검증 및 친절한 에러 안내
7. **모던 UX/UI**: 다크 모드 테마, 동적 로딩 스피너, 실시간 마크다운 HTML 렌더링

---

## 📁 프로젝트 파일 구조 (Directory Structure)

```text
resume-builder/
├── app.py                     # Flask 백엔드 서버 (Gemini API 호출 및 라우팅)
├── requirements.txt           # 파이썬 패키지 의존성 목록
├── .env                       # 비밀 Gemini API Key 저장 파일 (Git 제외)
├── .env.example               # 환경변수 예시 템플릿
├── .gitignore                 # Git 관리 제외 파일 지정 목록
├── README.md                  # 프로젝트 설명 문서
├── venv/                      # 독립된 파이썬 가상환경 폴더
├── templates/
│   └── index.html             # 메인 입력 폼 및 결과 표시 웹 화면
└── static/
    ├── css/
    │   └── style.css          # 다크 테마 및 반응형 레이아웃 CSS
    └── js/
        └── app.js             # API 통신, 로딩, 복사/다운로드 처리 JS
```

---

## 🛠️ 기술 스택 (Tech Stack)

- **Backend**: Python 3.14, Flask 3.0.3, `google-genai` SDK, `python-dotenv`
- **Frontend**: HTML5, Vanilla CSS3 (Custom Dark Theme), Vanilla JavaScript (ES6+)
- **AI Model**: Google Gemini (`gemini-3.1-flash-lite`)
- **Libraries**: Marked.js (Markdown HTML Parsing)
- **Version Control**: Git

---

## 🚀 실행 방법 (Getting Started)

### 1. 가상환경 활성화 (PowerShell)
```powershell
Set-Location "C:\AI-study\resume-builder"
.\venv\Scripts\Activate.ps1
```

### 2. 필수 패키지 설치 (최초 1회)
```powershell
py -m pip install -r requirements.txt
```

### 3. `.env` 파일 설정
`resume-builder` 루트 폴더의 `.env` 파일에 [Google AI Studio](https://aistudio.google.com/)에서 발급받은 실제 API 키를 입력합니다.
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
FLASK_SECRET_KEY=dev_secret_key_987654321
```

### 4. 서버 구동
```powershell
py app.py
```

### 5. 웹 브라우저 접속
주소창에 아래 주소를 입력하여 접속합니다.
- 👉 **`http://127.0.0.1:5000`**

---

## 📝 라이선스 (License)

This project is created for educational purposes.
