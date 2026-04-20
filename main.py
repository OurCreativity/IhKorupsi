import argparse
import sys
import json
from ih_korupsi.utils.data_loader import DataLoader
from ih_korupsi.core.engine import FraudEngine
from ih_korupsi.utils.report_generator import ReportGenerator

try:
    from ih_korupsi.utils.reporter import EvidenceReporter
except ImportError:
    EvidenceReporter = None

def main():
    parser = argparse.ArgumentParser(description="IH-Korupsi: Open Source Forensic Data Toolkit")
    parser.add_argument("--input", type=str, help="Path to input data (CSV/JSON)")
    parser.add_argument("--type", type=str, choices=['csv', 'json', 'sample'], default='sample', help="Data format")
    parser.add_argument("--output", type=str, default="fraud_report.json", help="Path to JSON report output")
    parser.add_argument("--html", type=str, help="If provided, save a visual HTML report to this path")
    parser.add_argument("--report-url", type=str, help="(Optional) URL to send the audit evidence (e.g., Blockchain Validator)")
    
    args = parser.parse_args()

    print("--- IH-Korupsi Forensic Toolkit ---")
    
    if args.type == 'sample':
        print("Generating 500 rows of synthetic transaction data...")
        df = DataLoader.generate_sample_data(500)
    else:
        if not args.input:
            print("Error: --input is required for non-sample data.")
            sys.exit(1)
        df = DataLoader.load(args.input, args.type)

    engine = FraudEngine()
    report = engine.process(df)
    
    # Save JSON
    engine.save_report(report, args.output)
    
    # Save HTML if requested
    if args.html:
        html_content = ReportGenerator.generate_html(report)
        with open(args.html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Visual HTML report saved to {args.html}")

    print("Analysis complete. Check the report for detailed mathematical evidence.")
    
    # Remote Reporting / Blockchain Anchoring
    if args.report_url:
        print("\n--- Remote Reporting / Evidence Anchoring ---")
        
        if EvidenceReporter is None:
            print("Error: module 'modules.reporter' not found. Cannot send report.")
        elif args.type == 'sample':
            print("Warning: Cannot anchor sample data (no physical input file to hash).")
            print("   Please use a real CSV/JSON file with --input to use this feature.")
        else:
            reporter = EvidenceReporter(args.report_url)
            
            print(f"Sending evidence to: {args.report_url}...")
            server_response = reporter.send_report(args.input, report)
            
            if server_response:
                if "relay_processed_id" in server_response:
                    print(f"Evidence Anchored Successfully!")
                    print(f"Proof ID: {server_response['relay_processed_id']}")
                    
                    val_resp = server_response.get("validator_response", {})
                    if "txHash" in val_resp:
                        print(f"Blockchain TX: {val_resp['txHash']}")
                        print(f"Check on explorer : https://sepolia.scrollscan.com/tx/{val_resp['txHash']}")
                else:
                    print(f"Server Response: {json.dumps(server_response, indent=2)}")

if __name__ == "__main__":
    main()
