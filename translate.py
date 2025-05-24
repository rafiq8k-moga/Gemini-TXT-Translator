from google import genai
import time
from tqdm import tqdm
import datetime

# 🔐 API Key
client = genai.Client(api_key="Your_api_key")

BASE_PROMPT = (
    "saya ingin meminta kepadamu untuk mentranslatekan teks yang saya berikan kepada bahasa indonesia, "
    "namun ada beberapa hal yang perlu kamu perhatikan yaitu berikan saja hasil terjemahannya, tidak dengan "
    "apapun seperti rekomendasi kata lain, sbg, hanya hasil akhirnya saja. kalimatnya adalah:"
)

def translate_text(text, max_retries=5):
    retries = 0
    wait_time = 5  # initial wait time

    while retries < max_retries:
        try:
            full_prompt = f"{BASE_PROMPT}\n{text}"
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite-001",
                contents=full_prompt
            )
            return response.text.strip()
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                tqdm.write("⚠️ Rate limit hit (429). Menunggu 70 detik...")
                time.sleep(70)
            elif "503" in error_str or "UNAVAILABLE" in error_str:
                tqdm.write(f"⚠️ Server terlalu sibuk (503). Coba lagi dalam {wait_time} detik...")
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff
            else:
                tqdm.write(f"❌ Error fatal: {e}")
                return "[Terjemahan gagal]"
            retries += 1

    tqdm.write("❌ Gagal menerjemahkan setelah beberapa percobaan.")
    return "[Terjemahan gagal]"

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    start_time = datetime.datetime.now()
    tqdm.write("🚀 Mulai menerjemahkan...\n")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(tqdm(lines, desc="Translating", unit="line"), 1):
            line = line.strip()
            if not line:
                outfile.write("\n")
                continue

            translated = translate_text(line)
            outfile.write(translated + "\n")

    end_time = datetime.datetime.now()
    elapsed = end_time - start_time
    tqdm.write(f"\n🎉 Semua selesai! Disimpan di: {output_file}")
    tqdm.write(f"⏱️ Total waktu: {str(elapsed).split('.')[0]}")

# 🚀 Jalankan
translate_file("/content/tobeherox07.txt", "/content/tobeherox07-translated.txt")
