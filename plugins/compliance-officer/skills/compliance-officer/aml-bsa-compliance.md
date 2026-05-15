# Anti-Money Laundering (AML) and Bank Secrecy Act (BSA) Compliance

Guide to AML/BSA compliance for broker-dealers and voluntary implementation for investment advisers.

## Regulatory Framework

### Applicability

**Required:**
- Broker-dealers (SEC Rule 17a-8, FINRA Rule 3310)
- Mutual funds
- Banks and credit unions
- Money services businesses

**Not Required (but often implemented voluntarily):**
- SEC-registered investment advisers
- State-registered investment advisers

**Why RIAs Implement Voluntarily:**
- Customer due diligence best practice
- Preparation for potential future requirements
- Red flag detection
- Reputational risk management
- Custodian requirements may impose obligations

### Legal Authority

**Bank Secrecy Act (1970):**
- Requires financial institutions to assist government in detecting money laundering
- Recordkeeping and reporting requirements

**USA PATRIOT Act (2001):**
- Enhanced due diligence
- Beneficial ownership identification
- Information sharing
- Prohibitions on foreign shell banks

**FinCEN (Financial Crimes Enforcement Network):**
- Treasury Department bureau
- Administers BSA
- Issues regulations and guidance

## AML Program Requirements (Broker-Dealers)

### Four Pillars

**1. Written Policies and Procedures**
- Risk-based and reasonably designed
- Detect and report suspicious activity
- Comply with BSA requirements

**2. Designated AML Compliance Officer**
- Individual responsible for program
- Adequate authority and resources
- Reports to senior management

**3. Ongoing Training**
- All appropriate personnel
- Relevant to their functions
- At least annually

**4. Independent Testing**
- Audit of AML program
- At least every 12 months
- By independent party (outside firm or internal audit not involved in AML function)

### Written AML Program Components

**Customer Identification Program (CIP):**
- Verify identity of customers
- Procedures to obtain and verify information
- Recordkeeping

**Customer Due Diligence (CDD):**
- Understand nature and purpose of customer relationships
- Ongoing monitoring
- Risk-based approach

**Suspicious Activity Monitoring:**
- Surveillance for red flags
- Investigation procedures
- SAR filing when appropriate

**Currency Transaction Reporting:**
- Identify transactions >$10,000 in currency
- File CTRs

**OFAC Screening:**
- Screen against Specially Designated Nationals (SDN) list
- Block transactions if match
- Report to OFAC

**Information Sharing:**
- 314(a) information requests from government
- 314(b) voluntary information sharing with other institutions

**Recordkeeping:**
- Transaction records
- CIP records
- SARs and supporting documentation
- Training records

## Customer Identification Program (CIP)

### Required Information

**For Individuals:**
- Name
- Date of birth
- Address (residential or business)
- Identification number:
  - U.S. person: SSN
  - Non-U.S. person: Passport number and country of issuance, or other government-issued ID

**For Legal Entities (Corporations, Partnerships, Trusts):**
- Name
- Address (principal place of business)
- Identification number:
  - U.S. entity: EIN
  - Non-U.S. entity: EIN, passport, or other government-issued ID

### Verification Methods

**Documentary Verification:**
- Unexpired government-issued ID with photo
- Driver's license
- Passport
- State ID card

**Non-Documentary Verification (if cannot verify documentary):**
- Contact customer
- Check references
- Credit report
- Public databases

**Timeframe:**
- Verify identity within reasonable time before or after account opening
- Generally: Before conducting transactions or within first 30-60 days

**Example CIP Process:**
```
New Client: John Smith

Step 1: Obtain Information
- Full name: John Smith
- DOB: 1/15/1980
- Address: 123 Main St, Anytown, CA 90210
- SSN: 123-45-6789

Step 2: Verify Identity
- Request copy of driver's license
- Verify SSN against IRS database or credit report
- Confirm address matches

Step 3: Record
- Maintain copy of driver's license
- Document verification method
- Record date of verification

Step 4: Ongoing
- Update if address or name changes
- Re-verify if suspicious activity
```

### Reliance on Third Parties

**May rely on another financial institution's CIP if:**
- Written agreement in place
- Reasonable belief that other institution has complied with CIP
- Other institution certifies compliance

**Common Scenario:**
- Broker-dealer relies on clearing firm's CIP
- RIA relies on custodian's CIP (if agreement in place)

## Customer Due Diligence (CDD)

### CDD Rule (Effective May 2018)

**Four Core Requirements:**

**1. Customer Identification and Verification (CIP)**

**2. Beneficial Ownership Identification (for legal entities)**
- Identify individuals who own 25%+ of legal entity customer
- Identify one individual with control over legal entity

**3. Understand Nature and Purpose of Customer Relationships**
- Obtain information to develop customer risk profile

**4. Ongoing Monitoring**
- Monitor transactions and update customer information

### Beneficial Ownership

**Applies to:**
- Legal entity customers (corporations, LLCs, partnerships)
- Excludes: Publicly traded companies, government entities, certain regulated entities

**Certification Form:**
- Customer completes Beneficial Ownership Certification
- Identifies:
  - Ownership: Each individual owning 25%+ (directly or indirectly)
  - Control: One individual with significant control (CEO, CFO, managing member, etc.)

**Example:**
```
ABC LLC (new account)

Ownership:
- Jane Doe: 40% owner
- John Smith: 35% owner
- Bob Jones: 25% owner

All three must be identified and verified (≥25%)

Control:
- Jane Doe, Managing Member

Beneficial Owners: Jane Doe, John Smith, Bob Jones (all verified via CIP)
```

### Risk-Based Approach

**Customer Risk Factors:**
- Type of customer (individual, entity, foreign, domestic)
- Nature of business or occupation
- Geography (high-risk jurisdictions)
- Products and services used
- Transaction patterns

**Risk Categories:**

**Low Risk:**
- Domestic individual
- Standard investment account
- Predictable transaction pattern
- No high-risk factors

**Medium Risk:**
- Small business entity
- Use of multiple products
- Moderate transaction volume

**High Risk:**
- Foreign entity or individual
- High-risk jurisdiction (FATF list)
- Large cash transactions
- Complex entity structures
- Politically Exposed Persons (PEPs)
- Businesses involving high-risk industries (money services, precious metals, etc.)

**Enhanced Due Diligence (High Risk):**
- Obtain additional information
- More frequent monitoring
- Senior management approval
- Source of funds verification

## Suspicious Activity Reporting (SARs)

### When to File SAR

**Suspicious Activity Defined:**
- Transaction ≥$5,000 (aggregate) involving or aggregating funds or assets of at least $5,000
- **AND** any of the following:

**1. Involves funds from illegal activity**
- Proceeds of drug trafficking, fraud, theft, etc.

**2. Designed to evade BSA requirements**
- Structuring to avoid CTR reporting
- Breaking transactions into <$10,000 to avoid detection

**3. No business or lawful purpose**
- Transaction has no apparent economic rationale
- Customer cannot explain purpose

**4. Unusual complexity or patterns**
- Unusual use of account
- Rapid movement of funds
- Inconsistent with customer profile

### Red Flags

**Account Opening/Early Activity:**
- Provides false or suspicious information
- Reluctant to provide information required by CIP/CDD
- Opens account with large cash deposit
- Immediately wires funds out

**Transaction Patterns:**
- Rapid movement of funds in and out
- Transactions inconsistent with stated purpose
- Round-dollar transactions (exactly $50,000, $100,000)
- Deposits followed immediately by wire transfers
- Multiple accounts with similar beneficiaries

**Structuring:**
- Multiple transactions just under $10,000
- Pattern of deposits/withdrawals designed to avoid reporting
- Multiple locations, days, or accounts to break up transactions

**Account Behavior:**
- Customer exhibits unusual concern about reporting/recordkeeping
- Attempts to avoid contact with firm
- Transactions inconsistent with customer's business or occupation
- Unusual secrecy about account

**Third-Party Activity:**
- Third parties involved in transactions without apparent reason
- Authorized signer unrelated to customer
- Attorney or accountant deposits/withdraws on behalf of customer without explanation

### SAR Filing Process

**Investigation:**
1. Identify suspicious activity (automated monitoring, manual review, employee report)
2. Gather facts (transaction history, customer information, communications)
3. Analyze (compare to customer profile, assess red flags)
4. Determine if SAR filing warranted
5. Escalate to AML Compliance Officer

**Filing:**
- File FinCEN SAR electronically via BSA E-Filing System
- Deadline: **30 days from initial detection** (may extend to 60 days if need to identify suspect)
- No minimum dollar amount (if meets suspicious criteria)

**Contents:**
- Part I: Subject Information (who)
- Part II: Suspicious Activity (what)
- Part III: Information about Financial Institution
- Part IV: Filing Institution Contact
- Part V: Suspicious Activity Narrative

**Narrative (Part V):**
- Who, what, when, where, why
- Detailed description of suspicious activity
- Supporting facts
- Customer explanation (if any)
- Steps taken to investigate

**Example SAR Narrative:**
```
On 3/1/2025, customer John Smith (SSN 123-45-6789) deposited $9,800 in cash. On 3/2/2025, $9,500 cash. On 3/3/2025, $9,700 cash. Total: $29,000 over 3 days.

Customer's account had minimal activity previously (average balance $5,000, no cash deposits in past year). Customer's stated occupation is software engineer (salary $100,000/year).

When asked about source of funds, customer stated "savings" but could not provide details. The pattern of deposits just under $10,000 appears designed to avoid CTR reporting (structuring).

Account has been flagged for ongoing monitoring. No transactions have been blocked. This SAR is filed due to apparent structuring activity.
```

### After Filing SAR

**Confidentiality:**
- **Do NOT notify customer** that SAR was filed
- No disclosure to anyone except:
  - FinCEN
  - Law enforcement
  - Federal regulator
  - With court order (subpoena not sufficient)
- Violation: Criminal penalties

**Ongoing Monitoring:**
- Continue to monitor account
- File additional SARs if continued suspicious activity
- Consider account closure if risk too high

**Account Closure:**
- May close account after SAR filing
- Not required to close
- If close, do not disclose SAR as reason (maintain confidentiality)

**Retaining SAR:**
- Keep copy of SAR and supporting documentation for **5 years**
- Do not keep in customer file (confidentiality)
- Maintain in separate secure location

## Currency Transaction Reports (CTRs)

### When to File CTR

**Threshold:** Transaction >$10,000 in currency (cash)

**Currency Defined:**
- U.S. or foreign coins and bills
- Cashier's checks, money orders, bank drafts <$10,000 (treated as cash if purchasing with cash)

**NOT currency:**
- Personal checks
- Wire transfers
- Credit card transactions

**Examples:**
```
✅ File CTR:
- Customer deposits $12,000 cash
- Customer withdraws $15,000 cash
- Customer deposits $7,000 cash and purchases $5,000 money order with cash (total $12,000 currency)

❌ Do NOT file CTR:
- Customer deposits $12,000 via wire transfer (not currency)
- Customer deposits $12,000 personal check (not currency)
- Customer deposits $8,000 cash (under $10,000)
```

### Aggregation

**Must aggregate multiple currency transactions in single day if:**
- Same customer
- Same day
- Total >$10,000

**Example:**
```
Customer deposits:
- $6,000 cash at 10:00 AM
- $5,500 cash at 2:00 PM
Total: $11,500 → File CTR (aggregated)
```

### Filing Deadline

**15 days** after transaction date

### CTR Contents

**Part I: Person(s) Involved in Transaction**
- Name, address, SSN/EIN, DOB, occupation
- Account number(s)
- Method of identity verification

**Part II: Amount and Type of Transaction**
- Cash in, cash out
- Amount
- Date

**Part III: Financial Institution

**Part IV: Account Information**

### Exemptions

**Certain customers may be exempt from CTR filing:**
- Other banks
- Government agencies
- Listed public companies
- Established customers (based on analysis, annual review)

**Exemption Process:**
- File FinCEN Form 110 (Designation of Exempt Person)
- Annual review
- Generally NOT applicable to broker-dealers or investment advisers

## OFAC Compliance

### Office of Foreign Assets Control (OFAC)

**Purpose:** Enforce economic sanctions against countries, entities, and individuals

**Sanctions Programs:**
- Country-based: Cuba, Iran, North Korea, Syria, Russia (sectoral)
- List-based: Specially Designated Nationals (SDN), Sectoral Sanctions Identifications List (SSI)

### Specially Designated Nationals (SDN) List

**Who:** Individuals and entities designated by OFAC
- Terrorists
- Drug traffickers
- Proliferators of weapons of mass destruction
- Other threats to national security

**Prohibition:**
- U.S. persons cannot transact with SDNs
- Must block assets
- Cannot open accounts or process transactions

### OFAC Screening

**When to Screen:**
- Account opening (new customers)
- Ongoing (existing customers against updated SDN list)
- Transactions (wires, trades)

**How to Screen:**
- Compare customer names against SDN list
- Use software tools (compliance systems have OFAC screening)
- Manual review of potential matches

**SDN List Updates:**
- OFAC updates list frequently
- Screen existing customers against updated list
- Recommended: Daily screening

**Match Evaluation:**
- **Exact match:** Block immediately, report to OFAC
- **Close match:** Investigate (compare address, DOB, other identifiers)
- **False positive:** Document investigation, proceed if not match

### Blocking and Reporting

**If SDN Match:**
1. **Block:** Freeze assets, reject transaction
2. **Do NOT notify customer** (tipping off)
3. **Report to OFAC:** Within 10 days
   - Online through OFAC portal
   - Provide details of blocked property/transaction
4. **Await OFAC guidance:** Do not release without OFAC authorization

**Example Scenario:**
```
Wire transfer request: John Smith to send $50,000 to Ali Hassan in Dubai

OFAC Screening: "Ali Hassan" appears on SDN list

Investigation:
- Compare DOB: Match
- Compare address: Dubai matches
- Conclusion: Likely SDN

Action:
- Reject wire transfer
- Block any assets in account
- File OFAC report within 10 days
- Do not notify customer
- Wait for OFAC guidance
```

### Penalties for OFAC Violations

**Civil:** Up to $250,000 per violation or 2× transaction amount

**Criminal:** Up to $1 million and 20 years imprisonment

## AML Training

### Requirements

**Who:** All relevant personnel
- Customer-facing employees
- Operations staff
- Compliance staff
- Management

**Frequency:** At least annually

**Content:**
- AML regulations (BSA, PATRIOT Act)
- Firm's AML program
- Red flags and suspicious activity
- SAR and CTR filing
- OFAC screening
- CIP/CDD procedures
- Reporting suspicious activity
- Confidentiality (SARs)
- Consequences of violations

**Documentation:**
- Training materials
- Attendance records
- Testing (if applicable)
- Retain for 5 years

**New Hire Training:**
- Within 30-60 days of hire
- Before customer contact

## Independent Testing

### Requirements

**Frequency:** At least every 12 months

**Scope:**
- Test AML program effectiveness
- Review policies and procedures
- Test implementation
- Identify deficiencies

**Independence:**
- **Outside firm:** Independent auditor, consultant
- **Internal audit:** If separate from AML function
- **NOT independent:** AML Compliance Officer testing own program

### Testing Areas

**CIP/CDD:**
- Are new accounts properly verified?
- Are beneficial owners identified for legal entities?
- Is customer information updated?

**Suspicious Activity Monitoring:**
- Are red flags identified?
- Are SARs filed when appropriate?
- Is SAR documentation adequate?

**OFAC Screening:**
- Is screening conducted at account opening?
- Is screening conducted against updated SDN list?
- Are matches investigated properly?

**Training:**
- Is training conducted annually?
- Is training appropriate for personnel?
- Are records maintained?

**Recordkeeping:**
- Are CIP records maintained 5 years?
- Are SARs and supporting docs maintained 5 years?
- Are CTRs filed timely?

### Testing Report

**Contents:**
- Executive summary
- Scope and methodology
- Findings (deficiencies and strengths)
- Recommendations
- Management response

**Example Finding:**
```
Finding: SAR Filing Timeliness
- Reviewed 25 SARs filed in 2024
- 5 SARs (20%) filed after 30-day deadline
- Causes: Staffing shortage, lack of calendar tracking

Recommendation:
- Implement calendar ticklers for SAR deadlines
- Assign backup AML staff for coverage during absences
- Consider automated SAR tracking software

Management Response:
- Agree with recommendation
- Implemented SAR tracking spreadsheet with alerts
- Hired additional compliance analyst
- Target completion: Q2 2025
```

## Recordkeeping Requirements

**Customer Identification Records:**
- Retain for **5 years** after account closure
- Name, address, DOB, ID number
- Copy of ID documents
- Verification method and date

**SARs:**
- Retain copy for **5 years** from filing date
- Supporting documentation
- Store separately from customer files (confidentiality)

**CTRs:**
- Retain copy for **5 years** from filing date

**Beneficial Ownership Certification:**
- Retain for **5 years** after account closure

**Training Records:**
- Retain for **5 years**
- Training materials, attendance, testing

**Independent Testing:**
- Retain for **5 years**
- Testing reports, workpapers

## Investment Adviser AML (Voluntary)

### Why Implement Even Though Not Required?

1. **Best Practice:** Enhanced due diligence reduces fraud risk
2. **Custodian Requirements:** Custodians may require CIP/CDD information
3. **Fraud Prevention:** Red flag detection protects firm and clients
4. **Regulatory Direction:** FinCEN has proposed AML requirements for RIAs
5. **Reputational Risk:** Involvement in money laundering harms reputation

### Recommended Components for RIAs

**Customer Identification:**
- Obtain and verify identity at account opening
- Use custodian's CIP if reliance agreement in place

**Due Diligence:**
- Understand client background, source of wealth
- Risk-based approach for high-risk clients

**Monitoring:**
- Watch for unusual transactions
- Red flag awareness

**OFAC Screening:**
- Screen clients at onboarding
- Screen wires and transactions

**No SAR/CTR Filing (unless voluntary):**
- RIAs not required to file SARs or CTRs
- May file voluntarily (FinCEN accepts)
- Refer suspicions to custodian or law enforcement

**Training:**
- Educate staff on red flags
- OFAC screening procedures

## Common AML Deficiencies

**1. Inadequate Risk Assessment**
- Not conducting firm-wide AML risk assessment
- Solution: Annual risk assessment based on products, customers, geography

**2. Ineffective SAR Monitoring**
- Not identifying suspicious activity
- Delays in SAR filing
- Solution: Automated monitoring, manual reviews, timely investigations

**3. OFAC Screening Gaps**
- Not screening existing customers against updated SDN list
- Solution: Daily OFAC screening of all customers

**4. Incomplete CIP**
- Missing information or verification
- Solution: Checklist for account opening, compliance review before activating account

**5. Beneficial Ownership Not Obtained**
- Legal entity accounts opened without beneficial ownership certification
- Solution: Require certification before account opening

**6. Training Deficiencies**
- Annual training not conducted
- Training not tailored to firm's business
- Solution: Calendar reminder, customize training to firm's risks

**7. No Independent Testing**
- Testing not conducted annually
- Testing not independent
- Solution: Engage outside firm or internal audit, calendar annual testing

## Resources

**FinCEN:**
- SAR Filing: https://bsaefiling.fincen.treas.gov
- OFAC SDN List: https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists

**FINRA:**
- Rule 3310 (AML Program): https://www.finra.org/rules-guidance/rulebooks/finra-rules/3310
- AML Template: https://www.finra.org/rules-guidance/guidance/small-firm-aml-template

**SEC:**
- IA AML FAQ: https://www.sec.gov/investment/im-guidance-2015-01

**Industry Resources:**
- ACAMS (Association of Certified Anti-Money Laundering Specialists)
- AML training courses and certifications

---

**AML/BSA compliance is critical for broker-dealers and a best practice for investment advisers. Implement strong CIP, monitor for suspicious activity, screen OFAC, file SARs/CTRs timely, train staff, and conduct annual independent testing.**
