# Step-by-Step Execution Guide

## Step 1: Extract the project
Open the `Operation-Hydra` folder.

## Step 2: Verify Python
Run:
```bash
python --version
```
Python 3.9+ is sufficient. No external packages are required.

## Step 3: Review the simulated phishing evidence
Open:
- `evidence/phishing_emails/phishing_email_1.txt`
- `evidence/email_headers/header_1.txt`

Look for:
- urgency
- mismatched sender identity
- suspicious display/domain relationship
- suspicious attachment/link indicators

## Step 4: Run IP indicator analysis
```bash
python scripts/ip_analysis.py
```
The script reads fictional documentation-range IP addresses and checks whether they are private/reserved.

## Step 5: Review malware indicators
Open:
- `analysis/malware_analysis.md`
- `iocs/indicators_of_compromise.csv`

This project does **not** include executable malware.

## Step 6: Run financial fraud tracing
```bash
python scripts/transaction_trace.py
```
The script reads dummy CSV data and identifies the movement chain.

## Step 7: Read legal analysis
Open `analysis/legal_analysis.md`.

## Step 8: Prepare screenshots
Take screenshots of:
1. Project folder structure
2. IP analysis terminal output
3. Transaction trace output
4. GitHub repository page
5. GitHub Actions result

## Step 9: Upload to GitHub
```bash
git init
git add .
git commit -m "Initial Operation Hydra investigation"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

## Step 10: Final submission
Submit the GitHub link and the final report after adding your name, roll number, and screenshots.
