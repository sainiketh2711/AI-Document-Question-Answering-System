from pathlib import Path
import sys

from flask import Flask, render_template, request, jsonify


# Project paths
PROJECT_FOLDER = Path(__file__).resolve().parent
SRC_FOLDER = PROJECT_FOLDER / "src"
DOCUMENT_PATH = PROJECT_FOLDER / "documents" / "library_guide.txt"

# Allow Python to import the existing source files
sys.path.insert(0, str(SRC_FOLDER))

from knowledge_base import build_knowledge_base
from reasoning_engine import process_with_reasoning


# Create Flask application
app = Flask(__name__)


# Load document and construct knowledge base
def initialize_system():

    if not DOCUMENT_PATH.exists():
        raise FileNotFoundError(
            f"Library guide not found: {DOCUMENT_PATH}"
        )

    document_text = DOCUMENT_PATH.read_text(
        encoding="utf-8"
    )

    knowledge_base = build_knowledge_base(
        document_text
    )

    if not knowledge_base:
        raise ValueError(
            "Knowledge base could not be constructed."
        )

    return knowledge_base


# Initialize the AI system
knowledge_base = initialize_system()


# Homepage
@app.route("/")
def home():

    return render_template("index.html")


# Question answering API
@app.route("/ask", methods=["POST"])
def ask_question():

    data = request.get_json(silent=True) or {}

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "error": "Please enter a question."
        }), 400

    try:

        answer = process_with_reasoning(
            question,
            knowledge_base
        )

        return jsonify({
            "question": question,
            "answer": answer
        })

    except Exception as error:

        print("Error processing question:", error)

        return jsonify({
            "error": "An error occurred while processing your question."
        }), 500


# Run the website
if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )