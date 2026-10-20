> **Evidence status (added when this report was filed, 2026-10-20):** The treg findings come from PyPI/npm registry pages that were actually fetched, and the Claude prices from a locally cached table. Everything else is unverified model knowledge. Fact-check: 4 confirmed, 3 corrected, 13 unverifiable.
> This is raw research output from an automated multi-agent run. Treat every price, date, law and vendor claim as *unverified until you check the primary source*.

# Building in-house lead generation with APIs and LLM agents (client: AI Agentic Enterprises, as of 2026-10-20)

## 0. Research method and limits (read this first)

- **Environment limits on 2026-10-20:**
  - The WebSearch budget for this workflow run was already used up ("limit: 200 WebSearch calls per turn, shared by every agent").
  - WebFetch returned `getaddrinfo ENOTFOUND` for every non-registry host: treg.to, theirstack.com, developer.adzuna.com, coresignal.com, apify.com, support.google.com, datatracker.ietf.org and developer.company-information.service.gov.uk.
  - A direct curl to a vendor pricing page (zerobounce.net) was refused by the session's egress proxy (`CONNECT tunnel failed, response 403`). As the proxy README instructs, I reported this and did not route around it.
- **What I could verify:**
  - Package registries (pypi.org, registry.npmjs.org), which turned out to be very informative about treg.
  - Anthropic's bundled API reference (claude-api skill, model and price table cached 2026-10-06).
- **Everything else** (vendor prices, legal rules, vendor status) comes from my prior knowledge (training data to about mid-2026; much of the pricing knowledge dates from 2024–2025).
  - It is marked **UNVERIFIED** and every number is "approximately".
  - URLs given as "verify at" were **not fetched** in this session. They are pointers to the canonical pages, not citations.
- **Recommended follow-up:** re-run the price and legal checks in a session with web access before any money or contract decision.

---

## 1. treg (treg.to): what can be verified

### 1.1 Verified facts (source: PyPI JSON for `tools-registry`, fetched 2026-10-20: https://pypi.org/pypi/tools-registry/json)

| Item | Finding |
|---|---|
| Identity | PyPI package **`tools-registry`** installs the `treg` CLI. Homepage **https://treg.to**. Repository github.com/superdesigndev/treg. Author **SuperDesign**: "Unclecode (unclecode@superdesign.dev)". PyPI Owner jasonzhou1993, Maintainer unclecode. |
| Positioning | "OpenRouter, but for agent tools instead of models." A remote registry that turns team skills into callable tools behind a **credential-injecting proxy**. Callers never hold the keys; the proxy injects auth server-side. |
| Maturity | 0.1.0 released **2026-07-16**; latest **0.26.0 on 2026-10-16**. About 27 releases in 3 months (no 0.13.0). Requires Python 3.12–3.13. This is a very young, fast-iterating product. Minor-version bumps may break things. |
| Billing | "priced per call, from a cent". "New verified accounts receive **$1.00 free**" (once, at team creation). Own-key calls draw on the team's **prepaid balance**. Anonymous catalog calls are free. When the balance runs out, calls get **HTTP 402** with `balance_micro`, `estimated_cost_micro` and a `topup_url`. `treg topup` supports adding funds or automatic top-ups. Endpoints with no published price are **refused**, not served free. |
| Bring your own key (BYOK) | "Your own key always wins over treg's, and those calls are never metered." Teams can also register their own API keys, OAuth connections, CLIs and `SKILL.md` skills. |
| Routing | The README names routed endpoints **`treg.web.search`, `treg.web.extract`, `treg.people.email.find`, `treg.people.phone.find`**. The header `X-Treg-Route-Verify: true` "also checks the found address or number in the same call, as its own charge". Routed calls let treg choose the provider, and treg "names it". The README also says treg "**does not silently pick or fail over**". |
| Not found in the README | `treg.companies.enrich` and `treg.people.email.verify` (the client used these) do not appear in the README text I fetched. That does not mean they don't exist. It means I could not verify them. |
| Catalog size | The README says only "thousands of endpoints across many providers". `treg upload` matches `.env` keys "against ~80 known providers". |
| Surfaces | CLI (`treg login`, `treg catalog search`, `treg call`), a Claude Code plugin, a **Claude.ai connector at `/mcp/v2/`**, and workflow skills including **`lead-signals`** ("Find in-market buyers from public signals (complaints, job changes, hiring, funding, tool adoption)"). |
| Self-hosting | `pip install "tools-registry[server]"`. The local dev script needs tmux and uv; the dashboard needs Node 22.12+. You must back up the Fernet key `TREG_SECRET_KEY` ("Lose the Fernet key and every stored secret becomes unrecoverable"). |
| Licence | Apache 2.0 **plus Additional Terms**: "you may NOT use this software, in original or modified form, to provide a hosted, managed, or embedded service". Per the README, using the hosted treg.to API inside your own product "is allowed without permission". |
| Telemetry and privacy | The CLI sends anonymous command usage to **PostHog** (no arguments or credentials), unless `TREG_TELEMETRY=0` or `DO_NOT_TRACK=1` is set. The proxy writes an audit record per call. `treg runs` and `treg calls` serve as audit logs. **The README does not say whether request or response bodies are stored, or for how long.** |

### 1.2 Corroborating third-party ecosystem (npm registry, fetched 2026-10-20)

These are third-party packages, so they show adoption and usage. They are not vendor statements.

- **`@listeningkit/treg`** (Convex component, created 2026-09-23, v0.1.4 2026-09-26): https://registry.npmjs.org/@listeningkit/treg
  - Describes treg.to as "the OpenRouter for developer tools" with **3,000+ endpoints across 60+ providers**; its 0.1.0 description said 2,600+.
  - Names SpyFu, Firecrawl, SE Ranking, SerpApi, Perplexity, GitHub, Stripe and Resend as providers.
  - Example prices: `spyfu.google.domain.competitors` ≈ $0.0002/row, `seranking...` ≈ $0.0179/call.
  - Says spend is reserved upfront and calls are refused with 402 when they exceed a set maximum.
  - Note: it labels routes "primary/failover/alternate", which sits awkwardly next to treg's own README ("does not silently pick or fail over"). Treat failover as something you implement yourself.
- **`n8n-nodes-treg`** (v0.1.0, 2026-10-01): https://registry.npmjs.org/n8n-nodes-treg
  - Operations: search catalog, get endpoint, call, get result, balance, list calls.
  - Paid calls need a cost ceiling header `X-Treg-Route-Max-Cost`.
  - Responses include `_treg.costMicro` (settled cost) and `X-Treg-Call-Id`. An Idempotency Key allows safe retries.
  - Base URL is `https://treg.to` "or a self-hosted registry".
- **`agentic-treg`** (v0.1.1, 2026-10-14): https://registry.npmjs.org/agentic-treg. A client with an MCP server (`treg_search`, `treg_get`, `treg_call`, `treg_doctor`) and a default $1 max-cost ceiling. Its author notes zero live verification.
- **`sift-gtm`** (v0.1.1, 2026-10-08): https://registry.npmjs.org/sift-gtm. Uses Apollo, treg or Monid as data providers. It quotes "a credit is $0.026 … about $0.05 for a new company and $0.026 per email" for treg/Monid. This is a third-party estimate, consistent with the client's own measured ≈$0.028 per fully enriched lead.
- **`agentic-leads`** (v0.2.1, 2026-10-14): https://registry.npmjs.org/agentic-leads. Its email preset uses `hunter.companies.emails` through treg.
- **`@lowdefy/connection-treg`** (7.0.0, 2026-10-19), "a catalogue of external API endpoints behind one token".
- **`@superdesign/treg`** (npm launcher, 2026-07-16) points to treg.superdesign.dev and the repo superdesigndev/tools-registry. This confirms the SuperDesign link.
- **Search used:** https://registry.npmjs.org/-/v1/search?text=treg&size=20

### 1.3 Not verified (treg.to itself was unreachable)

- Pricing page and markup over provider cost.
- Terms of service, DPA or sub-processor list.
- Legal entity and jurisdiction.
- Uptime/SLA and status page.
- `llms.txt` content.
- Whether `treg.companies.enrich` really routes among "~24 providers".

### 1.4 Risk assessment and mitigations

| Risk | Evidence | Mitigation |
|---|---|---|
| Young vendor or single point of failure | 3 months old; a small maintainer set; rapid releases | Put all provider calls behind your own `EnrichmentProvider` interface. Keep direct accounts with at least one email finder and one verifier. Pin CLI/SDK versions. |
| Silent behaviour changes | 27 releases since July 2026 | Contract tests on the 5–6 endpoints you depend on, run nightly. Alert on schema drift and on `_treg.costMicro` anomalies. |
| No automatic failover | treg README: "does not silently pick or fail over" | Write your own waterfall and cross-check logic. That is what the client's "verified email bounced" lesson calls for anyway. |
| Data protection (UK GDPR) | Retention of payloads not documented. treg (and each upstream provider) processes personal data when finding emails. | Get a DPA and sub-processor list from SuperDesign before sending UK/EU personal data at volume. Record treg as a processor in your RoPA (record of processing activities). |
| Licence (this matters because the client builds systems for others) | Additional Terms ban using the software to provide a hosted, managed or **embedded** service | Self-hosting for internal use looks fine. **Do not embed self-hosted treg in a client deliverable** without written permission. Calling hosted treg.to from a product is allowed per the README. |
| Cost runaway in agent loops | Per-call billing; prepaid balance | Always send `X-Treg-Route-Max-Cost`. Use idempotency keys. Keep a low auto-top-up cap. Read the 402 `estimated_cost_micro`. |
| Telemetry | PostHog CLI telemetry | Set `TREG_TELEMETRY=0` on servers. |

**Verdict on treg:** treg suits the client well as a fast multi-provider gateway, and as a demo asset, since it is MCP-native like the client's own positioning. Use it as a replaceable gateway, not as a foundation. Its BYOK mode is the built-in escape hatch: you can keep its proxy and audit log while paying providers directly.

---

## 2. The build-your-own stack, layer by layer

> Pricing column: **all UNVERIFIED and approximate**, recalled from 2024–2026 knowledge unless marked VERIFIED. Re-check on the vendor pricing page before buying.

### 2.1 Discovery and signals (the differentiator)

| Source | What it gives reqwatch | Approx. cost (UNVERIFIED) | Gotchas and legal posture |
|---|---|---|---|
| **Adzuna API** | UK and roughly 15–20 other countries' aggregated job ads, with created date, company, category and salary; search and histogram endpoints | Free developer key (app_id/app_key); paid/commercial terms on request | Free-tier rate limits are low (recalled at around tens of calls per minute and hundreds per day; verify). Attribution ("Jobs by Adzuna") is required. **Check the ToS on using it for B2B outreach.** Its "created" date is when Adzuna first saw the ad, not when it was posted, so reposts may be de-duplicated away. Verify at developer.adzuna.com. |
| **Public ATS job-board feeds** (Greenhouse job board API, Lever postings API, Ashby posting API, Workable) | For a watch-list of target companies: exact job IDs, created/updated timestamps, and repost detection (new ID, same title) | Free | These feeds exist so companies can embed their job boards. They are lower risk than LinkedIn scraping. You need each company's board token, which you can discover via careers-page links. Check each ATS's terms. Unverified this session. |
| **TheirStack** | Jobs aggregated from many boards, including LinkedIn/Indeed-derived data; tech-stack inferred from job posts; historical backfill; webhooks | Free tier plus credit-based paid plans (recalled in the tens to low hundreds of USD per month) | Probably the fastest way to get **historical** postings, so you don't wait 90 days. Repost/age fields are unverified. It resells data from scraped sources, so ask for their legal posture in writing. |
| **Coresignal** | Multi-source jobs, company and employee datasets via API or bulk | Self-service plans recalled from about $49/month; datasets are enterprise-priced | Their employee data is LinkedIn-derived, which raises GDPR questions in the UK/EU. Their jobs data is mostly company-level, which is lower risk. |
| **HarvestAPI / other Apify LinkedIn job actors** | LinkedIn job search results (title, company, posted date, applicants) | Pay per result on Apify (recalled at about $1 per 1,000 jobs; verify). Apify plans have a monthly free credit. | **LinkedIn's User Agreement prohibits scraping and automated access.** In *hiQ v. LinkedIn* the 9th Circuit limited CFAA claims over public data, but hiQ later lost on breach of contract (2022) and settled under an injunction (recalled, unverified). Using a third-party actor keeps your own account out of it, which matches the client's decision. You still face data-supply risk (actors break, vendors get sued) and you need a GDPR basis for any personal data. Job data itself is mostly non-personal. |
| **UK Companies House API** | Company profile, SIC codes, status, incorporation date, accounts category and dates, **officers**, PSCs, **filing history** (e.g. **SH01 share allotments**, a UK-specific funding signal), advanced search by SIC/date/location; streaming API; free monthly bulk CSV | **Free** with a registered key; rate limit recalled at about 600 requests per 5 minutes per key (verify) | Best free filter for the "product vs IT-services/staffing" problem. Include SIC 62012 (business and domestic software development) and 58290 (other software publishing). Down-weight 62020/62090 (IT consultancy/services) and 78xxx (employment agencies), since these are competitors per the client's Chennai finding. Officer data is personal data: use it to *identify* decision-makers, not to email home addresses. Verify at developer.company-information.service.gov.uk. |
| **Crunchbase API** | Funding rounds, investors, firmographics | Basic/limited access, then enterprise API pricing (recalled at thousands of USD per year) | Probably poor value for UK seed/Series A product companies. Companies House SH01 plus news covers much of it for free. Verify. |
| **News/funding feeds** | Funding, launches, leadership changes | GDELT (free); NewsAPI-type services; SerpApi Google News; UK-specific: Beauhurst, Dealroom (enterprise) | Use an LLM to extract the event and its date, and *always keep the source URL*. |
| **Exa** (search API, Websets, agent runs) | Semantic company discovery ("UK B2B SaaS companies hiring a platform engineer"), page contents | Per-search plus per-content pricing; Websets is plan/credit based (UNVERIFIED) | VERIFIED: the `exa-py` 2.26.0 SDK exposes `search`, `get_contents`, `answer`, `agent.runs.create`, `beta.agent.monitors.create` and `websets.list` (https://pypi.org/pypi/exa-py/json). Good for resolving company names to domains. |
| **SerpApi** | Google SERP, Google Jobs, News | Developer plan recalled at about $75/month for 5,000 searches (verify) | **Vendor-risk flag (UNVERIFIED, low–medium confidence):** I recall Google filing suit against SerpApi in December 2025. Confirm before relying on it, and keep an alternative SERP provider. treg also routes SerpApi (per the @listeningkit README). |
| **Firecrawl** | Scraping company sites and careers pages into markdown for LLM research | Credit plans (recalled: free trial credits; hobby tier about $16–19/month; standard about $83–99/month for 100k credits) | VERIFIED: `firecrawl-py` 4.53.2 exposes `scrape`, `crawl`, `map`, `search`, batch scrape and more (https://pypi.org/pypi/firecrawl-py/json). Respect robots.txt and site terms. |
| **BuiltWith** | Tech-stack detection (e.g. "uses Odoo/ERPNext/legacy stack") | Plans recalled from about $295/month; API credits separate | Expensive for this volume. Tech mentioned in job ads (via TheirStack or your own parsing) is a cheaper proxy. |

**Signal design for reqwatch:**
- Main signal: (company, normalized title, location) seen for ≥90 days, **or** ≥2 reposts (new job IDs with the same normalized title) within 120 days.
- Combine it with: the company is a product company (SIC plus LLM classification), 10–250 staff, not a staffing or IT-services firm, and preferably a recent SH01 or funding event.
- **Practical gotcha:** you need your *own* longitudinal history. Start ingesting now, or buy a backfill from TheirStack/Coresignal.

### 2.2 Enrichment and contact finding

| Provider | Role | Approx. cost (UNVERIFIED) | Notes |
|---|---|---|---|
| **People Data Labs** | Person and company enrichment and search | Free tier recalled at about 100 lookups/month; paid tiers recalled at about $0.20–0.30 per person credit at entry level | VERIFIED SDK methods (`peopledatalabs` 6.4.13): `person.enrichment`, `person.search`, `person.identify`, `company.enrichment`, `company.search`, `job_title`, `ip` and cleaners (https://pypi.org/pypi/peopledatalabs/json). Charges on match (recalled). Strong for people-by-domain search. |
| **Apollo API** | People/company search plus email reveal | Paid seats recalled at about $49–119/user/month; credits per reveal | Third-party data (sift-gtm README) says Apollo people search is free but returns no emails, and enrichment costs credits. The npm Apollo MCP server **`@thevgergroup/apollo-io-mcp` is third-party, not official** (npm search, 2026-10-20). UNVERIFIED: LinkedIn removed Apollo's company page in 2025, and Apollo had a historical data breach (2018). Check status. |
| **Hunter** | Domain search, email finder, verifier | Free tier (about 25 searches/month); paid recalled from about $49/month | Long-lived and transparent about sources. Reachable through treg too (`hunter.companies.emails`, per the agentic-leads README). |
| **Prospeo / LeadMagic / Findymail / Icypeas** | Email (and mobile) finders, mostly charging only for valid results | Entry plans recalled at roughly $20–60/month for about 1,000–2,500 credits | Good waterfall members. Coverage differs by region, so measure UK hit rate and bounce rate per provider. Icypeas is French and comparatively cheap (UNVERIFIED). |
| **Dropcontact** | EU/GDPR-focused enrichment. It positions itself as generating and verifying emails algorithmically rather than reselling a stored database. | Plans recalled from about €24/month | A useful compliance story for UK/EU prospects. Its input is name plus company/website. Verify its current claims. |
| **Kitt (trykitt.ai)** | Pattern-based email finder with verification | UNVERIFIED (not researched) | The client's own test found Kitt returned the live email where another provider's "verified" email bounced. One data point, not a benchmark. |
| **Proxycurl (Nubela)** | Was a LinkedIn profile/company enrichment API | n/a | **Status: UNVERIFIED but recalled with medium confidence.** LinkedIn sued Proxycurl in early 2025 and Proxycurl announced it was shutting down around mid-2025. VERIFIED only: the official `proxycurl-py` SDK's last release is 0.1.0.post2 (2024-09-27), and its README still describes the service as live, with no shutdown notice (https://pypi.org/pypi/proxycurl-py/json). **Do not build on it.** It is the textbook example of data-provider churn. |
| **quickenrich** (used by the client) | People search by domain | Not researched | Unverified. |

**Waterfall: Clay vs DIY**
- **Clay** runs provider waterfalls inside a spreadsheet UI, paid in Clay credits (plans recalled at about $134–349/month at entry/mid levels; Clay changed its pricing in 2025; UNVERIFIED). You get quick setup and many integrations. You give up some control and visibility into per-provider bounce data, and credit burn compounds as volume grows.
- **DIY waterfall (recommended, about 150 lines of Python):**
  1. Cache lookup (email ≤90 days old and verified ≤30 days ago).
  2. Provider A (best UK hit rate).
  3. If no result, or the result is catch-all/unknown, try provider B.
  4. Then pattern generation from known emails at the domain.
  5. Verify with verifier V1. If the domain is catch-all, require **two independent finders to agree** or a catch-all-specific check, and mark `confidence=medium`.
  6. Store `provider_of_origin`, `verifier_result`, `checked_at`.
  7. Each month, rank providers by **bounce rate on sent mail**, not by their own "verified" label. This turns the client's lesson into a control loop.

### 2.3 Email verification

| Verifier | Approx. cost (UNVERIFIED, verify) | Notes |
|---|---|---|
| ZeroBounce | About $0.008–0.01/email at low volume; small free monthly allowance | Catch-all scoring add-ons |
| NeverBounce | About $0.008/email for the first ~10k | Reported to be owned by ZoomInfo (verify) |
| MillionVerifier | About $37 per 10,000 (≈$0.004/email) | Cheapest mainstream option. Check its refund policy for unknown/catch-all results. |
| Bouncer | About $0.006–0.008/email at low volume | EU-based (Poland), positions on GDPR |
| Reoon | About $0.001–0.002/email at volume; frequent lifetime deals | Small vendor, so continuity risk |

**Catch-all handling:**
- Accept-all domains, and many Microsoft 365 tenants, cannot be confirmed by SMTP probing.
- Options:
  - Agreement between two finders, or a pattern match against a known-good email at the same domain.
  - Specialist catch-all verifiers (they exist; I can't price them this session).
  - Send catch-alls only from a separate, lower-risk mailbox pool, capped at a small share of daily volume.
- Re-verify anything older than about 30 days before sending.
- Pause a mailbox if hard bounces exceed about 2% (practitioner rule of thumb, not a published standard).

### 2.4 Sending and deliverability

**Sending platforms (UNVERIFIED prices):**
- **Instantly:** Growth recalled at about $37/month, Hypergrowth about $97/month. Unlimited mailboxes plus warm-up. API v2; check which plan includes API and webhooks.
- **Smartlead:** recalled at about $39/month (Basic) and about $94/month (Pro, API).
- Both connect Google Workspace or Microsoft 365 mailboxes.
- Mailboxes:
  - Google Workspace Business Starter is recalled at about $7–8.40 per user per month after the 2025 price change.
  - Domains cost about $10–15 per year.
  - "Bulk mailbox" resellers exist, but Google and Microsoft act against them, so treat them as higher risk.

**Infrastructure practice (practitioner consensus, not regulation):**
- Never send cold email from ai-agentic-enterprises.com. Use 2–3 secondary look-alike domains, each redirecting to the main site.
- 2–3 mailboxes per domain.
- SPF, DKIM (2048-bit) and DMARC (start `p=none` with `rua` reporting, move to `quarantine`).
- Custom tracking domain, or better, **no open tracking** (pixels hurt deliverability, and Apple Mail Privacy Protection makes opens meaningless).
- Plain text. No links or attachments in the first touch.
- **2–4 weeks of warm-up** before cold sends.
- Then about 20–40 cold emails per mailbox per day.
- Rotate or retire "burned" domains.

**Mailbox-provider rules (UNVERIFIED this session; high confidence from prior knowledge):**

| Rule | What it requires | Verify at (not fetched) |
|---|---|---|
| Google, from 1 Feb 2024 | All senders: SPF **or** DKIM, valid forward/reverse DNS, TLS, spam rate kept **below 0.3%** in Postmaster Tools (aim for below 0.1%). **Bulk senders** (about 5,000+ messages a day to personal Gmail accounts): SPF **and** DKIM **and** DMARC (at least `p=none`) with alignment, **one-click unsubscribe** for marketing/subscribed mail (enforcement of that piece from about June 2024), and unsubscribes honoured within 2 days. Recalled: stricter rejection-based enforcement from late 2025. | support.google.com/a/answer/81126 |
| Yahoo, Feb 2024 | Aligned with Google: authentication, DMARC, one-click unsubscribe, spam rate below 0.3% | senders.yahooinc.com/best-practices |
| Microsoft Outlook.com consumer (outlook/hotmail/live), announced Apr 2025, **enforced from 5 May 2025** | Senders of more than 5,000 messages a day: SPF, DKIM and DMARC (at least `p=none`, aligned). Non-compliant mail is first sent to junk, then rejected (recalled error: `550 5.7.515`). Recommends a working unsubscribe and list hygiene. | Microsoft Defender for Office 365 Tech Community blog, "Outlook's new requirements for high-volume senders" |
| RFC 8058 (Jan 2017) | One-click unsubscribe: a `List-Unsubscribe` header with an HTTPS URI **plus** `List-Unsubscribe-Post: List-Unsubscribe=One-Click`. The POST must work without cookies or extra interaction. Both headers must be covered by a valid DKIM signature. | datatracker.ietf.org/doc/html/rfc8058 |

**What this means for the client:**
- At about 1,000–2,000 sends a month, the client is far below the 5,000-per-day bulk threshold.
- Still implement authentication and an unsubscribe header plus a plain-text opt-out line. It is cheap, it lowers complaint rates, and UK PECR and US CAN-SPAM require a working opt-out anyway.

### 2.5 Legal guardrails relevant to the build (UNVERIFIED this session; confirm with ICO guidance or counsel)

- **UK (primary market):**
  - Under PECR, marketing email to **corporate subscribers** (limited companies, LLPs, public bodies) does not need prior consent. It must identify the sender and give a valid opt-out address.
  - Sole traders and some partnerships count as "individual subscribers" and need consent or the soft opt-in.
  - **UK GDPR still applies** to a named employee's work email. You need a lawful basis (legitimate interests with a documented LIA), an Article 14 privacy notice at the latest at first contact, and an absolute right to object to direct marketing, so keep a suppression list.
  - The **Data (Use and Access) Act 2025** (Royal Assent June 2025, recalled) raises PECR fines to UK GDPR levels and commences in stages. Verify the commencement dates.
- **EU:** rules differ by country. Germany (UWG §7) is strict even for B2B email; France (CNIL) allows B2B email related to the recipient's job. Use per-country gating.
- **US:** CAN-SPAM requires accurate headers and subject lines, a physical postal address, and opt-outs honoured within 10 business days. Per-email penalties are inflation-adjusted (tens of thousands of dollars).
- **Scraping:** EU/UK data protection authorities issued joint statements on data scraping (2023, with a 2024 follow-up; recalled). Personal data obtained by scraping is still personal data.
  - Design point in reqwatch's favour: its **core signal (job postings, SIC codes, filings) is mostly company-level, non-personal data**. Personal data only enters at the contact stage, which keeps the GDPR footprint small.

### 2.6 Orchestration and agents

| Option | Fit | Approx. cost |
|---|---|---|
| **n8n** (self-hosted community edition, Sustainable Use Licence; or cloud) | Good for cron ingest, webhooks (Instantly reply webhooks) and glue. A **treg community node exists** (`n8n-nodes-treg`, VERIFIED). | Self-host on about a $5–20/month VPS. Cloud plans recalled at about €20–60/month (UNVERIFIED). |
| **Make** | Fine for no-code flows; weaker for stateful data and versioning | Recalled at about $9–11/month entry (UNVERIFIED) |
| **Clay as orchestrator** | Fastest no-code waterfall plus LLM ("Claygent"), with HTTP columns for custom APIs | Credits (see above). It doesn't fit longitudinal state such as "seen for 90 days" well, so keep that in your own database. |
| **Python + Postgres + Claude** (recommended core) | Signal state, entity resolution, waterfall, cost ceilings, tests | Infrastructure cost is trivial. Engineering time is the cost. |
| **Claude Agent SDK** | Batteries-included agent harness with built-in WebSearch/WebFetch/Bash and MCP. Good for the *research agent* step and for a human-in-the-loop "analyst" agent. | VERIFIED: `claude-agent-sdk` 0.2.168 exposes `query()`, `ClaudeSDKClient`, `ClaudeAgentOptions`, the `@tool` decorator and `create_sdk_mcp_server()` (https://pypi.org/pypi/claude-agent-sdk/json). For deterministic steps, prefer plain Messages API calls (single call or Tool Runner). |
| **MCP** | Expose your pipeline (reqwatch, CRM, treg) as MCP tools so the founder can query "show this week's stale-role accounts" from Claude. Doubles as a client-facing demo. | VERIFIED: TypeScript `@modelcontextprotocol/sdk` 1.32.1 (2026-10-05) is on npm. treg offers a Claude.ai connector at `/mcp/v2/`. |
| **LangGraph** | Durable, stateful agent graphs if you outgrow simple workers | VERIFIED: `langgraph` 1.2.16, MIT, classified "Production/Stable" (https://pypi.org/pypi/langgraph/json) |

**LLM prices (VERIFIED: Anthropic claude-api skill table, cached 2026-10-06; per million tokens, input/output):**
- Claude **Haiku 5.5** $0.10 / $0.50 (prompts ≤100K tokens).
- Claude **Sonnet 5.5** $2 / $10.
- Claude **Opus 5.5** $4 / $20.
- The Message Batches API runs asynchronously at **50% cost**. Prompt-cache reads cost about 0.1× the input price.
- Thinking tokens bill as output, so set `output_config.effort` to `low` for classification.
- Maintenance note (VERIFIED from the same reference): 2025–2026 model generations introduced breaking API changes. Examples: `budget_tokens` is rejected with a 400 on newer models, forced `tool_choice` returns a 400 on Opus 5.5 and Sonnet 5.5, and assistant prefill was removed. Budget for model-migration upkeep.
- OpenAI prices: not verified this session.

**Where LLMs add real value:**
1. **ICP classification** of messy company descriptions and job ads: product company vs agency/IT-services/staffing. This is exactly the client's 61% vs 12% problem.
2. **Job-description analysis** into a pain hypothesis ("they have tried to hire a platform/AI engineer for 4 months; the stack implies X").
3. **Account research briefs**, grounded in fetched pages, with citations kept.
4. **First-line personalisation and offer framing**, with a human approving.
5. **Reply classification** (interested, not now, referral, unsubscribe, out of office, bounce) and routing.
6. **Fuzzy entity resolution suggestions** (company name to domain to Companies House number), checked deterministically.

**Where LLMs don't add value (use deterministic code or APIs):**
- Email finding and verification.
- De-duplication and suppression.
- Date arithmetic for "open 90+ days".
- Send scheduling and throttling.
- Compliance gating.
- Any "fact" without a source. Agents tend to hallucinate funding rounds or names, so require citations.
- **Do not let an agent send autonomously** in the first months.

### 2.7 CRM and feedback loop

- **System of record:** Postgres for raw signals and postings (append-only, with `first_seen`/`last_seen`). The CRM holds only accounts and people that pass the filters.
- **CRM choice:** the client already runs Frappe/ERPNext and Odoo, and this repo is a Frappe app scaffold. Use **Frappe CRM or ERPNext Lead/Opportunity** with custom fields:
  - `signal_type`, `signal_evidence_url`, `signal_first_seen`, `ch_company_number`, `sic_codes`
  - `provider_of_origin`, `email_confidence`
  - `sequence_id`, `lawful_basis=LI`, `notice_sent_at`
- Building it on their own platform is also a portfolio piece. Alternatives: HubSpot free CRM, Attio, Pipedrive.
- **Dedupe keys:**
  - Account: registrable domain plus Companies House number.
  - Person: lowercase email plus hashed LinkedIn URL if you hold one.
- **Suppression:** a global do-not-contact list (opt-outs never expire), clients and partners, competitors, and "contacted in the last 180 days" (a policy choice). Check it at enqueue time *and* at send time.
- **Attribution:** signal → account → contact → send → reply → positive reply → meeting → proposal → won. Report conversion **by signal type** (stale 90+ days vs repost vs funding plus hiring) and **by provider of origin** (bounce rate). Review weekly and recalibrate thresholds.

---

## 3. (a) Reference architecture: signal-first "reqwatch"

**Prose:**
- A nightly worker ingests job postings from Adzuna (UK), a watch-list of public ATS boards, and optionally a paid aggregator for historical backfill.
- Postings are normalized and stored with first-seen and last-seen dates. A detector flags roles open ≥90 days or reposted ≥2 times.
- Each flagged company is resolved to a domain and a Companies House number. It is filtered by SIC code, size, status and accounts category, then classified by a cheap LLM as product company vs services/staffing.
- The survivors get a grounded research brief (site and careers pages via Firecrawl or `treg.web.extract`, job descriptions, Companies House filings such as SH01) from a mid-tier LLM. A human approves the top N each week.
- Only approved accounts enter the contact stage:
  - people search by domain for CTO, VP Engineering or founder
  - an email waterfall with cross-checks
  - verification, with special handling for catch-all domains
  - a suppression check
- Approved contacts go to the CRM. A personalized 3-step sequence is pushed to Instantly or Smartlead on warmed secondary domains.
- Replies come back by webhook, are LLM-classified, update the CRM and suppression list, and alert the founder.
- Weekly metrics feed back into signal thresholds and provider ordering.

```
                ┌──────────────────────── DISCOVERY (company-level, low GDPR footprint) ─────────────────────────┐
 Adzuna API ───┐│                                                                                               │
 ATS feeds  ───┼┼─> ingest (n8n cron / Python) ─> postings table (first_seen,last_seen,job_id,norm_title,hash)  │
 TheirStack ───┘│        (optional backfill)          │                                                         │
                │                                      v                                                        │
                │                    stale/repost detector (>=90d open OR >=2 reposts in 120d)                 │
                └──────────────────────────────────────┬────────────────────────────────────────────────────────┘
                                                       v
   entity resolution: name -> domain (Exa / treg.web.search) -> Companies House no. (free API: SIC, officers, SH01)
                                                       v
   ICP gate: rules (SIC 62012/58290 in; 62020/62090/78xxx out; size; active) + Haiku 5.5 classifier (product vs services)
                                                       v
   research agent (Sonnet 5.5, Batch API): site/careers via Firecrawl or treg.web.extract -> brief + pain hypothesis + citations
                                                       v
   ===== HUMAN REVIEW QUEUE (founder approves top N/week) =====
                                                       v
   contacts: people-by-domain (treg / PDL / Apollo) -> email waterfall [cache -> A -> B -> pattern] -> verify V1
             (catch-all? -> 2nd finder agreement / catch-all check -> confidence=medium, separate mailbox pool)
                                                       v
   suppression + compliance gate (DNC, clients, competitors, 180-day rule, country rules, LIA flag)
                                                       v
   CRM (Frappe CRM / ERPNext Lead+Opportunity, provenance fields)  ──>  sender (Instantly/Smartlead API)
                                                                          2-3 secondary domains, 4-6 mailboxes,
                                                                          <=20-40/day each, SPF/DKIM/DMARC, unsubscribe
                                                       v
   reply webhook -> Haiku 5.5 reply classifier -> CRM stage + suppression -> founder alert for "interested"
                                                       v
   weekly metrics by signal type & provider -> retune thresholds, reorder waterfall   (expose all of it as MCP tools)
```

**Controls built in:**
- Per-call cost ceilings (`X-Treg-Route-Max-Cost`) and a daily spend cap.
- Idempotency keys.
- Contract tests on provider responses.
- Provenance on every field.
- A human approves before first send.

---

## 4. (b) Cost model (all numbers approximate; provider prices UNVERIFIED except the Anthropic rates)

**Assumptions:**
- Each month: about 20,000 UK postings scanned, giving about 1,000 candidate companies after detection, about 200 approved accounts, and about 400 contacts (2 per account).
- 3-step sequences, so about 1,200 sends a month.
- 4 mailboxes on 2 domains at about 15–20 sends per day each (well under capacity).

**Per account (2 contacts):**

| Step | Low | High | Basis |
|---|---|---|---|
| Job data (Adzuna/ATS) | $0 | $0 | Free tiers (a paid aggregator is counted as a monthly fixed cost) |
| Companies House | $0 | $0 | Free API |
| Domain resolution / company enrichment | $0.01 | $0.05 | treg-style per-call prices; sift-gtm says about $0.05 per new company (third-party) |
| ICP classification (Haiku 5.5, about 2.5K in / 200 out, plus effort-low thinking), spread over about 5 candidates per approved account | $0.002 | $0.005 | VERIFIED rates: about $0.0004–0.001 per candidate |
| Research brief (Sonnet 5.5, about 20K in / 4K out incl. thinking; Batch -50% for the low end) | $0.04 | $0.08 | VERIFIED rates. Opus 5.5 would be about $0.16. |
| Page fetches (about 5 pages) | $0.005 | $0.02 | Firecrawl/treg extract credits (UNVERIFIED) |
| People search by domain | $0.01 | $0.03 | UNVERIFIED |
| Email find ×2 (waterfall average incl. second-provider cross-checks) | $0.02 | $0.10 | Client measured ≈$0.028 per fully enriched lead via treg; cross-checks add more |
| Verification ×2 (plus re-verify) | $0.008 | $0.03 | About $0.004–0.01 per email |
| Copy drafting ×2 (Sonnet 5.5) | $0.01 | $0.03 | VERIFIED rates |
| **Total per approved account** | **≈ $0.11** | **≈ $0.35** | About **$0.05–0.18 per contact** |

**Per month:**

| Item | Low | High | Notes |
|---|---|---|---|
| Variable (200 accounts) | $22 | $70 | From the table above |
| Sending platform | $37 | $97 | Instantly/Smartlead tier with API (UNVERIFIED) |
| Mailboxes (4) | $28 | $34 | About $7–8.40 per Google Workspace seat (UNVERIFIED) |
| Domains (2–3) | $2 | $4 | Annual cost spread over 12 months |
| Orchestration + DB (VPS / n8n self-host) | $10 | $40 | |
| Optional paid job data or backfill (TheirStack/Coresignal) | $0 | $200 | Placeholder; verify plans |
| treg minimum balance buffer | $0 | $20 | Prepaid |
| **Cash total** | **≈ $100** | **≈ $465** | |
| Ops labour (maintenance + deliverability + data QA) | 2 h/wk | 6 h/wk | Not included in cash |

**Funnel sensitivity (illustrative assumptions, not benchmarks):**
- At 400 contacts a month, a reply rate of 2–8%, 30–50% of replies positive, and 50–60% of positive replies converting to meetings gives about **1–10 meetings a month**.
- Cash cost per meeting would then be about $10–450. Including labour it is roughly $150–1,500.
- The spread is huge, so instrument the funnel by signal type from day one.
- One closed 8-week build engagement probably pays for a year of the pipeline. Check this against the client's actual deal size, which I don't know.

---

## 5. (c) Build vs buy vs hybrid: 12-month TCO (approximate; labour at about $95/h ≈ £75/h, an assumption)

| | **Buy** (Clay + Instantly + Apollo + HubSpot free) | **Build** (all DIY: own ingest, waterfall, direct provider contracts, own UI) | **Hybrid (recommended)**: build reqwatch signal plus LLM layers; buy enrichment via treg/2–3 providers behind an abstraction, a sending SaaS, and Frappe CRM |
|---|---|---|---|
| Cash / month | ≈ $220–530 (Clay about $134–349 UNVERIFIED, plus sending, mailboxes, Apollo seat) | ≈ $100–300 | ≈ $120–350 |
| Initial setup | 20–30 h | 100–160 h | 50–80 h |
| Ongoing ops | 2–3 h/wk | 4–6 h/wk | 2–4 h/wk |
| 12-month TCO | **≈ $14–23k** | **≈ $30–47k** | **≈ $16–30k** |
| Time to first send | About 3–4 weeks (warm-up is the bottleneck) | About 6–8 weeks | About 4–5 weeks |
| Differentiation | Low–medium. Competitors can buy the same signals; longitudinal "stale role" state is awkward in Clay. | High | High where it matters (discovery); commodity elsewhere |
| Data-provider churn exposure | Absorbed by Clay, but prices and credit rules change under you | Fully yours (e.g. a Proxycurl-type shutdown, recalled) | Contained by the abstraction layer plus treg BYOK |
| Strategic value to this firm | Low | High (case study) but costly | **High**: a live agentic + MCP system they can demo to prospects |

**Hidden costs most often missed (all three options):**
1. **Deliverability operations:** warm-up lead time; DNS and DMARC report review; blocklist and spam-rate monitoring; replacing burned domains and mailboxes. Allow about 1–2 h a week plus about $50–100 every time a domain set is replaced.
2. **Data-provider churn:** shutdowns (Proxycurl, recalled), lawsuits (Google vs SerpApi, recalled, low confidence), pricing-model changes (Clay, Hunter, recalled), API version changes, and broken scraping actors. Each costs about 2–8 h of rework.
3. **Data-quality drift:** a provider's "verified" label degrades. Budget a monthly per-provider bounce review.
4. **LLM/model upkeep:** model migrations with breaking parameter changes (VERIFIED in Anthropic's own reference), prompt regressions, and keeping a small eval set (about 50 labelled companies) to re-test the ICP classifier.
5. **Compliance administration:** the legitimate-interests assessment (LIA), privacy notice, data-subject requests (DSARs), suppression, processor DPAs (treg and each provider), and per-country rules if expanding to the EU.
6. **The humans:** reply handling and meetings, which no pipeline removes.

---

## 6. (d) Recommendation

**Go hybrid, signal-first, UK-first.**

1. **Week 0 (start the clocks):**
   - Buy 2 secondary domains and set up 4 mailboxes with SPF/DKIM/DMARC.
   - Start warm-up.
   - Start nightly ingestion of Adzuna UK postings plus ATS boards for a seed list. History is the asset.
   - Write the LIA and privacy notice.
   - Set `TREG_TELEMETRY=0`. Ask SuperDesign for a DPA, sub-processor list and pricing schedule.
2. **Weeks 1–4 (MVP):**
   - Postgres schema and the stale/repost detector.
   - Companies House enrichment and SIC filter.
   - Haiku ICP classifier with a 50-company labelled eval set.
   - Sonnet research brief, then a human approval queue in Frappe CRM.
   - Enrichment through treg with cost ceilings, plus one direct finder and one direct verifier as fallback.
   - First 50 hand-approved accounts. Send manually reviewed copy at ≤20 sends per mailbox per day.
3. **Weeks 5–8:**
   - Reply webhook and classifier.
   - Funnel dashboard by signal type and provider.
   - Decide whether paid backfill (TheirStack/Coresignal) is worth it, based on how much signal Adzuna/ATS coverage produces.
4. **Weeks 9–12:**
   - Expose reqwatch as an MCP server: internal use plus a client demo ("we built our own pipeline this way").
   - Consider US/EU only after the UK funnel converts, with per-country legal gating.

**Explicit don'ts:**
- No LinkedIn scraping from your own account (consistent with the client's decision).
- No sending from the primary domain.
- No bought static lists.
- No autonomous agent sending.
- Don't treat any single provider's "verified" label as truth.
- Don't embed self-hosted treg in client deliverables (licence terms).

**Implications for the lead-gen hire (as seen from the build track):**
- **Must-have skills:**
  - Hands-on API/JSON/SQL and at least one of n8n or Python.
  - Waterfall and verification design with per-provider measurement.
  - Deliverability operations (DNS auth, warm-up, monitoring, 2024–2025 mailbox-provider rules).
  - UK PECR/UK GDPR literacy (corporate vs individual subscribers, LIA, suppression).
  - Signal and experiment design.
  - Concise B2B copy.
  - LLM prompt and eval hygiene.
  - Honest metric reporting.
- **Practical exercise (paid, about 4–6 h):**
  - Give the candidate a CSV of about 200 UK postings with first-seen dates and a $10 enrichment budget (a treg team token with a cost ceiling).
  - Ask them to:
    1. Flag stale or reposted roles and exclude staffing/IT-services firms (SIC plus reasoning).
    2. Resolve 15 companies to Companies House numbers.
    3. Produce 10 decision-maker contacts with email, provider of origin, verifier result and a catch-all flag.
    4. Report cost per verified contact.
    5. Write a 3-step sequence for 3 accounts using the signal.
    6. Write a one-page deliverability and compliance plan.
  - **Score on:** precision (spot-check), honesty about catch-alls and unknowns, cost discipline, reproducibility (script or workflow export), compliance correctness, and copy.
  - **Red flags:** proposes LinkedIn account automation, "guaranteed inbox", sending from the main domain, or skipping verification.

---

## 7. Sources actually fetched in this session (all 2026-10-20)

- https://pypi.org/pypi/tools-registry/json: treg (SuperDesign); main source for section 1.
- https://registry.npmjs.org/-/v1/search?text=treg&size=20: treg ecosystem packages.
- https://registry.npmjs.org/@listeningkit/treg: 3,000+ endpoints / 60+ providers claim; example prices.
- https://registry.npmjs.org/n8n-nodes-treg: cost ceiling header, idempotency, self-hosted base URL.
- https://registry.npmjs.org/agentic-treg: MCP tools; $1 default ceiling.
- https://registry.npmjs.org/sift-gtm: third-party treg/Monid per-credit price ($0.026).
- https://registry.npmjs.org/agentic-leads: `hunter.companies.emails` via treg.
- https://registry.npmjs.org/@superdesign/treg: SuperDesign launcher (treg.superdesign.dev).
- https://registry.npmjs.org/@lowdefy/connection-treg and https://registry.npmjs.org/@assemblyline-agents/treg: further integrations.
- https://pypi.org/pypi/proxycurl-py/json: last SDK release 2024-09-27.
- https://pypi.org/pypi/exa-py/json, https://pypi.org/pypi/firecrawl-py/json, https://pypi.org/pypi/peopledatalabs/json: SDK method names.
- https://pypi.org/pypi/claude-agent-sdk/json, https://pypi.org/pypi/langgraph/json: orchestration SDKs.
- https://registry.npmjs.org/-/v1/search?text=enrichment%20mcp&size=25: the Apollo MCP server is third-party; MCP SDK versions.
- Anthropic claude-api skill (bundled locally; model and price table cached 2026-10-06): Claude prices, Batch 50%, API drift.
- Attempted but blocked (DNS failure or proxy 403): treg.to, treg.to/llms.txt, theirstack.com, developer.adzuna.com, coresignal.com, apify.com, support.google.com, datatracker.ietf.org, developer.company-information.service.gov.uk, zerobounce.net.

---

## Fact-checker's notes on this report

- Web search and fetch were unavailable in this pass, so I could only re-check the PyPI JSON for tools-registry and proxycurl-py, using curl. Every other claim is still unverified.
- The release count is wrong: there are 32 release keys, not about 27.
- The licence summary leaves out the 'to third parties' qualifier and the explicit permission to run a registry internally. It also leaves out the contact (jason@superdesign.dev) for asking permission to embed treg in a client deliverable.
- The quote that bring-your-own-key calls are 'never metered' could not be matched in the README text. It may be paraphrased or out of date.
- All legal and deliverability rules (Google, Yahoo, Microsoft, RFC 8058, PECR, DUAA) and all vendor prices are still unverified. Check them before making any decision.

### Open questions raised by the researcher

- All vendor prices outside Anthropic and the treg per-call data points (TheirStack, Coresignal, Apify/HarvestAPI, Exa, SerpApi, Firecrawl, BuiltWith, Crunchbase, PDL, Apollo, Hunter, Prospeo, LeadMagic, Findymail, Icypeas, Dropcontact, Kitt, Clay, ZeroBounce, NeverBounce, MillionVerifier, Bouncer, Reoon, Instantly, Smartlead, n8n, Make, Google Workspace) need re-checking in a session with web access. Egress was blocked here.
- treg.to: pricing schedule and markup over provider cost, ToS, DPA and sub-processors, legal entity and jurisdiction, SLA/status page, payload retention, and whether treg.companies.enrich / treg.people.email.verify exist and which providers they route to (the client reported ~24 for company enrichment; unverified).
- Contradiction to resolve with SuperDesign: treg's own README says it 'does not silently pick or fail over', while a third-party README labels routes primary/failover/alternate.
- Does treg's licence ban (hosted/managed/embedded service) affect the client's plan to build systems for its own clients? Get written clarification.
- Proxycurl shutdown and the LinkedIn lawsuit (2025), the Google v. SerpApi suit (Dec 2025), and LinkedIn's 2025 action against Apollo/Seamless are recalled, not verified.
- Adzuna API terms: is use for B2B outbound/lead generation allowed, what are the current free-tier rate limits, and does its 'created' date or de-duplication hide reposts?
- Does TheirStack (or Coresignal) expose repost/first-posted fields and historical backfill for UK small companies, at what cost per 1,000 jobs?
- Exact Companies House API rate limit and the current status of officer-data changes under the Economic Crime and Corporate Transparency Act reforms.
- Current enforcement state of Google/Yahoo/Microsoft sender rules in late 2026 (rejection-based enforcement), and whether Instantly/Smartlead add RFC 8058 headers automatically.
- UK Data (Use and Access) Act 2025: which PECR/direct-marketing provisions have commenced as of Oct 2026.
- Client-specific inputs the cost model needs: average engagement value, target meetings per month, the founder's real hourly opportunity cost, and whether the new hire will own pipeline operations (this shifts the TCO between options).
- Real UK reply/meeting rates for signal-based outreach to small product companies. No benchmark was verified; the client must measure its own, by signal type.
