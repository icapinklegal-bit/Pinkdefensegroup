from mk import P
D = 'theft-property-crimes'; F = 'theft-property-crimes/fraud-forgery'; W = 'white-collar-crimes'
def S(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{D}/{slug}', title, desc, body, levels, faq, cat=D, **kw)
def FF(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{F}/{slug}', title, desc, body, levels, faq, cat=D, **kw)
def WC(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{W}/{slug}', title, desc, body, levels, faq, cat=W, **kw)

THEFT = [('Less than $100', 'C'), ('$100 to less than $750', 'B'), ('$750 to less than $2,500', 'A'), ('$2,500 to less than $30,000', 'SJF'), ('$30,000 to less than $150,000', 'F3'), ('$150,000 to less than $300,000', 'F2'), ('$300,000 or more', 'F1')]

PAGES = [
P(D, 'Theft & Property Crimes', 'Houston and Fort Bend County theft lawyer: shoplifting, burglary, auto theft, fraud, forgery and embezzlement defense.', hub=True, cat=D,
  h1='Houston & Fort Bend Theft & Property Crimes Lawyer', hub_label='Theft & Property Topics', body="""
Theft is considered a crime of "moral turpitude," which means even a misdemeanor conviction can cost someone a job, a professional license, or an immigration benefit. Employers and landlords treat theft convictions as red flags for honesty.

Texas consolidates most property offenses into a single theft statute, Penal Code § 31.03, and grades the offense mainly by the value of the property. Prior theft convictions and certain victims, such as elderly people, can raise the level.

Many first-time theft cases in Harris and Fort Bend Counties qualify for pretrial intervention, which can lead to dismissal and expunction. We also evaluate value, ownership, and intent defenses and, where appropriate, restitution-based resolutions.
""", levels=THEFT),
S('shoplifting', 'Shoplifting', 'Shoplifting charges at Houston-area stores and malls: penalties, civil demand letters and diversion.', """
Shoplifting is charged as theft, and the value of the merchandise determines the level. Most cases involve items under $750, a Class B or Class C misdemeanor, but a theft conviction still has serious long-term consequences.

Retailers at the Galleria, Memorial City, First Colony Mall and other locations often rely on loss-prevention video and staff testimony. Mistakes happen, especially with self-checkout lanes and items carried between departments. Retailers may also send a civil demand letter seeking money; that is separate from the criminal case. Diversion programs are often available for first-time cases.
""", THEFT[:4]),
S('self-checkout-theft', 'Self-Checkout Theft', 'Self-checkout theft accusations in Houston and Fort Bend County: intent and defenses.', """
Self-checkout lanes have produced a wave of theft accusations involving items that did not scan, were scanned at the wrong price, or were left in a cart. Theft requires intent to deprive the owner of property; an honest mistake with a scanner is not a crime.

We obtain the transaction log, store video, and receipts to show what actually happened. Many of these cases are good candidates for dismissal.
"""),
S('cite-and-release-theft-tickets', 'Cite and Release for Theft', 'Theft citations instead of arrest in Texas: what a cite-and-release theft ticket means.', """
For some low-level theft offenses, Texas law allows officers to issue a citation instead of making an arrest, depending on local policy. A citation is still a criminal charge, and failing to appear can lead to a warrant.

Treat a theft citation as seriously as an arrest. We can often resolve these cases through dismissal or deferred disposition that keeps the record eligible for expunction.
"""),
S('burglary', 'Burglary', 'Burglary of a habitation, building and vehicle charges in Houston and Fort Bend County.', """
Burglary is entering a building or habitation without consent with intent to commit a felony, theft, or assault, or committing one of those offenses after entering. Burglary of a vehicle is a separate offense.

## Penalty Levels
Burglary of a building is a state jail felony; burglary of a habitation is a second-degree felony, and a first-degree felony if the intended offense was another felony other than theft. Burglary of a vehicle is a Class A misdemeanor, with enhancements for prior convictions.

Intent at the time of entry is often contested, as is identification from video or fingerprints. Our affiliated family firm has obtained dismissal of a combined burglary and family violence case.
""", [('Burglary of a vehicle', 'A'), ('Burglary of a building', 'SJF'), ('Burglary of a habitation', 'F2'), ('Habitation, intent to commit other felony', 'F1')]),
S('auto-theft', 'Auto Theft', 'Unauthorized use of a vehicle and auto theft charges in Texas.', """
Taking a vehicle can be charged as theft, based on the vehicle's value, or as unauthorized use of a motor vehicle, a state jail felony that does not require intent to permanently deprive the owner.

Many cases involve borrowed cars, disputes over ownership or payments, and rideshare or rental situations. Consent and ownership are frequently contested.
""", [('Unauthorized use of a vehicle', 'SJF')]),
S('receiving-stolen-property', 'Receiving Stolen Property', 'Possession of stolen property charges in Texas: knowledge and defenses.', """
Texas prosecutes receiving stolen property as theft. The State must prove you knew the property was stolen. Buying something at a low price or from an informal seller does not by itself prove knowledge.

Pawn shop, online marketplace, and resale cases often turn on what the buyer was told and what they reasonably believed.
""", THEFT[:5]),
S('employee-theft', 'Employee Theft', 'Employee theft and internal theft accusations in Houston businesses.', """
Employers often discover alleged employee theft through audits, inventory shrinkage, or video. Some confront the employee and request a written statement before calling police. Do not sign anything without legal advice.

Many workplace theft allegations are civil or contractual disputes over commissions, reimbursements, or authority. We push back on premature criminal referrals and, where appropriate, negotiate resolutions that avoid prosecution.
"""),
S('theft-by-check', 'Theft by Check', 'Theft by check and issuance of a bad check charges in Texas.', """
Writing a check that bounces can lead to two different charges. Issuance of a bad check is a Class C misdemeanor. Theft by check, which requires proof that the check was used to obtain property with intent to deprive, is graded by value like other theft.

The law presumes intent in certain circumstances, but that presumption can be rebutted. Many cases resolve through restitution and dismissal.
""", [('Issuance of a bad check', 'C')]),
S('theft-of-service', 'Theft of Service', 'Theft of service charges in Texas: unpaid services, rentals and contractors.', """
Theft of service involves obtaining services, such as hotel stays, restaurant meals, rentals, or contractor work, with intent to avoid payment. It is graded by value like theft.

Disputes over quality of work or billing are not crimes. We distinguish civil disagreements from criminal intent and seek dismissal where the facts support it.
""", THEFT[:5]),
S('credit-debit-card-abuse', 'Credit & Debit Card Abuse', 'Credit card abuse and fraudulent use of identifying information charges in Houston.', """
Credit or debit card abuse, such as using a card without the owner's consent, is a state jail felony. Fraudulent use or possession of identifying information is graded by the number of items involved and can reach a first-degree felony.

Many cases involve family members or roommates who believed they had permission. Video, IP and device data, and delivery records are central to the evidence.
""", [('Credit or debit card abuse', 'SJF')]),
S('criminal-mischief', 'Criminal Mischief', 'Criminal mischief and vandalism charges in Texas: penalties by damage amount.', """
Criminal mischief means intentionally or knowingly damaging, destroying, or tampering with someone else's property without consent. Like theft, it is graded by the amount of loss, from a Class C misdemeanor to a first-degree felony.

Many cases arise from heated disputes between partners or neighbors. Ownership, consent, and the actual cost of repair are often disputed.
""", THEFT[:5]),
S('criminal-trespass', 'Criminal Trespass', 'Criminal trespass charges in Houston and Fort Bend County: notice and defenses.', """
Criminal trespass is entering or remaining on property without consent after receiving notice that entry was forbidden. Notice can be oral or written, or given by fencing, signs, or purple paint marks. It is usually a Class B misdemeanor, and a Class A misdemeanor in a habitation or with a deadly weapon.

Lack of proper notice and a good-faith belief that you were allowed to be there are common defenses.
""", [('Standard', 'B'), ('Habitation, shelter center, or with a deadly weapon', 'A')]),
S('misapplication-of-fiduciary-property', 'Misapplication of Fiduciary Property', 'Misapplication of fiduciary property charges against trustees, agents and contractors in Texas.', """
A fiduciary, such as a trustee, executor, attorney-in-fact, or a contractor holding construction trust funds, can be charged with misapplying property in a way that risks loss to the owner. The offense is graded by value.

These cases often begin as family disputes over estates or as business disputes. Authorization, documentation, and good faith are central defenses.
""", THEFT[1:]),
S('sedd', 'Securing Execution of a Document by Deception', 'Securing execution of a document by deception charges in Texas.', """
This offense involves deceiving someone into signing or executing a document that affects property, services, or someone's financial interests. It is graded by the value involved.

Contract disputes are often recast as criminal deception. We examine what was represented, what the parties understood, and whether a civil remedy is the appropriate path.
"""),
P(F, 'Fraud & Forgery', 'Fraud and forgery defense in Houston and Fort Bend County: embezzlement, insurance fraud, forgery and tampering charges.', hub=True, cat=D, hub_label='Fraud & Forgery Topics', body="""
Fraud and forgery charges usually involve documents, financial records, and digital evidence, and they often follow months of investigation. Getting a lawyer involved before charges are filed can make the difference between a civil resolution and a criminal case.

See also our [White-Collar & Fraud](/white-collar-crimes/) practice for investigations involving businesses, securities, and federal agencies.
"""),
FF('embezzlement', 'Embezzlement', 'Embezzlement charges in Houston: theft by employees, officers and fiduciaries.', """
Texas prosecutes embezzlement as theft or misapplication of fiduciary property, graded by the total amount. Because separate takings can be aggregated into one charge, small amounts over time can become a serious felony.

We work with forensic accountants to test the State's calculations, identify authorized transactions, and evaluate restitution-based resolutions.
""", THEFT[3:]),
FF('forgery-of-a-financial-instrument', 'Forgery', 'Forgery of checks and financial instruments in Texas: penalties and defenses.', """
Forgery is altering, making, completing, or passing a writing with intent to defraud or harm. Forging a check or other financial instrument is a state jail felony; forging government records or money is more serious.

The State must prove intent to defraud and that you knew the document was forged. Passing a check someone else forged, without knowledge, is not forgery.
""", [('Forgery of a financial instrument', 'SJF')]),
FF('false-statement-to-obtain-credit', 'False Statement to Obtain Credit', 'False statement to obtain property or credit charges in Texas.', """
Knowingly making a materially false statement to obtain property or credit, including loans and mortgages, is graded by value. These cases frequently overlap with federal bank and mortgage fraud.

Loan applications are often completed by brokers or loan officers. Who prepared the information, and whether the statement was material to the lender's decision, are central questions.
""", THEFT[2:]),
FF('insurance-fraud', 'Insurance Fraud', 'Insurance fraud charges in Texas: auto, property and health claims.', """
Insurance fraud involves presenting a statement in support of a claim that the person knows is false and material. It is graded by the value of the claim.

Insurers' special investigation units often refer cases to prosecutors after denying a claim. Disagreements about the extent of damage or loss are not fraud. We examine the claim file and communications closely.
"""),
FF('online-impersonation', 'Online Impersonation', 'Online impersonation charges in Texas: fake profiles and messages.', """
Using another person's name or persona to create a web page or post messages on social media without consent, with intent to harm, defraud, intimidate, or threaten, is a third-degree felony. Sending messages that falsely appear to come from someone else is a lesser offense.

Attribution is the key issue: proving who actually created the account and sent the messages.
""", [('Creating a profile or posting as another person', 'F3')]),
FF('tampering-with-evidence', 'Tampering With Evidence', 'Tampering with or fabricating physical evidence charges in Texas.', """
Tampering with evidence means altering, destroying, or concealing something with intent to impair its availability as evidence, knowing an investigation is pending or in progress. It is generally a third-degree felony.

These charges are often added when someone discards an item during a police encounter. The State must prove the specific intent and knowledge required by the statute.
""", [('Tampering with physical evidence', 'F3')]),
FF('tampering-with-government-records', 'Tampering With Government Records', 'Tampering with a governmental record charges in Texas, including temporary tags.', """
Tampering with a governmental record includes making false entries in, altering, or using a false government record, such as a driver's license, temporary vehicle tag, or official document. Penalties range from a Class A misdemeanor to a felony depending on the record and intent.

Counterfeit temporary paper tags have been a particular enforcement focus in the Houston area.
"""),

P(W, 'White-Collar & Fraud Defense', 'Houston white-collar crime defense lawyer: fraud, embezzlement, securities, health care fraud, money laundering and federal investigations.', hub=True, cat=W, kind='criminal',
  h1='Houston White-Collar Crime Defense Lawyer', hub_label='White-Collar Topics', body="""
White-collar cases are won with documents, preparation, and early strategy. Many begin with a subpoena, a target letter, a search warrant, or an agent's unannounced visit. What you say and produce in those first days can shape everything that follows.

Ishmael G. A. Pink brings a combined litigation and transactional background to these cases. Having advised startups and privately held companies on SaaS agreements, B2B disputes, and securities matters, he understands how businesses actually operate, which is often the key to explaining conduct that investigators have misread.

## How We Help
- Respond to subpoenas, target letters, and agent contacts.
- Conduct internal reviews with forensic accountants.
- Present information to prosecutors before charges are filed.
- Defend state cases in Harris and Fort Bend Counties and federal cases in the Southern District of Texas.
- Coordinate parallel civil litigation and regulatory proceedings.
"""),
WC('securities-fraud', 'Securities Fraud', 'Securities fraud investigations and charges in Houston: state and federal defense.', """
Securities fraud can be charged under the Texas Securities Act and under federal law, and it often runs alongside SEC or Texas State Securities Board investigations. Issues include misrepresentations to investors, unregistered offerings, and acting as an unregistered dealer or advisor.

Startups and private companies are especially exposed when fundraising documents are informal. We analyze offering materials, investor communications, and the intent behind them, and we coordinate the criminal defense with any regulatory matter.
"""),
WC('health-care-fraud', 'Health Care Fraud', 'Health care and Medicaid fraud defense in Houston: billing, kickbacks and medical necessity.', """
Houston is a national focus for health care fraud enforcement. Cases involve billing for services not rendered, upcoding, medical necessity disputes, and kickback allegations under federal and Texas law.

Many cases rest on complex billing rules that honest providers struggle to apply. We work with billing and coding experts to show good faith and challenge the government's loss calculations.
"""),
WC('money-laundering', 'Money Laundering', 'Money laundering charges in Texas and federal court.', """
Money laundering involves knowingly conducting financial transactions with proceeds of criminal activity. Texas grades it by amount, from a state jail felony to a first-degree felony, and federal law imposes up to 20 years.

The government must prove knowledge that the funds came from crime. Business owners and family members are sometimes accused based on transactions they did not understand.
""", [('$2,500 to less than $30,000', 'SJF'), ('$30,000 to less than $150,000', 'F3'), ('$150,000 to less than $300,000', 'F2'), ('$300,000 or more', 'F1')]),
WC('wire-and-mail-fraud', 'Wire & Mail Fraud', 'Federal wire fraud and mail fraud defense in the Southern District of Texas.', """
Wire fraud and mail fraud are the federal government's most common fraud charges, covering any scheme to defraud that uses interstate wires or the mail. Each email or transfer can be a separate count, each carrying up to 20 years.

The core question is intent to defraud. Business failures, optimistic projections, and contract disputes are not crimes. We use the documents to tell the full story.
"""),
WC('bank-and-mortgage-fraud', 'Bank & Loan Fraud', 'Bank fraud, PPP loan fraud and mortgage fraud defense in Houston.', """
Bank and loan fraud investigations, including those involving pandemic-era PPP and EIDL loans, remain active. Federal bank fraud carries up to 30 years, and the statute of limitations can be long.

Many borrowers relied on preparers or lenders who completed applications for them. We examine who supplied the information, what the borrower understood, and how the funds were used.
"""),
]
