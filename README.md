# Public Bank Finance Workbench: deploy kit

> **Disclaimer:** This is an independent demo built to show how Databricks can support a bank's Finance function. It is not affiliated with, endorsed by, or produced for Public Bank Berhad or any other bank named in it. Headline figures are approximations of publicly reported disclosures (annual reports, interim results, Pillar 3) and may be out of date. All other balances, customers, scenarios and AI answers are illustrative. Bank names, logos and trademarks belong to their respective owners and are used only for illustration.

A single-page Databricks App for a bank's Group Finance team. It walks through how a CFO Office, ALM desk, regulatory reporting team and finance quality team would work on one governed lakehouse, with AI/BI Genie style Q&A on every page.

## Pages

A persona dropdown (CFO, ALM Manager, Head of Regulatory & Treasury Reporting, and others) swaps the sidebar to show that role's pages.

| Group | Pages |
|---|---|
| CFO Office | CFO Briefing, Market & Peers |
| Asset Liability Management | Balance Sheet & Gaps, OPR Scenario Lab, Scenario Studio, Funding Strategy, Customer Behaviour, Product Dynamics |
| Group Financial & Treasury | Basel 3 Rule Assistant, Regulatory Data Hub, Capital & RWA, Accounting Config Studio, Product Classification, Financial Analysis, Board Pack Studio |
| Quality Assurance | Data Quality Monitor, Root Cause Tracer, ECL & Trend Insights |
| Workbench | Ask Finance, How It Works |

The app opens on `#cfo-brief`. Each page is a hash route, for example `#ma-opr` or `#gf-board`.

## What's in the kit

```
app/                 <- the Databricks App source (deploy this folder)
  app.py             <- 9-line static file server (Python standard library only)
  app.yaml           <- runs `python app.py`
  index.html         <- the whole app: HTML, CSS, JavaScript, embedded logos
GENIE_CODE_PROMPT.md <- paste into Genie Code to deploy it for you
```

## What the app needs in the workspace

Only Databricks Apps. The app has **no dependencies on other Databricks services**:

- No Unity Catalog tables, functions or volumes
- No SQL warehouse, Genie space, model serving endpoint or Vector Search index
- No Lakebase database, secrets or app resources
- No `requirements.txt`; nothing is installed at deploy time
- No calls to external websites, CDNs or web fonts; logos are embedded in `index.html`

The Genie answers, table names (for example `edw.dim_customer`), lineage and Lakehouse Federation sources shown in the UI are scripted for the demo. Nothing queries live data. If you want the panels to be live, that is a separate build: create the tables and Genie spaces, then wire the pages to them.

## Deploy with Genie Code

1. Get the code into your workspace. The easiest way is a Git folder: Workspace > Create > Git folder, and paste this repository's URL. Alternatively, download the repo and import the `app/` folder (for example to `/Workspace/Users/<you>/pbb-finance-workbench`).
2. Open Genie Code, fill in the folder path in `GENIE_CODE_PROMPT.md`, and paste the prompt.
3. Genie Code creates the app, deploys it and gives you the URL. It takes 2 to 3 minutes.

## Deploy manually

**UI:** Compute > Apps > Create app > Custom app, name it `pbb-finance-workbench`, then Deploy and point the source code path at the `app/` folder in your workspace.

**CLI:**

```bash
databricks workspace import-dir ./app /Workspace/Users/<you>/pbb-finance-workbench
databricks apps create pbb-finance-workbench --description "Public Bank Finance Workbench"
databricks apps deploy pbb-finance-workbench \
  --source-code-path /Workspace/Users/<you>/pbb-finance-workbench
```

## Run locally

```bash
cd app
python app.py          # serves on http://localhost:8000
```

Or just open `app/index.html` in a browser.
