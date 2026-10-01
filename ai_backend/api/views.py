import os
from dotenv import load_dotenv
from google import genai
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

candidate_models = [
    "gemini-3.5-flash",
    "gemini-2.0-flash-lite",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
]


@api_view(["POST"])
def ask_gemini_ai(request):
    user_prompt = request.data.get("prompt")

    if not user_prompt:
        return Response(
            {"error": "send prompt"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    ai_answer = None

    for model_name in candidate_models:
        try:
            print(f"try: {model_name}...")
            response = client.models.generate_content(
                model=model_name, contents=user_prompt
            )
            ai_answer = response.text
            print("answer successfull!")
            break
        except Exception as e:
            print(f"{model_name} fail: {e}")
            continue

    if ai_answer:
        return Response(
            {"status": "success", "question": user_prompt, "answer": ai_answer}
        )
    else:
        return Response(
            {"error": "all model are busy please try again later"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )