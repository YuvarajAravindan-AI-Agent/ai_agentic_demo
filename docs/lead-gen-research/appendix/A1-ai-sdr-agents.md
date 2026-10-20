> **Evidence status (added when this report was filed, 2026-10-20):** Built from web-search result summaries only (page fetch was blocked). The independent fact-check pass could not run (search budget exhausted): 0 of 20 key claims were independently confirmed.
> This is raw research output from an automated multi-agent run. Treat every price, date, law and vendor claim as *unverified until you check the primary source*.

# Off-the-shelf AI SDRs and autonomous lead-generation agents: market landscape, 20 October 2026

**Prepared for:** AI Agentic Enterprises. They are a founder-led UK/US/EU systems consultancy selling high-ticket work; this is input for hiring a lead-generation expert.

## How this was researched (read first)

**Network limits**
- The page-fetch tool (WebFetch/curl) was blocked by the session's network proxy for every vendor domain tried: 11x.ai, artisan.co, aisdr.com, techcrunch.com, reddit.com.
- So **every fact below comes from search-engine summaries of the URLs cited**. I did not read the full pages myself. All searches ran on **2026-10-20**.

**Search budget**
- The session's web-search budget (200 calls) ran out near the end.
- Two things were not checked as a result: UK GDPR Article 14 (the duty to tell people when you got their data from a third party), and some per-vendor UK/EU data coverage.

**How to read the numbers**
- Every price below is approximate and should be confirmed on the vendor page or in a written quote.
- "Vendor claim" means the figure comes from the vendor's own site. "Competitor-authored" means the review was written by a rival vendor.
- Many 2026 "reviews" (11x.ai/guides, artisan.co/blog, marketbetter.ai, joinvalley.co, salesforge.ai, amplemarket.com/blog, reply.io/blog) are competitors reviewing each other.

---

## 1. The landscape in October 2026: five groups

| Group | Products | How they're sold | Typical price (approx.) |
|---|---|---|---|
| A. Autonomous "digital worker" AI SDRs | 11x Alice/Julian, Artisan Ava, Alta (Katie), Landbase, Topo, Monaco | Sales calls, annual contracts | ~$2k–$15k+/mo |
| B. Self-serve / SMB AI SDRs | AiSDR, Reply.io Jason, Salesforge Agent Frank, Persana Nia, Instantly agents, lemlist agents, Valley (LinkedIn) | Card on file, monthly or quarterly | ~$50–$2.5k/mo |
| C. Agents inside data or sales-engagement platforms | Apollo AI Assistant / Messaging OS, Amplemarket Duo, Unify, Regie.ai, Outreach agents, Salesloft agents | Per seat + credits | $20–$160/seat/mo, plus platform fees |
| D. Agents built into CRMs | HubSpot Prospecting Agent; Salesforce Agentforce Engagement (formerly Lead Nurturing/SDR), Hunter (outbound), Piper (inbound, from Qualified) | Usage credits on top of CRM seats | $1/lead (HubSpot); Salesforce Flex Credits |
| E. Builders / workflow | Clay (Claygent, Sculptor, Sequencer), Relevance AI, Lindy, Rox | Credits / actions | $30–$500/mo self-serve; enterprise custom |

**Trend.** In 2026 the products are converging on "signals → research → draft → (human approves) → send," and moving away from "fully autonomous replacement."
- Monaco puts human "forward-deployed" sellers inside the loop ([TechCrunch, 2026-02-11](https://techcrunch.com/2026/02/11/former-founders-fund-vc-sam-blond-launches-ai-sales-startup-to-upend-salesforce/)).
- HubSpot recommends starting in review mode ([HubSpot KB](https://knowledge.hubspot.com/prospecting/use-the-prospecting-agent)).
- Clay sends Claygent-drafted replies to Slack for a rep to approve ([Clay blog](https://www.clay.com/blog/clay-email-sequencer)).
- Apollo's Slack agents "require approval" ([Apollo](https://www.apollo.io/magazine/apollo-launches-agents)).
- One April 2026 industry piece describes Artisan and 11x as having repositioned toward "hybrid human copilots" ([salesmotion.io](https://salesmotion.io/blog/ai-sdr-claims-scrutiny-what-buyers-should-verify)). That is a secondary source.

---

## 2. Vendor-by-vendor findings

### Group A: autonomous "digital workers"

#### 11x: Alice (outbound) and Julian (inbound voice/chat)
- **Status.** Operating.
  - TechCrunch (2025-03-24) reported that 11x showed logos of companies that were not customers. Per search summaries of the article: ZoomInfo said it only ran a one-month trial; Airtable said its logo was never authorised.
  - Former and current employees said 11x counted full-year ARR on contracts with ~3-month exit clauses. One employee estimated "$14M ARR" was really about $3M of contracts that survived the trial.
  - One employee said "We were losing 70–80% of customers." 11x replied that its retention was "79%."
  - Sources: [TechCrunch](https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/).
  - Founder-CEO Hasan Sukkar stepped down on 2025-05-05. CTO Prabhav Jain became CEO ([TechCrunch](https://techcrunch.com/2025/05/05/11x-ceo-hasan-sukkar-steps-down/), [Tech.eu](https://tech.eu/2025/05/06/founder-of-a16z-backed-11x-steps-down-as-ceo/)).
  - I found no 2026 funding or layoff news (unverified either way).
- **What it does.** Builds lists from your ICP, researches prospects, writes, sends, follows up and handles replies.
  - Setup per 11x docs: authenticate the sending domain → build the knowledge base → define the ICP → configure the sequence → review before launch ([docs.11x.ai](https://docs.11x.ai/alice/setup)).
  - Channels: email is the backbone. LinkedIn is optional for senior roles. Calling, SMS and WhatsApp apply "where consented."
- **Data.** Vendor claim: 400M+ contacts drawn from 50+ sources ([11x guides](https://www.11x.ai/guides/ai-sdr-agents-b2b-sales-teams)).
- **Pricing (11x's own pages, seen 2026-10-20 via search).**
  - Alice Growth: "Starting at $3,750/mo billed annually," up to 5 users, 2,000 new prospects/mo. Pro and Enterprise are custom.
  - The same site also shows "$36,000 per year" in the FAQ and "Plans from $2,000/mo" in a header, so 11x's own figures conflict.
  - Julian Growth: from about $5,333/mo (voice) or $2,417/mo (chat).
  - Annual billing is the default; multi-year discounts are available.
  - Sources: [Alice pricing](https://www.11x.ai/products/alice/pricing), [11x pricing overview](https://docs.11x.ai/help-center/overview/11x-pricing-overview), [Julian pricing](https://www.11x.ai/products/julian/pricing).
- **Reviews.**
  - G2 shows about 4.4 from about 33 reviews ([G2](https://www.g2.com/products/11x/reviews)).
  - Complaints: follow-up logic that ignores existing replies; setup effort.
  - Secondary roundups report Reddit complaints: irrelevant companies added to the CRM, existing customers contacted, duplicates ([ciela.ai roundup](https://ciela.ai/blogs/11x-ai-reddit-review)). These are secondhand and unverified.
- **Fit for this client: Poor.**
  - Cost: about $45k/yr or more on an annual contract.
  - It is built for volume.
  - Its history on customer claims undermines trust in vendor case studies.

#### Artisan: Ava (AI BDR)
- **Status.** Operating.
  - Raised $25M (TechCrunch, 2025-04-09: [link](https://techcrunch.com/2025/04/09/artisan-the-stop-hiring-humans-ai-agent-startup-raises-25m-and-is-still-hiring-humans/)).
  - Known for its "Stop Hiring Humans" billboards (late 2024). Coverage was widely negative ([Windows Central](https://windowscentral.com/software-apps/work-productivity/stop-hiring-humans-controversial-billboard-enrages-silicon-valley)).
  - **Banned from LinkedIn just before Christmas 2025 and reinstated after about 2 weeks.** Per the CEO, LinkedIn objected to Artisan using LinkedIn's name and alleged that Artisan's data brokers had scraped LinkedIn. It was not about AI spam ([TechCrunch, 2026-01-07](https://techcrunch.com/2026/01/07/yes-linkedin-banned-ai-agent-startup-artisan-but-now-its-back/)).
- **What it does.** Research, signal detection (job changes, hiring, growth), individually written emails, reply handling with escalation rules, and a native dialer.
  - Artisan's support docs list only **email and phone** as connectable outreach channels ([support.artisan.co](https://support.artisan.co/getting-started/connect-your-mailbox)), although marketing pages mention LinkedIn steps.
- **Data.** Vendor claim: about 270M B2B contacts plus about 130M local businesses, using "waterfall" enrichment across about a dozen providers (trying one provider after another until one returns a result) and bounce-testing emails. Older Artisan pages cite 250M–350M+, so the numbers are inconsistent ([artisan.co blog](https://www.artisan.co/blog/the-best-ai-sdrs)).
- **Pricing has changed several times.**
  - With Ava 2.0, Artisan published a self-serve card: Intern at $250/mo on annual billing ($280 monthly) with 10,000 credits (about 500 leads/mo), plus a 30-day trial worth 10,000 credits.
  - A third-party tracker reports that on about **2026-07-14** the public rate card was removed. It was replaced by sales-only tiers: Team (~2,500 leads/mo), Scale (~6,000), and Enterprise ([usagepricing.com](https://usagepricing.com/blueprint/activity/artisan-2026-07-14-pricing-sales-gated), [Artisan launch post](https://www.artisan.co/blog/artisan-launches-ava-2-0-the-first-autonomous-ai-bdr-now-self-serve)).
  - Third-party estimates: about $2k–$5k+/mo; annual contracts about $24k–$36k/yr ([joinvalley](https://www.joinvalley.co/blog/artisan-pricing-explained-2026), [marketbetter](https://marketbetter.ai/blog/artisan-ai-review-2026/)). Both are competitor-authored.
  - Dialer: about $67 or $75 per seat/mo; sources conflict.
- **Reviews.** One page reports about 4.1/5 from 51 G2 reviews as of September 2026 (secondary). Recurring complaints: generic copy, more maintenance than advertised, difficulty cancelling ([marketbetter](https://marketbetter.ai/blog/artisan-ai-review-2026/)).
- **Fit for this client: Poor to fair.** Strong data and dialer, but sales-only pricing, annual contracts, and a volume-oriented design. The LinkedIn episode is a supply-chain risk.

#### Alta (Katie), Landbase, Topo, Monaco
- **Alta.** Quote-only; no free plan. G2 about 4.8–4.9 from 31–39 reviews. Funding figures conflict ([Artisan, competitor](https://www.artisan.co/blog/alta-pricing-and-reviews), [11x, competitor](https://www.11x.ai/guides/alta-review)).
- **Landbase (GTM-1 Omni).** Pricing is custom ("Talk to an Expert"). About $42.5M raised per third parties. Its 4–7x conversion claims are vendor claims ([marketbetter](https://marketbetter.ai/blog/landbase-review-2026/)).
- **Topo** (YC W24; described as French-founded and Paris-based).
  - Pricing page: one custom plan that includes 3 user licences, 6,000 credits (1 credit = 1 enriched lead), 2 domains, 6 mailboxes and **human support**. Extra seats $89/user/mo; extra credits $175 per 500 ([topo.io/pricing](https://www.topo.io/pricing)).
  - Funding is unclear: one €1M pre-seed (2023) versus an uncorroborated $25M Series A claim ([extruct](https://www.extruct.ai/hub/topo-io/), [neuronfeed](https://neuronfeed.com/startups/topo)).
  - Of the agents in this group it is the most EU-native, but its EU data claims are unverified.
- **Monaco** (Sam Blond, formerly of Founders Fund and Brex).
  - An AI-native CRM with a prospect database, email agents, a notetaker and human sellers in the loop. Raised $35M (seed plus Series A, Founders Fund). Public beta since 2026-02-11. Flat fee, not disclosed ([TechCrunch](https://techcrunch.com/2026/02/11/former-founders-fund-vc-sam-blond-launches-ai-sales-startup-to-upend-salesforce/)).
  - A later $50M Series B claim comes only from a competitor's blog (unverified).

### Group B: self-serve and SMB AI SDRs

#### AiSDR
- **What it does.** Builds lists from live web research or your CRM, researches each prospect, then runs sequences across email, LinkedIn DMs/InMails and calls. Targets on signals such as job changes, funding and hiring surges ([aisdr.com/platform](https://aisdr.com/platform/)). Its own pages contradict each other on whether it has a 300M+ contact database or is "not a contact database" ([llm-info](https://aisdr.com/llm-info/)).
- **Pricing** (AiSDR's "canonical" page, seen 2026-10-20):
  - Solo: **$250/mo**, 200 researched contacts, 1 user, billed monthly.
  - Explore: $900/mo, 800 contacts, billed quarterly.
  - Scale: $2,500/mo, 2,500 contacts, billed quarterly.
  - No annual lock-in and no per-message overages. AiSDR warns that third-party sites show stale prices ([aisdr.com/llm-info](https://aisdr.com/llm-info/), [aisdr vs artisan](https://aisdr.com/blog/aisdr-vs-artisan-pricing/)).
- **Reviews.** G2 about 4.6 from about 101 reviews. Complaints: learning curve, inaccurate output, email problems; "expect testing and tweaks in the first months." G2 lists no free trial ([G2](https://www.g2.com/products/aisdr-inc-aisdr/reviews)).
- **Fit for this client: Fair, as a low-commitment autonomous benchmark.**

#### Reply.io: Jason AI SDR
- **Pricing.** Vendor pages say from **$500/mo** as a standalone plan, with a 14-day trial ([reply.io/jason-ai](https://reply.io/jason-ai/)). An agent index lists it as month-to-month ([AI Agent Index](https://theaiagentindex.com/agents/jason-ai)). Other third parties quote $139/user or $259; these conflict.
- **Base platform.** About $49/user (email) and $89/user (multichannel), billed annually.
- **Fit for this client: Fair.** An alternative to AiSDR as the control group.

#### Salesforge: Agent Frank
- **Pricing.** About $499/mo billed quarterly (about $416 annually) for roughly 1,000 active contacts; $0.25 per contact above 2,000. The site shows both $499 and $599 in different places ([prospeo](https://prospeo.io/s/salesforge-pricing), [salesgear](https://www.salesgear.io/blog/salesforge-pricing/)). Domains, mailboxes and data are billed separately.

#### Persana AI: Nia
- **What it does.** Vendor pages describe a 24/7 SDR agent across email, LinkedIn and phone, built on "1B+ contacts / 75+ sources" (vendor claim) ([persana.ai](https://persana.ai/features/sdr)).
- **Pricing.** Credit-based. Approximate tiers: Starter ~$85, Growth ~$151, Pro ~$400, Unlimited ~$600 per month ([PricingSaaS](https://pricingsaas.com/companies/persana)). Sources conflict.

#### Instantly and lemlist
- **Instantly.** Vendor says from $47/mo with "three AI agents" and 450M+ leads. Toolradar (September 2026) reports a Starter bundle at $94/mo with the agent using 5 credits per lead ([Instantly blog](https://instantly.ai/blog/best-ai-sales-agents-2026/), [toolradar](https://toolradar.com/guides/best-ai-sdr-agents-for-startups)). G2 about 4.8 from about 4,158 reviews ([G2 AI SDR category](https://www.g2.com/categories/ai-sdrs)). Strong as sending infrastructure; its agent features are lighter.
- **lemlist.** "Agentic enrichment" agents (April 2026) were described as early-stage. 2026 prices conflict: $39–$109 flat versus per-user ([hackceleration](https://hackceleration.com/labs/review/lemlist), [joinvalley](https://www.joinvalley.co/blog/lemlist-pricing-explained-2026)).

#### Valley (LinkedIn-first)
- **What it does.** Targets warm LinkedIn signals (profile viewers, post engagers) and researches each person.
- **Pricing** (Valley's site, July 2026): $149/mo billed quarterly or $199 monthly; $499 "Deep"; $1,499 done-for-you. Other sources: $395/mo (ZoomInfo, March 2026) and $995 for 3 seats ([joinvalley pricing](https://www.joinvalley.co/blog/valley-ai-pricing-explained-2026), [ZoomInfo](https://pipeline.zoominfo.com/sales/valley-ai-review)).
- **Risks.**
  - It runs outreach **from the user's own LinkedIn account**. Valley's own pages describe it variously as cloud-based and as a Chrome extension.
  - It claims "zero suspensions across 1,000+ accounts"; unverified ([joinvalley](https://www.joinvalley.co/blog/linkedin-automation-safety-2026)).
  - LinkedIn's help page says third-party bots, scrapers and automation extensions violate User Agreement §8.2 ([LinkedIn](https://www.linkedin.com/help/linkedin/answer/a1341387)).
- **Fit for this client: Excluded.** It conflicts with their decision not to risk their LinkedIn account.

### Group C: agents inside data and sales-engagement platforms

#### Apollo.io
- **Pricing.** Basic $49, Professional $79, Organization $119 per user/mo on annual billing (Organization has a 3-user minimum); 30k, 48k and 72k credits/yr respectively, per Apollo's own content ([apollo.io insights](https://www.apollo.io/insights/more-information-on-what-they-are-paying-for-in-apollo-plan-detailsusage-walkthrough)). Confirm on apollo.io/pricing.
- **Agent features.**
  - AI Assistant left beta on 2026-03-04. It is "currently free as an introductory offer" on paid plans ([Apollo](https://www.apollo.io/newsroom/announcements/apollo-launches-ai-assistant-powering-end-to-end-agentic-workflows-in-the-first-ai-native-all-in-one-gtm-platform)).
  - Three Slack agents (Lead Discovery, Sequence Creation, Sequence Optimization) all require approval; Pro/Org only ([Apollo](https://www.apollo.io/magazine/apollo-launches-agents)).
  - On 2026-09-30 Apollo announced an "AI GTM System": the Intelligence Layer is live now; Builder Studio and Messaging OS are "available soon" ([Apollo](https://www.apollo.io/newsroom/announcements/apollo-reveals-the-ai-gtm-system-bringing-data-intelligence-and-execution-into-a-single-engine-ushering-in-the-future-of-go-to-market)).
  - Apollo is the data partner for Salesforce Hunter (vendor claim: 240M contacts) ([Apollo](https://www.apollo.io/newsroom/announcements/apollo-named-flagship-data-partner-for-hunter-salesforces-new-outbound-sales-agent)).
- **Controversy.** LinkedIn removed Apollo's and Seamless.AI's company pages around 2025-03-06/07, with no public reason given. Apollo's page was later restored ([MarTech](https://martech.org/a-pair-of-lead-gen-providers-have-disappeared-from-linkedin/), [salesmotion, updated Aug 2026](https://salesmotion.io/blog/linkedin-removed-apollo-brand-page-2025-alternatives)).
- **UK/EU.** Comparisons (mostly vendor-written) say Apollo's EU/UK data is sparser than Cognism's ([bouncezero](https://bouncezero.io/apollo-vs-cognism-2026)). Not independently audited.

#### Amplemarket: Duo
- **What it does.** Duo Copilot (signal, research and sequence agents), Duo Inbox (drafts replies; **the rep clicks send**), Duo Voice (AI voicemail in the rep's voice, reviewed before sending). Data: 200M+ contacts (vendor claim) ([amplemarket.com](https://www.amplemarket.com/blog/best-ai-sales-agents)).
- **Pricing.** Startup: **$600/mo, flat annual rate, 2 users, 30k contacts**, Duo Copilot included. Growth and Elite are custom; third-party estimates are about $2k–$5k and $10k–$50k/mo. Reportedly annual-only ([ZoomInfo](https://pipeline.zoominfo.com/sales/amplemarket-pricing), [prospeo](https://prospeo.io/s/amplemarket-pricing)).
- **Reviews.** G2 about 4.6 from about 657 reviews ([G2](https://www.g2.com/sellers/amplemarket)).
- **Fit for this client: Fair to good**, but the annual commitment is a drawback.

#### Unify
- **What it does.** A signals-to-plays engine: website, CRM, **job-posting** and review-site signals feed AI-agent research and sequences, with managed deliverability. It has a ready-made **"Job Posting Signal Play"** that monitors hiring at target accounts and filters by role and technology ([Unify University](https://webflow.unifygtm.com/university/the-job-posting-play)).
- **Pricing conflicts.**
  - The pricing page snippet shows Free, **Base $20/seat/mo (800 credits)**, **Pro $60/seat/mo (2,400 credits)** and custom Business ([unifygtm.com/pricing](https://www.unifygtm.com/pricing)).
  - Unify's own "explore" articles and third parties cite a **Growth tier at about $1,740/mo on annual billing** (50k credits, 8 managed mailboxes) ([ZoomInfo](https://pipeline.zoominfo.com/sales/unify-gtm-pricing)).
  - Agent runs cost 0.1 credits (vendor) ([Unify](https://www.unifygtm.com/blog/introducing-nextgen-ai-agents)).
- **Fit for this client: Good.** It is the closest off-the-shelf match to "hiring signal → outreach." It does not natively measure "open 90+ days / reposted" (unverified).

#### Regie.ai
- **Pricing.**
  - The official page snippet (seen 2026-10-20) shows Free (250 one-time credits), **Pro $41/mo on annual billing ($49 monthly)**, Team $125/seat on annual billing ($150 monthly, 2-seat minimum), and custom Enterprise ([regie.ai/pricing](https://regie.ai/pricing)).
  - A tracker logs a new plan added on 2026-10-07 ([CostBench](https://costbench.com/changelog/regie-ai-plan-added-2026-10/)).
  - Older figures: AI SEP $180/user and Force Multiplier $499/user; the RegieOne enterprise bundle is "from $35k/yr" ([landbase](https://www.landbase.com/blog/regie-ai-pricing)).
- **What it does.** Agents source, enrich, dial (parallel dialer up to 9 lines) and email from the user's own inbox ([Regie](https://regie.ai/blog/introducing-regie-one)).

#### Outreach and Salesloft
- **Outreach.**
  - Research Agent (analysis of individual stakeholders, bulk or scheduled runs).
  - Revenue Agent ("identifies high-intent accounts, sources fresh contacts, crafts messaging").
  - Deal Agent.
  - Agent Studio (April 2026) ([Outreach release notes, Apr 2026](https://support.outreach.io/support/solutions/articles/159000429739-outreach-product-release-notes-april-2026)).
  - Third-party price estimates: about $100–$160/user/mo plus $5k–$15k onboarding ([prospeo](https://prospeo.io/s/outreach-ai-agent)).
- **Salesloft.**
  - Merged with Clari; the deal closed 2025-12-03 ([claap timeline](https://www.claap.io/blog/clari-competitors)).
  - Agents: 15 launched in spring 2025, 21 later. MCP server in 2026 ([Salesloft](https://www.salesloft.com/company/newsroom/spring-2025-ai-agents-launch)).
- **Fit for this client: Poor.** These are enterprise sales-engagement platforms; overkill for a founder-led firm.

### Group D: agents built into CRMs

#### HubSpot: Breeze Prospecting Agent
- **Pricing.** **100 HubSpot Credits = $1 per lead recommended for outreach.** This replaced a recurring per-contact charge from 2026-04-14 ([HubSpot news](https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete), [HubSpot product page](https://www.hubspot.com/products/sales/ai-prospecting-agent)). Credits reset monthly and do not roll over.
- **Seats** (HubSpot pricing pages, approximate):
  - Sales Hub Starter: $20/seat list (promotions of $7–$10).
  - Professional: $90/seat on annual billing, plus a $1,500 one-off onboarding fee.
  - Enterprise: $150/seat, plus a $3,500 onboarding fee ([HubSpot pricing](https://hubspot.com/pricing/sales), [HubSpot blog](https://blog.hubspot.com/sales/hubspot-sales-hub-pricing)).
- **Availability.** The setup article lists Starter, Professional and Enterprise. A June 2026 update says all paid tiers. Trial length conflicts between 14 and 28 days ([HubSpot KB](https://knowledge.hubspot.com/prospecting/use-the-prospecting-agent)).
- **What it does.**
  - Monitors chosen signals, including **job postings**, funding and leadership changes, and research or visitor intent. Monitoring reportedly uses no credits.
  - Researches and drafts personalised emails.
  - Runs in "Review emails" or "Send without review" mode, with caps on emails per contact and daily recommendations.
- **Fit for this client: Good, but only if they adopt HubSpot.** They currently run ERPNext/Odoo.

#### Salesforce: Agentforce Engagement, Hunter, Piper
- **Agentforce Engagement** (renamed from Lead Nurturing/SDR).
  - Writes a personalised first email from CRM record data, sends "nudges," detects interest, books via the owner's calendar, and answers product questions from uploaded material.
  - "Send as Seller" puts an **AI disclosure** at the start of each email ([Salesforce Help](https://help.salesforce.com/s/articleView?language=en_US&id=sales.sales_agent_sdr_intro.htm&type=5)).
- **Hunter.** A new outbound agent announced at Dreamforce 2026. Pilot now; general release "November '26." Salesforce pages conflict on timing ([Salesforce](https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents/)).
- **Piper** (inbound website chat, voice and email). Came from Qualified.
  - The acquisition was signed 2025-12-17 and **closed 2026-04-01** ([Salesforce](https://www.salesforce.com/news/stories/signs-definitive-agreement-to-acquire-qualified/), [FY27 Q1 highlights](https://www.salesforce.com/news/stories/fy27-q1-highlights/)).
  - About a $1.2B deal per a third party citing a 10-Q (unverified).
  - Historical Qualified pricing is estimated at about $42k–$100k/yr ([knock-ai](https://www.knock-ai.com/blog/qualified-pricing), [prospeo](https://prospeo.io/s/qualified-pricing-reviews-pros-and-cons)).
- **Pricing (third-party).** Flex Credits: $500 per 100k credits, so about $0.10 per standard action. The legacy model was $2 per conversation. Add-ons about $125/user/mo; Agentforce 1 editions from $550/user/mo ([eesel](https://www.eesel.ai/blog/agentforce-pricing)).
- **Fit for this client: Poor.** Requires Salesforce; enterprise cost.

### Group E: builders

#### Clay: Claygent, Sculptor, Sequencer
- **Pricing.** Free: 100 Data Credits and 500 Actions. **Launch ~$185/mo** (~$167 on annual billing): 2.5k–3k Data Credits and 15k Actions. **Growth ~$495/mo** (~$446 on annual billing): 6k Data Credits and 40k Actions. Enterprise custom. Data Credits "from $0.05"; unused Data Credits roll over up to 2x, Actions do not ([clay.com/pricing](https://www.clay.com/pricing), [Clay FAQ](https://www.clay.com/faq/what-features-are-included-in-the-new-plans-how-do-i-pick-the-right-plan)).
  - One source says CRM sync and HTTP API integrations need Growth ([gojiberry](https://blog.gojiberry.ai/blog/clay-pricing)). If so, connecting treg needs Growth; verify.
- **Agent features.**
  - Claygent research agents and the Claygent Builder.
  - Sculptor (a conversational agent builder).
  - **Clay Sequencer**, generally available per a September 2026 post: warming, mailbox rotation, out-of-office handling, and **Claygent-drafted replies sent to Slack for approval**.
  - "Inbox-as-a-source" via AgentMail (July 2026).
  - An inbound SDR agent (Sculpt 2026).
  - Sources: [Clay Sequencer](https://www.clay.com/blog/clay-email-sequencer), [Sculpt 2026 recap](https://www.clay.com/blog/sculpt-2026-recap).
- **Reviews.** G2 about 4.6 from about 232 reviews in the AI SDR category listing ([G2](https://www.g2.com/categories/ai-sdrs)).
- **Fit for this client: Best.** It is a builder's tool. It can take the reqwatch signal and treg data as inputs, keeps a human in the loop, and costs little each month.

#### Relevance AI, Lindy, Rox
- **Relevance AI.** Has a BDR agent template. Self-serve tiers were reportedly withdrawn in May–July 2026 (Enterprise-only now) ([usecarly](https://www.usecarly.com/blog/relevance-ai/), [automationatlas](https://automationatlas.io/answers/relevance-ai-pricing-explained-2026/)).
- **Lindy.** Restructured in 2026 to Plus $29.99, Pro $99.99 and Max $199.99 per user/mo (third-party, September 2026) ([jetadmin](https://www.jetadmin.io/blog/lindy-pricing/)). A general agent builder, not SDR-specific.
- **Rox.** An "agentic CRM." Reported $1.2B valuation (TechCrunch, 2026-03-12, sources say; unconfirmed by the company). Projected about $8M ARR for 2025 ([Yahoo/TechCrunch](https://finance.yahoo.com/news/sales-automation-startup-rox-ai-222550353.html)). Built for enterprise account teams.

---

## 3. Summary comparison table

All prices are approximate, as seen 2026-10-20 via search summaries; verify before relying on them.

| Vendor / product | Does (list / research / write / send / reply / book) | Channels | Data | Entry price | Commitment | Target customer | Fit for this client |
|---|---|---|---|---|---|---|---|
| 11x Alice | all six | Email, LinkedIn, calls, SMS/WhatsApp | Own aggregation, 400M+ (claim) | $3,750/mo (Growth, annual); site also says $36k/yr | Annual | Mid-market / enterprise | Poor |
| Artisan Ava | all six | Email, phone (LinkedIn per marketing) | ~270M B2B (claim), waterfall | Sales-only since ~Jul 2026; est. $2k–5k/mo | Annual (reported) | SMB to mid-market | Poor–fair |
| AiSDR | all six | Email, LinkedIn, calls | Live web + CRM (claims conflict) | $250/mo Solo | Monthly | SMB | Fair (control group) |
| Reply.io Jason | all six | Email, LinkedIn, calls | 1B+ (claim) | ~$500/mo | Month-to-month (reported) | SMB | Fair |
| Amplemarket Duo | list, research, write; reps send | Email, LinkedIn, phone, voice | 200M+ (claim) | $600/mo, 2 users | Annual | SMB to mid-market | Fair–good |
| Unify | signals → research → sequences | Email (managed mailboxes), plus others | Aggregated, credits | $20–60/seat **or** ~$1,740/mo (conflict) | Varies | Growth-stage B2B | Good |
| Clay (+ Sequencer) | build lists, research, write, send; replies with approval | Email (native), others via integrations | 100+ providers via credits | $185/mo (Launch) | Monthly | Any (builders) | **Best** |
| HubSpot Prospecting Agent | research, write, send (review or auto) | Email | HubSpot CRM + signals | $1/lead + seats | Monthly credits | SMB on HubSpot | Good if on HubSpot |
| Apollo AI Assistant / agents | list, research, write; approval | Email, phone, LinkedIn tasks | Own DB (US-strong) | $49–119/user/mo | Annual discount | SMB to mid-market | Fair (data source) |
| Regie.ai | source, enrich, dial, email | Email, phone | Credits | $41/mo Pro (new) | Monthly / annual | SMB to enterprise | Fair |
| Valley | LinkedIn research and messages | LinkedIn (+ email from Aug 2026, vendor) | LinkedIn signals | $149–199/mo | Monthly / quarterly | Founders, SMB | **Excluded** (LinkedIn account risk) |
| Salesforge Agent Frank | all six | Email | Separate data add-on | ~$499/mo | Quarterly / annual | SMB | Fair |
| Topo | agent + human support | Email (2 domains, 6 mailboxes) | Credits (1 = enriched lead) | Custom; extras $89/seat, $175/500 credits | Unclear | EU startups | Fair (EU angle; unverified) |
| Agentforce / Hunter / Piper | nurture, outbound, inbound | Email, chat, voice | Salesforce + Apollo (Hunter) | Flex Credits; Piper ~$42k+/yr (est.) | Enterprise | Salesforce customers | Poor |

---

## 4. UK rules and deliverability limits that apply to any of these tools

**UK email-marketing law (PECR, enforced by the ICO, the UK data regulator)**
- **Companies.** Under PECR, "corporate subscribers" (companies, LLPs, Scottish partnerships, some government bodies) can receive marketing email without prior consent. You must still identify yourself and give a valid opt-out address. The ICO says opt-outs should be honoured ([ICO B2B](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/)).
- **Sole traders and some partnerships** count as individuals, so you need consent or the "soft opt-in." **If unsure, treat a contact as an individual.** UK GDPR still applies to named business contacts.
- **Fines.** The Data (Use and Access) Act 2025 raised maximum PECR fines from £500k to **£17.5m or 4% of global turnover**. Law firms report most provisions commenced on **5 February 2026** ([Lewis Silkin, 2026-02-09](https://www.lewissilkin.com/insights/2026/02/09/uk-data-reform-becomes-reality-what-this-means-for-you-and-what-you-need-to-do-n-102mh5x), [Hill Dickinson](https://www.hilldickinson.com/our-view/articles/data-use-and-access-act-changes-to-uk-data-protection-law-come-into-effect/), [Addleshaw Goddard](https://www.addleshawgoddard.com/en/insights/insights-briefings/2025/data-protection/data-use-and-access-act-2025-top-7-changes/)). Verify on legislation.gov.uk.
- **Not checked this session:** UK GDPR Article 14, the duty to tell people when you obtained their data from a third party such as a data vendor. Get legal advice.

**Mailbox providers**
- **Gmail.** Keep the user-reported spam rate **below 0.1% and never at or above 0.3%**. Bulk marketing mail needs RFC 8058 one-click unsubscribe ([Google](https://support.google.com/mail/answer/81126?hl=en), [FAQ](https://support.google.com/mail/answer/14229414?hl=en)).
- **Microsoft Outlook.com** (consumer addresses), for senders of more than 5,000 messages a day: SPF and DKIM must pass, plus DMARC of at least p=none, aligned. Enforcement began 2025-05-05, initially by routing to Junk ([Microsoft](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730)). Whether outright rejection has started is unverified.

**LinkedIn**
- User Agreement §8.2 prohibits bots, scrapers and unauthorised automation ([LinkedIn help](https://www.linkedin.com/help/linkedin/answer/a1341387)).
- Enforcement examples: lawsuits against Proxycurl (filed January 2025, resolved July 2025) and against ProAPIs and Netswift (October 2025) ([Security Affairs](https://securityaffairs.com/183001/security/linkedin-sues-proapis-for-15k-month-linkedin-data-scraping-scheme.html), [Bloomberg Law](https://news.bloomberglaw.com/ip-law/linkedin-battles-online-scrapers-in-perpetual-struggle-over-data)).
- Plus the Artisan ban and the removal of Apollo's and Seamless's pages described above.
- Claims that ~40% of accounts using flagged tools were restricted in Q1 2026 trace to an untraceable "Northlight" study (unverified).

---

## 5. Where AI SDRs work and where they fail

**Where they work (credible patterns, mostly from vendors and practitioners)**
- **Large markets and lower-value deals.** Thousands of accounts, a clear ICP, and value in volume. Instantly's 2025-data benchmark puts the average cold reply rate at about 3.43% (vendor data) ([Instantly](https://instantly.ai/blog/ai-sales-agent-benchmarks-2026-the-complete-performance-report/)).
- **Inbound speed-to-lead and qualification:** Piper, Julian, HubSpot, Clay's inbound agent.
- **Re-engaging dormant CRM records**, which is Agentforce Engagement's stated purpose.
- **Research and drafting under human approval.** SaaStr (self-reported) says its AI SDRs send 11–40x human volume. It advises starting outbound "where it's less risky," segmenting ruthlessly, and avoiding "hero purchases" ([SaaStr](https://www.saastr.com/stop-learning-ai-start-doing-ai-the-20-agents-running-saastr)).
- **Buyers.** Gartner (March 2026, 646 buyers): 67% prefer a rep-free experience ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience)). But in May 2026 Gartner reported 69% turn to reps to *validate* AI-generated insights ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights)). Humans still matter for trust.

**Where they fail, especially for high-ticket consulting**
1. **Small markets cannot absorb mistakes.** The reqwatch list may be a few hundred UK product companies a month. Burning an account with a generic or wrong email is close to irreversible, and each account is worth tens of thousands. Autonomous tools are tuned for volume; the client needs precision.
2. **Consulting is bought on credibility.** An AI-written note from the founder's name is the brand. Salesforce's own agent adds an AI disclosure when sending as a seller. Either the disclosure or a discovered undisclosed AI email can undercut a "we build serious agentic systems" pitch.
3. **The signal is not off-the-shelf.** Job-posting signals exist in Unify, HubSpot, Artisan and Clay. "Open 90+ days" or "reposted N times" does not appear as a native trigger anywhere I checked (unverified).
   - It needs a job-data source with posted and closed dates. For example, TheirStack has closed-job status and webhooks, and API plans from free to $600/mo ([TheirStack docs](https://theirstack.com/en/docs/guides/how-to-track-closed-jobs), [pricing](https://theirstack.com/nl/pricing)). Days-open must be derived.
   - The client's in-house signal is the differentiator. The AI SDR should consume it, not replace it.
4. **Deliverability damage.** Vendor and practitioner sources consistently say burned domains take weeks to recover, and dashboards show "delivered" while mail lands in spam. Specific numbers ("38-point reputation drop in 90 days," "50–70% churn") are **unsourced** ([leadgen-economy](https://leadgen-economy.com/blog/ai-sdr-cancellation-wave-failure-forensics/), [abmatic](https://abmatic.ai/blog/ai-sdr-no-replies-diagnosis-and-fix)).
5. **Invented personalisation.** Sources describe agents congratulating prospects on funding or expansions that never happened. One widely repeated 11x LinkedIn-screenshot story could not be verified. The mechanism is credible: when the input data lacks a fact, the model invents one.
6. **Data quality outside the US.** US-centric databases are reportedly weaker in the UK and EU. The client already saw a "verified" email bounce. Cross-provider checks and independent verification remain essential whatever the vendor claims about bounce-testing.
7. **Commercial traps.** Annual contracts with exit clauses (11x), sales-only pricing (Artisan since ~July 2026), and credit systems that make cost unpredictable (Unify, Clay, Lindy, Salesforce).
8. **Meetings that don't convert.** A vendor claims AI-booked meetings show up 60–70% of the time versus 75–85% for human-booked ones ([laxis](https://laxis.com/blog/state-of-ai-sdr-2026)). Even if roughly right, the metric that matters for a consultancy is signed engagements, which no vendor reports.

**Cost per lead versus the client's own pipeline** (rough arithmetic on vendor figures; approximate)
- The client's treg chain costs about $0.028 per fully enriched lead.
- AI SDR "per prospect" costs:
  - AiSDR Solo: about $1.25 ($250/200).
  - 11x Growth: about $1.88 ($3,750/2,000).
  - HubSpot: $1.
  - Artisan's old Intern tier: about $0.50.
  - Agent Frank above 2,000 contacts: about $0.25.
  - Topo extra credits: about $0.35.
- These prices include research, writing and sending infrastructure, not just enrichment. At low volume the money is minor. **The real cost is brand and domain risk.**

---

## 6. Shortlist: 3–5 options worth trialling

Run a 60-day bake-off on **separate secondary sending domains**, never the main ai-agentic-enterprises.com domain.

Success metrics: ICP-fit positive replies; qualified discovery calls; spam rate below 0.1% (Postmaster Tools); hard bounces (the common practitioner rule of ~2% is unverified); and founder edit time per message.

1. **Clay (Launch ~$185/mo → Growth ~$495/mo if the HTTP API is needed).** The primary build.
   - Feed reqwatch signals plus treg enrichment into Clay tables.
   - Use Claygent for research, the Sequencer for sending, and Slack approval for replies.
   - Why: it keeps their differentiator in-house, matches their "systems layer" identity, is month-to-month, and doubles as a practical-exercise platform for candidate hires.
2. **Unify.** The packaged "signal → play" option, with a ready-made job-posting play and managed mailboxes.
   - Why: the fastest COTS route to hiring-signal outbound.
   - Caveat: pricing conflicts ($20–60/seat versus ~$1,740/mo Growth); get a written quote. Confirm UK coverage with a test list.
3. **AiSDR Solo ($250/mo, monthly) or Reply.io Jason (~$500/mo).** The autonomous control group.
   - Why: a cheap, cancellable way to measure whether full autonomy beats a founder-approved workflow for this market.
   - Keep it in review mode at first. Never let it use the main domain.
4. **HubSpot Prospecting Agent ($1/lead, plus Sales Hub seats).** Only if the client adopts HubSpot as its sales CRM, as opposed to ERPNext/Odoo.
   - Why: low commitment, a review-before-send mode, a job-postings signal, and pay-per-lead pricing.
5. **Amplemarket Startup ($600/mo, 2 users, annual).** Optional.
   - Why: a well-reviewed all-in-one copilot (G2 ~4.6 from ~657 reviews) where reps still click send.
   - Downside: the annual commitment.

**Not recommended now:**
- 11x and Artisan: cost, annual or sales-only terms, controversy, volume orientation.
- Valley and other LinkedIn-account automation: conflicts with the client's ban-risk policy.
- Salesforce Agentforce, Hunter and Piper: Salesforce-only, enterprise, mostly inbound.
- Outreach and Salesloft: enterprise sales-engagement platforms.
- Monaco: beta.
- Relevance AI: now Enterprise-only.
- Landbase and Alta: quote-only and volume-oriented.

**What this means for the lead-gen hire** (brief)
- Hire for:
  - deliverability engineering (SPF, DKIM, DMARC, domains and mailboxes, warm-up, Postmaster Tools);
  - waterfall enrichment and cross-provider verification;
  - signal design (turning reqwatch into triggers);
  - UK PECR/GDPR literacy (the corporate versus sole-trader test, suppression lists);
  - the discipline to run controlled A/B pilots;
  - the judgement to keep AI on research and drafting while humans own final sends to high-value accounts.
- A good practical exercise: give the candidate 20 reqwatch-flagged UK companies. Ask them to build (in Clay or with treg) a list, research and draft pipeline with cost per lead. They should flag sole-trader and PECR risks, propose a domain and mailbox plan, and explain which of the agents above they would pilot and how they would measure it.


---

## Fact-checker's notes on this report

- PROCESS CAVEAT (most important): this fact-check could not run any fresh check. The shared per-turn WebSearch budget of 200 calls was already used up. Every fetch failed: WebFetch returned DNS ENOTFOUND, and curl through the agent proxy got 403 CONNECT refusals, for techcrunch.com, ico.org.uk, support.google.com, legislation.gov.uk, 11x.ai and hubspot.com. The original report also says it never read a primary page and relied on search-engine summaries only. So NONE of the 20 claims has been checked against a primary source by either pass. Treat every price, date and statistic as a lead to verify. The user can send a follow-up message to rerun this check with a fresh search budget.
- Competitor-authored sources are not flagged consistently. pipeline.zoominfo.com is cited for Amplemarket, Unify and Valley pricing, and ZoomInfo competes with all of them on data. landbase.com is cited for Regie.ai pricing, and Landbase is itself an AI SDR vendor in Group A. prospeo.io, salesgear.io, knock-ai.com, eesel.ai, claap.io, gojiberry and bouncezero.io also sell overlapping tools. The report labels only some sources as 'competitor-authored'.
- Internal inconsistencies in the summary table. (a) Reply.io Jason's data is listed as '1B+ (claim)', but the Reply section never sources it; the only sourced 1B+ claim is Persana's. (b) Valley '+ email from Aug 2026, vendor' does not appear in the body. (c) Clay '100+ providers via credits' is not sourced in the body.
- EU law omitted although the client may sell into the EU. B2B email rules under ePrivacy differ by member state; for example, Germany's UWG s.7 is generally read as requiring prior consent even for B2B cold email (checker's knowledge, unverified this session). A UK-only legal section is not enough for EU outreach; get country-specific advice.
- US law omitted. CAN-SPAM requires a working opt-out honoured within 10 business days, a valid physical postal address, and non-deceptive headers and subject lines. Civil penalties are per email, approximately $50k+ after inflation adjustments; verify the current figure on ftc.gov. Checker's knowledge, unverified this session.
- UK PECR rules for calls are omitted, even though the report discusses dialers and voice AI: Artisan's dialer, Regie's parallel dialer, 11x Julian voice, and Amplemarket Duo Voice AI voicemails in the rep's voice. Live B2B marketing calls must be screened against TPS/CTPS, and automated or recorded calls generally need prior consent, so AI voicemail drops may fall under the automated-call rules. Checker's knowledge, unverified; needs legal advice.
- EU AI Act Article 50 transparency duties for AI systems that interact with people are not mentioned. On the Act's original timetable they apply from 2 August 2026. Whether AI-drafted sales email is in scope, and whether later amendments (the 'Digital Omnibus' proposals) changed the timing, is unverified. Still relevant to the report's own point about AI disclosure (Salesforce 'Send as Seller').
- Data-supply-chain legal risk is underplayed. The checker recalls, unverified, that France's CNIL fined KASPR (a LinkedIn contact-data extension) about EUR 240,000 in December 2024 over contact data collected from LinkedIn. That is directly relevant to the 'data brokers that scraped LinkedIn' issue in the Artisan episode and to the UK GDPR Article 14 duty the report admits it did not check. Verify on cnil.fr.
- Missing vendors relevant to a UK/London target and the build path: Cognism (UK-founded, known for UK/EU data; the report mentions it only in passing), ZoomInfo's own AI/Copilot products, Lusha, Smartlead (sending infrastructure, an alternative to Instantly), Common Room and Warmly (signal-based outbound), and 6sense (AI email agents). For the reqwatch 'days open / reposted' signal, other job-data providers besides TheirStack are worth checking, for example PredictLeads and Coresignal (whether they expose first-seen/last-seen dates is unverified).
- Proxycurl: the report says LinkedIn's suit was 'resolved July 2025'. The checker recalls that Proxycurl announced it was shutting down around July 2025 after the suit (verify). 'Shut down' is the more useful fact for a supply-chain-risk discussion.
- The Gmail and Microsoft bulk-sender rules are presented as hard limits for B2B outreach. They are written for consumer mailboxes (personal Gmail; Outlook.com/Hotmail/Live). Most B2B prospects sit on Google Workspace or Microsoft 365 domains. The thresholds are sound practice, but the framing overstates their legal or contractual reach. Yahoo's parallel requirements are also omitted.
- Clay's 'Best' fit rating depends on several unverified points: the 2026 plan structure, Sequencer being generally available, and whether the HTTP API needs Growth. Combining Clay credits with treg enrichment may also mean paying twice for enrichment unless one system is clearly chosen to own it.
- The cost-per-lead comparison ($0.028 for treg enrichment against ~$0.25 to $1.88 per AI SDR prospect) compares different things, as the report admits. It also leaves out the in-house path's own costs: sending domains and mailboxes, warm-up, independent email verification, and founder review time per message.
- Salesloft-Clari merger close date (2025-12-03) is sourced only from a competitor's blog (claap.io); verify with Salesloft or Clari press releases. The Relevance AI 'Enterprise-only' and Lindy pricing claims also rest on low-authority third-party blogs.
- Statistics from vendors or self-reports should not be read as market benchmarks: Instantly's 3.43% reply rate, laxis's 60-70% vs 75-85% show rates, and SaaStr's '11-40x human volume'. The report labels most of them, but the Gartner 'rep-free' figure also moves between releases (see claim 19) and should not be presented as a stable trend without checking.

### Open questions raised by the researcher

- Methodology gap: the page-fetch tool was blocked by the network proxy for every vendor domain, so no pricing page was read directly. All figures come from search-engine summaries dated 2026-10-20 and need confirmation on the live pages or in written quotes.
- The web-search budget ran out before UK GDPR Article 14 (the duty to inform people whose data came from a third-party vendor) and ICO guidance on AI-generated outreach could be checked. Get UK legal advice before running any AI SDR on purchased data.
- UK/EU data coverage and accuracy of each vendor's database (11x, Artisan, AiSDR, Amplemarket, Apollo, Unify) is unverified. Only vendor-authored comparisons exist. Test each with a sample of 50-100 known UK target contacts and measure bounce rates independently.
- Unify's actual current price for the features needed (job-posting plays, managed mailboxes, AI agents) conflicts: $20-60/seat on the pricing page snippet versus a ~$1,740/mo Growth tier elsewhere.
- Artisan's current (post-July 2026) tier prices and minimum contract are not public. 11x's own pages give three different entry prices ($2,000/mo, $3,750/mo, $36,000/yr).
- No AI SDR checked was confirmed to support a native 'role open 90+ days / reposted N times' trigger. This likely needs a custom feed (e.g., job-data APIs with posted and closed dates) pushed into Clay, Unify or HubSpot.
- Whether the client will adopt a sales CRM (HubSpot) alongside ERPNext/Odoo determines whether the HubSpot Prospecting Agent is viable.
- Client context needed: target deal size, number of reqwatch-qualified accounts per month, whether the founder accepts AI-disclosed or AI-drafted outreach under their name, and an existing secondary-domain and mailbox setup.
- Whether Microsoft Outlook.com has moved from junk-routing to outright rejection of non-compliant bulk mail is unverified.
- Unverified market claims to treat cautiously: Monaco's reported $50M Series B; Topo's reported $25M Series A; Alta's reported $25M Series A; the 'Northlight' LinkedIn restriction-rate study; the widely repeated '50-70% AI SDR churn' and '38-point domain reputation drop' statistics; the specific 11x hallucination screenshot incident.
- HubSpot Prospecting Agent trial length (14 versus 28 days) and exact tier eligibility conflict across HubSpot help pages.
- Regie.ai's pricing appears to have changed in October 2026 (new self-serve Pro $41/mo); older third-party figures ($180/$499 per user) may be stale.
