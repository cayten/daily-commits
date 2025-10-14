# Day 10 – Flaky Testleri Alt Etmenin 5 Gerçekçi Yolu ✍️

Flaky testler, aynı kod değişmeden bazen geçip bazen kalan testlerdir. Güveni ve hızınızı düşürür.

## 1) Akıllı Bekleme Stratejileri
- Sabit sleep yerine **explicit wait** ve koşul bazlı beklemeler kullanın.
- UI animasyonları ve network gecikmelerini hesaba katın.

## 2) Stabil Test Verisi
- Her test için izole veri oluşturun; testler birbirini etkilemesin.
- Factory/fixtures veya seed script’leri kullanın.

## 3) Yeniden Deneme (Retry) Mantıklı Kullanım
- Flaky alanı kökten çözene kadar geçici olarak retry kullanın.
- Raporlarda kaçıncı denemede geçtiğini işaretleyin.

## 4) Paralel ve CI Ortamı Hijyeni
- Paylaşımlı kaynak çakışmalarını azaltın.
- CI’da tarayıcı/driver sürümlerini sabitleyin.

## 5) Gözden Geçirme ve Ölçüm
- Flake oranını takip edin, en çok kırılan testleri listeleyin.
- Test mimarisini düzenli aralıklarla sadeleştirin.

> Flaky testler kader değil; iyi mimari + temiz veri + doğru bekleme ile kontrol altına alınır. 🛡️
