
# Gemini TXT Translator

🇮🇩 Alat sederhana untuk membantu fansub menerjemahkan subtitle hasil ekspor dari Aegisub ke dalam Bahasa Indonesia (atau ke bahasa lain) secara otomatis menggunakan Google Gemini API.

🇬🇧 A simple tool to help fansub teams automatically translate subtitles exported from Aegisub into Indonesian(or to the other languages) using Google Gemini API.

---

## 🎯 Tujuan

Alat ini dirancang untuk fansubber yang ingin mempercepat proses terjemahan dengan bantuan AI. Cukup ekspor subtitle dari Aegisub ke format `.txt`, lalu jalankan skrip ini untuk menerjemahkan baris demi baris secara otomatis.

---

## 🧩 Fitur

- 🔁 Terjemahan baris per baris dari file `.txt`.
- ✍️ Prompt bisa dikustomisasi melalui variabel `BASE_PROMPT`.
- ⚠️ Penanganan otomatis jika terkena rate limit dari API.
- 📄 Input dan output berupa file teks sederhana.
- 🤐 Output bersih: tanpa saran kata lain, tanda baca tambahan, atau penjelasan.
- ⌚ Jika kena RateLimit, maka akan berhenti sementara, diberi jeda 2 menit, dan lanjut ke baris yang sama

---

## 🧰 Persiapan

### 1. Mendapatkan API Key Gemini (Google AI Studio)

1. Kunjungi: [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Login dengan akun Google.
3. Klik **"Create API Key"**
4. Salin API key yang muncul.
5. Simpan baik-baik — **jangan dibagikan ke publik**.

---

## 🧠 Cara Pakai

### Langkah 1: Ekspor dari Aegisub

1. Buka subtitle kamu di Aegisub.
2. Klik `File` → `Export Subtitles...`
3. Pada dialog ekspor:
   - Pilih format: **Plain Text (*.txt)**
   - Hilangkan semua centang untuk formatting/metadata.
4. Simpan file sebagai `awal.txt`.

### Langkah 2: Edit File Python

1. Buka `translate.py`.
2. Cari bagian berikut dan ganti API key:

```python
client = genai.Client(api_key="YOUR_API_KEY_HERE")
````

3. (Opsional) Edit instruksi default Gemini dengan mengubah `BASE_PROMPT`:

```python
BASE_PROMPT = (
  "Tolong terjemahkan teks berikut ke dalam bahasa Indonesia yang alami dan sesuai konteks subtitle. "
  "Berikan hanya hasil terjemahan, tanpa penjelasan tambahan."
)
```

### Langkah 3: Jalankan Program

Install dependencies terlebih dahulu:

```bash
pip install google-genai
```

Jalankan program:

```bash
python translate.py
```

Hasilnya akan disimpan di `translated.txt`.

> Jika kamu menggunakan nama file selain `awal.txt`, edit bagian berikut:

```python
translate_file("awal.txt", "translated.txt")
```

Ganti `awal.txt` dengan nama file yang kamu pakai.

---

## 📁 Contoh

**awal.txt**

```
What are you doing here?
I can't believe this is happening.
```

**translated.txt**

```
Apa yang kamu lakukan di sini?
Aku tidak percaya ini sedang terjadi.
```

---

## 💬 Tips Tambahan

* Review hasil terjemahan secara manual untuk menjaga kualitas.
* Tidak mempertahankan timing dari subtitle (`.ass`), hanya konten teks.
* Cocok digunakan sebagai langkah awal (pretranslate) sebelum proofreading.
* Jangan pakai untuk subtitle dengan tag atau format khusus.

---

## 🚧 Rencana Fitur (TODO)

* [ ] Input langsung dari file `.ass`
* [ ] Output ke format `.ass` dengan timing dipertahankan
* [ ] GUI sederhana (drag & drop)
* [ ] Batch processing untuk banyak file sekaligus

---

## 🔐 Keamanan

* Jangan pernah commit API key ke GitHub.
* Gunakan key hanya dalam project lokal atau server pribadi.
* Gemini API punya kuota gratis terbatas, dan bisa menimbulkan biaya jika melewati batas.

---

## 📄 Lisensi

Proyek ini dirilis di bawah lisensi MIT.

[Lihat LICENSE](LICENSE)

---

## 🤝 Kontribusi

Pull request sangat diterima! Terutama untuk:

* Penambahan dokumentasi
* Dukungan berbagai format subtitle
* Terjemahan ke bahasa lain
* Otomatisasi yang lebih canggih

---
