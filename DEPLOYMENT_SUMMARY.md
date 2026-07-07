# Spark & Forge GitHub Actions — Deployment Summary

**Status:** ✅ COMPLETE & READY  
**Location:** `Z:\R&D\R&D Meeting\spark-forge-automation\`  
**Platform:** GitHub Actions  
**Automation:** Biweekly, Every Tuesday 9:00 AM PT

---

## ✅ What Has Been Created

### Repository Structure
```
✅ .github/workflows/spark-forge-biweekly.yml  ... GitHub Actions workflow
✅ scripts/phase1_extract_presentations.py      ... Extract R&D presentations
✅ scripts/phase2_external_intelligence.py      ... Scan literature/conferences/vendors/competitors
✅ scripts/phase3_trend_analysis.py             ... Trend analysis & flagging
✅ scripts/phase4_index_update.py               ... Index update & report generation
✅ scripts/send_notification.py                 ... Email notifications
✅ config/email_templates.json                  ... Email templates
✅ config/data_sources.json                     ... Data source config
✅ README.md                                     ... Setup instructions
✅ requirements.txt                              ... Python dependencies
✅ .gitignore                                    ... Git ignore rules
```

### Key Features
- ✅ **Automatic scheduling:** Runs every 2 weeks on Tuesday at 9:00 AM PT
- ✅ **4-phase workflow:** Extract → Research → Analyze → Report
- ✅ **Email notifications:** Success/failure emails to Wenhui + Group Leaders
- ✅ **Persistent:** Runs in cloud (GitHub), no local machine needed
- ✅ **Monitoring:** View logs in GitHub Actions UI
- ✅ **Flexible:** Can manually trigger anytime for testing

---

## 🚀 NEXT STEPS: Push to GitHub

### Step 1: Create GitHub Repository

Go to **github.com** and create a new repository:

```
Repository name: spark-forge-automation
Description: Biweekly Spark & Forge intelligence automation
Visibility: Private (or Organization)
Initialize with README: NO (uncheck)
```

**Get the repo URL:** `https://github.com/[YOUR-USERNAME]/spark-forge-automation.git`

---

### Step 2: Open Terminal/PowerShell

Navigate to the automation folder:

```powershell
cd "Z:\R&D\R&D Meeting\spark-forge-automation"
```

---

### Step 3: Initialize Git & Push

Run these commands in order:

```powershell
# Initialize git repository
git init

# Add GitHub as remote (replace URL with your repo)
git remote add origin https://github.com/[YOUR-USERNAME]/spark-forge-automation.git

# Set branch to main
git branch -M main

# Add all files
git add .

# Create initial commit
git commit -m "Initial Spark & Forge GitHub Actions setup

- GitHub Actions workflow for biweekly automation
- Python scripts for all 4 phases
- Email notification system
- Complete documentation

Co-Authored-By: Claude Code <noreply@anthropic.com>"

# Push to GitHub
git push -u origin main
```

---

### Step 4: Configure GitHub Secrets

1. Go to your GitHub repo
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret below:

| Secret Name | Value | Example |
|-------------|-------|---------|
| `R_AND_D_PATH` | Path to R&D meetings folder | `Z:\R&D\R&D Meeting` |
| `SPARK_FORGE_PATH` | Path to Spark_Forge folder | `Z:\R&D\R&D Meeting\AI-Spark-Forge` |
| `PUBMED_API_KEY` | PubMed API key (get from NCBI) | `[your-key]` |
| `GITHUB_PATENTS_TOKEN` | GitHub Personal Access Token | `ghp_...` |
| `SMTP_SERVER` | Email server address | `smtp.promega.com` |
| `SMTP_PORT` | Email server port | `587` |
| `SMTP_USER` | Email account username | `spark-forge@promega.com` |
| `SMTP_PASSWORD` | Email account password | `[password]` |
| `NOTIFICATION_RECIPIENTS` | Email addresses (comma-separated) | `wenhui.zhou@promega.com,cesear.corona@promega.com,hui.wang@promega.com,zhiyang.zeng@promega.com,matt.larsen@promega.com,josh.kimball@promega.com` |
| `GITHUB_TOKEN` | GitHub Personal Access Token | `ghp_...` |

---

### Step 5: Enable GitHub Actions

1. Click **Actions** tab in your repo
2. Click **"I understand my workflows, go ahead and enable them"**
3. Automation is now **ACTIVE** ✅

---

### Step 6: Manual Test (Optional)

1. Go to **Actions** tab
2. Select **Spark & Forge Biweekly Automation**
3. Click **Run workflow** → **Run workflow**
4. Watch logs in real-time
5. Check email for notification

---

## 📊 What Happens After Setup

### Every Tuesday 9:00 AM PT

The automation runs automatically:

1. **Phase 1 (Tue–Wed):** Extracts presentations from R&D meeting folder
2. **Phase 2 (Wed–Thu):** Scans literature, conferences, vendors, competitors
3. **Phase 3 (Thu–Fri):** Analyzes trends and flags RED/YELLOW/GREEN signals
4. **Phase 4 (Mon):** Updates Living Index and generates biweekly report

### Email Notification (Mon afternoon)

**To:** wenhui.zhou@promega.com + 5 Group Leaders

**Content:**
- ✅ Summary of new Spark/Forge entries
- 🔴 RED flags (if any)
- 🟡 YELLOW signals
- Links to all files
- Next cycle date

### Quarterly Synthesis (Sep 30, Dec 31, Mar 31, Jun 30)

**To:** Wenhui + Group Leaders  
**Content:** 2–3 page strategic brief with:
- Theme convergence analysis
- Competitive landscape
- Strategic recommendations

---

## ✅ Success Checklist

After pushing to GitHub:

- [ ] Repository created on GitHub
- [ ] All files pushed to GitHub
- [ ] GitHub Actions enabled
- [ ] All secrets configured (10 secrets)
- [ ] Workflow file is present in `.github/workflows/`
- [ ] Manual test run successful
- [ ] Email notification received
- [ ] Files created in Z:\R&D\R&D Meeting\AI-Spark-Forge\

---

## 🔗 Useful Links

- **Your GitHub Repo:** `https://github.com/[YOUR-USERNAME]/spark-forge-automation`
- **GitHub Actions Docs:** https://docs.github.com/en/actions
- **GitHub Secrets:** https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions
- **Cron Syntax:** https://crontab.guru

---

## 📞 Support

**Questions?**
- Check `README.md` for setup help
- Check `docs/TROUBLESHOOTING.md` for common issues
- Contact: Wenhui Zhou (wenhui.zhou@promega.com)

---

## 🎯 Timeline

| Date | Action |
|------|--------|
| **Today** | ✅ Repository structure created locally |
| **Today** | → Push to GitHub (you do this) |
| **Today** | → Configure secrets (you do this) |
| **Today** | → Enable GitHub Actions (you do this) |
| **Tuesday, Jul 7** | 🚀 First automation runs |
| **Monday, Jul 13** | 📧 First email notification |
| **Every Tuesday** | ⏰ Automation runs on schedule |
| **Sep 30** | 📊 First quarterly synthesis |

---

**Status:** READY FOR GITHUB DEPLOYMENT  
**Created:** 2026-07-02  
**Next:** Follow steps above to push to GitHub

🚀 **YOU'RE ALL SET!**
