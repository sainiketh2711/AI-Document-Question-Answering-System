from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import re
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 15 * 1024 * 1024
active = {"name": None, "facts": []}
ALLOWED = {"txt", "pdf", "docx"}
STOP = set("what who where when why how is are was were do does did can could would should the a an and or of to in on for from with about tell me please this that it be as by at which document according".split())

def extract(file, ext):
    if ext == "txt":
        data=file.read()
        try: return data.decode("utf-8")
        except UnicodeDecodeError: return data.decode("latin-1")
    if ext == "pdf":
        from PyPDF2 import PdfReader
        return "\n".join(p.extract_text() or "" for p in PdfReader(file).pages)
    if ext == "docx":
        from docx import Document
        d=Document(file); rows=[p.text for p in d.paragraphs if p.text.strip()]
        for table in d.tables:
            rows.extend(" | ".join(c.text.strip() for c in r.cells) for r in table.rows)
        return "\n".join(rows)
    return ""

def build_kb(text):
    text=re.sub(r"\s+", " ", text).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text) if len(s.strip()) > 12]

def words(text): return {w for w in re.findall(r"[a-z0-9₹]+", text.lower()) if len(w)>2 and w not in STOP}

def answer(q):
    qwords=words(q); scored=[]
    for fact in active["facts"]:
        overlap=qwords & words(fact)
        if overlap: scored.append((len(overlap)/max(1,len(qwords)) + .25*len(overlap)/max(1,len(words(fact))),len(overlap),fact))
    scored.sort(reverse=True)
    if not scored: return "I couldn't find information about that in the uploaded document."
    results=[]; seen=set()
    for score,n,fact in scored[:3]:
        if fact not in seen and n >= 1: results.append(fact); seen.add(fact)
    return " ".join(results) if results else "I couldn't find information about that in the uploaded document."

@app.route("/")
def home(): return render_template("index.html")
@app.route("/upload", methods=["POST"])
def upload():
    f=request.files.get("document")
    if not f or not f.filename: return jsonify(error="Choose a document to upload."),400
    name=secure_filename(f.filename); ext=name.rsplit(".",1)[-1].lower() if "." in name else ""
    if ext not in ALLOWED: return jsonify(error="Supported formats: TXT, PDF, DOCX."),400
    try: text=extract(f,ext)
    except Exception as e: print("Extraction error:",e); return jsonify(error="Could not read this file. Try another document."),400
    facts=build_kb(text)
    if not facts: return jsonify(error="No readable text found. Scanned PDFs are not supported."),400
    active["name"]=name; active["facts"]=facts
    return jsonify(filename=name, facts=len(facts), message="Document processed successfully.")
@app.route("/ask", methods=["POST"])
def ask():
    q=(request.get_json(silent=True) or {}).get("question","").strip()
    if not q: return jsonify(error="Enter a question."),400
    if not active["facts"]: return jsonify(error="Upload a document first."),400
    return jsonify(question=q,answer=answer(q),document=active["name"])
@app.route("/status")
def status(): return jsonify(loaded=bool(active["facts"]),filename=active["name"],facts=len(active["facts"]))
if __name__ == "__main__": app.run(host="0.0.0.0",port=5000,debug=True)
