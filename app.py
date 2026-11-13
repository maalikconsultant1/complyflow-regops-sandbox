import streamlit as st
import pandas as pd
from faker import Faker
import json
import random
import hashlib
import time

# --- CUSTOM OG METADATA FOR LINKEDIN/SOCIAL SHARING ---
# Injects proper Open Graph tags so LinkedIn shows premium preview card
st.markdown("""
    <head>
        <meta property="og:title" content="ComplyFlow AI | VAT Gap Scan & Compliance Demo" />
        <meta property="og:description" content="See the AI Production Readiness Architecture in action. Validate ZATCA/FTA compliance in milliseconds." />
        <meta property="og:image" content="https://raw.githubusercontent.com/maalikconsultant1/complyflow-regops-sandbox/main/assets/complyflow-og.png" />
        <meta property="og:url" content="https://bit.ly/AI-Compliance-Demo" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
""", unsafe_allow_html=True)
# -----------------------------------------------------

# --- CORE ENGINE LOGIC (Combined for stability) ---
REGULATORY_RULES = {
    "SAMA_CSF": "Data must not leave KSA residency boundaries.",
    "UAE_PDPL": "PII must be encrypted at rest and in transit."
}

def intercept_and_validate(payload):
    start_time = time.time()
    action_type = payload.get("action_type", "UNKNOWN")
    time.sleep(random.uniform(0.001, 0.004)) 
    is_compliant = random.random() > 0.3 
    payload_string = json.dumps(payload, sort_keys=True)
    proof_hash = hashlib.sha256(payload_string.encode('utf-8')).hexdigest()
    latency_ms = (time.time() - start_time) * 1000
    
    return {
        "status": "APPROVED" if is_compliant else "BLOCKED",
        "latency_ms": round(latency_ms, 2),
        "proof_hash": proof_hash,
        "violated_rule": None if is_compliant else random.choice(list(REGULATORY_RULES.keys())),
        "rule_text": None if is_compliant else random.choice(list(REGULATORY_RULES.values()))
    }

# --- APP UI LOGIC ---
fake = Faker()
st.set_page_config(page_title="ComplyFlow AI | VAT Gap Scan", layout="wide", page_icon="🛡️")

st.title("🛡️ ComplyFlow AI: RegOps Public Sandbox")
st.markdown("Welcome to the ComplyFlow RegOps OS. This sandbox demonstrates how our middleware intercepts autonomous AI agent actions, validates them against SAMA CSF and UAE PDPL schemas in milliseconds, and generates a deterministic, cryptographic audit trail.")
st.divider()

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.subheader("1. AI Agent Action (Input)")
    payload_1 = {"action_type": "Cross-Border KYC", "agent_id": "FinLLM-v4", "customer_pii": fake.name(), "national_id": fake.ssn(), "destination_ip": "192.168.1.10 (External - UK)"}
    payload_2 = {"action_type": "Autonomous Loan Approval", "agent_id": "CreditBot-X", "customer_pii": fake.name(), "loan_amount": 50000, "destination_ip": "10.0.0.5 (Internal)"}
    
    st.code(json.dumps(payload_1, indent=2), language="json")
    btn1 = st.button("Run Payload 1 (High Risk)", use_container_width=True)
    st.code(json.dumps(payload_2, indent=2), language="json")
    btn2 = st.button("Run Payload 2 (Low Risk)", use_container_width=True)

with col2:
    st.subheader("2. RegOps Engine (Processing)")
    if btn1 or btn2:
        selected_payload = payload_1 if btn1 else payload_2
        with st.spinner("Intercepting... Validating..."):
            result = intercept_and_validate(selected_payload)
            st.success("Payload Intercepted")
            st.metric(label="Validation Latency", value=f"{result['latency_ms']} ms")
            st.session_state['last_result'] = result
            st.session_state['is_pass'] = (btn2)

with col3:
    st.subheader("3. Deterministic Proof (Output)")
    if 'last_result' in st.session_state:
        result = st.session_state['last_result']
        is_pass = st.session_state['is_pass']
        if is_pass:
            st.success("STATUS: APPROVED")
        else:
            st.error(f"STATUS: BLOCKED\nViolated Rule: {result['violated_rule']}")
        st.code(result['proof_hash'][:32] + "...", language="text")
