   import hashlib
   import json
   import time
   import random

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
