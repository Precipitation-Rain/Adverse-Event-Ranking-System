# 💊 Adverse Event Ranking System (AERS)

A pharmacovigilance signal detection pipeline that processes drug-adverse event reports, computes disproportionality scores, and ranks drug-event pairs by safety signal strength — built with Python and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit)
![Domain](https://img.shields.io/badge/Domain-Healthcare--AI-teal?style=flat-square)
![Pharmacovigilance](https://img.shields.io/badge/Field-Pharmacovigilance-purple?style=flat-square)

---

## 📌 What This Project Does

AERS (Adverse Event Reporting System) mimics the core logic used by drug regulatory agencies (like the FDA's FAERS system) to detect potential safety signals from post-market drug surveillance data.

The pipeline:
1. **Ingests** raw drug-adverse event report pairs
2. **Computes** disproportionality scores (signal strength per drug-event combination)
3. **Ranks** all drug-event pairs from highest to lowest signal
4. **Visualizes** ranked signals in a Streamlit dashboard for review

---

## 🔬 What is Pharmacovigilance?

After a drug is approved and reaches the market, healthcare providers and patients report any adverse effects they observe. Pharmacovigilance is the science of monitoring these reports to detect new or previously unknown drug safety issues — called **signals**.

The key question: *"Is this adverse event happening more than we'd expect by chance, given how often this drug and this event each appear in reports?"*

This is answered with disproportionality analysis.

---

## 🧮 Signal Scoring Method

The system computes a **disproportionality score** for each drug-event pair — comparing how often they co-occur against how often they'd occur independently.

Common methods in pharmacovigilance include:
- **PRR (Proportional Reporting Ratio)** — ratio of observed to expected reporting proportion
- **ROR (Reporting Odds Ratio)** — odds ratio approach, similar to case-control studies

Pairs with high scores and sufficient report counts are flagged as signals worth investigating.

---

## 🛠️ Tech Stack

- **Python** — core processing
- **Pandas** — data ingestion, merging, aggregation, scoring
- **Jupyter Notebooks** — `ingest.ipynb` (data preparation) and `scoring.ipynb` (signal computation)
- **Streamlit** — dashboard to explore and filter ranked signals
- **CSV pipeline** — Fares Raw → Pairs Dataframe → Signal Ranked

---

## 📁 Project Structure

```
Adverse-Event-Ranking-System/
│
├── ingest.ipynb            # Data loading and preprocessing notebook
├── scoring.ipynb           # Disproportionality scoring computation
├── app.py                  # Streamlit dashboard for signal exploration
├── Fares Raw.csv           # Raw drug-adverse event report data
├── Pairs Dataframe.csv     # Processed drug-event pair counts
├── Signal Rannked.csv      # Final ranked signals output
└── requirements.txt        # Dependencies
```

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Precipitation-Rain/Adverse-Event-Ranking-System.git
cd Adverse-Event-Ranking-System

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run notebooks in order
# Open and run: ingest.ipynb → scoring.ipynb

# 4. Launch the dashboard
streamlit run app.py
```

---

## 📊 Pipeline Flow

```
Raw Report Data (Fares Raw.csv)
        ↓
   [ingest.ipynb]
   Data cleaning, pairing, counting
        ↓
Pairs Dataframe (drug × adverse event counts)
        ↓
   [scoring.ipynb]
   Disproportionality scoring per pair
        ↓
Signal Ranked (sorted by signal strength)
        ↓
   [app.py]
   Streamlit dashboard — explore, filter, download
```

---

## 🎯 Real-World Relevance

The FDA's FAERS (FDA Adverse Event Reporting System) uses similar disproportionality analysis to trigger safety investigations. Pharmaceutical companies, academic pharmacologists, and health agencies use these methods daily. Building a working pipeline from raw reports to ranked signals demonstrates understanding of both the domain and the analytical methodology.

---

## 💡 What I Learned

- How post-market drug surveillance works conceptually and computationally
- Disproportionality analysis as a signal detection framework
- Building a multi-stage data pipeline: ingest → score → visualize
- Separating pipeline stages into purpose-specific notebooks for maintainability

---

## 📬 Author

**Rajvardhan Shewale**
- [GitHub](https://github.com/Precipitation-Rain)
- [LinkedIn](https://www.linkedin.com/in/rajvardhanshewale/)
- [Portfolio](https://sites.google.com/view/rajvardhanshewale1771/home)
