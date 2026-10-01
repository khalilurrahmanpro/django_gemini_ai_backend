import time
from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6Je7-vWfBBDfPb7l37AMYBy2Cmb-QFtbfwx5HuUZ3cnUw"
)

candidate_models = [
    "gemini-3.5-flash",
    "gemini-2.0-flash-lite",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
]

prompt = "how to career with django and python"

success = False

for model_name in candidate_models:
    try:
        print(f"print try: {model_name}...")
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
        )
        print("\n--- AI-answer ---")
        print(response.text)
        success = True
        break  

    except Exception as e:
        print(f"{model_name} bussy ({e})")
        print("try next model...\n")
        time.sleep(1)

if not success:
    print(
        "now busy google server please wait just a munites"
    )