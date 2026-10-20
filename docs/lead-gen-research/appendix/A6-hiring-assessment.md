> **Evidence status (added when this report was filed, 2026-10-20):** No live sources at all - model knowledge only for facts and salary figures; the assessment design is recommended practice. Fact-check: 0 of 20 claims verified.
> This is raw research output from an automated multi-agent run. Treat every price, date, law and vendor claim as *unverified until you check the primary source*.

# Hiring a lead generation expert in 2026: role choice, skills, interview questions, paid work sample, scorecard

As of 2026-10-20. Prepared for AI Agentic Enterprises (ai-agentic-enterprises.com).

---

## 0. Evidence status (read first)

**This track could not do any live research.**
- The first WebSearch call returned: "web search budget is used up (limit: 200 WebSearch calls per turn, shared by every agent in it)".
- WebFetch failed with `getaddrinfo ENOTFOUND` (a DNS failure) on every host tried:
  - www.clay.com/pricing
  - ico.org.uk (the PECR electronic mail marketing guidance page)
  - support.google.com/a/answer/81126 (Google's email sender guidelines)
  - www.legislation.gov.uk/ukpga/2025/18 (the Data (Use and Access) Act 2025)
  - en.wikipedia.org
  - www.gov.uk

**What this means for the report:**
- No URL here was fetched or seen in a search result in this run.
- Where a domain is named, it tells you where to check. It is not a citation.
- I have not quoted any vendor price that I could not check.

**Labels used:**
- **[BK-unverified]**: a fact from my background knowledge (training data to about mid-2026). I believe it is accurate, but it was not checked in this run. Verify it before relying on it.
- **[RP]**: recommended practice or my own design proposal. No external source is claimed.
- **[ASSUMPTION]**: a starting target to adjust against your own data.

**To finish verification:** send a follow-up message to rerun this track once the search budget resets, or raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`. Section 9 lists exactly what to check.

---

## 1. Role options

### 1.1 What the client actually needs [RP]

**Already solved:**
- Data plumbing. treg gives ~2,600 endpoints across ~40 providers, with routed endpoints for enrich, email find and email verify.
- Low enrichment cost: about $0.028 per fully enriched lead.
- A proprietary signal idea: reqwatch, which flags roles open 90+ days or reposted at small product companies.

**Not yet proven:**
1. **The offer and message** that make a CTO, VP Engineering or founder at a 20-300 person UK product company reply.
2. **Sending infrastructure and deliverability discipline:** separate sending domains, authentication, warm-up, volume caps and monitoring.
3. **A measured funnel** from signal → reply → qualified meeting → opportunity → signed engagement, including cost per qualified meeting.
4. **Compliant operating procedures:** UK GDPR and PECR, suppression lists, LinkedIn terms of service.

**What this means for hiring:** the hire is not there to "find leads". Finding leads costs about 3 cents and is already automated. The hire is there to convert signals into qualified conversations for the founder, and to make that repeatable and documented. A candidate who pitches list size or enrichment volume is solving a problem you no longer have.

**What good B2B lead gen looks like in 2026** for a high-ticket, founder-sold consultancy [RP]:
- Small volumes, chosen by signal. Hundreds to low thousands of contacts per quarter, not tens of thousands.
- Deliverability comes before volume.
- Every address is verified, and provider results are cross-checked.
- One clear offer with low risk for the buyer, rather than "book a demo".
- Founder-led credibility: LinkedIn content and case studies support the outbound.
- Results measured in qualified meetings and pipeline per £ spent, not opens or "leads".
- Documented compliance.

### 1.2 Archetypes compared

| Archetype | Typical work | Fit for this client | Main risk | Verdict [RP] |
|---|---|---|---|---|
| **GTM Engineer (Clay-style)** | Builds signal and enrichment pipelines, multi-provider fallback chains ("waterfalls"), AI research and personalisation, CRM sync, workflow automation (Clay, n8n/Make, APIs, Python/JS). I believe Clay popularised the title [BK-unverified]. | Overlaps heavily with what the founder already built (treg). Useful for turning reqwatch into a product. | You hire a second builder, and nobody owns the message, deliverability or meetings. Many "GTM engineers" build tables but have never been responsible for replies or meetings. | Only if they are also responsible for meeting outcomes (the hybrid below). |
| **Outbound SDR/BDR** | Runs sequences, calls and LinkedIn touches; books meetings for a closer. | Weak as a first hire. Junior SDRs rarely have credibility with CTOs on agentic AI or MCP builds. They need a proven playbook and a manager, which turns the founder into a manager. | Lots of activity, few qualified meetings; high turnover. | A good second hire, once the message works for the market. |
| **Demand-gen / growth marketer** | Inbound: content, SEO, webinars, paid ads, account-based ads, nurture emails. | Medium, but later. Feedback takes months and it needs budget. Founder-led technical content is still a real lever. | Spend you can't attribute when you only close a few deals a year. | Not first. Get content skills from the founder or the hybrid. |
| **Classic "lead generation specialist / executive"** | List building, research, data entry, sometimes appointment setting. Often judged on volume. | Low. treg already does this as a commodity. | Bought lists, volume metrics, compliance gaps. | No. |
| **Fractional consultant or agency** | Outsourced outbound (retainer or pay-per-meeting) or Clay-agency builds. | Medium, as a time-boxed experiment or benchmark. | Generic copy for a niche technical offer. Paid to book meetings, qualified or not. Can burn your domains. You don't keep the learnings. Some use scraped LinkedIn data. | Optional 60-90 day benchmark under a strict contract: your domains and data, a written definition of "qualified meeting", no LinkedIn automation on your accounts. |
| **Recommended hybrid: "signal-led outbound operator"** (a GTM engineer who is responsible for meetings) | Designs and runs the whole loop: signal → enrich → verify → sequence → reply handling → meeting. Writes the copy, runs deliverability, reports cost per qualified meeting. | High. | A rare profile, likely pricier, and claims are easy to inflate, so test hard. | **Hire first, on a 90-day contract-to-hire with a scorecard.** |

### 1.3 Recommendation [RP]

**Profile:**
- At least 3 years of being responsible for outbound results (meetings and pipeline), not only building tables.
- Ideally selling services or technical products to engineering or product leaders.
- Can operate APIs, a CLI or MCP tools (treg) from day one, or learn them within about a week.
- Writes credible, concise English for UK technical buyers.

**Shape of the role:**
- Part-time (for example 3 days a week) on a 90-day paid contract, converting to a permanent role if the scorecard is met.
- The founder takes every first meeting, because high-ticket consulting is sold by the founder.
- The hire's job ends at a qualified meeting that actually takes place, plus a clean handover of notes.

**Location trade-off:**
- A UK-based or UK-fluent candidate fits better for copy and cultural fit with London CTOs.
- An India-based candidate costs less and is often strong on data and automation. Test their copy for UK buyers explicitly in the work sample.
- A split that works: an India-based GTM engineer or operator, with the founder (or a fractional UK copy reviewer) approving all messaging.

**Sequencing:**
- **Phase 1 (days 0-90):** prove reqwatch plus the offer on about 1,000-2,000 carefully chosen contacts.
- **Phase 2:** if cost per qualified meeting and the meeting-to-opportunity rate hit target, add SDR capacity or volume.
- **Phase 3:** add demand gen (founder content, case studies) to lift reply rates.

### 1.4 Compensation (approximate, [BK-unverified], low confidence; verify before any offer)

| Role | UK (national; London often ~10-20% higher) | India (metro, e.g. Chennai/Bengaluru) | US (reference only) | Confidence |
|---|---|---|---|---|
| SDR/BDR (1-3 yrs) | base ~£25k-£35k; on-target earnings (OTE) ~£35k-£55k | fixed ~₹3-8 LPA plus variable; higher (~₹6-12 LPA) at SaaS firms selling to the US/UK | base ~$50k-$75k; OTE ~$75k-$110k | low |
| Senior BDR / outbound lead | base ~£35k-£50k; OTE ~£50k-£75k | ~₹8-15 LPA | unverified | low |
| Lead gen specialist / executive (research, list building) | ~£23k-£32k | ~₹2.5-6 LPA | unverified | low |
| Growth marketer | ~£35k-£65k | ~₹8-20 LPA | unverified | low |
| Demand gen manager | ~£50k-£80k; Head of ~£80k-£110k+ | ~₹15-35 LPA | unverified | low |
| GTM engineer (Clay-style) | ~£50k-£90k; senior higher; little data because the title is new | ~₹10-30 LPA; very little data | ~$100k-$180k (very uncertain) | very low |
| Freelance / fractional GTM or outbound consultant | ~£300-£800/day | ~$15-$50/hour | ~$75-$200/hour | low |
| Outsourced appointment-setting agency | retainer ~£2k-£8k/month, or ~£150-£500 per meeting | unverified (likely lower) | ~$3k-$10k/month | low |

Notes:
- These bands are my recollection of 2024-2026 job-ad and salary-site ranges, not data checked in this run.
- Check them against: Glassdoor UK/India, Reed and Hays/Robert Walters UK salary guides, Welcome to the Jungle (formerly Otta), LinkedIn Jobs, AmbitionBox and Naukri (India), and IT Jobs Watch (UK contract day rates).
- I recorded no Clay, Apollo, Instantly or Smartlead prices, because none could be checked. An attempted fetch of clay.com/pricing failed.

### 1.5 Engagement-model notes

**India employees:**
- Notice periods of 30-90 days are common [BK-unverified], so plan the start date accordingly.
- Probation is typically 3-6 months [BK-unverified].

**UK employees:**
- You need a UK payroll or entity, or an Employer of Record (for example Deel or Remote).
- Right-to-work checks are required.
- UK employment-law reforms (the Employment Rights Act 2025 changes to the qualifying period for unfair dismissal) are being phased in. **Check their current status before designing a probation period** [BK-unverified, low confidence].

**UK contractor through their own limited company (IR35):**
- The off-payroll ("IR35") duty to decide employment status falls on medium and large private-sector clients.
- Small clients, and generally clients with no UK presence, fall outside that duty.
- Verify the size thresholds and how they apply to you with an accountant [BK-unverified].

**Incentives [RP]:**
- Structure: base or day rate, plus a bonus per **qualified meeting held**, plus a bonus on signed engagements (for example 3-5% of the first contract value [ASSUMPTION]).
- Avoid paying per meeting *booked* or per "lead".
- Define a **qualified meeting** as one where:
  - the account is in the ICP and passes the disqualifiers;
  - the attendee is a decision-maker or direct influencer (CTO, VP Eng, Head of Product, founder or CEO);
  - the problem was acknowledged in the reply or on the call;
  - the meeting actually took place;
  - the founder confirms it within 48 hours.

**Ownership [RP]:** the firm owns all domains, mailboxes, the sending-tool workspace, CRM, sequences, prompts and workflows. Never the hire, and never an agency.

---

## 2. Skills matrix

"Weight" is the suggested importance for *this* client (totals 100). Compliance and ethics is also a pass/fail gate.

| Skill | Weight | Junior | Competent | Expert | How to test |
|---|---|---|---|---|---|
| **ICP & segmentation** | 8 | Firmographics only ("UK SaaS, 50-200 staff"). | ICP from win/loss analysis plus hypotheses. Persona and buying committee. Account tiers (A/B/C). Explicit exclusions (IT services and staffing firms are competitors). | Treats the ICP as testable hypotheses with a sized count per segment (as you did with 61% vs 12% addressability). Separates "fits" from "has the pain now". Links segment to offer and price. | Take-home task 1; questions 1-3 |
| **Signal design** | 12 | Generic intent (funding, "visited site", bought intent data). | Specific triggers, each with a detection method, freshness window and false-positive analysis (evergreen roles, recruiter postings, ghost jobs). Combines timing with a fit score. | Builds proprietary signals (role age, repost count, title drift, salary-band changes, ATS source). Tests them against a control group and measures lift. Only sources data legally and within terms. | Task 1 traps; questions 4-7 |
| **Data sourcing & enrichment waterfalls** | 6 | One tool, one export (e.g. an Apollo CSV). | Field-by-field fallback across 2-4 providers. Understands coverage vs accuracy vs cost. Normalises domains and titles; dedupes. | Measures each provider's hit rate and accuracy on its own ICP sample. Orders providers by cost per correct result. Records which provider supplied each field. Caches. Handles rate limits. Works API-first (e.g. treg routed endpoints). | Task 2; questions 8-10 |
| **Verification & data hygiene** | 8 | Trusts "verified" labels. | Verifies everything before sending. Understands catch-all, role and risky addresses. Keeps suppression lists. Re-verifies data older than ~30-90 days [RP]. | Combines providers to reach consensus. Pairs pattern guessing with SMTP checks. Has a catch-all policy. Feeds bounces back to score providers. Labels confidence per field. Manages data decay. | Traps T5/T6/T9; questions 11-13; debrief scenario 1 |
| **Deliverability engineering** | 12 | "Turn on the warm-up tool." | Separate secondary sending domains. SPF, DKIM and DMARC set up and aligned. 2-4 weeks of warm-up. Per-mailbox daily caps. Plain-text emails. Monitors bounces and complaints. | Knows the Gmail, Yahoo and Microsoft bulk-sender rules, Google Postmaster Tools, DMARC reports and blocklists. Reasons about the mix of Google and Microsoft mailbox providers and about link-tracking trade-offs. Rotates and retires domains. Protects the primary domain. Has recovered a burned domain. | Task 4; questions 14-18; debrief scenario 2; live check of your own DNS |
| **Copywriting & offer design (high-ticket services)** | 15 | Templates, feature dumps, "quick call?", AI-sounding fluff. | Short, problem-led, references the trigger, persona-specific, low-friction ask; tests one variable at a time. | Offers that lower the buyer's risk (fixed-scope 8-week build, paid discovery, outcome-based pilot). "Give-first" assets (a one-page build plan for the stalled role's project). Credible to CTOs about agentic AI and MCP without hype. Knows when email, LinkedIn or a warm intro fits. | Task 3; questions 19-23; live rewrite |
| **LinkedIn strategy** | 5 | Mass connection requests, automation tools, scraping from a personal account. | Optimises the founder's profile, sends manual connection requests with notes, engages genuinely, uses Sales Navigator for research within the terms. | Founder content strategy tied to the ICP. Captures warm signals (who engages). Combines LinkedIn with email sequences. Understands ban risk and terms of service; won't run unsanctioned automation. | Questions 24-26 |
| **Tooling & automation** (Clay, Apollo, Instantly/Smartlead, n8n/Make, APIs, Python/SQL) | 8 | Can operate one tool's interface. | Clay-style tables or equivalent; sequencer setup; n8n/Make workflows with webhooks; CRM integration; basic SQL or spreadsheets. | API-first: REST, JSON, auth, pagination, retries and back-off. Scripts in Python or JS. SQL analysis. Workflows with logging, alerts and version control. Picks the right tool for cost and maintainability. | Questions 27-29, 31; debrief scenario 4 |
| **LLM prompting & agents** | 5 | Asks ChatGPT to "write an email". | Prompt templates with variables, structured output, sample-based QA. | Research agents grounded in fetched sources (MCP tools fit here), with cited snippets, refusal when evidence is thin, a test set of examples, cost per lead, and human review for top accounts. | Question 30; debrief scenario 5 |
| **Reply handling & qualification** | 5 | Replies slowly, pushes for a call regardless of context. | Same-day replies. A playbook for positive, "not now", referral and objection replies. Clean handover to the founder. | Qualifies lightly before booking. Gets a second contact at the account. Nurtures "not now" replies into later meetings. | Question 23; debrief scenario 6 |
| **CRM hygiene & attribution** | 4 | Logs some activity. | Defined stages, required fields, dedupe, source/signal/campaign tags, meeting outcomes. | Simple data model (account, contact, signal, touch, opportunity). Pragmatic attribution at small deal volumes. Closed-loop reporting from signal to revenue. Automatic logging. | Questions 32-33 |
| **Experimentation & metrics** | 7 | Reports sends, opens and "leads generated". | Tracks reply rate, positive reply rate, meetings booked and held, show rate; runs A/B tests. | One hypothesis per test. Realistic about small samples. Uses cost per qualified meeting and per opportunity, plus pipeline value and speed. Knows open rates are unreliable. | Task 5; questions 34-36 |
| **Compliance & ethics** (UK GDPR/PECR, EU/US basics) — also a gate | 5 | "B2B is exempt from GDPR", or "we can't cold-email in the UK". | Knows PECR's split between corporate and individual subscribers, legitimate interests with a documented assessment (LIA), the Article 14 privacy notice, opt-out and suppression. Refuses deceptive tactics. | Adds per-country EU rules, CAN-SPAM, vendor contracts (DPAs) and international transfers, DSAR and objection handling, retention, and awareness of the Data (Use and Access) Act 2025. Sets guardrails to protect a small firm's reputation. | Task 6; trap T4; questions 37-40; debrief scenario 6 |

---

## 3. Interview question bank (40 questions) [RP]

How to use it [RP]:
- Pick 12-15 questions for a 60-75 minute structured interview. Use the rest in the debrief.
- Ask every candidate the same questions.
- Have each interviewer score 1-4 independently before discussing.
- Structured interviews and work samples are among the better-supported selection methods in published research [BK-unverified; see Section 7.10].

### ICP & segmentation
**Q1.** "Our own measurement found London product companies about 61% addressable versus 12% in Chennai, where most targets were IT-services and staffing firms (i.e. competitors). How would you turn that into an ICP and a target account count for next quarter?"
- *Strong:* asks how "addressable" was measured. Defines fit (product company, 20-300 staff, engineering team, UK) and timing (open technical roles). Lists explicit disqualifiers (services and staffing firms, enterprises with in-house AI platforms). Estimates segment size and proposes 2-3 segment tests.
- *Red flag:* "anyone who needs AI"; goes straight to tools; no exclusions.

**Q2.** "Who buys an 8-week agentic-AI build at a 60-person SaaS company, and who blocks it?"
- *Strong:* CTO, VP Eng, Head of Product, or the founder/CEO at small companies. Blockers: the in-house engineering lead (who may feel replaced), security or procurement, finance. Explains how messaging differs for each.
- *Red flag:* "HR, because they posted the job."

**Q3.** "Tell me about an ICP you narrowed or abandoned because of data."
- *Strong:* specific numbers with denominators, and the decision that followed.
- *Red flag:* never changed an ICP; only anecdotes.

### Signal design
**Q4.** "Design a job-posting signal that indicates budget plus failure to hire. What are its false positives?"
- *Strong:*
  - Role-age threshold and repost detection (same company and title, new posting ID).
  - Excludes evergreen requisitions, recruiter and agency postings, ghost jobs, multi-location duplicates and roles filled internally.
  - Sources: job APIs such as Adzuna, and public ATS boards (Greenhouse, Lever, Ashby pages).
  - Freshness windows and validation.
- *Red flag:* "Scrape LinkedIn Jobs from my account."

**Q5.** "How would you prove reqwatch beats a generic list?"
- *Strong:* a control group matched on fit, the same copy, and a comparison of positive-reply and meeting rates. Acknowledges sample size.
- *Red flag:* no control group; "it felt better".

**Q6.** "Give three more signals for this offer and how you'd detect each legally."
- *Strong:* examples such as a new CTO or VP Eng hire, a funding or filing event (e.g. Companies House, press), AI or LLM terms in job descriptions, engineering blog or product-launch activity. Each comes with a source and its limitations.
- *Red flag:* buying "intent data" without understanding what it measures.

**Q7.** "How fresh must a signal be, and how do you combine fit and timing?"
- *Strong:* decay windows, a simple scoring model, priority tiers, re-checking before sending.
- *Red flag:* one static list.

### Data sourcing & enrichment
**Q8.** "Walk me through a waterfall: UK company → right decision-maker → email. How do you set the provider order?"
- *Strong:* tests providers on your own sample, orders them by cost per *correct* result, stops on a confident hit, records the source of each field, caches, and is aware of UK-vs-US coverage differences.
- *Red flag:* "Apollo has everyone."

**Q9.** "We pay about $0.028 per fully enriched lead. Is that good? What would you trade for accuracy?"
- *Strong:* recognises data cost is trivial next to the value of a meeting on a high-ticket deal. Would pay 10x more for fewer bounces and better persona targeting. Reasons in cost per qualified meeting.
- *Red flag:* optimises for cents; or has no idea of their past data costs.

**Q10.** "Two providers disagree on employee count and on the CTO's name. What do you do?"
- *Strong:* precedence rules (most recent, most reliable source), cross-checks against the company site or a recent hire announcement, a confidence flag, and holds the account back if uncertain.

### Verification & hygiene
**Q11.** "One provider marked an email 'verified' and it bounced. Another provider's pattern-guessed address was live. What does that tell you, and what process change follows?" (This happened to you.)
- *Strong:* "verified" is a probability, not a fact. Catch-all domains defeat SMTP checks. Use an independent verifier plus agreement between providers. Track bounce rate per provider and feed it back into provider order. Send to small cohorts first.
- *Red flag:* "Just switch to the second provider."

**Q12.** "What is a catch-all domain and how do you treat its contacts?"
- *Strong:* the mail server accepts every address at the SMTP stage, so a check can't confirm the mailbox exists. Options: a separate low-volume cohort, specialist catch-all checks, a different channel, a pattern confidence score.
- *Red flag:* doesn't know.

**Q13.** "How do you keep a prospect database clean for 12 months?"
- *Strong:* re-verify before re-sending aged data. Permanent suppression of unsubscribes, objections and hard bounces. Dedupe. Detect job changes. Delete per a retention policy.
- *Red flag:* "Buy a fresh list each quarter."

### Deliverability
**Q14.** "Set up cold-email infrastructure from zero for ~500 new contacts a month."
- *Strong:*
  - Never send cold from the primary domain.
  - 2-3 secondary domains that redirect to the main site, each with 1-3 mailboxes.
  - SPF, DKIM and DMARC (starting at p=none with reporting), aligned to the From domain.
  - Little or no link or open tracking; plain text.
  - 2-4 weeks of warm-up, then a gradual ramp to roughly 20-50 cold emails per mailbox per day. This volume is a practitioner rule of thumb [BK-unverified].
  - Monitoring of bounces, complaints, blocklists and Postmaster Tools.
- *Red flag:* "Buy 50 domains and send 10k a day"; "warm-up solves it."

**Q15.** "Explain SPF, DKIM, DMARC and alignment."
- *Strong:* SPF authorises the sending servers. DKIM cryptographically signs the message. DMARC sets a policy and requires the From domain to align with the SPF or DKIM domain, and produces aggregate (rua) reports.
- *Red flag:* buzzwords with no mechanism.

**Q16.** "What did Gmail and Yahoo change in 2024, and does it matter for cold outreach?"
- *Strong:* bulk senders (about 5,000+ messages a day to personal Gmail accounts) need SPF, DKIM, DMARC and one-click unsubscribe for marketing mail, and must keep the spam rate below 0.3%. All senders need basic authentication. Microsoft brought in similar rules for Outlook.com consumer mailboxes in 2025 [BK-unverified]. Even below those volumes, complaint rate and authentication drive inbox placement at Google Workspace and Microsoft 365 recipients.
- *Red flag:* never heard of it.

**Q17.** "Bounce rate hits 6% on day 3. What do you do in the next hour, and the next week?"
- *Strong:* pause the campaign. Check bounce codes (unknown user vs policy block). Trace which segment and provider caused it. Re-verify. Check blocklists and Postmaster. Find the root cause. Resume at lower volume. Update the provider scoring.
- *Red flag:* "Keep sending, it'll average out."

**Q18.** "How do you know you're landing in the inbox if opens are unreliable?"
- *Strong:* reply and positive-reply trends per mailbox, Postmaster Tools, seed or placement tests (with caveats), open tracking switched off. Knows Apple Mail Privacy Protection inflates opens [BK-unverified].
- *Red flag:* "Our open rate was 70%."

### Copy & offer
**Q19. (Live, 10 minutes)** "Write the first email to the CTO of a 60-person London fintech whose senior ML engineer role has been open 120 days."
- *Score on:* relevance to the trigger, brevity (roughly under 120 words [RP]), no false claims, a clear offer, a low-friction ask, an opt-out line.
- *Red flag:* "I hope this finds you well", flattery, a fake "Re:", a feature list, a 30-minute meeting request with nothing offered.

**Q20.** "What offer would get a CTO to engage on a £40-80k engagement from cold?"
- *Strong:* something given first, e.g. a one-page build plan for the stalled role's project, a short teardown, a fixed-price paid discovery, or a fixed-scope pilot with a stated outcome. Lowers the buyer's risk. Backed by proof such as a demo or case study.
- *Red flag:* "Book a demo."

**Q21.** "How do you personalise at scale without sounding like AI?"
- *Strong:* relevance beats personal trivia; personalise on the signal itself. Constrain LLM output (length, banned phrases, grounding in fetched facts) and hand-check samples.
- *Red flag:* "AI writes a unique essay for everyone."

**Q22.** "Show me your best and worst sequence, with the numbers."
- *Strong:* raw counts (sent, delivered, replies, positive replies, meetings) and what they learned.
- *Red flag:* percentages only, or results claimed for a whole team.

**Q23.** "How do you handle a positive reply, a 'not now', and a 'who are you?'"
- *Strong:* replies within hours; books with context for the founder; moves "not now" to a dated follow-up; answers "who are you" briefly and honestly, with an opt-out.

### LinkedIn
**Q24.** "How would you use LinkedIn for us without risking the founder's account?"
- *Strong:* founder content, genuine engagement, manual and moderate connection requests with notes, Sales Navigator for research. No unsanctioned automation or scraping, because LinkedIn's User Agreement prohibits it [BK-unverified]. Aware of weekly invitation limits (roughly ~100 a week, varies; unverified).
- *Red flag:* "Run an automation tool across 3 profiles", or "scrape Sales Navigator".

**Q25.** "What's your view of tools whose data comes from scraping LinkedIn?"
- *Strong:* sees both terms-of-service and vendor risk, since such data sources can vanish. Can cite LinkedIn's litigation against scrapers, e.g. hiQ, and the 2025 Proxycurl case followed by Proxycurl's shutdown [BK-unverified]. Prefers compliant sources.
- *Red flag:* "Everyone does it."

**Q26.** "How do you combine LinkedIn and email in one sequence?"
- *Strong:* a sensible order and timing (e.g. profile view or engagement, then a connection request, then an email that refers to it), no spammy double-touching, one owner per conversation.

### Tooling, automation & AI
**Q27. (Live)** "Here is our API doc for an email-find endpoint. Sketch an n8n flow or pseudo-code that enriches a CSV."
- *Strong:* batching, retries with back-off, rate limits, safe re-runs (no double charges), caching, logging cost per row, alerts on silent failures.
- *Red flag:* can't read the docs.

**Q28.** "When would you use Clay vs n8n vs a Python script vs our MCP tools?"
- *Strong:* Clay for fast multi-provider trials with a UI. n8n for orchestration and webhooks. Python for scale, custom logic and cost control. MCP or agents for research tasks. Weighs who owns and maintains each.
- *Red flag:* one tool for everything.

**Q29. (Live)** "Write SQL for positive reply rate by signal type and week."
- *Strong:* correct joins and denominators (unique contacts reached, not emails sent).

**Q30.** "Design an LLM step that writes a first line from a company's site and job post. How do you stop hallucinations?"
- *Strong:* only uses fetched text; returns structured output plus the snippet it relied on; refuses when evidence is thin; tested on a set of examples; human review for tier-A accounts; cost per call tracked.
- *Red flag:* "The model is good enough."

**Q31.** "What breaks in automated pipelines, and how do you notice?"
- *Strong:* provider outages, API schema changes, credits running out, silent empty fields, duplicates. Handles them with monitors, sanity checks and spot audits.

### CRM & attribution
**Q32.** "Design the minimum CRM fields and stages for this motion."
- *Strong:* account and contact; signal type and date; source; sequence; reply category; meeting booked, held and qualified; opportunity value and stage; lost reason. Every term defined.

**Q33.** "A deal came from a cold email, a LinkedIn post and a referral. How do you attribute it?"
- *Strong:* pragmatic first-touch plus asking the buyer how they heard of you; honest about small numbers.
- *Red flag:* a multi-touch model for 10 deals a year.

### Experimentation & metrics
**Q34.** "Which metrics do you report weekly, and which do you ignore?"
- *Strong:* delivered, bounce, complaints, positive replies, meetings booked and held, qualified meetings, opportunities, pipeline, cost per qualified meeting. Ignores opens and "leads".

**Q35.** "Two variants, 200 sends each. A got 6 positive replies, B got 3. Is A better?"
- *Strong:* not conclusive at this sample size. Keep testing, test bigger changes, and set a decision rule up front.
- *Red flag:* "A is 2x better, ship it."

**Q36.** "What was your cost per qualified meeting in your last role, and how did you calculate it?"
- *Strong:* includes tools, data, domains and labour, with a clear denominator.
- *Red flag:* can't calculate it.

### Compliance & ethics
**Q37.** "Can we cold-email a named person at a UK limited company? A sole trader? A partnership?"
- *Strong:*
  - Under PECR, unsolicited marketing email to *corporate subscribers* doesn't need consent, but you must identify yourself and give a working opt-out.
  - Sole traders and (outside Scotland) partnerships count as *individual subscribers*, so they need consent or a soft opt-in.
  - UK GDPR still applies: legitimate interests with a documented assessment (LIA), a privacy notice under Article 14, and the right to object to direct marketing [BK-unverified].
- *Red flag:* "B2B is exempt from GDPR", or "we can't email anyone."

**Q38.** "Someone replies: 'Where did you get my data? Delete it.'"
- *Strong:* stop all contact immediately. Keep a minimal suppression record so they are never emailed again. Reply with the data source and a privacy-notice link. Treat it as an objection or erasure request within one month. Log it.
- *Red flag:* ignores it, or deletes everything including the suppression entry (so they get re-emailed later).

**Q39.** "What changes if we target Germany or the US?"
- *Strong:* Germany is stricter; prior consent is generally needed for email marketing, even B2B. The US (CAN-SPAM) is opt-out based but requires a postal address and a working unsubscribe. Check country by country [BK-unverified].

**Q40.** "Tell me about a tactic you refused to use even though it would have worked short-term."
- *Strong:* a concrete example showing judgement about reputation and law.
- *Red flag:* can't name one, or boasts about growth hacks (e.g. harvesting emails from GitHub commits or scraping communities).

---

## 4. Red flags in candidates [RP]

1. **Volume and vanity metrics:** "generated 10,000 leads", "50k emails a month", "70% open rate", with no meetings, pipeline or denominators.
2. **Can't explain cost per qualified meeting**, or how to calculate it.
3. **Bought or static lists as the strategy** ("we have a database of 200M contacts").
4. **LinkedIn scraping or automation** on a personal or founder account, or multiple fake profiles; dismisses terms-of-service risk.
5. **No deliverability depth:** can't explain SPF, DKIM or DMARC; would send cold from the primary domain; sees volume as the fix.
6. **Treats "verified" as truth;** no catch-all policy; no bounce thresholds or stop rules.
7. **"B2B is exempt from GDPR"** (or the opposite extreme); treats opt-outs and data requests as admin.
8. **Deceptive tactics:** fake "Re:"/"Fwd:" subjects, invented referrals, fake personalisation ("loved your recent post" written by AI), false scarcity.
9. **Generic, long, feature-led copy** that asks for 30 minutes in the first email; heavy AI-sounding text.
10. **Only knows one tool's interface;** can't read API docs. Or the reverse: only builds and has never been responsible for meetings.
11. **Claims without evidence:** no screenshares, no referee who took their meetings.
12. **Claims team results as personal** ("I generated $2M pipeline" as one of ten SDRs).
13. **Gamed incentives in the past:** many meetings that didn't happen or weren't qualified; thinks in pay-per-meeting terms.
14. **Declares A/B "winners" on tiny samples.**
15. **Asks nothing about the offer, deal size or ICP** and jumps straight to tools.
16. **Wants personal ownership of assets** (domains on their own account, data held by an agency).
17. **Submits polished AI output they can't defend live,** or won't do any work sample.
18. **Recommends "growth hacks"** that harvest personal data from platforms against their terms.
19. **Short job tenures with vague outcomes.** Treat this with care: SDR tenure is short across the industry, so it is only a flag alongside other signals.

---

## 5. Practical assessment design

### 5.1 Principles and fairness [RP]

- **Pay for the exercise.** I could **not verify** a formal standard that take-homes over ~3-4 hours should be paid. It is widely recommended practice, not a rule I can cite. Recommendation: pay a flat fee for the 4-hour exercise regardless of outcome. For example £200-£400 in the UK or ₹10,000-₹20,000 in India [ASSUMPTION; set your own].
- State in the brief that you **won't use the candidate's work commercially** without a separate paid agreement.
- **Hard time box (4 hours).** Incomplete sections are fine if the candidate says what they would do next.
- **No paid tools required.** Supply the data so candidates without a Clay or Apollo subscription aren't disadvantaged. Offer an optional sandbox treg key capped at about $10. Using it also shows API/CLI/MCP literacy, but must not be required.
- **No personal data shared with candidates.** Use real company-level signals (not personal data) and synthetic or redacted contact rows. This avoids sharing real prospects' personal data with candidates without a lawful basis [RP].
- **AI use allowed, but must be disclosed.** The live debrief tests whether they understand their own work.
- **Same brief, same rubric, scored independently** by at least two people (e.g. the founder plus one other) before discussing.
- **Feedback.** Give every candidate who completes it brief written feedback.

### 5.2 Process [RP]

| Stage | Length | Content |
|---|---|---|
| 0. Screen | 30 min | Motivation plus 5 screening questions (Q14, Q24, Q34, Q36, Q37). Ask for 2-3 sequences they wrote, with results. |
| 1. Paid take-home | 4 h of work, 5 working days to submit | The brief below |
| 2. Live debrief | 90 min | Walkthrough (15), 3-4 live scenarios (50), structured questions (15), their questions and critique of our approach (10) |
| 3. Evidence and references | 2 referees + 1 live screenshare | Section 6 |
| 4. Offer | — | 90-day contract-to-hire with the scorecard in 5.8. Optional 2-3 week paid pilot first if still unsure. |

**Logistics:** start warming up the company's sending domains and mailboxes about 3-4 weeks before the hire starts. Warm-up takes weeks, and without it the day-30 targets can't be reached [RP].

### 5.3 Take-home brief (copy-paste, then fill in the brackets)

> **Context.** AI Agentic Enterprises designs and builds agentic AI systems and Model Context Protocol (MCP) integrations for product companies, typically as a fixed-scope ~8-week build. We believe a strong buying signal is a technical role at a small or mid-sized product company that has been open 90+ days or reposted several times: proven budget plus difficulty hiring. Our target is UK (London-first) product companies of roughly 20-300 employees. Engagements are sold by our founder.
>
> **Time and pay.** 4 hours of work, hard stop. We pay [£X / ₹Y] on submission regardless of outcome. AI tools are allowed; tell us where and how you used them. We will not use your copy, lists or plans commercially without a separate paid agreement.
>
> **Rules.** Do not send any emails or LinkedIn messages. Do not scrape LinkedIn. Do not buy data. If you lack a tool, describe what you would do and estimate the cost.
>
> **Inputs.** `signals.csv` (60 job-signal rows: company, domain, country, city, employee band, industry, job title, first-seen and last-seen dates, repost count, source, salary band). `contacts.csv` (20 synthetic contact rows with results from two providers and a verifier: name, title, email A and status, email B and status, verifier result, cost). A one-page company profile. Optional: a sandbox API key for our tool registry, capped at $10.
>
> **Tasks.**
> 1. **Signal & ICP (~60 min).** Score all 60 signals and explain your model. Pick your top 15 accounts and list every exclusion with a reason. Propose 2 additional signals and how you'd detect them without breaking any platform's terms.
> 2. **Data & verification (~45 min).** For your top 10 accounts, name the best person to contact and why. Using `contacts.csv` (and optionally the sandbox), decide which email to use, or not to use, with a confidence level and reason. Describe your fallback order and verification rules. Report cost per usable contact.
> 3. **Outreach (~60 min).** Write a 3-step email sequence (with subject lines) and one LinkedIn touch for your top segment. Write openers for 3 named accounts. Define the offer and the ask, and explain why a CTO or founder would respond.
> 4. **Deliverability (~30 min).** Plan sending infrastructure from zero for ~500 new contacts a month: domains, mailboxes, DNS records, warm-up, daily volumes, monitoring, and when you would stop sending.
> 5. **Measurement (~30 min).** Build a funnel model (contacted → positive reply → meeting → qualified → opportunity → pipeline) with explicit assumptions. Estimate cost per qualified meeting. Give a first-4-weeks experiment plan and list what you'd log in the CRM.
> 6. **Compliance (~15 min).** In half a page: what makes this campaign lawful in the UK, what changes for EU and US prospects, and how you'd handle opt-outs and data requests.
>
> **Deliverables.** One spreadsheet (tabs: scored signals, top accounts, contact decisions, funnel model). One document of 5 pages or fewer, or a video of 10 minutes or less. A short log of time spent and tools/AI used.

### 5.4 Planted traps (for assessors only; put them in the data)

| # | Trap | What catching it looks like |
|---|---|---|
| T1 | An IT-services or staffing firm with many reposted roles (looks like a top reqwatch hit) | Excluded as a competitor or not a buyer (matches your Chennai finding) |
| T2 | A recruitment agency posting on behalf of an unnamed client | Excluded, or flagged with a sensible plan to identify the end client |
| T3 | An evergreen requisition ("Software Engineer, always hiring"), 300 days old | Recognised as a false positive for "failure to hire" |
| T4 | A sole trader (and/or an English partnership) in the list | Excluded from cold email, or treated as an individual subscriber under PECR |
| T5 | A catch-all domain where two providers return different "valid" emails | Flagged as risky; catch-all policy applied |
| T6 | Provider A "verified" vs provider B's pattern guess conflict, where the verifier says A is invalid | Doesn't trust labels; uses independent verification; mirrors your real lesson |
| T7 | Out-of-ICP rows (a 5,000-person bank; a non-UK services firm) | Excluded with a reason |
| T8 | One company appearing under two domains (rebrand or redirect) | Deduplicated |
| T9 | A personal webmail address (e.g. @gmail.com) returned as a "work email" | Not used for B2B cold email |

Expected scores [ASSUMPTION]: strong candidates catch 6 or more of 9; competent candidates catch 4-5.

### 5.5 Weighted scoring rubric (score each 0-4; weighted score = score/4 × weight)

| Criterion | Weight | 1 (weak) | 2 | 3 (competent) | 4 (expert) |
|---|---|---|---|---|---|
| A. Signal & ICP judgement | 20 | Gut feel or firmographics; misses most traps | Reasonable scores; catches obvious out-of-ICP rows; misses T1-T3 | Explicit fit × timing model; catches ≥5 traps; clear exclusions | As 3, plus a validation plan (control group), new legal signals with detection methods, and segment sizing |
| B. Data, enrichment & verification | 15 | Trusts "verified" | Verifies, but no handling of conflicts or catch-all | Clear rules: independent verification, conflict resolution, catch-all policy, no webmail, confidence labels, cost tracked | As 3, plus feeding bounces back to score providers, re-verification windows, persona logic per account |
| C. Copy & offer | 20 | Generic, long, salesy or deceptive | Competent but generic offer or "quick call" | Short, tied to the trigger, credible to a CTO, low-friction ask, opt-out line, distinct steps | As 3, plus a compelling low-risk or give-first offer, persona variants, copy test hypotheses |
| D. Deliverability & volume | 15 | Primary domain, big volumes, no DNS plan | Mentions SPF, DKIM, DMARC and warm-up superficially | Secondary domains, aligned authentication, warm-up period, per-mailbox caps, monitoring, stop rules | As 3, plus reasoning about mailbox-provider mix, link tracking, domain rotation and retirement, and bulk-sender rules |
| E. Measurement & economics | 15 | Opens or "leads" as KPIs | Replies and meetings, but no costs or assumptions | Full funnel, explicit assumptions, cost per qualified meeting, one variable per test | As 3, plus realism about small samples, decision rules, link from pipeline to deal size |
| F. Compliance & ethics | 10 | "B2B exempt" or illegal tactics (automatic fail) | Vague mention of GDPR | PECR corporate vs individual (catches T4), legitimate interests + LIA, Article 14 notice, opt-out and suppression | As 3, plus EU/US differences, DSAR handling, vendor and transfer considerations |
| G. Communication & honesty | 5 | Disorganised or over time | Clear but verbose | Prioritised; states assumptions | Crisp, honest about gaps, ready to decide on |

**Automatic fails (gates), regardless of score:**
- Proposes LinkedIn scraping or unsanctioned automation on personal or founder accounts.
- Recommends buying lists.
- Sends real messages during the exercise.
- Invents data or results (e.g. made-up emails presented as verified).
- Copy has no sender identification or opt-out.
- Deceptive tactics (fake reply threads, invented relationships).

**Thresholds [ASSUMPTION]:** 65 or more out of 100 with no gate failure moves to the debrief; 80 or more is strong.

### 5.6 Live debrief scenarios (pick 3-4) [RP]

1. **Verified-but-bounced.** "Your top provider said verified; it bounced. The pattern guess from another provider was live. Redesign your verification rule live."
2. **Bounce spike.** "Day 3, bounce rate 6%, one mailbox shows a policy-block bounce code. Next hour? Next week?"
3. **Persona switch.** "Rewrite your step-1 email for a non-technical CEO in 5 minutes."
4. **JSON mapping.** Show a real (redacted) `treg.companies.enrich` response. "Which fields go to the CRM, which do you distrust, and what would you cross-check?"
5. **LLM quality check.** "Write the prompt for first-line generation, and tell me how you'd evaluate 50 outputs before sending."
6. **Objection.** "A prospect replies: 'Where did you get my data? Remove me.' Write the reply and describe the back-office steps."
7. **Critique.** "What would you stop doing in our current approach, and why?"

### 5.7 Optional paid pilot (2-3 weeks, at the agreed day rate) [RP]

- Run on company-owned domains that were warmed up in advance.
- 150-300 contacts.
- Judge mainly on setup quality, guardrails, data accuracy and copy. Meeting counts at this sample size are mostly noise.

### 5.8 30-60-90 day scorecard (all targets are [ASSUMPTION] starting points to adjust)

| Area | Metric | Day 30 | Day 60 | Day 90 | Source of truth |
|---|---|---|---|---|---|
| Infrastructure | Secondary domains and mailboxes live with SPF/DKIM/DMARC aligned, warmed ≥2-3 weeks; primary domain never used for cold | Done (2-3 domains, 4-6 mailboxes) | Stable | Rotation and retirement plan written | DNS checks, sending tool |
| Strategy | ICP and signal document | v1 | v2 updated from data | Signal-lift analysis (reqwatch vs control) | Doc + CRM |
| Volume | New unique prospects contacted (cumulative) | 150-400 (ramp) | 600-1,000 | 1,200-2,000 | Sending tool |
| Guardrail | Hard bounce rate per campaign | <2% (stop and fix if >3%) | <2% | <2% | Sending tool |
| Guardrail | Spam complaint rate (where measurable) | <0.1%; never ≥0.3% | same | same | Google Postmaster Tools |
| Guardrail | Blocklist incidents on sending domains | 0 | ≤1, fixed within 72h | ≤1, fixed within 72h | Blocklist monitors |
| Outcome (leading) | Positive reply rate (positive replies ÷ unique contacted) | Baseline measured | ≥1.5% | ≥2-3% on the best segment | CRM reply categories |
| Outcome | Qualified meetings held (definition in 1.5), cumulative | ≥2 | ≥6 | ≥12-15 | CRM + founder confirmation |
| Outcome | Show rate (held ÷ booked) | tracked | ≥75% | ≥75% | CRM/calendar |
| Outcome (lagging) | Meeting → opportunity (scoped proposal or paid discovery) | — | measured | ≥30-40% | CRM |
| Outcome (lagging) | Pipeline value (open opportunities × estimated value) | — | first opportunities | ≥£150k-£300k (assumes £40-80k engagements, 3-5 opportunities) | CRM |
| Efficiency | Cost per qualified meeting: tools + data + domains, excluding pay | tracked | ≤£100-£250 | ≤£100-£250 | Finance + CRM |
| Efficiency | Fully loaded cost per qualified meeting (including the hire's pay) | — | tracked | ≤£500-£1,000 | Finance |
| Data quality | Weekly audit of 20 records: correct person, title and fit | ≥85% | ≥90% | ≥90% | Manual audit |
| CRM hygiene | Contacted accounts with signal, source, sequence and outcome filled in | ≥90% | ≥95% | ≥95% | CRM report |
| Compliance | Opt-outs suppressed within 1 business day; LIA and privacy notice documented; zero LinkedIn terms-of-service incidents | 100%; LIA done | 100% | 100% | Suppression log |
| Knowledge transfer | Weekly experiment log; written playbook | Log started | Playbook v1 | Playbook ready to hand over | Shared drive |

**How to read the scorecard [RP]:**
- Day 30 tests the process: infrastructure, data and compliance.
- Day 60 tests the leading indicators: reply quality.
- Day 90 tests the results: meetings and pipeline.
- A guardrail miss (bounce rate, terms of service, opt-outs) is a performance issue for the person.
- An outcome miss with excellent process and a clean experiment log may mean the offer or market is wrong rather than the person. Review it together before deciding.

**Worked funnel example [ASSUMPTION], to set expectations:**
- 1,500 contacted × 2% positive replies = 30 positive replies
- × ~60% booked = ~18 booked × ~80% held = ~14 held × ~70% qualified = ~10 qualified meetings
- × ~35% become opportunities = ~3-4 opportunities × £50k = ~£175k pipeline
- At ~25% win rate, that is ~1 signed engagement within 1-2 quarters.
- One signed engagement probably pays for the trial. Replace every rate with your own data after day 60.

---

## 6. Reference checks and verifying claimed results

### 6.1 Questions for referees [RP]

Get the candidate's consent before contacting referees. Ask for at least one former manager **and** one person who actually took the candidate's meetings (an AE or founder).

1. What was your working relationship, and over which dates did you overlap?
2. What did they own end to end (data, copy, sending infrastructure, replies, calls), and what did others do?
3. In a typical month, how many qualified meetings did they create? How many became opportunities, and who ran those meetings?
4. What did "qualified" mean on your team? Were their meetings ever disputed on quality or no-shows?
5. Tell me about a campaign of theirs that failed. What did they do next?
6. Did they ever cause or fix a deliverability problem (a blocklisted domain, a bounce spike)?
7. How did they handle opt-outs, complaints or data requests?
8. Did they ever push for tactics you considered risky (scraping, LinkedIn automation, misleading subject lines)?
9. How much management did they need, and how did they report?
10. How good was their writing for senior or technical buyers?
11. What would you *not* hire them to do?
12. Would you hire them again for an outbound role where they own the results? Why or why not?

### 6.2 Evidence to request, by claim [RP]

| Claim | Ask for | How to check | Caveat |
|---|---|---|---|
| "Booked N meetings a month" | **Live screenshare** of a CRM report (meetings by owner and source, by month) | Ask them to change date filters live; compare with send volumes; confirm with the referee who took the meetings | Static screenshots are easy to edit; prefer live |
| "X% reply rate" | Live view of sending-tool campaign analytics (Instantly, Smartlead, Apollo, Outreach, etc.): sent, bounced, replied, positive, date range | Get raw counts and compute the rate yourself; check out-of-office and auto-replies are excluded; separate positive from all replies | Some tools count auto-replies as replies |
| "Strong deliverability" | Google Postmaster Tools reputation and spam-rate charts; summaries of DMARC aggregate reports; blocklist history | **Live test:** have them audit *your* domain's SPF, DKIM and DMARC in the interview (DNS lookup or an online checker) and explain what they see | Postmaster shows no data at low volume, which is normal |
| "Generated £X pipeline" | CRM opportunity report filtered by source = outbound and by creator; stage definitions; closed-won | Ask the win rate, average deal size and time to close; the referee confirms | Pipeline figures are often inflated or shared across a team |
| "Built Clay / n8n workflows" | A cleaned template or export, a short video walkthrough, or a repo | Ask them to explain each column or node, the credit cost per row and how failures are handled | Community templates are easy to copy |
| "Wrote high-performing sequences" | The actual copy with results per step | Ask why each line is there; live rewrite (Q19) | — |
| "Managed tool and data budget" | Redacted invoices or usage pages | Have them compute cost per meeting from it | — |

### 6.3 Confidentiality and fairness [RP; legal aspects BK-unverified]

- **Never ask candidates to share prospect personal data** or a former employer's confidential data. Accept redacted or aggregate views.
- A refusal on NDA grounds is acceptable if they can describe the work in convincing detail and a referee confirms it.
- **Avoid "backchannel" references without the candidate's consent.** It is unfair to them, and processing their personal data that way raises UK GDPR transparency questions.
- Some UK employers' policies only confirm dates and job title. Rely on referees the candidate nominates, plus the live evidence above.

---

## 7. Compliance and platform facts the hire must know (all [BK-unverified]; verify before use)

### 7.1 UK PECR: email and calls
- The consent or soft opt-in rule for unsolicited marketing email (reg. 22) covers **individual subscribers**. That includes sole traders and, in England, Wales and Northern Ireland, partnerships.
- For **corporate subscribers** (companies, LLPs, Scottish partnerships, government bodies), PECR does not require consent. You must still identify the sender and give a valid address for opting out (reg. 23). The ICO also advises keeping a suppression list.
- Unsolicited live B2B sales **calls** must be screened against TPS and Corporate TPS, unless the subscriber has consented.
- Texts follow the email rules.
- Where to verify: ico.org.uk guidance on electronic mail marketing and B2B marketing. My fetch of that page failed with a DNS error.

### 7.2 UK GDPR
- Named business email addresses are personal data.
- The usual lawful basis is legitimate interests, which needs the three-part test written up as a legitimate interests assessment (LIA).
- **Article 14:** when data wasn't collected from the person, give them privacy information within a reasonable time (at most one month), or at the first communication if you use the data to contact them.
- **Article 21(3):** an objection to direct marketing must always be honoured. Keep a suppression record.
- Data minimisation and retention apply.
- You need data processing agreements (DPAs) with vendors, and transfer safeguards for US or Indian providers.

### 7.3 Data (Use and Access) Act 2025
- Royal Assent on 19 June 2025 [medium confidence].
- Raises maximum PECR fines to UK GDPR levels: the higher of £17.5m or 4% of worldwide turnover [medium].
- Extends the soft opt-in to charities.
- Clarifies that direct marketing *may* be a legitimate interest [medium-low].
- **Brought into force in stages.** Check which provisions apply on the hire date (legislation.gov.uk; ICO). My fetch of the Act page failed.

### 7.4 EU
- ePrivacy rules are implemented country by country.
- Germany (UWG §7) generally requires prior consent for email marketing, even B2B [medium].
- France broadly allows B2B email related to the recipient's job, with an opt-out [medium].
- Check each country before running an EU campaign.

### 7.5 US (CAN-SPAM)
- No prior consent needed.
- No deceptive headers or subject lines; identify the message as an advertisement.
- Include a valid physical postal address.
- Provide a working opt-out and honour it within 10 business days [high].

### 7.6 India
- The DPDP Act 2023 applies, with DPDP Rules notified in 2025 and phased commencement [low].
- Only relevant if you prospect Indian contacts.

### 7.7 Mailbox-provider rules
- **Gmail and Yahoo, from February 2024:**
  - All senders need SPF or DKIM, valid reverse DNS and TLS, and a spam rate below 0.3% (Google recommends below 0.1%).
  - Senders of about 5,000+ messages a day to personal Gmail accounts also need SPF, DKIM and DMARC aligned, plus one-click unsubscribe for marketing mail [high].
  - Where to verify: Google's email sender guidelines (support.google.com/a/answer/81126). My fetch failed.
- **Microsoft Outlook.com consumer mailboxes, from about May 2025:** similar SPF, DKIM and DMARC requirements for senders above 5,000 a day [medium].
- These rules target *consumer* mailboxes. B2B prospects on Google Workspace or Microsoft 365 are filtered by those providers' own systems, but authentication and complaint rates still matter.

### 7.8 Open tracking is unreliable
- Apple Mail Privacy Protection (from 2021) pre-loads images, which inflates open rates [high].
- Many practitioners switch off open tracking for cold email.

### 7.9 LinkedIn
- The User Agreement prohibits scraping and unauthorised automated access or messaging [high].
- Invitation limits are roughly ~100 a week; this varies and is unverified.
- LinkedIn has litigated against scrapers:
  - hiQ Labs: a long-running case ending in 2022 largely in LinkedIn's favour on breach of contract [medium].
  - Proxycurl: LinkedIn sued in early 2025, and Proxycurl announced it was shutting down in mid-2025 [medium].
- It was reported in March 2025 that LinkedIn removed the company pages of Apollo.io and Seamless.AI [low; verify].
- **Implications:** any tool whose data relies on scraping LinkedIn carries vendor risk. Your decision not to scrape from your own account is sound.

### 7.10 Selection-method evidence
- Schmidt & Hunter (1998) put the predictive validity of work-sample tests at about .54 [medium].
- Sackett, Zhang, Berry & Lievens (2022) revised most estimates downward:
  - Structured interviews came out highest, at about .42.
  - Work samples came out at about .33 [medium].
- Practical reading: combine a structured interview with a work sample rather than relying on either alone.

---

## 8. Job description skeleton [RP]

**Title options:** "Outbound & GTM Engineer (founding)" or "Signal-led Outbound Lead". Avoid "Lead Generation Executive", which attracts list builders.

**Must-haves:**
- 2-3+ years of being responsible for outbound results (qualified meetings → pipeline), ideally selling services or technical products to engineering or product leaders.
- Has set up deliverability from scratch and recovered from a deliverability problem.
- A portfolio of concise, credible copy for technical buyers, with results.
- Experience with multi-provider enrichment and email verification; comfortable with APIs and JSON; willing to use CLI/MCP tooling.
- Fluent with metrics: denominators, cost per qualified meeting, caution with small samples.
- Working knowledge of UK GDPR and PECR (plus EU/US basics); respects platform terms of service.

**Nice-to-have:** Clay, n8n/Make, Python/SQL, LLM structured outputs and agents, founder-led content, familiarity with agentic AI and MCP, a UK tech network.

**State explicitly in the ad:** "We don't scrape LinkedIn, buy lists or use deceptive tactics. We measure qualified meetings and pipeline, not leads." This filters out mismatched candidates early.

---

## 9. Verification checklist (do this when search access returns)

1. **Salaries and day rates:** Glassdoor UK and India, Reed, Hays and Robert Walters 2026 UK salary guides, AmbitionBox, Naukri, LinkedIn Jobs, Welcome to the Jungle, and IT Jobs Watch for contract day rates. Search current job ads titled "GTM Engineer" in London and Bengaluru/Chennai.
2. **GTM engineer role definition:** Clay's own material on GTM engineering and Clay-related job boards.
3. **SDR benchmarks:** ramp time, tenure, meetings per month (e.g. Bridge Group SDR reports).
4. **Cold-email benchmarks:** vendor benchmark reports (Instantly, Woodpecker, etc.). Treat these as vendor marketing, not independent evidence.
5. **Legal:** ICO PECR and B2B guidance; Data (Use and Access) Act 2025 commencement regulations; GOV.UK on the Employment Rights Act 2025 timetable; HMRC off-payroll (IR35) small-company thresholds.
6. **Platforms:** Google sender guidelines, Yahoo sender best practices, the Microsoft Outlook high-volume sender announcement, the LinkedIn User Agreement and prohibited-software help page, the Proxycurl shutdown notice, and reports on the Apollo/Seamless page removals.
7. **Paid take-home norms:** look for any authoritative guidance; otherwise keep it as recommended practice.
8. **Research:** Sackett et al. (2022), *Journal of Applied Psychology*, for the exact validity figures.


---

## Fact-checker's notes on this report

- Fact-checker run also had no web access: the search budget was exhausted and the legislation.gov.uk fetch failed with a DNS error. No claim was independently verified or refuted; the whole track needs a rerun.
- The report names no COTS vendors with prices (Clay, Apollo, Instantly, Smartlead, Lemlist, etc.), so the client's COTS-vs-build question is not answered in this track.
- The 'GTM Engineer' compensation figures and the claim that Clay popularised the title rest on sparse data; treat them as very low confidence.
- The worked funnel and the scorecard targets are assumptions, not benchmarks; do not present them to candidates as industry norms.
- The ICO's post-DUAA guidance updates and the commencement status of the Employment Rights Act 2025 should be checked before the hire is made.

### Open questions raised by the researcher

- No live research was possible in this run. The shared WebSearch budget (200 per turn across all agents) was exhausted, and every WebFetch failed with DNS errors. All facts and numbers need checking. Rerun this track with a follow-up message once search budget is available, or raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.
- Current 2026 UK and India salary and day-rate data for GTM Engineer, SDR/BDR, demand gen and growth roles. The figures given are low-confidence background estimates.
- Current pricing for Clay, Apollo, Instantly, Smartlead and n8n (needed to budget cost per meeting). Clay's pricing page could not be fetched, so no prices are stated.
- Which Data (Use and Access) Act 2025 provisions (PECR fine levels, the legitimate-interests direct-marketing clarification) are actually in force as of the hire date.
- The status and timetable of the UK Employment Rights Act 2025 changes to unfair-dismissal qualifying periods and probation, if hiring a UK employee.
- Where the client will contract the hire from (Indian entity, UK entity, or EOR), and whether UK off-payroll (IR35) rules apply to a UK limited-company contractor.
- The client's real average engagement value, win rate and sales cycle. The 30-60-90 pipeline and cost-per-meeting targets (£150k-£300k pipeline, 12-15 qualified meetings) are assumptions built on £40-80k engagements.
- Whether the client wants a UK-fluent hire (better for copy to London CTOs) or an India-based hire (cheaper, strong on automation) with founder review of messaging.
- Whether the client will give candidates an optional capped treg sandbox key, and how to generate a synthetic or anonymised contacts.csv without sharing real personal data.
- Independent (non-vendor) benchmarks for positive reply rate and meetings per 1,000 contacts in signal-based UK B2B outreach to technical buyers. Vendor benchmark reports should be treated as marketing.
- Whether LinkedIn's March 2025 removal of the Apollo/Seamless company pages and the Proxycurl lawsuit and shutdown happened as recalled. Both are flagged unverified.
- Whether the founder will commit to taking all first meetings within 48 hours, which the qualified-meeting definition and the incentive design assume.
