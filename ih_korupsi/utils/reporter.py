import requests
import json
import hashlib
import time
from typing import Dict, Any

class EvidenceReporter:
    def __init__(self, target_url: str, api_key: str = None):
        self.target_url = target_url
        self.api_key = api_key

    def calculate_file_hash(self, file_path: str) -> str:
        """Menghitung SHA-256 hash dari file untuk integritas data."""
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    sha256.update(data)
            return "0x" + sha256.hexdigest()
        except FileNotFoundError:
            return None

    def send_report(self, input_file: str, output_json: Dict[str, Any]) -> Dict[str, Any]:
        """
        Mengirim hasil audit ke server eksternal (Validator/Relay).
        """
        print(f"\n[Reporter] Preparing to send evidence to: {self.target_url}")

        # 1. Hitung Hash Input (CSV)
        input_hash = self.calculate_file_hash(input_file)
        if not input_hash:
            return {"status": "error", "message": "Input file not found"}

        # 2. Hitung Hash Output (JSON Content)
        # Kita hash string JSON-nya agar konsisten
        json_str = json.dumps(output_json, sort_keys=True)
        output_hash = "0x" + hashlib.sha256(json_str.encode('utf-8')).hexdigest()

        print(f"   🔹 Input Fingerprint  : {input_hash}")
        print(f"   🔹 Output Fingerprint : {output_hash}")

        # 3. Payload Standar
        payload = {
            "input_hash": input_hash,
            "output_hash": output_hash,
            "metadata": output_json.get("metadata", {}),
            "timestamp": time.time()
        }
        
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["x-api-key"] = self.api_key

        try:
            # Kirim Request
            response = requests.post(self.target_url, json=payload, headers=headers, timeout=30)
            
            if response.status_code == 200:
                print(f"   ✅ Success! Server responded: {response.status_code}")
                return response.json()
            else:
                print(f"   ❌ Failed! Server responded: {response.status_code}")
                return {"status": "failed", "error": response.text}
                
        except Exception as e:
            print(f"   ❌ Connection Error: {str(e)}")
            return {"status": "error", "message": str(e)}