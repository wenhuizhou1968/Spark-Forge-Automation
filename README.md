# Spark & Forge Biweekly Automation

**Status:** ✅ Ready to Deploy to GitHub  
**Automation Platform:** GitHub Actions  
**Schedule:** Every 2 weeks, Tuesday 9:00 AM PT  
**Owner:** Promega Chemistry Research

---

## 🚀 Quick Start

### 1. Create GitHub Repository

```bash
# Create new repo on github.com:
# - Name: spark-forge-automation
# - Visibility: Private (or Organization repo)
# - Initialize with README: NO (we have one)
```

### 2. Initialize Local Git Repository

```bash
cd "Z:\R&D\R&D Meeting\spark-forge-automation"

# Initialize git
git init

# Add remote
git remote add origin https://github.com/[YOUR-ORG]/spark-forge-automation.git

# Set branch to main
git branch -M main

# Add all files
git add .

# Initial commit
git commit -m "Initial Spark & Forge automation setup

- GitHub Actions workflow for biweekly cycles
- Python scripts for all 4 phases
- Email notification system
- Documentation and configuration

Co-Authored-By: Claude Code <noreply@anthropic.com>"

# Push to GitHub
git push -u origin main
```

### 3. Configure GitHub Secrets

Go to **GitHub Repository → Settings → Secrets and variables → Actions**

Add these secrets:

| Secret | Value | Example |
|--------|-------|---------|
| `R_AND_D_PATH` | R&D meeting folder path | `Z:\R&D\R&D Meeting` |
| `SPARK_FORGE_PATH` | Spark_Forge folder path | `Z:\R&D\R&D Meeting\AI-Spark-Forge` |
| `PUBMED_API_KEY` | PubMed API key (optional) | `[your-key]` |
| `GITHUB_PATENTS_TOKEN` | GitHub API token | `[your-token]` |
| `SMTP_SERVER` | Email server | `smtp.promega.com` |
| `SMTP_PORT` | Email port | `587` |
| `SMTP_USER` | Email user | `spark-forge@promega.com` |
| `SMTP_PASSWORD` | Email password | `[your-password]` |
| `NOTIFICATION_RECIPIENTS` | Email list (comma-separated) | `wenhui.zhou@promega.com,cesear.corona@promega.com,...` |
| `GITHUB_TOKEN` | GitHub Personal Access Token | `ghp_...` |

### 4. Enable GitHub Actions

1. Go to **Actions** tab in your GitHub repo
2. Click **"I understand my workflows, go ahead and enable them"**
3. Automation is now **ACTIVE** ✅

---

## 📁 Folder Structure

```
spark-forge-automation/
├── .github/
│   └── workflows/
│       └── spark-forge-biweekly.yml ........ GitHub Actions workflow (MAIN FILE)
├── scripts/
│   ├── phase1_extract_presentations.py .... Extract R&D presentations
│   ├── phase2_external_intelligence.py ... Scan literature, conferences, vendors, competitors
│   ├── phase3_trend_analysis.py ........... Trend analysis & RED/YELLOW/GREEN flagging
│   ├── phase4_index_update.py ............ Update index & generate report
│   └── send_notification.py .............. Send emails
├── config/
│   ├── email_templates.json .............. Email notification templates
│   └── data_sources.json ................. External data source configuration
├── docs/
│   ├── SETUP.md .......................... Setup instructions (this file)
│   ├── WORKFLOW_OVERVIEW.md .............. How the automation works
│   └── TROUBLESHOOTING.md ................ Common issues & fixes
├── logs/ .................................. Workflow logs (created during runs)
├── README.md ............................. This file
├── .gitignore ............................ Git ignore rules
└── requirements.txt ...................... Python dependencies
```

---

## 🔄 How It Works

### Schedule
- **Trigger:** Every 2 weeks on Tuesday at 9:00 AM PT (17:00 UTC)
- **Cron:** `0 17 * * 2` (every Tuesday at 17:00 UTC)
- **Manual trigger:** Can run anytime via GitHub Actions UI

### Workflow Phases

1. **Phase 1: Extract Presentations** (Tue–Wed)
   - Finds presentations from Z:\R&D\R&D Meeting\
   - Extracts Spark & Forge topics
   - Saves entries to JSON

2. **Phase 2: External Intelligence** (Wed–Thu)
   - Searches PubMed, bioRxiv, ChemRxiv (literature)
   - Scans AACC, ASMS, ACS conference abstracts
   - Checks vendor announcements
   - Monitors competitor activity (Roche, Thermo, Bio-Rad)

3. **Phase 3: Trend Analysis** (Thu–Fri)
   - Analyzes tag frequency
   - Scores convergence signals
   - Flags RED/YELLOW/GREEN signals

4. **Phase 4: Index Update** (Mon)
   - Updates Spark_Forge_Index.xlsx
   - Generates biweekly trend report (Markdown)
   - Sends email notification to Wenhui + Group Leaders

### Notifications

**Success Email:** 
- To: Wenhui + 5 Group Leaders
- Subject: "Spark & Forge Biweekly Cycle Complete — [Date]"
- Content: Summary + new entries + RED flags + links

**Failure Email:**
- To: Wenhui + IT
- Subject: "⚠️ Spark & Forge Automation Failed"
- Content: Error details + log file link

---

## 🧪 Testing

### Test Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run Phase 1
python scripts/phase1_extract_presentations.py

# Run Phase 2
python scripts/phase2_external_intelligence.py

# Run Phase 3
python scripts/phase3_trend_analysis.py

# Run Phase 4
python scripts/phase4_index_update.py
```

### Test in GitHub

1. Go to **Actions** → **Spark & Forge Biweekly Automation**
2. Click **"Run workflow"** → **"Run workflow"**
3. Watch logs in real-time
4. Check email for notification

---

## 📊 Monitoring

### View Workflow Runs

- GitHub UI: **Actions** tab → **Spark & Forge Biweekly Automation**
- See: Execution time, success/failure, logs

### Check Logs

- Click on a workflow run → **phase-4-index-update** → **Logs**
- Or: Check `logs/` folder in repo

### Check Results

- Living Index: `Z:\R&D\R&D Meeting\AI-Spark-Forge\Spark_Forge_Index.xlsx`
- Biweekly Report: `Z:\R&D\R&D Meeting\AI-Spark-Forge\Biweekly_Reports\[date]_Trend_Report.md`
- Email: Should arrive within 30 minutes of workflow completion

---

## 🔧 Customization

### Change Schedule

Edit `.github/workflows/spark-forge-biweekly.yml`:

```yaml
on:
  schedule:
    # Change this line for different schedule
    - cron: '0 17 * * 2'  # Currently: Every Tuesday at 9 AM PT
```

**Cron format:** `minute hour day month day-of-week`
- `0 17 * * 2` = Tuesday 9 AM PT
- `0 9 * * 1-5` = Weekdays 1 AM PT
- `0 0 1 * *` = First of each month

### Add/Remove Recipients

Edit GitHub Secret `NOTIFICATION_RECIPIENTS`:
```
wenhui.zhou@promega.com,cesear.corona@promega.com,hui.wang@promega.com
```

### Update Email Templates

Edit `config/email_templates.json` to customize notification emails.

---

## ⚠️ Troubleshooting

### Workflow doesn't run at scheduled time
- Check: GitHub Actions is enabled
- Check: Repo has commits in past 60 days (GitHub disables workflows on inactive repos)
- Solution: Manually trigger via **Actions** tab

### Emails not sending
- Check: SMTP secrets are configured correctly
- Check: Email server allows GitHub Actions IP range
- Check: Recipient emails are valid

### Presentations not found
- Check: `R_AND_D_PATH` secret is correct
- Check: Presentations exist in folder
- Check: Date range is correct (past 14 days)

### External data sources failing
- Check: API keys are valid (PubMed, GitHub Patents)
- Check: Internet connectivity
- Check: Rate limits not exceeded

See `docs/TROUBLESHOOTING.md` for more details.

---

## 📚 Documentation

- **SETUP.md** — Installation & configuration
- **WORKFLOW_OVERVIEW.md** — How each phase works
- **TROUBLESHOOTING.md** — Common issues & fixes
- **Spark_Forge_Biweekly_Workflow.md** — Original workflow documentation

---

## 👥 Support

**Spark_Forge Owner:** Wenhui Zhou (wenhui.zhou@promega.com)  
**Questions?** See `docs/` folder or contact Wenhui

---

## ✅ Status

- ✅ GitHub Actions workflow configured
- ✅ Python scripts created for all 4 phases
- ✅ Email notification system ready
- ✅ Documentation complete
- ✅ Ready to deploy

**Next step:** Push to GitHub and configure secrets 🚀

---

**Created:** 2026-07-02  
**Last Updated:** 2026-07-02  
**Status:** Ready for Production
