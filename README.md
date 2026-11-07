# 🛡️ ComplyFlow AI: RegOps Public Sandbox

**AI Production Readiness Infrastructure for the GCC**

Welcome to the public sandbox for **ComplyFlow AI's RegOps OS**. This repository contains the source code for our interactive demonstration, showcasing how our middleware intercepts autonomous AI agent actions, validates them against **SAMA CSF** and **UAE PDPL** schemas in milliseconds, and generates a deterministic, cryptographic audit trail.

## 📉 The Problem: The "POC Graveyard"
80% of enterprise AI projects in the GCC die in the "POC Graveyard." Not because the technology fails, but because the compliance evidence chain breaks. Regulators (SAMA, CBUAE) require runtime monitoring and logging evidence. Third-party LLM APIs cannot provide inference-level audit trails, causing Model Risk Committees to block deployments.

## 🚀 The Solution: Continuous Runtime Assurance
ComplyFlow AI acts as the "missing middle" layer. We do not replace your core banking or AI detection engines; we integrate with their outputs to make them instantly regulator-ready.

### Key Capabilities Demonstrated in this Sandbox:
* **Real-Time Interception:** Catches AI agent payloads before they hit enterprise APIs.
* **Sub-Millisecond Validation:** Checks payloads against mapped regulatory JSON schemas (SAMA CSF, UAE PDPL) in <5ms.
* **Deterministic Proof:** Generates an immutable, SHA-256 hashed audit trail for *every single inference*.
* **Zero Latency Impact:** Asynchronous validation ensures no disruption to core banking operations.

## 🏗️ Architecture & Workflow
The sandbox demonstrates our 3-step RegOps workflow:
1. **Input:** Simulated AI agent actions (e.g., Cross-Border KYC Data Transfer, Autonomous Loan Approval).
2. **Processing:** The RegOps Engine intercepts the payload, validates data residency and PII rules, and calculates latency.
3. **Output:** A deterministic `APPROVED` or `BLOCKED` status, complete with a cryptographic proof hash for regulator review.

## 🛠️ Running Locally
To run this sandbox locally, ensure you have Python 3.8+ installed.

```bash
# Clone the repository
git clone https://github.com/maalikconsultant1/complyflow-regops-sandbox.git
cd complyflow-regops-sandbox

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
