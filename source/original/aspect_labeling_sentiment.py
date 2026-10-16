import pandas as pd
import re
from collections import Counter
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter

# --- YAPILANDIRMA ---
INPUT_PATH = "C:/Users/emre.ozturk/Downloads/Games_Rewievs_Cleaned.xlsx"
OUTPUT_PATH = "C:/Users/emre.ozturk/Downloads/Games_Sentiment_Analysis_Results.xlsx"

ASPECT_KEYWORDS = {
    "Grafik": ["grafik", "görsel", "görüntü", "tasarım", "renk", "art", "doku", "estetik",
               "görsellik", "atmosfer", "pixel", "animasyon", "render", "vfx", "efekt",
               "gölgelendirme", "detaylı", "parlak", "canlı", "ışıklandırma", "derinlik",
               "kompozisyon", "minimal", "soyut", "modern", "klasik", "retro", "manzaralar", "manzara"],
    "AI (yapay zeka)": ["ai", "yapay zeka", "düşman", "boss", "algoritma", "öğrenme",
                        "adaptasyon", "strateji", "npc", "davranış", "yapay", "zeka",
                        "patika", "karar", "mantık", "otonom", "reaksiyon", "sistem"],
    "Oyunun Oynanışı": ["oynanış", "kontrol", "mekanik", "sistem", "combo", "hikaye", "zor", "oyun",
                        "zorluk", "akış", "kontroller", "oyunu", "oyunun", "oyunlar", "mükemmel",
                        "harika", "gerçekçi", "akıcı", "kaliteli", "tavsiye", "güzel", "iyi",
                        "büyüleyici", "en iyi", "öneririm", "strateji", "refleks", "etkileşim",
                        "deneyim", "gerçek zamanlı", "çoklu görev", "işbirliği", "rekabet", "dinamik",
                        "oyunculuk", "akıcılık", "karmaşık", "esnek", "özelleştirilebilir", "hızlı tempolu", "Öneririm", "tavsiye"]
}

SENTIMENT_WORDS = {
    "Olumlu": [
        "mükemmel", "harika", "gerçekçi", "akıcı", "kaliteli", "tavsiye", "güzel", "iyi", "büyüleyici", "en iyi",
        "beğeni", "üstün", "fevkalade", "olağanüstü", "göz alıcı", "muhteşem", "etkileyici", "cazip", "özenli",
        "profesyonel", "başarılı", "takdir", "memnun", "harikulade", "nefes kesici", "şaheser", "akıl almaz",
        "sürükleyici", "bağımlılık yapan", "unutulmaz", "yenilikçi", "övgü", "taktir", "alkış", "müthiş",
        "kusursuz", "ideal", "parlak", "dahice", "keyifli", "sarıyo", "sarıyor", "oynayın", "zevkli", "süper",
        "başyapıt", "aşık", "aşk", "baş yapıt", "efsane", "mük", "kalite", "taş", "inanılmaz", "hoş", "fantastik",
        "eğlenceli", "tatmin edici", "şahane", "yeterli", "yetenekli", "hayranlık verici", "doyurucu", "ustaca",
        "tatlı", "nefis", "görkemli", "zarif", "dinamik", "etkin", "rahatlatıcı", "seçkin", "aydınlık", "umut verici",
        "hoşnut edici", "kararlı", "güçlü", "becerikli", "sevindirici", "nitelikli", "canlı", "çekici", "ferah",
        "açık", "dengeli", "ilginç", "başarımı yüksek", "güvenilir", "eğitimli", "kusursuzca", "uyumlu", "verimli",
        "yetkin", "sadık", "motive edici", "pozitif", "iyi niyetli", "şık", "temiz", "basit", "anlaşılır", "özgün",
        "heyecan verici", "dikkat çekici", "baş döndürücü", "iç açıcı", "parlak fikirli", "vizyoner", "çığır açan",
        "enfes", "tadında", "yüce", "yüksek kaliteli", "iyi düşünülmüş", "akıllıca", "mükemmel tasarım",
        "tatmin edici performans", "canlandırıcı", "rahat", "modern", "enerjik", "sadelik", "doygun", "akıl dolu",
        "heyecanlı", "esprili", "olumlu hava", "minnettar", "etkileyicilik", "en üst seviye", "kolay", "pratik",
        "verimli çözüm", "en iyisi", "üst düzey", "parlak zeka", "çok iyi", "olumlu izlenim", "gelişmiş",
        "tatminkâr", "başarı", "yetkinlik", "ilerleme", "seviye atlamış", "ustalaşmış", "akıcı oynanış",
        "takdire şayan", "zirve", "öncü", "rehber", "akılcı", "hızlı", "zekice", "mutlu", "eğlencelik",
        "oynanabilir", "şanslı", "enfes görsellik", "şahane tasarım", "çok güzel", "fevkaladelik", "kapsayıcı",
        "etkinleştirici", "etkili", "çözümleyici", "bağımlı", "Öneririm", "ZEVKLİ"
    ],
    "Olumsuz": [
        "kötü", "oynamayın", "kanser", "berbat", "hatalı", "yavaş", "sıkıcı", "donuk", "zayıf", "kötücül",
        "işe yaramaz", "eksik", "yetersiz", "kaba", "acımasız", "düzensiz", "hayal kırıklığı", "verimsiz",
        "mutsuz", "çirkin", "fiyasko", "tatsız", "tekdüze", "vasat", "sinir bozucu", "tutarsız", "başarısız",
        "kırık", "çöküyor", "dengesiz", "kafa karıştırıcı", "pişman", "iğrenç", "rezil", "kalitesiz",
        "dayanılmaz", "bozuk", "çöp", "almayın", "karmaşık", "anlamsız", "kırılmış", "gereksiz", "hoş olmayan",
        "beceriksiz", "sorunlu", "sıkıntılı", "şaşırtıcı derecede kötü", "yoğun", "ağır", "yavaşlatıcı",
        "yanlış", "absürt", "çürük", "akılsızca", "rahatsız edici", "nefret edilesi", "bozucu", "negatif", "eksi",
        "kötüleşmiş", "zaman kaybı", "felaket", "değersiz", "fazla", "kararsız", "dikkatsiz", "bulanık",
        "gereksizce", "sahte", "korkunç", "ürkütücü", "rezalet", "rahatsız", "saldırgan", "uygunsuz", "sefil",
        "düşük kaliteli", "çökük", "eski", "bozulmuş", "geçersiz", "karışık", "kararsızlık", "sorun çıkartan",
        "yönsüz", "eksik içerik", "berbat hissiyat", "eksik fonksiyon", "gereksiz uzatılmış", "karmakarışık",
        "net olmayan", "boş", "uzun", "gıcık", "mantıksız", "karışıklık", "çözüm yok", "uyumsuz", "kaza", "riskli",
        "aşırı zor", "bıktırıcı", "kusurlu", "ezbere", "sinir bozucu deneyim", "gereksiz diyalog", "çok yavaş",
        "tekrarlayan", "eski teknoloji", "sistemsiz", "yenilikten uzak", "bağlantısız", "eksik veri",
        "hatalı tasarım", "başarısızlık", "sinir edici", "dengesizlik", "devamsız", "hatalı yön", "eksik bilgi",
        "yanlış yönlendirme", "eksik oyun", "donanım hatası", "yanıltıcı", "fazlalık", "zayıflık", "bozuk görsel",
        "görsel karmaşa", "anlamsız görevler", "hatalı grafik", "ses hatası", "anlamsız oyun", "gereksiz detay",
        "eksik içerik"
    ]
}

COLOR_MAP = {
    "Olumlu": PatternFill(start_color="90EE90", fill_type="solid"),
    "Olumsuz": PatternFill(start_color="FFA07A", fill_type="solid"),
    "Nötr": PatternFill(start_color="D3D3D3", fill_type="solid")
}

# --- SABİT DEĞERLER ---
# Pencere büyüklüğü: eşleşme etrafındaki kaç kelimeyi inceleyeceğiz
WINDOW_SIZE = 5
# Suffix listesi – has_keyword_with_suffix fonksiyonu ile aynı
SUFFIXES = [
    "", "i", "ı", "u", "ü", "e", "a", "de", "da", "den", "dan", "ye", "ya",
    "nin", "nın", "nun", "nün", "ne", "na", "ler", "lar", "si", "sı",
    "su", "sü", "inden", "undan", "lerinin", "larının", "deki", "daki",
    "yle", "yla", "li", "lı", "lu", "lü", "ik", "ık", "ük", "ek", "ak"
]

# --- FONKSİYONLAR ---
def normalize_text(text):
    replacements = str.maketrans("çğıöşü", "cgiosu")
    return text.translate(replacements)

def get_keyword_pattern(keyword):
    """Verilen keyword için suffix'leri de içeren regex desenini oluşturur."""
    norm_kw = normalize_text(keyword.lower())
    pattern = r'\b' + re.escape(norm_kw) + '(' + '|'.join(SUFFIXES) + r')\b'
    return pattern

def find_local_sentiment(sentence, keyword):
    """
    Cümle içindeki keyword eşleşmesinin yer aldığı lokal pencere içinde,
    pozitif ve negatif kelimeleri arar. Eğer hem pozitif hem de negatif kelime varsa,
    en yakın olanın mesafesine göre karar verir.
    """
    norm_sentence = normalize_text(sentence.lower())
    tokens = re.findall(r'\w+', norm_sentence)
    
    # Keyword için pattern
    pattern = get_keyword_pattern(keyword)
    
    votes = []  # her eşleşme için "Olumlu" veya "Olumsuz" kararı
    
    for match in re.finditer(pattern, norm_sentence):
        # Belirlenen eşleşmenin karakter konumunu alıyoruz
        start, end = match.span()
        # Token'ların başlangıç indeksleri için basit bir yöntem: 
        # cümleyi yeniden tokenize edip, eşleşmeye en yakın tokenı bulacağız.
        token_positions = []
        pos = 0
        for token in tokens:
            # cümledeki token aramasını yaparken her seferinde ilk uygun konumu alıyoruz
            m = re.search(re.escape(token), norm_sentence[pos:])
            if m:
                token_positions.append(pos + m.start())
                pos += m.start() + len(token)
            else:
                token_positions.append(-1)
        # Bulduğumuz token listesi üzerinden eşleşmeye en yakın token indeksini tespit etmeliyiz.
        # Bunun için, match.start() noktasına en yakın token konumunu bulalım:
        distances = [abs(start - tp) for tp in token_positions if tp != -1]
        if not distances:
            continue
        # Basitçe en yakın tokenin indeksini tespit ediyoruz.
        # Burada, pencere için token listesinde aralık belirleyeceğiz; 
        # tam indeksi bulmak yerine tüm tokenlar arasında döneriz.
        # Alternatif: her eşleşme için tüm tokenlar üzerinden pencere belirle
        # Bu örnekte, keyword'un geçtiği token dizisinin ortalama indeksi olarak alalım:
        approx_index = token_positions[0]
        for tp in token_positions:
            if abs(start - tp) < abs(start - approx_index):
                approx_index = tp
        # Token listesinde keyword token'ı olarak kabul ettiğimiz indeksi bulalım:
        # Not: Bu yöntem tam kesin olmayabilir; basit bir uygulamadır.
        try:
            token_index = token_positions.index(approx_index)
        except ValueError:
            token_index = 0
        
        # Pencere aralığı
        start_index = max(0, token_index - WINDOW_SIZE)
        end_index = min(len(tokens), token_index + WINDOW_SIZE + 1)
        window_tokens = tokens[start_index:end_index]
        
        # Lokal pencere içindeki sentiment kelimelerini inceleyelim:
        pos_matches = [w for w in window_tokens if normalize_text(w) in [normalize_text(p) for p in SENTIMENT_WORDS["Olumlu"]]]
        neg_matches = [w for w in window_tokens if normalize_text(w) in [normalize_text(n) for n in SENTIMENT_WORDS["Olumsuz"]]]
        
        # Eğer hem pozitif hem negatif kelime varsa, en yakın olanı belirleyelim:
        if pos_matches and neg_matches:
            # Bulduğumuz tokenlar arasında, her birinin cümle içindeki konumlarını hesaplayalım:
            pos_distances = []
            neg_distances = []
            # Konumları tespit etmek için, pencere tokenlarının cümledeki relative offsetlerini arıyoruz.
            # Bu basit yöntem tokenların sırasına göre yapılmaktadır.
            for i, token in enumerate(window_tokens):
                if normalize_text(token) in [normalize_text(p) for p in SENTIMENT_WORDS["Olumlu"]]:
                    pos_distances.append(abs(i - (token_index - start_index)))
                if normalize_text(token) in [normalize_text(n) for n in SENTIMENT_WORDS["Olumsuz"]]:
                    neg_distances.append(abs(i - (token_index - start_index)))
            min_pos = min(pos_distances) if pos_distances else None
            min_neg = min(neg_distances) if neg_distances else None
            if min_pos is not None and min_neg is not None:
                if min_pos < min_neg:
                    votes.append("Olumlu")
                elif min_neg < min_pos:
                    votes.append("Olumsuz")
                else:
                    # eşit mesafe durumunda, cümlede önce gelen kararı alalım:
                    # pencere içerisindeki sıraya göre
                    first_token = window_tokens[min(min_pos, min_neg)]
                    if normalize_text(first_token) in [normalize_text(p) for p in SENTIMENT_WORDS["Olumlu"]]:
                        votes.append("Olumlu")
                    else:
                        votes.append("Olumsuz")
        elif pos_matches:
            votes.append("Olumlu")
        elif neg_matches:
            votes.append("Olumsuz")
    if votes:
        # Eğer birden fazla eşleşme olduysa, çoğunluk oyu belirlenir.
        pos_count = votes.count("Olumlu")
        neg_count = votes.count("Olumsuz")
        if pos_count > neg_count:
            return "Olumlu"
        elif neg_count > pos_count:
            return "Olumsuz"
        else:
            # Eşit oy durumunda, ilk eşleşmenin sonucunu döndür
            return votes[0]
    else:
        return "Nötr"

def detect_sentiment(text, aspect_keyword):
    """
    Gelen text içerisinde aspect_keyword geçen cümleleri tespit eder 
    ve her eşleşmenin lokal penceresinde sentiment analizi yapar.
    Bu sayede, bir cümlede hem olumlu hem de olumsuz kelime geçse bile,
    local bağlam değerlendirilerek doğru sentiment (Olumlu ya da Olumsuz) belirlenir.
    """
    try:
        text_lower = text.lower()
        aspect_keyword_lower = aspect_keyword.lower()
        # İlgili cümleleri ayıklamak için cümle sonu noktalama işaretlerine göre bölüyoruz
        sentences = re.split(r'[.!?]', text_lower)
        target_sentences = [sentence.strip() for sentence in sentences if re.search(get_keyword_pattern(aspect_keyword), normalize_text(sentence))]
        
        votes = []
        for sentence in target_sentences:
            sentiment = find_local_sentiment(sentence, aspect_keyword)
            # Eğer lokal analiz "Nötr" dönüyorsa; ama pencere içerisinde herhangi bir sentiment kelime varsa
            if sentiment != "Nötr":
                votes.append(sentiment)
        if votes:
            pos_count = votes.count("Olumlu")
            neg_count = votes.count("Olumsuz")
            if pos_count > neg_count:
                return "Olumlu"
            elif neg_count > pos_count:
                return "Olumsuz"
            else:
                # Eşit oy durumunda, ilk oyu esas alalım
                return votes[0]
        else:
            return "Nötr"
    except Exception as e:
        print(f"⚠️ Sentiment analiz hatası: {str(e)}")
        return "Nötr"

def analyze_review(text):
    """
    Her aspect için review içinde mevcut olan aspect_keyword'ler üzerinden sentiment analizi yapar.
    İlk bulunan sentiment (Nötr dışı) belirlenirse o aspect için sonucu verir.
    """
    result = {aspect: "Nötr" for aspect in ASPECT_KEYWORDS}
    text_lower = text.lower()
    for aspect, keywords in ASPECT_KEYWORDS.items():
        for keyword in keywords:
            if re.search(get_keyword_pattern(keyword), normalize_text(text_lower)):
                sentiment = detect_sentiment(text, keyword)
                if sentiment != "Nötr":
                    result[aspect] = sentiment
                    break  # İlk bulunan anlamlı sentiment ile sonraki kelimelere bakmaya gerek yok
    return result

# --- VERİ YÜKLE ---
df = pd.read_excel(INPUT_PATH, usecols=["app_id", "review_text"], dtype={"app_id": str, "review_text": str}).dropna()

# --- ANALİZ ---
results = []
for _, row in df.iterrows():
    analysis = analyze_review(row["review_text"])
    results.append({
        "app_id": row["app_id"],
        "review_text": row["review_text"],
        **analysis
    })
df_results = pd.DataFrame(results)

# --- RENKLİ KAYDET ---
with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
    df_results.to_excel(writer, index=False, sheet_name="Analizler")
    worksheet = writer.sheets["Analizler"]
    # Aspect sütunları için (örneğin, 3. sütundan 5. sütuna kadar) renklendirme
    for col in range(3, 6):
        col_letter = get_column_letter(col)
        for row in range(2, len(df_results) + 2):
            cell = worksheet[f"{col_letter}{row}"]
            cell.fill = COLOR_MAP.get(cell.value, COLOR_MAP["Nötr"])
    worksheet.column_dimensions['A'].width = 15
    worksheet.column_dimensions['B'].width = 80

# --- ÖZET SHEET ---
summary_data = []
for aspect in ASPECT_KEYWORDS:
    counts = df_results[aspect].value_counts().to_dict()
    summary_data.append({
        "Kategori": aspect,
        "Olumlu": counts.get("Olumlu", 0),
        "Olumsuz": counts.get("Olumsuz", 0),
        "Nötr": counts.get("Nötr", 0)
    })
df_summary = pd.DataFrame(summary_data)
with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl", mode="a") as writer:
    df_summary.to_excel(writer, index=False, sheet_name="Özet")

# --- NÖTR KELİMELER ---
neutral_reviews = df_results[
    (df_results["Grafik"] == "Nötr") &
    (df_results["AI (yapay zeka)"] == "Nötr") &
    (df_results["Oyunun Oynanışı"] == "Nötr")
]["review_text"].tolist()
neutral_corpus = " ".join(map(str, neutral_reviews)).lower()
neutral_corpus = normalize_text(neutral_corpus)
neutral_words = re.findall(r'\b\w{3,}\b', neutral_corpus)
most_common_words = Counter(neutral_words).most_common(100)
df_top_words = pd.DataFrame(most_common_words, columns=["Kelime", "Frekans"])
with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl", mode="a") as writer:
    df_top_words.to_excel(writer, index=False, sheet_name="Nötr En Çok Kelimeler")

print(f"✅ İşlem tamamlandı! Excel çıktısı: {OUTPUT_PATH}")
