> **Evidence status (added when this report was filed, 2026-10-20):** No live sources at all - model knowledge only. Fact-check: 0 of 20 claims verified. NOT LEGAL ADVICE.
> This is raw research output from an automated multi-agent run. Treat every price, date, law and vendor claim as *unverified until you check the primary source*.

# Legal, compliance and platform-risk constraints for B2B lead generation
**Client:** AI Agentic Enterprises (India-based; selling mainly to UK, also EU/US) | **As of:** 20 Oct 2026 | **Track:** legal, compliance and platform risk

> **NOT LEGAL ADVICE.** This is a research brief for planning and hiring. Anything marked **[LAWYER]** should be confirmed with a qualified lawyer in that jurisdiction (UK, plus Germany/France/the EU, the US, and India) before you act on it.

---

## 0. Read first: how this was researched

- **No live sources this run.** The shared WebSearch budget for this workflow turn (200 calls) was used up before this track began. WebFetch returned `getaddrinfo ENOTFOUND` for every host tried: gov.uk, legislation.gov.uk, ico.org.uk, linkedin.com, support.google.com, ftc.gov, edpb.europa.eu, en.wikipedia.org. **So no primary page was fetched, and no URL below is cited as a source.**
- Everything comes from model knowledge (training data to about mid-2026). Each item carries a confidence tag:
  - **[K-high]**: long-established, widely documented
  - **[K-med]**: fairly sure, but details or dates need checking
  - **[K-low]**: hazy memory; treat as a lead to check
- "Verify at" names the official publisher (regulator or legislation site) to check against. These are pointers, not citations.
- Anything that happened after early 2026 (commencement orders, Digital Omnibus, DPDP timeline changes, new lawsuits) is most likely to be stale or missing.
- **Recommended:** re-run this track with search budget, so that each claim gets a primary URL and an as-of date. To do that, send a follow-up message or raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`.

---

## 1. Bottom line by jurisdiction and channel

| Channel | UK corporate subscriber (Ltd/PLC/LLP, Scottish partnership, public body) | UK sole trader / non-Scottish partnership | Germany | France | US |
|---|---|---|---|---|---|
| **Cold email** | Allowed under PECR, but UK GDPR applies: LIA, Art 14 notice by the first email, opt-out, sender identity shown [K-high] | Needs consent or soft opt-in. **In practice, don't cold email** [K-high] | Prior express consent needed even B2B (UWG §7). **In practice, no cold email** [K-high] | Allowed without consent if relevant to the recipient's job, with opt-out in every message [K-high] | Allowed (CAN-SPAM opt-out regime) [K-high] |
| **Cold call (live, human)** | Allowed unless the number is on CTPS or has objected [K-high] | Allowed unless the number is on TPS or has objected [K-high] | B2B needs at least *presumed* consent; risky [K-med] | Generally allowed with opt-out for professionals [K-low] | Business landlines generally OK; check DNC lists and state law. Mobiles are higher risk [K-med] |
| **Automated, prerecorded or AI voice** | Prior consent needed for all subscribers (PECR reg 19) [K-high] | Prior consent [K-high] | Prior consent [K-med] | Prior consent [K-med] | Prior express consent (written, for telemarketing). FCC 2024: AI voice counts as "artificial" [K-med] |
| **Cold SMS** | Avoid: you usually can't tell whether a mobile belongs to a corporate or individual subscriber [K-med] | Consent [K-high] | Consent [K-med] | Consent [K-med] | TCPA consent; texts count as calls [K-high] |
| **LinkedIn messages (manual)** | Allowed under LinkedIn terms if manual. Whether PECR's "electronic mail" definition covers DMs to sole traders is unclear [K-low] [LAWYER] | Same | Unclear [LAWYER] | Unclear | No CAN-SPAM issue for platform DMs [K-low] |

Other EU states (Austria, Italy, Spain, Netherlands, Poland, Nordics…) set their own B2B rules under ePrivacy Directive Art 13. Several are believed stricter than France. **Verify country by country before targeting.** [K-low]

Canada is out of scope, but note that CASL needs consent (express or implied) for B2B commercial email too, with a narrow "conspicuous publication" exception. [K-med]

---

## 2. United Kingdom

### 2.1 PECR (Privacy and Electronic Communications Regulations 2003)
Verify at: ico.org.uk (Guide to PECR; business-to-business marketing pages) and legislation.gov.uk (SI 2003/2426).

**Reg 22: electronic mail (email, SMS, and probably in-app and social DMs)**
- Unsolicited direct-marketing email to **individual subscribers** needs prior consent or the soft opt-in. [K-high]
- The soft opt-in means the person is an existing customer, the product is similar, and they had a chance to opt out at collection and in every message. [K-high]
- "Individual subscribers" include **sole traders and partnerships, except Scottish partnerships**. [K-high]
- **Corporate subscribers** (companies, LLPs, Scottish partnerships, government bodies) are outside the reg 22 consent rule. [K-high]
- The ICO's view is that the "electronic mail" definition is broad and can include direct messages on social media. Whether that covers LinkedIn InMail to a sole trader is untested as far as I know. [K-low] [LAWYER]

**Reg 23: applies to all subscribers, including corporate**
- Do not disguise or conceal who is sending.
- Provide a valid address for opt-out requests. [K-high]
- Practical upshot: a lookalike sending domain is fine only if the email clearly identifies AI Agentic Enterprises.

**Calls**
- **Reg 21:** live unsolicited marketing calls may not go to numbers registered with **TPS** (individuals, including sole traders) or **CTPS** (corporates), or to anyone who has objected. [K-high]
- The ICO expects screening against TPS/CTPS shortly before calling; a 28-day refresh is commonly cited. [K-med]
- **Reg 19:** automated calls (and almost certainly AI voice agents) need prior consent for all subscribers. [K-high] (AI-voice classification [K-med])

**Employees at corporate email addresses**
- PECR may not require consent for `jane.smith@company.co.uk`, but **UK GDPR still applies**, because a named work address is personal data. [K-high]

### 2.2 UK GDPR obligations that apply even to compliant B2B email [K-high unless marked]

- **Lawful basis:** legitimate interests (Art 6(1)(f)), with a written **LIA** covering three tests:
  - purpose (why you need it)
  - necessity (no less intrusive way)
  - balancing (recipient's reasonable expectations, relevance to their role, opt-out ease)
  - The ICO publishes an LIA template.
- **Transparency (Art 14):** when data comes from a vendor, enrichment API, Companies House, a job board and so on, you must give the privacy information by **the first communication at the latest**, and within one month at most. It covers:
  - identity and contact details
  - purposes and lawful basis
  - the legitimate interest pursued
  - categories of data
  - **source of the data**
  - retention
  - rights, including the right to object
  - right to complain to the ICO
  - The "disproportionate effort" exemption is hard to use for direct marketing. In practice: a short notice in the first email plus a link to a full privacy notice.
- **Right to object to direct marketing (Art 21(2)-(3))** is absolute. Stop at once and suppress (keep a minimal suppression record so you never re-contact).
- **Data minimisation and accuracy:** collect only what the outreach needs. Your own lesson applies here: a vendor-"verified" email bounced, so provenance and verification also serve accuracy.
- **Retention:** set a period for non-responders and delete when it ends. Keep only the suppression entry.
- **Records:**
  - Art 30 ROPA: the under-250-employee exemption does not cover regular, non-occasional processing like prospecting. [K-med]
  - DPIA screening: the ICO lists "invisible processing" (data from third parties without notice) as likely needing a DPIA. [K-med]
- **Profiling / lead scoring** (e.g. AI research on a prospect) should be described in the privacy notice. It is not an Art 22 automated decision unless it has legal or similarly significant effects. [K-med]

**Territorial reach and representatives [LAWYER]**
- UK GDPR Art 3(2) reaches non-UK controllers who offer goods or services to people in the UK, or who monitor their behaviour (open and click tracking and profiling could count as monitoring).
- If caught, **Art 27 requires a UK representative** unless processing is occasional and low-risk. Systematic prospecting is not "occasional". [K-med]
- Whether a non-UK controller must pay the **ICO data protection fee**: unverified.

**International transfers**
- If UK or EU vendors or partners export prospect data to India, a transfer tool is needed (IDTA or UK Addendum; EU SCCs). India has no UK or EU adequacy decision. [K-high on no adequacy as of training data]

### 2.3 Data (Use and Access) Act 2025 (DUAA)
Verify at: legislation.gov.uk (the DUAA is believed to be 2025 c. 18, plus its commencement regulations); GOV.UK "plans for commencement"; ico.org.uk DUAA pages.

| Change | What I believe it does | Confidence |
|---|---|---|
| Royal Assent | 19 June 2025 | [K-med] |
| **PECR fines** | Brings PECR enforcement under the UK GDPR / DPA 2018 penalty regime. Maximum rises from **£500,000** to the higher of **about £17.5m or 4% of worldwide annual turnover** | [K-med] |
| Direct marketing and legitimate interest | Adds to Art 6 a list of processing that *may* be a legitimate interest, including **direct marketing** (formerly only in Recital 47). **This does not remove the balancing test.** | [K-med] |
| "Recognised legitimate interests" (new Annex 1) | No balancing test needed, but the list covers things like crime prevention, safeguarding, national security and emergencies. **Not marketing.** | [K-med] |
| Soft opt-in | Extended to **charities** (not relevant to the client) | [K-med] |
| Cookies / storage | New consent exemptions, e.g. analytics/statistics and site functionality. Some need an opt-out | [K-med] |
| Complaints | Controllers must make complaints easy (e.g. an online form), acknowledge within 30 days, and respond without undue delay | [K-med]; commencement date [K-low] |
| DSARs | Codifies a "reasonable and proportionate" search; "stop the clock" while clarifying | [K-low] |
| ICO governance | ICO becomes a corporate "Information Commission" | [K-low] on timing |
| **Commencement** | Staged, by commencement regulations. My understanding is that **most data protection and PECR changes, including the higher PECR fines, commenced around 5 February 2026**, and the complaints duty around 19 June 2026 | **[K-low]: verify exact SI and dates** |

**Takeaway for the client:**
- PECR breaches (e.g. emailing UK sole traders without consent, or calling CTPS-listed numbers) now carry GDPR-scale maximum fines.
- The DUAA does **not** make B2B cold email "automatically legitimate". Keep doing LIAs.

### 2.4 Buying or renting lists: ICO expectations
Verify at: ico.org.uk direct marketing guidance ("buying or renting data" sections).

The ICO expects real due diligence, not reliance on contract warranties alone. [K-high in substance] Check:
- who compiled the data, how, and when
- what people were told about their data being passed on and used for marketing; for consent-based lists, the buyer must have been **named specifically** (no generic "selected partners")
- whether the vendor gave Art 14 notices
- whether it was screened against TPS/CTPS and suppression lists
- how recent and accurate it is
- whether opt-outs propagate

Keep a vendor due-diligence file. Bought lists for B2C consent channels are high-risk.

Historical context:
- The ICO's 2020 enforcement notice against Experian over "invisible processing" for marketing was largely overturned by the First-tier Tribunal in 2023 [K-med]. Later appeals: unverified.
- Even so, the ICO's position on transparency for data-broker sourcing remains strict.

---

## 3. European Union

### 3.1 GDPR legitimate interest for B2B outreach
- Art 6(1)(f) plus Recital 47 ("direct marketing may be regarded as carried out for a legitimate interest"). [K-high]
- **CJEU C-621/22 (KNLTB), 4 Oct 2024:** a purely commercial interest can be a legitimate interest, but the necessity and balancing tests are applied strictly. [K-med]
- **EDPB Guidelines 1/2024 on legitimate interest:** adopted for public consultation in October 2024. Whether a final version has been adopted by Oct 2026 is unverified. [K-med on the draft] (Verify at edpb.europa.eu)
- Art 14 notice, Art 21 objection and Art 27 representative: same logic as the UK. A non-EU firm systematically prospecting EU residents should get advice on Art 3(2) and on appointing an EU representative. [LAWYER]

### 3.2 ePrivacy national variation (Directive 2002/58/EC Art 13)
- The proposed **ePrivacy Regulation** was, to my knowledge, listed for **withdrawal** in the Commission's 2025 work programme (Feb 2025). The Directive and its national laws remain the rules. [K-med]
- **Germany: UWG §7(2)** [K-high on the email rule]
  - Advertising by **email** without the addressee's **prior express consent** is an "unacceptable nuisance", **B2B and B2C alike**.
  - §7(3) has a narrow existing-customer exception.
  - B2B **phone** advertising needs at least **presumed consent**; B2C needs express consent and documentation under §7a. [K-med]
  - Enforcement is often by competitors and associations through cease-and-desist letters (Abmahnung) with cost claims. German courts have treated even a **single** unsolicited B2B email as actionable. [K-med]
  - **Practical rule: no cold email to German recipients.** Use inbound, events, referrals, content, manual LinkedIn engagement, or postal letters (GDPR still applies). [LAWYER for any phone outreach]
  - Verify at gesetze-im-internet.de (UWG §7).
- **France: CNIL / CPCE Art L.34-5** [K-high]
  - B2B email to professionals is allowed **without prior consent** if the message relates to the recipient's **profession or role**.
  - The person must have been informed and able to object at collection, and every message needs an opt-out.
  - Generic addresses (contact@, info@) are treated as legal persons.
  - The CNIL's reference retention for prospect data is often cited as **3 years from collection or last contact**. [K-med]
  - Verify at cnil.fr.
- **Others:** Austria, Italy, Spain and others are believed to need consent for some or all B2B email; the Netherlands is believed to distinguish natural from legal persons. [K-low] **Encode per-country rules as data in the pipeline and verify each before launch.**

### 3.3 Enforcement precedent directly on point: CNIL v. Kaspr
- The CNIL fined **Kaspr** (a Chrome extension that extracted LinkedIn users' contact details) **about €240,000**. The decision is believed to be dated late 2024 and published around January 2025. [K-med]
- Reported failings:
  - no valid lawful basis for collecting contact details of LinkedIn members who had limited visibility to first-degree connections
  - excessive retention (about 5 years, renewed on each update)
  - poor transparency, including notices only in English and only years after collection
  - inadequate handling of access requests
- **Lesson:** data extracted from LinkedIn by extensions or scrapers is a regulatory target, and buyers of such data inherit transparency and lawful-basis problems.
- Older example: Polish UODO fined Bisnode in 2019 (about PLN 943k) for failing to give Art 14 notices to people whose data came from public business registers. [K-med]. Later court outcome: unverified.

### 3.4 EU AI Act (Regulation (EU) 2024/1689)
Verify at eur-lex.europa.eu and the Commission's AI Act pages.

**Timeline** [K-med]
- In force 1 Aug 2024
- Prohibited practices and **AI literacy (Art 4)**: from 2 Feb 2025
- General-purpose AI obligations: 2 Aug 2025
- **Most remaining obligations, including Art 50 transparency: 2 Aug 2026**
- Some high-risk (Annex I) obligations: 2 Aug 2027

**Art 50 transparency** [K-high on content]
- **50(1):** *providers* must design AI systems that interact directly with people so the people are told they are dealing with an AI, unless that is obvious. Covers website chatbots, AI SDR agents that converse by email or chat, and voice agents. If the client **builds** such an agent for itself or a customer, it is likely the **provider**.
- **50(2):** providers of generative AI must machine-mark synthetic output.
- **50(4):** *deployers* must disclose deepfakes, and AI-generated text **published to inform the public on matters of public interest** (unless human-reviewed under editorial responsibility). One-to-one AI-drafted sales emails do not obviously fall under 50(4), but deception, impersonation or fabricated personalisation is still risky under other laws.
- Fines for Art 50 breaches: up to €15m or 3% of turnover. [K-med]

**Extraterritorial reach** [K-med]
- The Act applies to third-country providers and deployers where the AI output is used in the EU (Art 2(1)(c)).

**Digital Omnibus** [K-low]
- Proposed in Nov 2025: delaying some high-risk deadlines, a grace period for Art 50(2) marking for systems already on the market, and softening the Art 4 AI-literacy duty.
- **Whether it was adopted, and in what form, by Oct 2026 is unverified.** Check before you state any date to a client.
- A Commission code of practice on marking and labelling AI-generated content was being drafted in 2025-26. Status unverified.

**UK:** there is no AI Act equivalent. UK GDPR transparency and consumer and advertising rules apply instead.

---

## 4. United States

### 4.1 CAN-SPAM (15 U.S.C. 7701 et seq.; FTC)
Verify at ftc.gov (CAN-SPAM compliance guide for business).

- **Covers B2B commercial email.** No consent is needed; it is an opt-out regime. [K-high]
- Requirements [K-high]:
  - no false or misleading header information (From, Reply-To, routing)
  - no deceptive subject lines
  - identify the message as an advertisement (clear and conspicuous) unless the recipient opted in
  - include a **valid physical postal address**
  - a clear opt-out that works for **at least 30 days** after sending
  - honour opt-outs within **10 business days**
  - no fee or extra information required to opt out
  - never sell or transfer opted-out addresses
  - you stay liable for vendors and agencies who send for you
- **Penalty:** up to about **$53,088 per violating email** under the January 2025 inflation adjustment. The FTC adjusts it each January; **verify the 2026 figure.** [K-med]
- **Aggravating factor relevant to your pipeline** (15 U.S.C. 7704(b)) [K-med]: sending an otherwise-unlawful commercial email is aggravated where addresses were
  - (i) harvested by automated means from sites that post a no-sharing notice, or
  - (ii) generated by "**combining names, letters, or numbers into numerous permutations**" (dictionary attacks).
  - Pattern-guessed addresses (as with the trykitt result) are not illegal on their own. But if any other CAN-SPAM requirement is missed, the guessing becomes an aggravating factor. Make every message fully compliant and record the address source.
- Note also that CAN-SPAM largely pre-empts state email laws except on falsity or deception. [K-med]

### 4.2 TCPA, TSR and telephone rules
- **TCPA (47 U.S.C. 227)** [K-high]
  - Calls or texts to **mobile numbers** using an autodialer or **artificial/prerecorded voice** need prior express consent; telemarketing needs **prior express written consent**.
  - It applies even when the mobile is used for business, and many vendor "direct dials" are mobiles.
  - Statutory damages: **$500 per violation, up to $1,500 if wilful**. Class actions are common.
- **AI voices:** the FCC's February 2024 Declaratory Ruling (FCC 24-17) treats AI-generated voices as "artificial" under the TCPA. [K-med]
- **Autodialer definition:** narrowed by *Facebook v. Duguid* (2021). [K-high]
- **2025 developments** [K-med]
  - The 11th Circuit vacated the FCC's "one-to-one consent" rule (*Insurance Marketing Coalition v. FCC*, Jan 2025).
  - The Supreme Court (*McLaughlin Chiropractic v. McKesson*, June 2025) held district courts are not bound by FCC interpretations of the TCPA, so outcomes may diverge by circuit.
- **Do-Not-Call:** National DNC protects residential subscribers; the FCC confirmed in 2023 that DNC protections cover texts. Courts split on business-use mobiles. [K-med]
- **State "mini-TCPAs":** e.g. Florida and Oklahoma use broader automated-dialing definitions. [K-med]
- **FTC Telemarketing Sales Rule:** B2B calls are mostly exempt, but a 2024 amendment extended the misrepresentation bans to B2B calls. [K-low]
- **Practical rule:** no AI or prerecorded voice and no cold SMS to US numbers. Only live manual calls to business landlines, after DNC and state-law checks.

### 4.3 State privacy and data-broker laws
- **CCPA/CPRA (California):** the B2B and employee exemptions **expired on 1 Jan 2023**, so B2B contact data of California residents is in scope. [K-high] That applies only if the business meets a threshold [K-med]:
  - gross revenue above about $26.6m (CPI-adjusted from $25m; verify)
  - **buys, sells or shares** personal information of 100,000+ consumers a year
  - 50%+ of revenue from selling or sharing personal information
  - A small consultancy is probably below these, but bulk-buying 100k+ Californian contacts could matter. [LAWYER]
- **Other comprehensive state laws** (roughly 19-20 states by 2026; e.g. Virginia, Colorado, Connecticut, Texas) generally **exclude** people acting in a commercial or employment context. B2B prospecting is largely out of scope, apart from California. [K-med]
- **Data brokers:** the California Delete Act created the CPPA's **DROP** platform, a single deletion request to all registered brokers. Consumer access is believed to have started 1 Jan 2026, with brokers processing from **1 Aug 2026**. [K-med]
  - Effect: vendor datasets for Californians will shrink and churn.
  - If the client ever **resells** contact data, it could itself become a data broker (also registries in Vermont, Texas, Oregon). [K-med]
- **Website chatbots and pixels:** California Invasion of Privacy Act (CIPA) "wiretap" class actions have targeted site chat widgets and trackers that share transcripts with third-party vendors. Disclose and get consent in the chat UI. [K-med]
- **Right of publicity:** people-data vendors (ZoomInfo among them, I believe) have faced class actions over using individuals' names to market subscriptions or free trials. Details unverified. [K-low]

---

## 5. India: DPDP Act 2023 and DPDP Rules 2025
Verify at meity.gov.in (Act text, Rules, notifications) and pib.gov.in press releases.

### Status [K-med]
- The Act (No. 22 of 2023) received assent in August 2023.
- The **DPDP Rules 2025 were notified in mid-November 2025** (around 13-14 Nov), with phased commencement:
  - Data Protection Board provisions: on notification
  - **Consent-manager provisions: about 12 months later** (around Nov 2026)
  - **Most substantive obligations about 18 months later** (around **May 2027**): notices, security safeguards, breach notification, retention or erasure, children's data, Significant Data Fiduciary duties
- I have a faint memory of reports that MeitY considered shortening this. **Unverified; check.** [K-low]

### Why it matters to this client
1. **Scope (s.3):** the Act covers processing of digital personal data **within India**, and its definition of Data Principal is not limited to Indian residents. So prospect data about UK, EU or US people that the client stores and processes in India looks in scope. [K-med] [LAWYER]
2. **Exemption s.17(1)(d):** covers personal data of non-residents processed **under a contract with a person outside India** by a person in India (the outsourcing exemption). [K-med]
   - It would cover the client doing lead generation **as a service for a UK customer**.
   - It does **not** obviously cover the client's **own** prospecting.
   - Even where it applies, security (s.8(5)) and some duties remain. [K-med]
3. **No legitimate-interest ground.** The lawful grounds are consent (s.6) or narrow "certain legitimate uses" (s.7), and none covers marketing. [K-high] Once the 18-month phase commences, prospect data in scope may need consent, which clashes with UK/EU legitimate-interest prospecting.
4. **Public-data exclusion (s.3(c)(ii)):** the Act does not apply to personal data made public by the Data Principal themselves, or by someone under a legal duty to publish it. [K-high that the clause exists; its application to self-published LinkedIn profiles vs. vendor-compiled or guessed emails is uncertain] [LAWYER]
5. **Penalties** (Schedule) [K-med]:
   - up to ₹250 crore for failing to take reasonable security safeguards
   - up to ₹200 crore for failing to notify breaches, or breaching children's-data duties
   - up to ₹50 crore residual
6. **Hiring and vendors** [K-med]:
   - Candidate and employee data (CVs, test submissions) is Indian personal data and in scope: give a notice, take consent for candidate processing, and note the employment "legitimate use" in s.7.
   - The firm (as Data Fiduciary) answers for its processors. You need written contracts with enrichment vendors, CRM and email tools, and the hire if they are a contractor.
   - Until the relevant DPDP provisions commence, the IT Act s.43A and SPDI Rules 2011 regime continues. [K-med]
7. **Options to discuss with counsel** [LAWYER]:
   - a UK entity as controller for UK prospecting
   - structuring lead-gen work as a service under contract
   - leaning on the public-data exclusion
   - consent-first designs (inbound) ahead of May 2027

---

## 6. Platform and data-sourcing risk

### 6.1 LinkedIn
- **User Agreement §8.2 ("Don'ts")** prohibits [K-high in substance; check current wording and effective date at linkedin.com/legal/user-agreement]:
  - developing, supporting or using software, scripts, robots, crawlers, or browser plug-ins and add-ons to scrape or copy the Services, including profiles
  - copying or distributing data from the Services without LinkedIn's consent, including via third parties
  - using bots or unauthorised automated methods to access the Services, add or download contacts, send messages, or drive inauthentic engagement
- LinkedIn's Help Center keeps a "prohibited software and extensions" page. Accounts using automation tools are restricted or banned. [K-med]
- **Weekly invitation limits** often quoted by practitioners (about 100-200) are unofficial folklore. [K-low]
- **The client's choice not to automate or scrape from its own account is correct.**

**Case law and enforcement**
- **hiQ v. LinkedIn** [K-med on details]
  - The 9th Circuit (2019; reaffirmed April 2022 after *Van Buren*) said scraping *public* pages probably isn't "without authorization" under the CFAA.
  - **But** in Nov 2022 the district court found hiQ **breached the User Agreement**, including through fake accounts.
  - The parties ended the case in **Dec 2022 with a consent judgment**: about **$500,000** payable by hiQ, a **permanent injunction** on scraping and fake accounts, and destruction of scraped data and derived models.
  - **The real lesson is contract and fake-account liability, not "scraping is legal".**
- **Meta v. Bright Data** (N.D. Cal., Jan 2024): logged-out scraping of public data was held outside Meta's terms, and Meta dropped the case. Logged-in scraping is a different matter. [K-med]
- **LinkedIn v. Proxycurl (Nubela)** [K-med]: LinkedIn announced the suit in **January 2025**, alleging hundreds of thousands of fake accounts used to scrape profiles. **Proxycurl reportedly shut down around July 2025.**
- **LinkedIn v. ProAPIs** (around Oct 2025, alleged fake-account scraping): **unverified.** [K-low]
- Reports that LinkedIn **removed the Apollo.io and Seamless.ai company pages** (around March 2025): **unverified.** [K-low]

**Implications for reqwatch**
- Job-posting data is mostly *company* data, so its GDPR exposure is low. Strip recruiter or poster names unless needed.
- LinkedIn job data bought from third-party scraper vendors (e.g. the harvestapi actor) carries **supply-chain risk**: the vendor can disappear, as Proxycurl did. It also carries provenance risk.
- Prefer licensed or official sources:
  - Adzuna API (official, under its terms)
  - company careers pages via ATS public job-board endpoints such as Greenhouse and Lever (public by design; check each one's terms)
  - Companies House API for UK company facts (director names in it are personal data)

### 6.2 People-data vendors (Apollo, ZoomInfo and similar)
- **Where the data comes from** (vendor descriptions; marketing, not independent evidence) [K-med]:
  - "contributory networks", where users who connect their mailbox or calendar share contacts and email-signature data
  - public web crawling
  - third-party data partners
  - human research teams (ZoomInfo)
  - Under GDPR this raises questions about **transparency (Art 14)** and **lawful basis at the vendor**, which buyers inherit.
- **Incidents:** Apollo disclosed a **2018 breach** in which reportedly about **200 million contact records** were taken. [K-med] I know of no major 2025-26 Apollo or ZoomInfo regulatory fines, but **unverified; search before relying on this.**
- **Due-diligence questions for any vendor or treg route** (`treg.companies.enrich` picks among about 24 providers, so **each underlying provider is a separate source to document**):
  - source and collection method per field
  - whether Art 14 notices were given
  - EU/UK representative and DPA
  - transfer mechanism to India
  - suppression and erasure propagation
  - refresh date
  - whether any data came from LinkedIn scraping or extensions (the Kaspr risk)
  - **record `source_provider` and `retrieved_at` per field**

---

## 7. Mailbox-provider rules
Verify at support.google.com (Email sender guidelines and FAQ), senders.yahooinc.com, and techcommunity.microsoft.com (Outlook high-volume sender post).

| Provider | Applies to | Requirements | Confidence |
|---|---|---|---|
| **Gmail** (announced Oct 2023; enforcement phased from **1 Feb 2024**; one-click unsubscribe from about June 2024; stricter rejection of non-compliant mail ramped up from about **Nov 2025**) | **All senders:** SPF *or* DKIM, valid forward/reverse DNS (PTR), TLS, RFC 5322 format, spam rate under 0.3%. **Bulk senders** (close to **5,000+ messages a day to personal Gmail accounts**; bulk status is permanent): SPF **and** DKIM, **DMARC (at least p=none)**, From-domain alignment, **one-click unsubscribe (RFC 8058)** for marketing mail with requests honoured within **2 days** | Spam rate in Postmaster Tools: aim **below 0.1%**, never reach **0.3%** | [K-high]; Nov 2025 ramp [K-med] |
| **Yahoo** (Feb 2024) | Bulk senders | Broadly the same: SPF+DKIM, DMARC p=none minimum, alignment, one-click unsubscribe honoured within 2 days, complaints below 0.3% | [K-med] |
| **Microsoft Outlook.com consumer** (outlook.com, hotmail.com, live.com); announced Apr 2025, **enforced from 5 May 2025** | Domains sending **5,000+ emails a day** to those addresses | SPF pass, DKIM pass, DMARC at least p=none aligned with SPF or DKIM. Non-compliant mail is rejected with **"550 5.7.515 Access denied, sending domain … does not meet the required authentication level"** (Microsoft first said junk-foldering, later rejection). Also recommended: working unsubscribe, list hygiene, valid From/Reply-To | [K-med] |

Practical notes:
- B2B prospects mostly sit on Google Workspace or Microsoft 365 tenants. The formal thresholds target consumer mailboxes, but the same filtering signals (authentication, complaints, bounces) decide inbox placement. **Treat the bulk-sender rules as the baseline for all sending.**
- Practitioner conventions, not rules [K-med]:
  - hard-bounce rate under about 2%
  - low daily volume per mailbox (often 30-50)
  - warmed secondary domains clearly branded as the company
  - immediate handling of replies and unsubscribes
- Your bounced-"verified" lesson ties directly into deliverability: verify every address, treat catch-all domains cautiously, and stop sending to a domain after a hard bounce.

---

## 8. Compliance checklist for the lead-generation hire (operating rules)

**A. Before any list is built**
1. Keep a written **LIA** per campaign type (UK/EU) and review it yearly.
2. Keep a **ROPA** entry and a short **DPIA screening** note (invisible processing, AI profiling).
3. Keep a **public privacy notice** (prospect section): sources, purposes, legitimate interest, retention, rights, contact, UK/EU representative if appointed.
4. Run **vendor due diligence** for every data source, including each provider behind any treg routed endpoint. Keep a file per vendor: provenance, Art 14 practice, DPA, transfer mechanism, no LinkedIn-extension or scraped data, erasure propagation.
5. Build a **jurisdiction rules table** into the pipeline as data:
   - `UK-corporate: email OK`
   - `UK-sole-trader/partnership: no email`
   - `DE: no cold email`
   - `FR: email only if role-relevant`
   - `other EU: blocked until verified`
   - `US: CAN-SPAM`
   - `CA (Canada): no cold email`
   - Classify UK company type (Ltd/LLP vs sole trader) from Companies House where possible. If unknown, **don't email**.
6. **Suppression list** (hashed emails and domains) shared across every tool, domain and mailbox, and checked before every send.

**B. Data handling**

7. Store **provenance per field**: source provider, retrieval timestamp, verification result, how the email was derived (vendor vs pattern-guessed).
8. **Minimise**: name, role, work email, company, and the business signal (e.g. job-ad age). No personal mobiles, home addresses or social-media personal content.
9. **Verify every email** before first send and cross-check providers; never send to unverified addresses.
10. **Retention**: delete non-responders after a set period (e.g. 6-12 months; justify it in the LIA). Keep the suppression entry indefinitely.
11. **Security**: least-privilege access to the CRM and enrichment keys; no exports to personal drives; DPAs with all SaaS tools, including LLM APIs used to research or draft.

**C. Every outbound email**

12. Real sender identity, company name, **physical postal address** (CAN-SPAM), and a working **reply-to**.
13. A short **Art 14 notice** in the first email: who we are, why you (role relevance), where we got your details, legitimate interest, how to object, a link to the privacy notice.
14. A clear **opt-out** in every email: one-click unsubscribe header plus "reply 'no' to opt out". Honour it **immediately** (CAN-SPAM's 10 business days is the outer limit).
15. Truthful subject lines. No fake "Re:" or "Fwd:", no false personalisation, no claims about the prospect that AI made up. **A human reviews AI-drafted copy.**
16. Low volume per mailbox; stop if spam complaints approach **0.1%** or hard bounces exceed about 2%.

**D. Channels**

17. **LinkedIn:** manual activity only. No automation tools, browser extensions or scrapers on any company or personal account. Don't buy LinkedIn-scraped people data.
18. **Phone:** UK numbers screened against TPS/CTPS before calling; US numbers against DNC plus state rules; Germany only with documented presumed consent [LAWYER]. **No AI, prerecorded or automated voice outreach, and no cold SMS, anywhere.**
19. **AI agents and chatbots:** tell people up front that they are dealing with AI (EU AI Act Art 50 from 2 Aug 2026; good practice elsewhere). Never impersonate a named human. Get consent and give notice before chat transcripts are stored by third-party vendors (CIPA risk).

**E. Responding to people**

20. "Where did you get my data?", "delete me", or "what do you hold?" means **log it, suppress, and answer within one month** (UK/EU), giving the source.
21. Complaints: acknowledge within 30 days (UK DUAA complaints duty; check commencement).

**F. India and governance**

22. Track **DPDP readiness for about May 2027** with Indian counsel: notices, consent design, security, breach response, processor contracts. Candidate and employee data handled under a DPDP-ready notice now.
23. **Monthly compliance log:** sends, bounces, complaints, opt-outs, DSARs, vendor changes. **Quarterly** re-check of any rule marked unverified in this brief.

---

## 9. Interview questions that test compliance knowledge (with what a good answer looks like)

1. **"We'll email 300 Heads of Engineering at UK product companies. What makes that lawful?"**
   *Good answer:*
   - PECR: corporate subscribers need no consent; identify sole traders and partnerships and exclude them.
   - UK GDPR: legitimate interests backed by a written LIA; role relevance; Art 14 notice by the first email; opt-out and suppression; sender identity not concealed; minimal data; set retention.
   - *Red flags:* "B2B is exempt from GDPR", "it's public data so it's fine", "just add an unsubscribe link".
2. **"A third of the list is in Germany and a third in France. What changes?"**
   *Good answer:*
   - Germany: UWG §7 needs prior express consent for advertising email even B2B. Exclude them, or use non-email channels; mentions the risk of cease-and-desist letters (Abmahnung).
   - France: allowed if the message relates to the recipient's role, with opt-out.
   - Other EU states: verify one by one.
3. **"A vendor says its data is 'GDPR compliant'. What do you ask?"**
   *Good answer:*
   - collection method per field; whether Art 14 notices were given; refresh dates
   - any LinkedIn extension or scraped origin; mentions Kaspr or a similar enforcement case
   - DPA and transfer mechanism to India; erasure propagation
   - a sample audit
   - does not rely on contract warranties alone (ICO due-diligence expectation)
4. **"Provider A's 'verified' email bounced; provider B's pattern-guessed email was live. How do you design the pipeline?"**
   *Good answer:*
   - waterfall plus cross-provider checks; SMTP verification; catch-all handling; bounce thresholds
   - provenance per field
   - knows that permutation-generated addresses are a CAN-SPAM aggravating factor if any other violation exists, so every message must be fully compliant
   - still needs a lawful basis and Art 14 notice in the UK/EU
5. **"A prospect replies: 'How did you get my email? Delete it.'"**
   *Good answer:*
   - suppress immediately everywhere
   - treat it as an objection and erasure or access request; reply within one month giving the source
   - keep only a hashed suppression record; log it
   - never argue or keep sending
6. **"Why not run a cloud LinkedIn automation tool on a burner account?"**
   *Good answer:*
   - breaches LinkedIn UA §8.2; fake or burner accounts were central to the hiQ consent judgment and the Proxycurl suit
   - account bans; the data's GDPR problems
   - alternatives: manual Sales Navigator use, content, events, warm intros
7. **"Let's have an AI voice agent call US CTOs on the mobile numbers Apollo gives us."**
   *Good answer:*
   - TCPA: AI voice is "artificial" (FCC 2024), so prior express written consent is needed for telemarketing to mobiles
   - $500-$1,500 per call; state mini-TCPAs; DNC
   - answer: no. Live manual calls to business lines only, after screening.
   - UK equivalent: PECR reg 19 consent for automated calls.
8. **"We're an Indian company prospecting in the UK. Which laws apply to us?"**
   *Good answer:*
   - UK GDPR and PECR via targeting (Art 3(2)); possible Art 27 representative
   - India's DPDPA applies to processing in India; s.17(1)(d) covers only processing under contract with a foreign party
   - DPDPA has no legitimate-interest ground; mentions the public-data exclusion
   - Rules phased, main duties around May 2027; get counsel
   - a strong candidate flags the UK/EU-vs-India tension unprompted
9. **"What do Gmail, Yahoo and Outlook require of senders?"**
   *Good answer:*
   - SPF, DKIM, DMARC (at least p=none) with alignment, PTR, TLS
   - one-click unsubscribe for bulk senders, honoured within 2 days
   - Gmail spam rate target under 0.1%, hard ceiling 0.3%
   - Outlook.com: 5,000+/day enforcement since May 2025 with 550 5.7.515 rejections
   - monitors with Postmaster Tools or SNDS
10. **"Should the AI chat assistant on our site, or an AI SDR, say it's an AI?"**
    *Good answer:*
    - yes: EU AI Act Art 50(1) from 2 Aug 2026 (provider duty, and we would be the provider if we build it); good practice in the UK and US
    - never pose as a named human; human review of AI-written outreach; no fabricated personalisation
    - consent and notice for stored chat transcripts (CIPA)
11. **"How long do we keep people who never replied?"**
    *Good answer:*
    - a defined, justified period (e.g. 6-12 months), then delete, keeping the suppression entry
    - knows the CNIL's roughly 3-year prospect reference and that Kaspr's 5-year renewal was criticised
12. **"Write the compliance footer or notice for our first-touch email."**
    *Good answer includes:*
    - who we are and our postal address
    - why the person was contacted (role relevance)
    - data source
    - lawful basis (legitimate interest)
    - one-line opt-out and a link to the privacy notice
    - kept short and human
13. **"What records would prove we're compliant if the ICO asked?"**
    *Good answer:* LIA(s), ROPA, DPIA screening, vendor due-diligence file, per-record provenance, suppression list, opt-out and DSAR log, TPS/CTPS screening logs, email-authentication configuration.
14. **"What changed with the UK Data (Use and Access) Act 2025?"**
    *Good answer:*
    - PECR fines raised to GDPR level (about £17.5m / 4%)
    - direct marketing named as a possible legitimate interest, but the balancing test still applies; not a "recognised legitimate interest"
    - complaints-handling duty; cookie exemptions
    - knows it commenced in stages, and that they would check dates
    - *Red flag:* "DUAA made B2B email consent-free and risk-free."

**Scoring:** look for (a) channel-by-country precision, (b) knowing where uncertainty lies and when to escalate to a lawyer, (c) building compliance into data structures, not slogans.

---

## 10. Compliance add-on for the practical hiring exercise (about 45 minutes)

**Give the candidate:**
- a 20-row CSV with these fields: name, title, company, legal form (Ltd / sole trader / LLP / GmbH / SAS / Inc), country / US state, email, `email_origin` (vendor-verified / pattern-guessed / unknown), phone type (mobile / landline), `data_source` (vendor / Companies House / LinkedIn-extension export / conference attendee list / job-ad signal)
- one vendor's marketing claim that its data is "100% GDPR compliant"

**Tasks:**
1. Label each row with the allowed channel(s) and the reason, plus required actions (Art 14 notice, TPS/CTPS screening, exclude).
2. Flag rows to drop: German emails, UK sole traders, LinkedIn-extension exports, unverified emails, US mobiles for calls.
3. Draft the first-touch email footer or notice.
4. Write 8 due-diligence questions for the vendor.
5. Propose the provenance and suppression fields to add to the treg enrichment chain output, so that compliance travels with each record.

**Pass bar:**
- no German or sole-trader emails
- recognises the Kaspr-type risk in the LinkedIn-extension rows
- CAN-SPAM postal address and opt-out present
- Art 14 elements present
- escalates at least two genuinely uncertain items to a lawyer (e.g. LinkedIn DMs to sole traders; DPDPA scope)

---

## 11. Items to confirm with a lawyer (and to re-verify with live sources)

- DUAA commencement: exact SI and dates for the PECR fine increase, the Art 6 direct-marketing example, and the complaints duty.
- Whether the client needs a **UK Art 27** and/or **EU Art 27 representative**, and an ICO fee.
- PECR treatment of **LinkedIn / social DMs** to sole traders and partnerships.
- B2B email rules country by country beyond Germany and France.
- German B2B phone outreach (presumed consent).
- **DPDPA:** whether the client's own prospecting of foreign people is in scope; how far the s.3(c)(ii) public-data exclusion reaches; any change to the 18-month timeline; structuring options (UK entity, service contracts).
- **EU AI Act:** whether the Digital Omnibus changed Art 50 timing; provider-vs-deployer status for agents the client builds for customers.
- **CCPA:** applicability if the client buys 100k+ Californian contacts; current CAN-SPAM penalty figure.
- Current status of LinkedIn litigation (Proxycurl, the reported ProAPIs case); any 2025-26 regulatory actions against Apollo, ZoomInfo or similar vendors.


---

## Fact-checker's notes on this report

- This fact-check could not run: the shared WebSearch budget (200 per turn) was used up and WebFetch failed with ENOTFOUND (legislation.gov.uk). No claim was independently verified. Re-run with search budget (a follow-up message, or raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION).
- The report itself has no primary sources, so every claim is model knowledge. Its 'high confidence' tags overstate how much evidence there is.
- Time-sensitive items most likely to be stale by Oct 2026: DUAA commencement dates, Digital Omnibus changes to the AI Act timeline, the 2026 CAN-SPAM penalty figure, the DPDP phasing, the CCPA threshold, and new LinkedIn lawsuits.
- Omission: the ICO's updated direct marketing guidance after DUAA (and any new ICO B2B guidance) is not discussed.
- Omission: the EU Data Act and NIS2 are not covered (probably out of scope). The UK Online Safety Act is not relevant.

### Open questions raised by the researcher

- TOOLING GAP: this track could not run any web search (the workflow's shared 200-search budget was already used up) and WebFetch failed DNS resolution for every host. All claims come from model knowledge (cutoff about mid-2026) and need primary-source checking. The user can send a follow-up to re-run this track with search budget, or raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.
- DUAA 2025: the exact commencement regulations and dates for (a) PECR fines rising to UK GDPR level, (b) the Art 6 direct-marketing legitimate-interest example, (c) the complaints-handling duty, (d) cookie exemptions. My belief that most changes commenced around 5 Feb 2026 is low-confidence.
- Does an India-based firm systematically prospecting UK/EU business contacts fall under UK/EU GDPR Art 3(2)? If so, must it appoint UK and EU Article 27 representatives and pay an ICO data protection fee? (Lawyer.)
- Does PECR's 'electronic mail' definition cover LinkedIn InMail or other social DMs to UK sole traders and partnerships, so that consent is needed?
- B2B cold-email rules by country beyond Germany and France (Austria, Italy, Spain, Netherlands, Poland, Nordics, Ireland, Belgium): consent or opt-out for legal persons and employees.
- EDPB Guidelines 1/2024 on legitimate interest: has a final version been adopted, and what does it say about B2B direct marketing?
- EU AI Act Digital Omnibus: was it adopted by Oct 2026, and did it change Art 50 timing (especially the 50(2) marking grace period) or the Art 4 AI-literacy duty? Is the client a 'provider' when it builds agents for customers?
- DPDP: is the 18-month commencement still about May 2027, or did MeitY shorten it? Is the client's own processing in India of foreign prospects' data in scope? Is s.17(1)(d) limited to processing under foreign contracts? How far does the s.3(c)(ii) public-data exclusion reach (self-published LinkedIn profiles vs vendor-compiled or pattern-guessed emails)? (Indian counsel.)
- Current CAN-SPAM per-email civil penalty after the January 2026 inflation adjustment.
- Status of LinkedIn enforcement: Proxycurl shutdown date and terms; whether LinkedIn sued ProAPIs (around Oct 2025); whether LinkedIn removed Apollo.io and Seamless.ai company pages (around March 2025).
- Any 2025-2026 regulatory actions, fines or breaches involving Apollo, ZoomInfo, Lusha, Cognism or other people-data vendors, and each vendor's current GDPR Art 14 notification practice.
- Whether the third-party LinkedIn-jobs scraper the client used (harvestapi via a vendor) faces LinkedIn legal action, and which licensed alternatives (Adzuna API terms, Greenhouse/Lever public job-board API terms) allow commercial reuse for signal detection.
- Client context needed: expected monthly send volumes; whether they will use phone or SMS at all; whether they plan a UK legal entity; whether they will do lead generation as a service for clients (which changes DPDP s.17(1)(d) and controller/processor roles); whether Canada (CASL) or other markets are in scope.
- Whether Gmail's one-click-unsubscribe and bulk-sender rules formally apply to low-volume 1:1 cold outreach to Google Workspace (rather than personal Gmail) recipients. In practice, treat them as the baseline anyway.
