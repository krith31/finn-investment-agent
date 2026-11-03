# FINN — AI development conversation record

> **Partial record, not a complete native chat export.** This file contains the original build prompt, selected follow-up messages and a separately labelled development summary. Tool calls, screenshots and some assistant messages are omitted.

## Original user build prompt (verbatim)

```text
# BUILD FINN — A DISTINCTIVE AI-POWERED FINANCIAL INVESTMENT INTELLIGENCE AGENT

You are acting as a senior full-stack engineer, product designer, AI engineer, and product architect.

I am participating in the ENAM Holdings AI Engineer Build Challenge. I have provided two PDF documents:

1. `ENAM_AI_Engineer_Build_Challenge_Main.pdf`
2. `ENAM_AI_Engineer_Build_Challenge_Reference.pdf`

These documents are the primary source of truth for this project.

Your task is to thoroughly understand both documents, inspect the existing project repository, and build a complete, working, mobile-first financial investment agent named **FINN (Financial Investment Agent)**.

This is not an ordinary dashboard-building exercise.

I want to build something that feels like a real product developed by a thoughtful engineering and investment research team. The design, interaction model, technical architecture, and overall experience should be distinctive enough to stand out among other submissions.

The challenge explicitly values creativity, product instinct, engineering judgment, and the ability to filter important information from noise.

Do not build a generic AI-generated dashboard.

---

# PHASE 1 — UNDERSTAND THE REQUIREMENTS BEFORE CODING

Before implementing anything:

1. Read both attached PDFs completely, including tables, illustrations, and all pages.
2. Extract every functional requirement from the main challenge document.
3. Understand the announcement categories, financial terminology, and document types in the reference document.
4. Identify the mandatory requirements versus optional research capabilities.
5. Inspect the existing repository, installed dependencies, folder structure, existing components, and available configuration.
6. Identify reusable code and avoid unnecessarily rewriting working functionality.

Create a concise internal implementation plan covering:

- Product architecture.
- Main user journeys.
- Frontend structure.
- Backend and data ingestion.
- AI/research pipeline.
- Data storage and caching.
- API design.
- Implementation priorities.
- Testing and deployment.

Do not stop after writing the plan. Proceed to implement the application.

If the existing project is empty, establish a clean and maintainable architecture.

Do not introduce unnecessary complexity.

# PHASE 2 — PRODUCT VISION AND IDENTITY

Product name: FINN

Full name: Financial Investment Agent.

Product positioning:

"An investment intelligence desk that knows what deserves your attention."

FINN should behave like a research associate who continuously monitors an investor's portfolio, identifies meaningful developments, investigates company fundamentals, and communicates findings concisely.

The product has two fundamental modes:

1. PUSH — FINN proactively surfaces important developments.
2. PULL — The investor asks FINN to investigate companies and financial questions.

The core product philosophy:

- Signal over noise.
- Evidence over speculation.
- Analysis over summarisation.
- Speed without sacrificing accuracy.
- Every important conclusion should have a traceable source.
- The interface should respect an investor's time.

Do not make this look like a stock-trading application. It is an investment intelligence and research product.

# PHASE 3 — VISUAL DESIGN AND DESIGN SYSTEM

This is one of the most important parts of the assignment.

I specifically do NOT want:

- Generic SaaS dashboard templates.
- Repeated rounded cards everywhere.
- Purple-blue AI gradients.
- Excessive glassmorphism.
- Generic chatbot interfaces.
- Randomly generated stock charts.
- Unnecessary decorative icons.
- Oversized empty dashboard sections.
- Identical layouts for every screen.
- Generic Tailwind/shadcn components used without customisation.

I want a carefully art-directed, premium institutional product.

## Creative direction: The Investor's Intelligence Desk

Take inspiration from the visual discipline of high-end financial terminals, editorial financial publications, institutional research platforms, and premium productivity software.

However, do not copy any existing product.

Create a distinct visual language for FINN.

### Colour system

Explore a palette built around:

- Deep ink / midnight navy.
- Warm ivory / parchment.
- Muted copper / burnt orange as the primary accent.
- Restrained sage green for positive signals.
- Muted red for genuine risk signals.
- Neutral greys for secondary information.

You can choose either a sophisticated light-first or dark-first interface, but establish a coherent theme.

Avoid using colours merely for decoration.

### Typography

Use a distinctive typographic hierarchy.

Consider pairing:

- An editorial serif typeface for important headlines and research narratives.
- A clean, modern sans-serif for interface elements.
- Tabular or monospaced numerals for financial data.

Financial numbers must be aligned and easy to compare.

Use typography, spacing, dividers, and layout composition to establish hierarchy instead of surrounding every element with a card.

### Custom components

Design a component library specifically for FINN.

Some possible components:

1. Signal Brief — A compact, editorial-style explanation of an important development.
2. Market Pulse — A visual representation of unusual market activity.
3. Filing Timeline — A chronological stream of corporate announcements.
4. Conviction Meter — A clearly explained analytical assessment, never an unsupported AI confidence score.
5. Evidence Drawer — The original source, extracted passages, page references, and supporting data.
6. Financial Delta — An elegant comparison of QoQ and YoY numbers.
7. Narrative Tracker — Management promises versus actual outcomes.
8. Research Note — A structured investment research document.
9. Attention Queue — A prioritised list of developments requiring investigation.
10. Watchlist Strip — A compact portfolio overview.

These are design directions, not mandatory component names. Improve upon them where appropriate.

Make components visually different according to their purpose.

### Responsive design

Mobile-first is mandatory.

The mobile application must feel intentionally designed for a phone, not like a desktop website squeezed into a smaller viewport.

Implement:

- Responsive navigation.
- Touch-friendly controls.
- Readable financial tables.
- Collapsible sections.
- Bottom navigation where appropriate.
- Carefully designed mobile research views.
- Responsive charts.
- Proper loading and empty states.

Desktop should still provide a sophisticated research workspace.

# PHASE 4 — CORE APPLICATION EXPERIENCE

Build the following major sections.

## 1. Intelligence Home

This should be the investor's landing page.

It should answer three questions immediately:

- What happened?
- Why should I care?
- What should I investigate next?

Include:

- Today's important signals.
- Portfolio movement.
- Recent high-priority announcements.
- Unusual volume and price activity.
- Important upcoming corporate events where data is available.
- A concise daily intelligence summary.
- Quick access to company research.

Do not make the home page a collection of meaningless KPI cards.

Give it a strong editorial hierarchy.

The most important development should visually dominate.

## 2. Portfolio

Allow the investor to maintain a mock portfolio containing 15–20 NSE/BSE-listed companies.

Choose a diversified initial portfolio across sectors and market capitalisations.

Do not select companies randomly. The selection should make the demonstration interesting.

Provide:

- Company name and ticker.
- Sector.
- Latest available EOD price.
- Daily percentage change.
- Trading volume.
- Recent announcement count.
- Important active signals.
- Company research entry point.

Include search, sorting, filtering, and company-level navigation.

Do not hardcode company-specific research logic.

## 3. Push Intelligence — Daily Digest

Implement a configurable corporate announcement digest.

Default period: Last 24 hours.

Allow the investor to select other time windows.

Fetch and classify corporate announcements from NSE/BSE.

Use the announcement categories described in the companion PDF:

- results
- M&A
- fund_raise
- management_change
- litigation
- insider_trading
- earnings_call
- investor_meetings
- credit_rating
- dividend
- bonus_split
- capex
- press_release
- postal_ballot
- agm_egm
- pledging
- unclassified

These categories may be adapted, but preserve their meanings.

The system should:

- Identify the company.
- Extract the announcement date.
- Identify the announcement category.
- Summarise the actual development.
- Estimate its potential relevance to the company.
- Prioritise important announcements.
- Collapse or de-emphasise routine announcements.
- Provide access to the original filing.

Clearly distinguish an observed fact from an AI interpretation.

Do not present every announcement as equally important.

## 4. Intelligent Triggered Alerts

Implement configurable monitoring rules.

At minimum:

A. Volume anomaly

Flag a company when trading volume exceeds approximately 2x its recent average.

B. Price anomaly

Allow the investor to configure positive and negative daily price movement thresholds.

C. Announcement alerts

Allow investors to select announcement categories they want to monitor.

Provide a settings interface where these thresholds and preferences can be changed.

Use historical EOD price and volume data.

Avoid creating fake live monitoring. Clearly communicate the data's actual update frequency.

If the data is EOD, describe the alert as an EOD signal rather than a real-time market alert.

## 5. Quarterly Results Intelligence

This is an important feature.

When a results filing is detected, extract:

- Revenue
- EBITDA
- PBT
- PAT

Show:

- Current quarter.
- Previous quarter.
- Same quarter in the previous year.
- QoQ percentage change.
- YoY percentage change.

Clearly label units and financial periods.

Where possible, calculate margins as well.

Do not invent unavailable values.

If the original filing cannot be parsed reliably, display an extraction warning rather than fabricated financial information.

## 6. Management Change Intelligence

When a significant executive appointment or resignation is detected:

- Identify the individual.
- Identify the position.
- Explain what changed.
- Retrieve professional background when reliable public information is available.
- Provide the source of the biography.
- Explain why the appointment might matter to investors.

Do not invent career history.

This professional-background enrichment is permitted on the PUSH side.

# PHASE 5 — PULL: ON-DEMAND RESEARCH ENGINE

This should be a distinctive part of FINN.

Build an interactive research experience.

The investor should be able to:

- Search for any supported NSE/BSE ticker.
- Open a structured company research workspace.
- Ask natural-language questions.
- Request a specific financial analysis.
- Investigate management commentary.
- Compare management guidance against actual results.

Use the following research capabilities as the foundation.

### A. Business Snapshot

- What the company does.
- Business segments.
- Revenue contribution.
- Business model.
- Key operating drivers.

### B. Financial Snapshot

- Revenue.
- EBITDA.
- EBITDA margin.
- PBT.
- PAT.
- Important financial ratios.

### C. Business Trajectory

- Multi-year revenue growth.
- Profitability trend.
- Margin expansion or compression.
- Segment performance.
- Significant changes in business direction.

### D. Balance Sheet

- Debt.
- Debt-to-equity.
- Leverage.
- Working-capital cycle.
- Funding structure.

### E. Cash Quality

- Operating cash flow.
- Free cash flow.
- Cash conversion.
- Profit versus actual cash generation.
- Potential cash-flow red flags.

### F. Narrative vs. Numbers

Give this capability special attention.

Compare management's statements and expectations with actual financial performance.

For example:

- What did management say about revenue growth?
- What did they say about margins?
- What capex did they announce or plan?
- What was actually delivered?
- Where did management meet expectations?
- Where did actual performance diverge?
- What explanations did management provide?

Present a comparison across the last four quarters where sufficient source data exists.

Every conclusion must be grounded in actual management commentary and financial statements.

### G. Management Guidance

Extract explicit management expectations for:

- Revenue growth.
- Margins.
- Capacity expansion.
- Capex.
- Other relevant business KPIs.

Distinguish explicit guidance from general optimistic commentary.

### H. Bull vs Bear

Present:

- Strongest evidence-backed bullish arguments.
- Strongest evidence-backed bearish arguments.
- Key risks.
- Unresolved questions.
- What an investor should monitor next.

Do not produce an unsupported buy/sell recommendation.

The research experience should feel like reading a well-written institutional research note, not receiving a generic AI-generated answer.

# PHASE 6 — CRITICAL DATA AND RESEARCH DISCIPLINE

This section is non-negotiable.

The challenge explicitly requires the PULL research engine to rely on primary sources.

Permitted sources include:

- Company annual reports.
- Quarterly results filings.
- Earnings/concall transcripts.
- Company investor presentations.
- Official company investor-relations disclosures.

Do NOT use:

- Broker reports.
- News articles.
- External research reports.
- Generic internet knowledge about the company.
- Unverified third-party summaries.

Do not let an LLM answer financial questions using its pretrained company knowledge.

## Implement source-grounded analysis

Build a pipeline:

1. Fetch the original document.
2. Extract its text and relevant tables.
3. Preserve document metadata.
4. Chunk the content intelligently.
5. Store source references.
6. Retrieve relevant chunks for each query.
7. Generate an answer using only retrieved evidence.
8. Attach citations to the conclusions.

Where practical, citations should include:

- Document name.
- Financial period.
- Page number.
- Relevant passage or table.
- Source URL.

If the model cannot find supporting evidence, it must explicitly say so.

Never invent figures, guidance, management quotes, or citations.

Separate:

FACT — Explicitly disclosed information.

CALCULATION — A value computed from disclosed information.

INTERPRETATION — An analytical conclusion derived from the evidence.

This distinction should be visible in the research interface.

# PHASE 7 — TECHNICAL ARCHITECTURE

Choose a pragmatic architecture that works reliably.

Inspect the existing repository before deciding on the stack.

If the project is empty, prefer a maintainable architecture using technologies appropriate to a modern Python/JavaScript full-stack application.

Possible choices:

Frontend:
- React / Next.js.
- TypeScript.
- Tailwind CSS with extensive custom styling.
- A lightweight charting library.
- Custom reusable UI components.

Backend:
- Python.
- FastAPI.
- REST APIs.
- Background processing where useful.

Data:
- yfinance for EOD market data.
- Official NSE/BSE sources for announcements.
- Screener.in or company investor-relations websites for annual reports and transcripts.
- SQLite or PostgreSQL depending on project complexity.
- FAISS or another suitable vector store for document retrieval.

AI:
- An appropriate LLM provider.
- Structured extraction.
- Retrieval-augmented generation.
- Source-grounded answers.
- Efficient model routing.

These are suggestions, not rigid requirements.

Prioritise reliability and simplicity.

Do not build unnecessary microservices.

## Important engineering principles

- Keep API keys in environment variables.
- Create an .env.example.
- Implement proper error handling.
- Cache frequently requested documents and financial data.
- Avoid repeated expensive LLM calls.
- Separate data fetching, extraction, analysis, and presentation.
- Use asynchronous processing where it improves responsiveness.
- Validate extracted financial values.
- Provide loading, empty, error, and partial-data states.
- Make the application runnable through clear instructions.
- Avoid excessive dependencies.

Where a source blocks scraping or an endpoint is unreliable, do not pretend the integration works. Implement an honest fallback, source link, or documented alternative.

# PHASE 8 — DEMONSTRATION AND PRODUCT POLISH

The application should be demonstrable immediately.

Create a meaningful initial portfolio.

Include 3–5 additional companies for ad-hoc research.

Where real data is available, use it.

For unavailable historical documents or API failures, provide clearly labelled demonstration fixtures.

Never mix demonstration data with verified real data without an explicit label.

A user should be able to understand FINN within the first minute of using it.

Provide meaningful interactions rather than static screenshots.

Important interactions should actually work:

- Navigation.
- Portfolio search.
- Company selection.
- Date filtering.
- Announcement filtering.
- Alert configuration.
- Research queries.
- Company comparisons.
- Expandable evidence.
- Source links.
- Dismissal and acknowledgement of alerts.

Add subtle animations only where they improve the experience.

Avoid unnecessary animation that slows down the application.

# PHASE 9 — QUALITY ASSURANCE

Before considering the project complete:

1. Run the application.
2. Verify that the frontend loads.
3. Test the backend endpoints.
4. Test portfolio navigation.
5. Test announcement filtering.
6. Test alert configuration.
7. Test the research workflow.
8. Verify that source citations work.
9. Check mobile layouts at different screen widths.
10. Check browser console errors.
11. Check missing assets and broken links.
12. Fix all critical runtime errors.

Do not claim that an integration, feature, or deployment works unless you have actually tested it.

A smaller functioning product is better than a large collection of broken features.

# PHASE 10 — FINAL DELIVERABLES

Prepare the repository for submission.

I need the following:

### 1. Working application

A deployable mobile-first prototype.

If deployment credentials are unavailable, prepare the application and provide exact deployment instructions. Do not claim deployment has happened.

### 2. GitHub-ready repository

Ensure the repository includes:

- Clean source structure.
- README.md.
- Installation instructions.
- Environment variable documentation.
- Architecture explanation.
- Data-source documentation.
- API documentation where appropriate.
- Demo instructions.
- Known limitations.

### 3. AI build history

Help me maintain a record of the coding-agent and LLM conversations used during development.

Do not fabricate conversation exports or claim to have created external share links.

### 4. Submission covering note

Prepare a concise, natural-sounding covering note for ENAM.

It must explain:

- What I built.
- The product decisions behind it.
- The technical architecture.
- The most interesting engineering choices.
- Trade-offs and limitations.
- What I deliberately left out.
- What I would build next.

Keep it human, thoughtful, and specific. Avoid generic AI-generated language.

# FINAL INSTRUCTIONS

I care deeply about the quality of the final product.

Do not optimise for the number of features.

Optimise for the quality of the investor experience.

I want FINN to feel like a product with a clear point of view.

The interface should have its own identity. The components should be purpose-built. The research should be evidence-based. The architecture should be understandable and maintainable.

Do not blindly follow this prompt if you discover a better technical or product decision. Use engineering judgment, but ensure every mandatory challenge requirement is addressed.

Most importantly:

**DO NOT JUST CREATE A BEAUTIFUL MOCKUP. BUILD A REAL, RUNNABLE, INTERACTIVE PRODUCT.**

Start by inspecting the repository and both PDFs, create your implementation plan, and then build the application incrementally.

At the end, give me:

1. What has been implemented.
2. What has actually been tested.
3. What remains incomplete.
4. How to run the project locally.
5. How to deploy it.
6. The exact submission checklist.
```

## Selected follow-up messages (verbatim)

```text
USER: dont see the deadline just focus on the work
ASSISTANT: Understood. I’ll focus on building and testing FINN.

USER: do it quick the deadline is in 20 mins

USER: can you change the UI more engaging like the sections part is not so engaging and there is no backgriund engagement
ASSISTANT: I’ll make the sections more visually distinct and add a subtle background treatment, while keeping FINN’s financial research style. I’ll also strengthen the navigation and selected-section states.

USER (browser comment): is this required
USER (browser comment): this is looking like a pdf on a page and not website
USER (browser comment): these boxes are very generic
USER: also give me the updated submission files and telll me what i have t sublmit
ASSISTANT: The demo label is necessary because the prices and filings are synthetic, but it can be much less prominent. I’ll replace the publication-style header with a practical app toolbar, turn the repeated filing boxes into a compact signal timeline, and refresh the submission package with a clear checklist.

USER: what should be in the github
USER: can you do that for me
USER: in which account
USER: give me the link for that
USER: there are no files in that
ASSISTANT: The files are still only on your computer. I’ll check the repository you created and upload the prepared source now.

USER: also give me a mail and also host it on vercel
ASSISTANT: I’ll prepare the submission email and check Vercel access. I’ll also make FINN compatible with Vercel’s hosting model, particularly its database storage, before attempting deployment.

USER: also push this conversations history in the mail
```

## Implementation outcome (summary, not a transcript)

The assistant read the original build prompt and both reference PDFs, created
an empty-workspace Python FastAPI application with a custom JavaScript frontend,
and implemented demonstration portfolio data, configurable alert rules, a filing
digest, acknowledgements, and user-supplied evidence retrieval. Six API tests
passed. The UI was revised twice following user feedback. Source was published
to https://github.com/krith31/finn-investment-agent . Vercel compatibility was
added with an explicit warning about temporary shared storage. The user then
inserted https://finn-investment-agent-tau.vercel.app/ into the email draft.
That deployment URL was supplied by the user, not independently verified in
this record.

Limitations disclosed during development: synthetic market and filing fixtures;
no live exchange ingestion, automated financial extraction or generative AI;
no completed browser/mobile verification. Local SQLite persists data; the Vercel
demo uses temporary storage. No email was sent by the assistant.
