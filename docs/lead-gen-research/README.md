# Lead generation: tools, build-vs-buy, and how to hire and test a lead-gen expert

Prepared 2026-10-20 for AI Agentic Enterprises. Read section 1 first, then section 2.

**Not legal, financial or HR advice.** Several conclusions below rest on facts that
could not be verified in this research run (see section 2). Check the primary source
before you spend money, sign a contract or make a job offer.

---

## 1. Short answers

**What is the best way to do lead generation now?**
For a small, founder-led, high-ticket consultancy, the research points to *precision
over volume*: a small number of well-chosen accounts, picked by a timing signal, with
verified contacts, sent from properly authenticated secondary domains, and measured in
*qualified meetings*, not "leads". Mass cold email and fully autonomous "AI SDR" tools
are a poor fit for you (reasons in section 4). Your own `reqwatch` idea (roles open 90+
days or reposted at small product companies) is the kind of signal this approach needs.
Evidence strength: the direction is consistent across sources, but the reply-rate and
conversion numbers come from vendors and are weak. Measure your own.

**Buy, build, or both?**
Hybrid. Build the part that is yours (the signal: reqwatch). Buy the commodity parts
(enrichment, email verification, sending). Your treg-based chain at about $0.028 per
fully enriched lead is already cheap; cost is not your bottleneck. What you have not yet
proven is the offer, the message, deliverability, and a measured funnel to meetings.
That is what the hire is for.

**Who should you hire?**
Not a "lead generation executive" (list builder) and not a junior SDR as the first hire.
Hire a **signal-led outbound operator**: a "GTM engineer" who is *also responsible for
meetings*, ideally on a paid 90-day contract that can convert to a permanent role. The
founder keeps positioning, discovery calls, pricing and closing.

**How do you tell whether a candidate really has the skills?**
Use a paid, time-boxed (4-hour) work sample built on *your own data with planted traps*,
followed by a live debrief where they must defend and modify their own work. Add live
evidence checks for claimed past results. Full design is in section 6 and Appendix A6.

---

## 2. How much to trust this report

The research ran as 6 parallel tracks, each followed by an adversarial fact-check. **The
fact-check stage largely failed to verify anything** because the run's shared web-search
budget (200 searches) was exhausted before it began, and page fetches were blocked for
most sites. Treat this table as the real confidence level:

| Track (appendix) | What it was built from | Fact-check result |
|---|---|---|
| A1 AI SDR agents | Web-search result summaries (pages not fetched). Many sources are competitor blogs | 0 of 20 key claims confirmed |
| A2 Data / signal / outreach platforms | Web-search result summaries, with URLs. Many sources are competitor blogs or aggregators | 0 of 22 confirmed; 1 corrected |
| A3 In-house build | treg facts from PyPI/npm pages that *were* fetched; Claude prices from a cached table; everything else is model knowledge | 4 confirmed, 3 corrected, 13 unverifiable |
| A4 State of practice 2026 | **No live sources** - model knowledge only | 2 confirmed, 17 unverifiable |
| A5 Compliance / legal | **No live sources** - model knowledge only | 0 of 20 verified |
| A6 Hiring and assessment | **No live sources** for facts and salaries; assessment design is recommended practice | 0 of 20 verified |

What this means in practice:

- **Every price is approximate and unverified.** Vendors reprice often (Clay reportedly
  restructured its plans in 2026; sources conflict on Unify, Common Room, Lusha and others).
- **Every legal statement is unverified.** Details most likely to be out of date: the
  commencement dates of the UK Data (Use and Access) Act 2025, the EU AI Act timetable,
  India's DPDP phasing, and the current CAN-SPAM penalty figure.
- **Salary and day-rate figures are low-confidence recollections.** Check them against
  live job ads before making an offer.
- **Reply-rate benchmarks come from sending-tool vendors** and should be treated as
  marketing, not evidence.
- **Your own memory notes and Drive files were used as context** (reqwatch, treg, the
  Chennai-vs-London finding). Those are your measurements, not independently verified.

Recommended next step: re-run the compliance, state-of-practice and hiring tracks, and the
price checks, in a session with a fresh search budget. Section 8 lists what to check first.

---

## 3. Commercial off-the-shelf options

Full detail: Appendix A1 (AI SDR agents) and A2 (platforms). All prices approximate,
unverified, and as read from search summaries on 2026-10-20.

### 3.1 Five kinds of product

| Kind | Examples named in the research | How sold | Rough price band (approx., unverified) |
|---|---|---|---|
| Autonomous "digital worker" AI SDRs | 11x (Alice/Julian), Artisan (Ava), Alta, Landbase, Topo, Monaco | Sales calls, annual contracts | about $2k to $15k+ per month |
| Self-serve AI SDRs | AiSDR, Reply.io (Jason), Salesforge (Agent Frank), Persana, Valley | Card on file | about $50 to $2.5k per month |
| Agents inside data / engagement platforms | Apollo, Amplemarket (Duo), Unify, Regie.ai, Outreach, Salesloft | Per seat plus credits | about $20 to $160 per seat per month plus platform fees |
| Agents inside CRMs | HubSpot Prospecting Agent, Salesforce Agentforce (Hunter, Piper) | Usage credits on top of CRM seats | HubSpot reported at about $1 per lead |
| Builders / orchestrators | Clay (Claygent), Relevance AI, Lindy | Credits | about $30 to $500 per month self-serve |

### 3.2 What the research concluded about AI SDRs

- **Independent evidence that they work is thin.** Most "reviews" are written by competing
  vendors.
- **Documented controversy (secondary reporting, not re-checked):** a March 2025
  TechCrunch report on 11x (non-customer logos displayed; ARR counted on contracts with
  short exit clauses; an employee alleging high churn; 11x disputed the churn figure). The
  11x CEO stepped down in May 2025. Artisan was reportedly banned from LinkedIn briefly in
  December 2025.
- **Poor fit for you** because: each account is worth tens of thousands of pounds, so a
  generic or invented-detail email is an expensive mistake; consulting is bought on
  credibility and the email goes out under the founder's name; and none of the products
  checked has a native "role open 90+ days / reposted" trigger, so your signal must be fed
  in anyway.
- **Where they do work:** large markets and lower-value deals, inbound speed-to-lead, and
  research-and-draft with a human approving each message.

### 3.3 Shortlist to trial (if you want a COTS comparison)

All of these are month-to-month or cheap to start. Confirm prices first.

| Option | Role in your setup | Approx. price (unverified) |
|---|---|---|
| Clay | Research / drafting layer fed by reqwatch signals, human approves | Launch about $185/mo; Growth about $495/mo (plans reported restructured March 2026; sources conflict) |
| Unify | Packaged job-posting-signal workflow | Pricing conflicts across sources; get a quote |
| AiSDR (Solo) or Reply.io Jason | Autonomous *control group* on a separate sending domain | about $250/mo; about $500/mo |
| HubSpot Prospecting Agent | Only if you adopt HubSpot as CRM | about $1 per lead; has a review-before-send mode |

**Avoid at your size:** 11x and Artisan (cost, annual contracts, history); Valley (it
automates the user's own LinkedIn account, which you have ruled out); the Salesforce
agents (need Salesforce, mostly enterprise/inbound).

### 3.4 Platforms by layer (A2)

- **Data / enrichment:** Apollo, ZoomInfo, Cognism, Lusha, Seamless.AI, UpLead, People Data
  Labs, Crustdata, Coresignal, LinkedIn Sales Navigator. Clearbit is now HubSpot Breeze
  Intelligence. Enterprise tools (ZoomInfo, Cognism) are quote-only and, by third-party
  estimates, cost roughly $15k+ per year, which is out of proportion for one or two users.
- **Intent / signals:** Bombora, 6sense, Demandbase, G2, UserGems, Common Room, Trigify.
  Most measure software-category research, which is the wrong question for a services
  firm. Job-posting data (TheirStack, Coresignal, PredictLeads) fits reqwatch much better.
  Koala was reported discontinued in 2025; Common Room was reported (July 2026) to be
  acquired by Zoom, closing unconfirmed.
- **Sending:** Instantly, Smartlead, lemlist, Saleshandy, Woodpecker. LinkedIn automation
  (HeyReach, Expandi, La Growth Machine) carries account-restriction risk; the research
  reports LinkedIn removing HeyReach's company page in March 2026 (single, vendor-sourced
  report).

**Lean stack suggested by the research (approx. $300-$400/month, rising to $650-$800 with
optional extras; excludes VAT and mixes annual and monthly prices):** a job-signal API
(TheirStack and/or Coresignal) plus the free Companies House API; treg for enrichment; one
second-opinion email finder and one verifier; Sales Navigator used *manually*; Instantly or
similar on 2-3 secondary domains; Frappe CRM.

---

## 4. Building in-house

Full detail: Appendix A3.

### 4.1 What was verified about treg

From the PyPI and npm registry pages (fetched 2026-10-20):

- treg is **SuperDesign's "tools-registry"** (PyPI `tools-registry`, homepage treg.to). It is
  about three months old: first release 2026-07-16, version 0.26.0 on 2026-10-16. Expect
  rapid change.
- Billing is per call from a prepaid balance; new accounts get $1.00 free; running out gives
  an HTTP 402. Its README says it **"does not silently pick or fail over"**, so cross-checking
  providers and failover are *your* job. (This matches your own lesson about the bounced
  "verified" email.)
- **Licence:** Apache 2.0 plus Additional Terms that forbid using the software to provide a
  hosted, managed or embedded service *to third parties*. Running your own registry for your
  own team is expressly permitted. **Embedding treg in a client deliverable needs written
  permission** (contact given in the package metadata). This matters because you build
  systems for clients.
- Not verified: pricing schedule and markup, terms/DPA/sub-processors, payload retention,
  legal entity, uptime/SLA. Your own Drive notes show `treg.companies.enrich`,
  `treg.people.email.find` and `treg.people.email.verify` working, but the README the
  researcher fetched does not list the first and last, so confirm them with the vendor.
- Treat treg as a **replaceable gateway, not a foundation**: put calls behind your own
  interface, keep a direct account with at least one finder and one verifier, pin versions,
  send a max-cost header, and get a DPA before sending UK/EU personal data at volume.

### 4.2 Reference architecture (signal first)

```
job postings (Adzuna / public ATS feeds / optional paid aggregator)
   -> store with first_seen / last_seen  -> detector: open >=90 days OR >=2 reposts
   -> resolve to domain + Companies House number (free API; SIC codes, filings)
   -> ICP gate: rules + cheap LLM (product company vs IT-services/staffing)
   -> research brief (LLM, grounded in fetched pages, with citations)
   ===== founder approves top N per week =====
   -> contacts: people-by-domain -> email waterfall (A -> B -> pattern) -> independent verify
      (catch-all domains: need two finders to agree, lower confidence, separate mailbox pool)
   -> suppression + compliance gate
   -> CRM (Frappe CRM / ERPNext) -> sender on warmed secondary domains
   -> reply webhook -> LLM reply classifier -> CRM + suppression -> founder alert
   -> weekly metrics by signal type and provider -> retune
```

Design points the research stressed:

- **History is the asset.** The "open 90+ days" signal needs your own longitudinal data, so
  start ingesting now (or buy a backfill). Greenhouse's list endpoint returns only
  `updated_at`; the single-job endpoint returns `first_published`; Lever's documented
  fields include no creation timestamp. So store your own `first_seen`.
- **LLMs help with** classification of messy company descriptions, job-ad analysis, grounded
  research briefs, first-line drafting (human approved), and reply classification. **They do
  not belong in** email finding/verification, dedupe, date arithmetic, send throttling or
  compliance gating. Do not let an agent send autonomously in the first months.
- **Never trust one provider's "verified" label.** Rank providers by bounce rate on mail you
  actually sent.

### 4.3 Cost (illustrative; assumptions in A3; vendor prices unverified)

At roughly 200 approved accounts and 400 contacts a month: about $100-$465 per month cash
(sending tool, mailboxes, domains, hosting, enrichment, LLM calls) plus roughly 2-6 hours a
week of upkeep. LLM spend is negligible in this design (fractions of a cent to a few cents
per account at the cached Claude prices in the research). Twelve-month total cost including
labour at an assumed $95/hour: buy about $14-23k, hybrid about $16-30k, full build about
$30-47k. These are the researcher's estimates, not benchmarks. The dominant hidden costs are
deliverability operations, data-provider churn, and compliance administration.

### 4.4 Recommended sequence

1. **Week 0 (start the slow clocks):** buy 2 secondary domains, set up mailboxes with SPF,
   DKIM and DMARC, begin warm-up (2-4 weeks); start nightly ingestion of job postings; write
   the legitimate-interests assessment and privacy notice; ask SuperDesign for a DPA.
2. **Weeks 1-4:** detector, Companies House filter, ICP classifier with a ~50-company labelled
   test set, research brief, founder approval queue, enrichment with cost ceilings.
3. **Weeks 5-8:** reply webhook and classifier, funnel dashboard by signal and provider.
4. **Weeks 9-12:** expose reqwatch as an MCP server (internal use and a client demo).

**Don'ts:** no LinkedIn scraping from your own account; no cold sending from the main
domain; no bought static lists; no autonomous sending; no single-provider trust.

### 4.5 Issues in your current stack the fact-checkers flagged

These are worth resolving before relying on reqwatch commercially:

- **Adzuna terms.** A search summary suggests Adzuna's January 2026 terms require commercial
  use to be agreed in advance and may carry a fee. The fact-checker warned the cited PDF may
  be Adzuna's *G-Cloud* terms rather than the free developer API terms, so confirm at
  developer.adzuna.com before concluding anything.
- **LinkedIn-derived job data (the harvestapi feed).** It keeps your own account safe, but
  the data's provenance still carries vendor and terms risk; the research notes LinkedIn
  litigation against scrapers (Proxycurl, reported shut down mid-2025; ProAPIs sued
  October 2025). Prefer licensed or multi-source job data, and ask vendors for their
  provenance position in writing.
- **Free-tier Adzuna rate limits** (reported 25/min, 250/day) are low for a nightly national
  sweep.

---

## 5. How lead generation is done now (for your situation)

Full detail: Appendix A4 (model knowledge, unverified).

1. **Precision beats volume.** Mailbox-provider rules (Google and Yahoo from 2024, Microsoft
   consumer mailboxes from May 2025) and saturated inboxes punish bulk sending. Caveat from
   the fact-checkers: these rules are written for *consumer* mailboxes (personal Gmail,
   Outlook.com). Most B2B prospects sit on Google Workspace or Microsoft 365, which apply
   their own filters. Still, authentication, low complaint rates and one-click unsubscribe
   are the right baseline.
2. **Signals as the targeting layer.** "Hiring for X for 90+ days" is a classic budget-and-
   pain trigger, but needs a second confirming signal and filters for evergreen requisitions,
   recruiter postings and ghost jobs.
3. **Credibility closes high-ticket services.** Buyers check the founder first; proof of work
   (case studies, open-source MCP servers, architecture write-ups) lifts outbound conversion.
4. **"GTM engineer" is the modern name for the hands-on builder role.** Reportedly
   popularised by Clay (medium confidence). It fits what you already do with treg.

**Recommended channel mix for the first six months (A4):**

| Channel | Role | Evidence strength (per the research) |
|---|---|---|
| Signal-led, low-volume outbound (reqwatch) | Primary engine: about 100-200 lower-tier accounts a month, 15-30 top-tier accounts a quarter, 1-3 contacts each, 2-4 touches | Structural reasoning strong; reply-uplift medium; validate with your own cohorts |
| Founder-led proof-of-work content | Warms outbound, builds search and AI-search visibility | Medium; attribution is hard |
| Partners and subcontracting (UK product agencies, dev shops, fractional CTOs) | Matches your subcontract shape; bypasses cold-trust problem | Medium; mostly anecdotal |
| London engineering-leader communities and hosted roundtables | In-person trust compresses sales cycles | Medium; practitioner consensus |

**Deprioritise:** marketplaces (including Upwork) for architect-level work, high-volume cold
email and look-alike domain farms, LinkedIn automation/scraping, autonomous AI SDRs, bought
static lists.

**Your own measurement still stands:** London product companies were far more addressable
(61%) than Chennai (12%, mostly services/staffing competitors). Nothing in the research
contradicts dropping the India slice.

---

## 6. Hiring: the role, the skills, and how to test them

Full detail, including a 40-question bank, scoring rubric and 30-60-90 scorecard:
Appendix A6. Salary figures there are low-confidence recollections.

### 6.1 Which kind of person

| Archetype | Verdict for you |
|---|---|
| **Signal-led outbound operator** (GTM engineer responsible for meetings) | **Hire first**, as a 90-day paid contract-to-hire |
| Outbound SDR/BDR | Good *second* hire once the message works; weak first hire (needs a playbook and a manager; lacks credibility with CTOs on agentic AI) |
| Demand-gen / growth marketer | Later; slow feedback, needs budget |
| "Lead generation executive" (list building) | No - treg already makes this a commodity |
| Agency / fractional | Optional time-boxed benchmark under a strict contract (your domains and data, written "qualified meeting" definition, no LinkedIn automation) |

A UK-fluent candidate fits London CTOs better; an India-based candidate costs less and is
often strong on data and automation. If India-based, have the founder (or a UK copy reviewer)
approve all messaging, and test their copy for UK buyers in the work sample.

### 6.2 Skills to require (weight for your situation, from A6)

Copywriting and offer design for high-ticket services (15); signal design (12);
deliverability engineering (12); ICP and segmentation (8); verification and data hygiene (8);
tooling and automation (8); experimentation and metrics (7); data sourcing and enrichment
waterfalls (6); LinkedIn strategy, LLM prompting/agents, reply handling, compliance (5 each);
CRM hygiene and attribution (4). Compliance and ethics is also a **pass/fail gate**.

Must-haves for the ad: 2-3+ years *owning outbound results* (meetings and pipeline, not just
building tables); has set up deliverability from scratch; concise credible copy for technical
buyers; multi-provider enrichment and verification; comfortable with APIs/JSON/CLI/MCP;
fluent with denominators and cost per qualified meeting; working knowledge of UK GDPR and
PECR. State in the ad: "We don't scrape LinkedIn, buy lists or use deceptive tactics. We
measure qualified meetings and pipeline, not leads."

### 6.3 Interview: highest-signal questions (more in A6)

Use the same 12-15 questions for every candidate and score independently before discussing.

- *"One provider marked an email 'verified' and it bounced; another's pattern-guessed address
  was live. What does that tell you and what changes?"* (Strong: "verified" is a probability;
  catch-alls defeat SMTP checks; independent verifier plus agreement between providers; feed
  bounce rates back into provider order. Red flag: "just switch to the second provider.")
- *"Set up cold-email infrastructure from zero for about 500 contacts a month."* (Strong:
  never the primary domain; 2-3 secondary domains; SPF/DKIM/DMARC aligned; 2-4 weeks warm-up;
  conservative per-mailbox volumes; plain text; monitoring. Red flag: "buy 50 domains and send
  10k a day".)
- *"Design a job-posting signal for 'budget plus failure to hire'. What are the false
  positives?"* (Strong: evergreen reqs, recruiter and ghost postings, repost detection,
  public ATS feeds. Red flag: "scrape LinkedIn Jobs from my account".)
- *"Two variants, 200 sends each: A got 6 positive replies, B got 3. Is A better?"* (Strong:
  not conclusive at this sample size. Red flag: "ship A".)
- *"What was your cost per qualified meeting, and how did you calculate it?"*
- *"Can we cold-email a named person at a UK limited company? A sole trader?"* (Strong:
  corporate vs individual subscribers under PECR; UK GDPR still applies; legitimate interests
  assessment; opt-out and suppression. Red flag: "B2B is exempt from GDPR".)
- *Live, 10 minutes:* write the first email to the CTO of a 60-person London fintech whose
  senior ML engineer role has been open 120 days. (Look for relevance to the trigger, brevity,
  no false claims, a low-friction ask, an opt-out line.)

### 6.4 The implementation test (the part you asked about)

**Format:** paid take-home, hard 4-hour time box, then a 90-minute live debrief. Pay a flat fee
regardless of outcome (A6 suggests roughly £200-£400 UK or ₹10,000-₹20,000 India as an
assumption; no authoritative standard on paying for take-homes was found, so this is
recommended practice). State that you will not use the work commercially without a separate
agreement. Allow AI tools but require disclosure; the debrief tests whether they understand
their own work. Share company-level signals and *synthetic* contact rows, never real people's
personal data.

**Inputs you prepare:** `signals.csv` (about 60 job-signal rows with first-seen, last-seen,
repost count, source, size band, industry), `contacts.csv` (about 20 synthetic contacts with
two providers' results and a verifier result), a one-page company profile, and optionally a
capped sandbox treg key (about $10; not mandatory).

**Tasks (about 4 hours):**

1. Score the 60 signals, explain the model, pick the top 15 accounts and justify every exclusion;
   propose two more signals and how to detect them without breaking any platform's terms.
2. Choose the best contact for the top 10 accounts; decide which email to use or not use, with
   confidence and reasons; state fallback order and verification rules; report cost per usable
   contact.
3. Write a 3-step email sequence and one LinkedIn touch; write openers for three named accounts;
   define the offer and the ask.
4. Plan sending infrastructure from zero for about 500 contacts a month (domains, DNS records,
   warm-up, volumes, monitoring, stop rules).
5. Build a funnel model with explicit assumptions and a cost per qualified meeting; plan the
   first four weeks of experiments.
6. Half a page on what makes the campaign lawful in the UK, what changes for EU/US, and how
   opt-outs and data requests are handled.

**Hard rules:** do not send anything, do not scrape LinkedIn, do not buy data.

**Traps to plant (assessor-only):**

| Trap | What catching it looks like |
|---|---|
| IT-services or staffing firm with many reposted roles | Excluded as a competitor (your Chennai finding) |
| Recruitment agency posting for an unnamed client | Excluded or flagged with a plan to find the end client |
| Evergreen "always hiring" requisition, 300 days old | Recognised as a false positive |
| A sole trader or English partnership in the list | Excluded from cold email (individual subscriber under PECR) |
| Catch-all domain where two providers return different "valid" emails | Flagged risky, catch-all policy applied |
| Provider A "verified" vs provider B pattern guess, verifier says A invalid | Doesn't trust labels (mirrors your real bounce) |
| Out-of-ICP rows (5,000-person bank, non-UK services firm) | Excluded with a reason |
| Same company under two domains | Deduplicated |
| Personal webmail returned as a "work email" | Not used for B2B outreach |

**Scoring (0-4 per criterion, weighted):** signal and ICP judgement 20; data, enrichment and
verification 15; copy and offer 20; deliverability and volume 15; measurement and economics 15;
compliance and ethics 10; communication and honesty 5. Starting thresholds (assumptions):
65/100 or more with no gate failure goes to the debrief; 80+ is strong; strong candidates catch
6+ of 9 traps.

**Automatic fails:** proposing LinkedIn scraping or unsanctioned automation on personal or
founder accounts; recommending bought lists; sending real messages during the exercise;
inventing data or results; copy with no sender identification or opt-out; deceptive tactics
(fake reply threads, invented relationships).

**Live debrief scenarios (pick 3-4):** redesign the verification rule after a verified-but-
bounced email; respond to a 6% bounce rate on day 3 (next hour, next week); rewrite step 1 for a
non-technical CEO in five minutes; map a redacted `treg.companies.enrich` response to CRM
fields and say which you distrust; write an LLM first-line prompt and say how you would
evaluate 50 outputs before sending; handle "Where did you get my data? Remove me."

**Verifying claimed past results:**

| Claim | Check |
|---|---|
| "Booked N meetings a month" | Live screenshare of a CRM report; change date filters live; confirm with the person who took the meetings |
| "X% reply rate" | Live sending-tool analytics; get raw counts and compute it yourself; check auto-replies are excluded |
| "Strong deliverability" | Google Postmaster Tools charts, DMARC report summaries, and a live audit of *your* domain's SPF/DKIM/DMARC |
| "Generated £X pipeline" | CRM report filtered by outbound and creator; ask win rate, deal size, time to close; referee confirms |
| "Built Clay / n8n workflows" | Walkthrough; ask them to explain each node, credit cost per row and failure handling |

Ask for two referees, one of whom took their meetings. Do not ask candidates to share prospect
personal data or a former employer's confidential data.

**30-60-90 trial scorecard (all targets are starting assumptions to calibrate):** infrastructure
live and warmed by day 30; hard bounce rate under 2%; spam-complaint rate under 0.1%; opt-outs
suppressed within one business day; qualified meetings held of about 2 by day 30, 6 by day 60
and 12-15 by day 90; pipeline of roughly £150k-£300k by day 90 (assumes £40-80k engagements).
Guardrail misses (bounces, terms-of-service incidents, opt-outs) count against the person; an
outcome miss with excellent process may mean the offer or market is wrong - review together.
Define a "qualified meeting" in writing (in ICP, decision-maker or direct influencer, problem
acknowledged, meeting actually held, founder confirms within 48 hours) and pay bonuses on
meetings *held*, not booked.

---

## 7. Compliance the hire must know (all unverified in this run; not legal advice)

Full detail with interview questions: Appendix A5. Confirm with a lawyer and the primary
sources.

- **UK PECR:** unsolicited marketing email to *corporate subscribers* (companies, LLPs) does not
  need prior consent, but the sender must be identified and an opt-out given. Sole traders and
  (outside Scotland) most partnerships are *individual subscribers* and need consent or the soft
  opt-in. Screen them out (Companies House helps).
- **UK GDPR still applies** to named work emails: a documented legitimate-interests assessment,
  privacy information by the first contact (Article 14, especially for data bought from a
  vendor), and an absolute right to object to direct marketing, so keep a suppression list.
- **Data (Use and Access) Act 2025:** reported to raise the maximum PECR fine to UK GDPR
  levels (higher of about £17.5m or 4% of turnover). **Sources conflict on the commencement
  date** (19 June 2025 vs 5 February 2026). Verify.
- **EU:** national rules differ. Germany's UWG s.7 is generally read as requiring prior consent
  even for B2B email (the fact-checker says the statute itself says so). France is more
  permissive for job-related B2B email. Gate by country.
- **US:** CAN-SPAM is opt-out; needs a postal address and honouring opt-outs within 10 business
  days. The per-email penalty figure changes every year; check the FTC.
- **India:** DPDP Act 2023 and 2025 Rules, with phased commencement (reported to complete
  around 2027; unverified). Whether an India-based firm prospecting UK/EU contacts also falls
  under UK/EU GDPR (and needs representatives) is a question for a lawyer.
- **Platforms:** LinkedIn's terms prohibit scraping and unsanctioned automation. Your decision
  not to automate from your own account is well supported. Google's Workspace acceptable-use
  policy reportedly prohibits unsolicited bulk commercial email, which is in tension with
  resold or bulk mailbox providers.
- **If you ever run outbound *for clients***, controller/processor roles and DPDP exemptions
  change; get advice first.

---

## 8. What to check first, and decisions only you can make

**Check these before relying on this report (highest impact first):**

1. Commencement status of the UK Data (Use and Access) Act 2025 PECR changes, and any ICO
   guidance after it (legislation.gov.uk, ico.org.uk).
2. Adzuna's developer-API terms for commercial/B2B use (developer.adzuna.com).
3. Current prices and plan names for Clay, Instantly or Smartlead, TheirStack, Coresignal
   (their own pricing pages).
4. treg: pricing schedule and markup, terms, DPA and sub-processors, retention, and whether
   `treg.companies.enrich` / `treg.people.email.verify` are documented; written permission if
   you intend to ship it inside client deliverables.
5. Whether ERPNext's built-in CRM module is really being removed in v17 (one docs snippet said
   so; it affects the Frappe CRM recommendation). Check Frappe's docs.
6. Salary and day-rate bands for your location from live job ads.
7. Whether Zoom's Common Room acquisition closed; whether the Clay pricing reported for March
   2026 is current.

**Decisions only you can make (the research could not answer them):**

- Average engagement value and win rate. They decide the acceptable cost per qualified
  meeting and whether the hire should be full-time, fractional or an agency.
- Where the hire is employed: India entity, UK entity or employer-of-record (UK contractor
  tax rules may also apply).
- UK-fluent versus India-based hire, and who reviews copy.
- Whether the founder commits to taking every first meeting within 48 hours (the incentive and
  scorecard design assume this).
- Whether to adopt a CRM beyond ERPNext/Frappe (this decides whether HubSpot's agent is viable).
- Whether ERP-adjacent partner-directory leads are acceptable given your "systems layer"
  positioning.
- How many UK product companies actually show the reqwatch signal each month; this sets the
  realistic ceiling on outbound volume.

---

## Appendices (raw research, same evidence caveats)

- [A1 AI SDR agents](appendix/A1-ai-sdr-agents.md)
- [A2 Data, signal and outreach platforms](appendix/A2-data-signal-outreach-platforms.md)
- [A3 Building in-house](appendix/A3-in-house-build.md)
- [A4 How lead generation is done in 2026](appendix/A4-state-of-practice.md)
- [A5 Compliance and platform risk](appendix/A5-compliance-risk.md)
- [A6 Hiring and assessment](appendix/A6-hiring-assessment.md)

Each appendix ends with the fact-checker's notes and the researcher's open questions.
