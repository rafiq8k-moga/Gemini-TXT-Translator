from google import genai
import time

# 🔐 API key
client = genai.Client(api_key="Your_Api_Key")

# 📝 Prompt dasar yang bisa kamu ubah kapan saja (basic prompt to indonesia, change it to what do you want)
BASE_PROMPT = (
    "saya ingin meminta kepadamu untuk mentranslatekan teks yang saya berikan kepada bahasa indonesia, "
    "namun ada beberapa hal yang perlu kamu perhatikan yaitu berikan saja hasil terjemahannya, tidak dengan "
    "apapun seperti rekomendasi kata lain, sbg, hanya hasil akhirnya saja. kalimatnya adalah:"
)

# don't change this!!
def translate_text(text):
    try:
        full_prompt = f"{BASE_PROMPT}\n{text}"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"⚠️ Error: {e}")
        if "429" in str(e) or "rate" in str(e).lower():
            print("⏳ Rate limit! Wait 2 Minutes...")
            time.sleep(120)
            return translate_text(text)
        return "[Terjemahan gagal]"

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:

        for i, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                outfile.write("\n")
                continue

            print(f"🔄 Translating Line {i}...")
            translated = translate_text(line)
            outfile.write(translated + "\n")
            print(f"✅ {translated}\n")

    print(f"\n🎉 All Done, Saved in: {output_file}")
# end

# 🚀 Jalankan
translate_file("awal.txt", "translated.txt")
