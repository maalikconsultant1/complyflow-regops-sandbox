   import streamlit as st
   import pandas as pd
   from faker import Faker
   import json
   import random
   from regops_engine import intercept_and_validate

   fake = Faker()
   st.set_page_config(page_title="ComplyFlow RegOps Sandbox", layout="wide", page_icon="🛡️")

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
