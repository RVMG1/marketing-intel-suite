
import argparse
import json
import pandas as pd
import streamlit as st
from pathlib import Path
from fpdf import FPDF
from dominate.tags import html, head, body, title, h1, p
from PIL import Image
import matplotlib.pyplot as plt

def load_prompts(file_path):
    with open(file_path, 'r') as f:
        return [json.loads(line) for line in f.readlines()]

def match_prompt(query, prompts):
    query = query.lower()
    for p in prompts:
        if query.split(" ")[0] in p['input'].lower():
            return p['output']
    return "No matching prompt found. Try rephrasing or add new examples."

def cli_mode():
    parser = argparse.ArgumentParser(description='Unified Marketing Intelligence CLI')
    parser.add_argument('--query', type=str, help='Your input question')
    parser.add_argument('--file', type=str, default='buyer_guide_prompts.jsonl', help='Prompt JSONL path')
    args = parser.parse_args()

    prompts = load_prompts(args.file)
    print(match_prompt(args.query, prompts))

def export_to_html(text, filename):
    doc = html()
    with doc:
        head()
        with body():
            title("Buyer Guide Export")
            h1("Generated Buyer Guide")
            for line in text.split("\n"):
                p(line)
    path = Path(f"/mnt/data/{filename}")
    path.write_text(str(doc))
    return path

def export_to_png(text, filename):
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.axis('off')
    wrapped_text = "\n".join(text.split("\n"))
    ax.text(0.01, 0.99, wrapped_text, fontsize=10, va='top')
    path = Path(f"/mnt/data/{filename}")
    fig.savefig(path, bbox_inches='tight')
    plt.close()
    return path

def dashboard_mode():
    st.set_page_config(page_title="Unified Marketing Dashboard", layout="wide")
    st.title("🧠 Marketing Intelligence System")

    prompts = load_prompts("buyer_guide_prompts.jsonl")
    keywords_df = pd.read_csv("trend_dashboard_sample.csv")

    st.subheader("LLM Prompt Evaluator")
    query = st.text_input("Ask a question or describe content to generate:")
    if query:
        result = match_prompt(query, prompts)
        st.text_area("Generated Output", value=result, height=300)

    st.subheader("Buyer Guide Visual Export")
    guide_text = st.text_area("Paste Buyer Guide Output:", height=200)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Export to PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            for line in guide_text.split("\n"):
                pdf.multi_cell(0, 10, line)
            output_path = Path("/mnt/data/buyer_guide_export.pdf")
            pdf.output(output_path)
            st.success("PDF Exported!")
            st.download_button("Download PDF", data=output_path.read_bytes(), file_name="buyer_guide.pdf")

    with col2:
        if st.button("Export to HTML"):
            path = export_to_html(guide_text, "buyer_guide_export.html")
            st.success("HTML Exported!")
            st.download_button("Download HTML", data=path.read_bytes(), file_name="buyer_guide.html")

    with col3:
        if st.button("Export to PNG"):
            path = export_to_png(guide_text, "buyer_guide_export.png")
            st.success("PNG Exported!")
            st.image(str(path))

    st.subheader("📊 Trend Keywords Dataset Preview")
    st.dataframe(keywords_df)

if __name__ == "__main__":
    import sys
    if st._is_running_with_streamlit:
        dashboard_mode()
    else:
        cli_mode()
