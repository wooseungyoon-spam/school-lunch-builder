import os
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

# 1. 환경변수(.env) 로드
load_dotenv()

# 2. Flask 백엔드 앱 생성
app = Flask(__name__)

# 3. 백엔드 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# 4. Gemini API Key 로드 및 정통 ASCII로 클리닝 (비ASCII 유니코드 및 따옴표 제거)
raw_key = os.getenv("GEMINI_API_KEY", "").strip().strip("'").strip('"')
gemini_api_key = raw_key.encode("ascii", "ignore").decode("ascii")

if not gemini_api_key or gemini_api_key == "your_gemini_api_key_here":
    logging.warning("⚠️ GEMINI_API_KEY가 설정되지 않았거나 예시 값입니다. .env 파일을 확인해 주세요.")

# 5. Gemini Client 객체 생성
client = genai.Client(api_key=gemini_api_key) if gemini_api_key else None

# 6. 메인 페이지 Route (http://127.0.0.1:5000/)
@app.route("/")
def index():
    logging.info("GET / - 메인 페이지(index.html) 접속 요청 수신")
    return render_template("index.html")

# 7. 급식 평가 AI 생성 Route (POST /generate)
@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        logging.info(f"POST /generate - 수신된 급식 데이터: {data}")

        if not data:
            logging.error("입력 검증 실패: JSON 요청 데이터가 없습니다.")
            return jsonify({"error": "요청 데이터가 올바르지 않습니다."}), 400

        grade_class = data.get("grade_class", "").strip()
        date = data.get("date", "").strip()
        menu = data.get("menu", "").strip()
        comment = data.get("comment", "").strip()
        prompt_type = data.get("prompt_type", "A").strip()

        if not grade_class:
            logging.error("입력 검증 실패: 학년/반 누락")
            return jsonify({"error": "학년/반을 입력해 주세요."}), 400

        if not date:
            logging.error("입력 검증 실패: 날짜 누락")
            return jsonify({"error": "오늘 날짜를 입력해 주세요."}), 400

        if not menu:
            logging.error("입력 검증 실패: 급식 메뉴 누락")
            return jsonify({"error": "급식 메뉴를 입력해 주세요."}), 400

        if not client or not gemini_api_key:
            logging.error("API 호출 불가: Gemini API Key 미설정")
            return jsonify({"error": ".env 파일에 GEMINI_API_KEY가 올바르게 설정되지 않았습니다."}), 500

        if prompt_type == "B":
            prompt = f"""
당신은 전문적이고 따뜻한 학교 영양사 선생님입니다.
학생들이 제출한 오늘 급식 메뉴와 소감을 바탕으로 영양학적 분석 및 따뜻한 총평 리포트를 작성해 주세요.

[급식 정보]
- 학년/반: {grade_class}
- 날짜: {date}
- 오늘 급식 메뉴: {menu}
- 학생 한줄평: {comment if comment else '별도 소감 없음'}

[출력 요구사항 - Markdown 형식]
1. 🥗 오늘의 급식 영양 균형 분석 (탄단지 및 주요 영양소)
2. 👩‍🍳 영양사 선생님의 따뜻한 피드백 코멘트
3. 💡 이 급식과 함께 먹으면 좋은 추천 저녁/간식 팁
4. ⭐ 영양사 선생님의 급식 종합 평점 (5점 만점)
"""
        else:
            prompt = f"""
당신은 위트 있고 유머러스한 AI 학생 급식 리뷰어입니다!
제공된 급식 메뉴와 학생의 한줄평을 바탕으로 재미있고 힙한 급식 총평 리포트를 작성해 주세요.

[급식 정보]
- 학년/반: {grade_class}
- 날짜: {date}
- 오늘 급식 메뉴: {menu}
- 학생 한줄평: {comment if comment else '별도 소감 없음'}

[출력 요구사항 - Markdown 형식]
1. 🍱 오늘의 급식 3줄 유머 요약
2. 🏆 오늘의 Best 메뉴 👑 vs 아쉬운 메뉴 🥈
3. 💬 학생 한줄평에 대한 AI의 재치 있는 찰떡 답글
4. 🔥 급식 맛 만족도 총평 등급 (예: SSS급 갓급식, A급 존맛 등)
"""

        logging.info("[Gemini API] 급식 평가 AI 요청 전송 중...")

        response = client.models.generate_content(
            model='gemini-3.1-flash-lite',
            contents=prompt,
        )

        result_text = response.text
        logging.info("[Gemini API] 급식 평가 결과 생성 완료")

        return jsonify({
            "status": "success",
            "result": result_text
        })

    except Exception as e:
        logging.error(f"서버 오류 발생: {str(e)}", exc_info=True)
        return jsonify({"error": f"급식 AI 평가 중 오류가 발생했습니다: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
