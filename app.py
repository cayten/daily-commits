# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Optional, List, Dict, Tuple
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import re, uuid

# ---------- Yol Ayarı (mutlak) ----------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

app = FastAPI(title="CAYTEN — Öğreten AI", version="1.0")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# ---------- Yardımcılar ----------
TR_GROUP_NAMES = ["birler", "binler", "milyonlar", "milyarlar", "trilyonlar"]
TR_PLACE_NAMES = [
    "birler","onlar","yüzler",
    "binler","on binler","yüz binler",
    "milyonlar","on milyonlar","yüz milyonlar",
    "milyarlar","on milyarlar","yüz milyarlar",
]
TR_DIGITS = "sıfır bir iki üç dört beş altı yedi sekiz dokuz".split()
TR_TENS   = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

def norm_tr_text(s: str) -> str:
    """Türkçe karakterler toleranslı + boşluk normalize"""
    table = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return re.sub(r"\s+", " ", s.strip().lower().translate(table))

def normalize_digits(text: str) -> str:
    m = re.findall(r"\d", text)
    return "".join(m) if m else ""

def group_by_three(nstr: str) -> List[str]:
    s = nstr.lstrip("0") or "0"
    parts = []
    while s:
        parts.append(s[-3:].rjust(3, "0"))
        s = s[:-3]
    return list(reversed(parts))

def format_grouped(parts: List[str]) -> str:
    first = parts[0].lstrip("0") or "0"
    rest = parts[1:]
    return " ".join([first] + rest) if rest else first

def words_triple(triple: str) -> str:
    h, t, u = int(triple[0]), int(triple[1]), int(triple[2])
    parts = []
    if h: parts.append("yüz" if h == 1 else f"{TR_DIGITS[h]} yüz")
    if t: parts.append(TR_TENS[t])
    if u: parts.append(TR_DIGITS[u])
    out = " ".join(parts).strip() or "sıfır"
    return out.replace("bir yüz", "yüz")

def number_in_words(nstr: str) -> str:
    parts = group_by_three(nstr)
    chunks = []
    k = len(parts)
    for i, p in enumerate(parts):
        idx = k - i - 1                 # 0→en sol
        name = TR_GROUP_NAMES[idx] if idx < len(TR_GROUP_NAMES) else ""
        w = words_triple(p)
        if w == "sıfır" and name:
            continue
        if name:
            if name == "binler" and p == "001":
                chunks.append("bin")     # bir bin → bin
            elif name == "birler":
                chunks.append(w)         # birler bölüğünde isim yok
            else:
                chunks.append(f"{w} {name[:-1]}")
        else:
            chunks.append(w)
    return " ".join(chunks).strip().replace("bir bin", "bin")

def place_table(nstr: str) -> List[Tuple[str, str, int]]:
    digits = list(nstr)
    rows = []
    for i, d in enumerate(reversed(digits)):
        name = TR_PLACE_NAMES[i] if i < len(TR_PLACE_NAMES) else f"{10**i}'lik"
        rows.append((name, d, int(d) * (10 ** i)))
    return list(reversed(rows))

def parse_rounding(text: str) -> int:
    t = text.lower()
    if "1000" in t or "bin" in t: return 1000
    if "100" in t or "yüz" in t or "yuz" in t: return 100
    return 10

def round_to_nearest(n: int, base: int) -> int:
    return int(base * round(n / base))

# ---------- Basit session (RAM) ----------
_SESS: Dict[str, Dict] = {}

# ---------- İstek Modelleri ----------
class StartReq(BaseModel):
    topic: str                 # read | place | compare | round
    question: str
    teacher_mode: Optional[bool] = False

class CheckReq(BaseModel):
    session_id: str
    step_id: str
    answer: str

# ---------- Sayfa + favicon ----------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    icon = STATIC_DIR / "favicon.ico"
    if icon.exists():
        return FileResponse(str(icon))
    return HTMLResponse("", status_code=204)

# ---------- Ders başlat ----------
@app.post("/api/lesson/start")
def lesson_start(req: StartReq):
    topic = req.topic.strip().lower()
    nstr = normalize_digits(req.question)
    if topic != "compare" and not nstr:
        return {"error": "Sayı bulunamadı."}

    session_id = str(uuid.uuid4())
    store = {"topic": topic, "nstr": nstr, "question": req.question}
    steps = []

    if topic == "read":
        parts = group_by_three(nstr)
        store["expected"] = {
            "grouped": format_grouped(parts),
            "groups": ", ".join(TR_GROUP_NAMES[:len(parts)]),
            "words": number_in_words(nstr),
        }
        steps = [
            {"id":"read-1","prompt":"Sayıyı sağdan sola üçlü gruplara ayır (boşlukla).","hint":"Her 3 rakamda bir boşluk: 123 456 789"},
            {"id":"read-2","prompt":"Bölük adlarını sırayla yaz (birler, binler, milyonlar ...).","hint":"Sayı kaç bölükse o kadar isim."},
            {"id":"read-3","prompt":"Sayının okunuşunu tam yaz.","hint":"Birler bölüğüne isim ekleme; 'bir bin' deme → 'bin' de."},
        ]

    elif topic == "place":
        rows = place_table(nstr)
        store["expected"] = {
            "grouped": format_grouped(group_by_three(nstr)),
            "place_names": ", ".join([r[0] for r in rows]),
            "values": ", ".join(str(r[2]) for r in rows),
        }
        steps = [
            {"id":"place-1","prompt":"Sayıyı üçlü bölüklere ayır (boşluklu).","hint":""},
            {"id":"place-2","prompt":"Soldan sağa basamak adlarını yaz.","hint":"… milyonlar, yüz binler, on binler, … birler"},
            {"id":"place-3","prompt":"Her basamağın basamak değerlerini virgülle yaz.","hint":"Örn: 500000000, 60000000, … 5"},
        ]

    elif topic == "compare":
        nums = [normalize_digits(x) for x in re.split(r"[;, ]+", req.question) if normalize_digits(x)]
        if len(nums) < 2:
            return {"error": "Karşılaştırma/sıralama için en az iki sayı yazılmalı."}
        ints = [int(x) for x in nums]
        store["cmp_nums"] = ints
        store["expected"] = {
            "grouped_list": "; ".join(format_grouped(group_by_three(x)) for x in nums),
            "sorted": ", ".join(map(str, sorted(ints))),
        }
        steps = [
            {"id":"cmp-1","prompt":"Her sayıyı üçlü bölüklere ayır (her biri boşluklu).","hint":"Her sayı için 3’lü gruplar yap; sayıları ';' ile ayır."},
            {"id":"cmp-2","prompt":"Küçükten büyüğe sırala ve virgülle yaz.","hint":"Örn: 25, 130, 2500"},
        ]

    elif topic == "round":
        base = parse_rounding(req.question)
        n = int(nstr)
        store["round"] = {"base": base, "result": round_to_nearest(n, base)}
        steps = [{"id":"round-1","prompt":f"Sayiyi {base}’e göre en yakına yuvarla.","hint":"Karar basamağı: 10→birler, 100→onlar, 1000→yüzler."}]
    else:
        return {"error":"Bilinmeyen konu."}

    _SESS[session_id] = store
    payload = {"session_id": session_id, "topic": topic, "steps": steps}
    if req.teacher_mode:
        payload["teacher"] = store.get("expected", store.get("round"))
    return payload

# ---------- Adım kontrol ----------
@app.post("/api/lesson/check")
def lesson_check(req: CheckReq):
    if req.session_id not in _SESS:
        return {"ok": False, "feedback": "Oturum bulunamadı."}
    s = _SESS[req.session_id]
    topic, nstr = s["topic"], s.get("nstr","")
    ans = req.answer.strip()

    if req.step_id == "read-1":
        target = s["expected"]["grouped"]
        ok = ans.replace(" ","") == nstr
        return {"ok": ok, "expected": target, "hint": "" if ok else "Her 3 rakamdan sonra boşluk bırak."}

    if req.step_id == "read-2":
        target = s["expected"]["groups"]
        ok = norm_tr_text(ans) == norm_tr_text(target)
        return {"ok": ok, "expected": target, "hint": "" if ok else "Bölük adlarını sırayla yaz."}

    if req.step_id == "read-3":
        target = s["expected"]["words"]
        ok = norm_tr_text(ans) == norm_tr_text(target)
        return {"ok": ok, "expected": target.lower(), "hint": "" if ok else "‘bir bin’ deme; fazladan/eksik boşluk bırakma."}

    if req.step_id == "place-1":
        target = s["expected"]["grouped"]
        ok = ans.replace(" ","") == nstr
        return {"ok": ok, "expected": target, "hint": "" if ok else "Üçlü gruplara ayır."}

    if req.step_id == "place-2":
        target = s["expected"]["place_names"]
        ok = norm_tr_text(ans) == norm_tr_text(target)
        return {"ok": ok, "expected": target, "hint": "" if ok else "Soldan sağa basamak adları."}

    if req.step_id == "place-3":
        target = s["expected"]["values"]
        norm = lambda x: ",".join(str(int(t)) for t in x.replace(" ","").split(",") if t!="")
        ok = norm(ans) == norm(target)
        return {"ok": ok, "expected": target, "hint": "" if ok else "rakam × 10^k değerleri (soldan sağa)."}

    if req.step_id == "cmp-1":
        target = s["expected"]["grouped_list"]
        ok = all(any(ch.isdigit() for ch in token) for token in ans.split(";"))
        return {"ok": ok, "expected": target, "hint": "" if ok else "Her sayı için 3’lü gruplama; sayıları ';' ile ayır."}

    if req.step_id == "cmp-2":
        target = s["expected"]["sorted"]
        user = ", ".join(x.strip() for x in ans.replace(" ","").split(",") if x.strip())
        ok = user == target.replace(" ","")
        return {"ok": ok, "expected": target, "hint": "" if ok else "Küçükten büyüğe virgülle yaz."}

    if req.step_id == "round-1":
        target = str(s["round"]["result"])
        ok = ans.replace(" ","") == target
        return {"ok": ok, "expected": target, "hint": "" if ok else "Karar basamağı: 5↑, 5’ten küçük ↓."}

    return {"ok": False, "feedback": "Bilinmeyen adım."}
