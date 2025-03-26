
# Marketing Intelligence Toolkit

A modular, AI-assisted marketing research and content generation system built to explore trends, create emotional copy, and build better digital strategies.

## 🔧 Features

- Research Navigator with keyword mining
- Emotional Copy Assistant using AIDA / PREP
- Trend Dashboard with export + scoring
- LLM-style training dataset and QA assistant
- Visual system blueprint (Mermaid-based)

## 📦 Modules

1. `trend_dashboard_app.py` — Streamlit dashboard for keyword trends
2. `llm_training_data.jsonl` — QA-format knowledge base
3. `marketing_flow_mermaid.txt` — Mermaid.js visual flow map
4. `Emotional Copy Assistant` — React UI + logic

## 🚀 How to Launch

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/marketing-intel-suite.git
   cd marketing-intel-suite
   ```

2. Install Python deps (for dashboard):
   ```bash
   pip install streamlit pandas
   ```

3. Launch Trend Dashboard:
   ```bash
   streamlit run trend_dashboard_app.py
   ```

4. Explore training data:
   Load `llm_training_data.jsonl` into your LLM or prompt tool.

## 📈 System Flow

See `marketing_flow_mermaid.txt` for the full Mermaid-based architecture.
Use draw.io or Mermaid Live Editor to visualize it.

---

Built from your personal research library + failures + experiments. Let this system evolve.
