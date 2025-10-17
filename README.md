# Günlük Kod Arşivi

Merhaba! Bu repo, her gün 2025-10-17 tarihinden başlayarak bir klasör (YYYY-MM-DD) içinde örnek görev, çözüm iskeleti ve testlerle ilerlemen için hazırlandı.

## Hızlı Başlangıç
1. Reponu oluştur ve bu zip'i çıkar.
2. Git'e ekle:
```bash
git init
git add .
git commit -m "Initial daily code pack"
git branch -M main
git remote add origin <REPO_URLİNİ_YAZ>
git push -u origin main
```
3. Her gün yeni klasör oluşturmak için:
```bash
python tools/generate_daily.py
```
> İstersen dilini `--lang py` veya `--lang js` ile seçebilirsin.

## Yapı
- `days/YYYY-MM-DD/` — Günlük çalışma klasörleri
- `templates/` — Dil bazlı iskeletler
- `tools/generate_daily.py` — Günlük klasör üretici
- `.github/workflows/lint.yml` — Basit lint ve test workflow (isteğe bağlı)

## Notlar
- Testleri koştur: `python -m pytest` veya `node test.js`
- İstediğin gibi özelleştir; ben üretici scripti minimal tuttum.
