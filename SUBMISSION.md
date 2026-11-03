# Submission checklist

- [ ] Run locally and complete the README demo.
- [ ] Check at 375px, 768px and desktop widths; inspect browser console.
- [ ] Deploy the Python application and verify the shareable link on a phone.
- [ ] Create a GitHub repository and push this folder, excluding the database and secrets.
- [ ] Include a genuine export/share link of the coding conversation. BUILD_HISTORY.md is a factual development summary, not a conversation export.
- [ ] Review the limitations and covering note so the submission accurately describes the prototype.
- [ ] Add the actual application URL, repository URL and conversation export/link to the covering email.
- [ ] Send to assessment@enam.com with subject `ENAM - IIT screening - 2027`.

No email has been sent and no external repository or share link has been created.

## Covering note draft

Hello ENAM team,

I built FINN as an investment intelligence desk organised around attention: review the important developments, adjust what merits an alert, then follow the supporting evidence.

The prototype includes a diversified mock portfolio, a configurable filing digest, EOD anomaly rules and a company research workspace. The interface uses an actionable workspace toolbar and a compact signal timeline, with expandable facts and clear distinctions between facts, calculations and interpretation. Routine notices are collapsed, and missing research evidence produces an explicit abstention.

The architecture is deliberately small: FastAPI, SQLite and a custom responsive JavaScript frontend. Research currently retrieves exact user-supplied primary-source passages with document, period, page and URL references. It does not generate answers from a model’s company knowledge.

The main trade-off is scope. Market data and announcements are clearly labelled synthetic fixtures. Live ingestion, automated financial extraction and generative analysis remain incomplete. I prioritised an interactive, runnable workflow and honest provenance over implying that these integrations work. The next step is official document ingestion, validated quarterly tables and a source-grounded comparison of management guidance against results.

Application: [insert verified deployed URL]
Repository: [insert GitHub URL]
AI build history: [attach actual conversation export or insert genuine share link]

Thank you for reviewing my submission.
