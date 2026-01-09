![IH-Korupsi Banner](banner.png)

# IH-Korupsi: Anti-Corruption Data Forensic Toolkit

**IH-Korupsi** (short for **Intelligent Hunting (IH) - Korupsi**) is an open-source Python toolkit designed to detect financial anomalies and potential corruption using pure mathematical methods **without AI/Machine Learning**.

Developed by **OurCreativity Edisi Coding** to support transparency and financial accountability worldwide.

---

## Why IH-Korupsi?

Corruption harms economies and societies. IH-Korupsi provides an educational and professional tool that can be used by:
- Government internal auditors
- Investigative journalists
- Anti-corruption researchers
- Students of data forensics
- Transparency NGOs
- Anyone committed to fighting corruption

### Core Principles
1. **Transparency**: Every anomaly detection can be explained through mathematical formulas.
2. **Auditable**: No "black box" algorithms—everything is open and deterministic.
3. **Zero AI Dependency**: Pure statistics and mathematics to ensure results are legally defensible.
4. **Open Source**: Free to use, study, and improve.

---

## Key Features

### 1. The Mathematician (Statistical Detection)

#### Benford's Law
Detects manipulation in financial reports. Benford’s Law states that in natural financial data, the first leading digit follows a specific logarithmic distribution. If someone fabricates numbers, the distribution will likely deviate.

**Case Example**: Financial reports that are manipulated tend to have an unusual spike in numbers starting with digits like 5, 6, 7, or 8.

#### Relative Size Factor (RSF)
Identifies unusual transactions for a specific entity. RSF compares an entity's largest transaction to the average of its other transactions.

**Formula**: `RSF = Largest Transaction / Average of Other Transactions`

**Case Example**: A vendor that usually receives $500–$1,000 suddenly gets a contract for $50,000.

#### Z-Score & IQR
Standard statistical methods to find extreme outliers in transaction data.

---

### 2. The Connector (Network Analysis)

#### Circular Trading Detection
Finds funds that return to the original sender through multiple intermediaries.

**Case Example**: 
```
Department A → Vendor X → Sub-vendor Y → Consultant Z → Department A
```
This pattern is often used for price mark-ups or money laundering loops.

#### Centrality Analysis
Finds hidden key actors in a network using algorithms like PageRank and Betweenness Centrality.

---

### 3. The Chronologist (Time-Series Analysis)

#### Fiscal Cliff Dumping
Detects unusual spending spikes during the final month of the fiscal year (budget dumping).

**Indicator**: Ratio of December spending vs. monthly average > 2.5x.

#### Velocity Check
Detects inhuman transaction frequencies within a short period.

**Case Example**: 50 transactions in a single day for the same vendor.

---

### 4. String Detective (Name Duplication)

#### Fuzzy Name Matching
Identifies "Ghost Vendors"—entities with slightly different names but likely the same identity.

**Examples**:
- `Global Solutions Corp` vs `Global  Solutions Corp` (double space)
- `Smith & Sons Ltd` vs `Smith and Sons Ltd`

Uses the Levenshtein Distance algorithm without external NLP libraries.

---

## Installation

### Prerequisites
- Python 3.10 or newer
- Windows / Linux / MacOS

### Setup

1. Clone this repository:
```bash
git clone https://github.com/[username]/ih-korupsi.git
cd ih-korupsi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

### Mode 1: Run with Sample Data (For Learning)

Run the toolkit with synthetic data containing injected anomalies:

```bash
python main.py --type sample --output sample_report.json --html visual_report.html
```

The system will:
1. Generate 500 rows of synthetic transaction data.
2. Inject intentional anomalies (Benford, RSF, Fiscal Cliff).
3. Execute all detection modules.
4. Generate a JSON data report and a beautiful HTML visual report.

### Mode 2: Analyze Your Own Data

#### CSV Format
Your CSV must include at least these columns:
- `amount`: Transaction value
- `vendor_name`: Vendor or recipient name
- `vendor_id`: Unique vendor ID
- `date`: Transaction date (YYYY-MM-DD)
- `sender_id`: Sender identifier
- `receiver_id`: Receiver identifier

Example:
```bash
python main.py --input my_data.csv --type csv --output my_results.json --html report.html
```

---

## Understanding the Report

The JSON report is structured as follows:

```json
{
  "metadata": {
    "total_rows": 500,
    "total_amount": 300000000,
    "currency": "IDR"
  },
  "findings": {
    "The Mathematician": { ... },
    "The Connector": { ... },
    "The Chronologist": { ... },
    "String Detective": { ... }
  }
}
```

### Interpreting Findings

#### Benford's Law (MAD Score)
- **MAD < 0.006**: High Conformity (Normal)
- **MAD 0.006–0.012**: Acceptable
- **MAD 0.012–0.015**: Marginal (Needs attention)
- **MAD > 0.015**: Non-conformity (Red flag!)

#### RSF (Relative Size Factor)
- **RSF < 5**: Normal
- **RSF 5–10**: Needs verification
- **RSF > 10**: Highly suspicious

---

## Important Notes & Limitations

1. **Not Legal Proof**: IH-Korupsi provides **indicators only**. Anomalies do not automatically mean corruption; they require further investigation.
2. **Context Matters**: Some anomalies can be legitimate (e.g., a massive infrastructure project causing a high RSF).
3. **Data Quality**: Garbage in, garbage out. Ensure your input data is clean.
4. **Ethical Use**: This toolkit is for transparency and education. Please use it responsibly.

---

## About OurCreativity Edisi Coding

We are a developer community that believes technology can be a force for social good. IH-Korupsi is one of our efforts toward a more transparent and accountable future.

**Slogan**: *"Code for Justice, Data for Transparency"*

---

## License

This project is licensed under the **MIT License**.

---

**Join us in building a cleaner, more transparent world!**
