# Genie Code prompt

Fill in the folder path at the top, then paste everything below the line into Genie Code.

---

Deploy the Public Bank Finance Workbench as a Databricks App in this workspace.

- Kit folder (this repo, already cloned as a Git folder or imported into the workspace): `<YOUR_FOLDER>`, for example `/Workspace/Users/<me>/pbb-finance-workbench`

Read `<YOUR_FOLDER>/README.md` first. The app is a static single-page app in `<YOUR_FOLDER>/app` (`app.py`, `app.yaml`, `index.html`). It needs no Unity Catalog data, SQL warehouse, model endpoint, secrets or app resources, so don't create or attach any. Don't change the app source. Do the following steps in order, and stop and tell me if any step fails.

1. **Create the app.** Create a Databricks App named `pbb-finance-workbench` with description "Public Bank Finance Workbench". If an app with that name already exists, reuse it.
2. **Deploy.** Deploy the app with source code path `<YOUR_FOLDER>/app`. Wait until the deployment state is SUCCEEDED and the app is RUNNING.
3. **Verify.** Give me the app URL. Opening it should land on the CFO Briefing page (`#cfo-brief`). If the deployment fails, show me the app logs.
