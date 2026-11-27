from mk import P
D = 'drug-charges'; M = 'marijuana-defense'
def S(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{D}/{slug}', title, desc, body, levels, faq, cat=D, **kw)
def MJ(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{M}/{slug}', title, desc, body, levels, faq, cat=M, **kw)

PG1 = [('Less than 1 gram', 'SJF'), ('1 to less than 4 grams', 'F3'), ('4 to less than 200 grams', 'F2'), ('200 to less than 400 grams', 'F1'), ('400 grams or more (10 to 99 years, fine up to $100,000)', 'F1')]
PG2 = [('Less than 1 gram', 'SJF'), ('1 to less than 4 grams', 'F3'), ('4 to less than 400 grams', 'F2'), ('400 grams or more (5 to 99 years, fine up to $50,000)', 'F1')]
PG3 = [('Less than 28 grams', 'A'), ('28 to less than 200 grams', 'F3'), ('200 to less than 400 grams', 'F2'), ('400 grams or more (5 to 99 years, fine up to $50,000)', 'F1')]
MJL = [('2 ounces or less', 'B'), ('More than 2 oz, up to 4 oz', 'A'), ('More than 4 oz, up to 5 lbs', 'SJF'), ('More than 5 lbs, up to 50 lbs', 'F3'), ('More than 50 lbs, up to 2,000 lbs', 'F2'), ('More than 2,000 lbs (5 to 99 years)', 'F1')]

PAGES = [
P(D, 'Drug Charges', 'Houston and Fort Bend County drug crime lawyer: possession, delivery, trafficking, fentanyl, cocaine, meth and prescription drug charges. Call (832) 979-0882.', hub=True, cat=D,
  h1='Houston & Fort Bend County Drug Crime Lawyer', hub_label='Drug Charge Topics', body="""
Texas prosecutes drug offenses under the Health and Safety Code, which sorts substances into penalty groups. The penalty depends on the group, the weight (including adulterants and dilutants), and whether the State alleges simple possession or intent to deliver. A small difference in weight can move a case from a state jail felony to a first-degree felony.

## Common Drug Charges in Houston
We defend possession of cocaine, methamphetamine, heroin, fentanyl, ecstasy, prescription pills and THC concentrates, as well as possession with intent to deliver, manufacture, trafficking and prescription fraud. Many cases arise from traffic stops on I-45, I-10, US-59/I-69 and Highway 6, from searches of apartments and vehicles, and from investigations by HPD's narcotics units, county task forces, and federal agencies.

## Programs That Can Protect Your Record
Harris and Fort Bend Counties offer pretrial intervention and specialty drug courts for eligible clients. Successful completion can lead to dismissal and, in many cases, expunction. Early representation improves the chance of being accepted.
"""),
S('texas-penalty-groups', 'Texas Drug Penalty Groups', 'How Texas drug penalty groups work: which drugs fall in Penalty Groups 1, 1-A, 1-B, 2, 2-A, 3 and 4.', """
Texas classifies controlled substances into penalty groups in Chapter 481 of the Health and Safety Code.

- **Penalty Group 1:** cocaine, methamphetamine, heroin, oxycodone, hydrocodone and other opioids.
- **Penalty Group 1-A:** LSD, measured in dosage units.
- **Penalty Group 1-B:** fentanyl and its analogues, created in 2023 with harsher delivery penalties.
- **Penalty Group 2:** ecstasy (MDMA), PCP, psilocybin mushrooms, amphetamine and THC concentrates such as vape oil and wax.
- **Penalty Group 2-A:** synthetic cannabinoids (K2, spice).
- **Penalty Group 3:** benzodiazepines such as Xanax and Valium, and certain other prescription drugs.
- **Penalty Group 4:** small amounts of certain opiates in compounds, such as some codeine cough syrups.

Marijuana is treated separately by weight. Knowing exactly which group the State alleges, and whether the lab confirmed it, is the first step in any drug defense.
"""),
S('possession-of-a-controlled-substance', 'Possession of a Controlled Substance', 'Possession of a controlled substance charges in Houston and Fort Bend County: penalty groups, weights and defenses.', """
Possession of a controlled substance means knowingly exercising care, custody, control or management over a drug listed in the Health and Safety Code. When drugs are found in a shared car or home, the State must show "affirmative links" connecting you to them, such as ownership, proximity, conduct, or statements. Presence alone is not enough.

The punishment depends on the penalty group and the aggregate weight, which includes any cutting agents. The table below shows the ranges for Penalty Group 1, the most common group in Houston felony drug cases.
""", PG1),
S('state-jail-felony-drug-charges', 'State Jail Felony Drug Charges', 'State jail felony drug possession in Texas: less than one gram, mandatory probation and diversion options.', """
Possessing less than one gram of a Penalty Group 1 drug, such as cocaine or methamphetamine, is a state jail felony. These "under a gram" cases make up a large share of felony dockets in Harris County.

For many first-time defendants, Texas law requires that the sentence be probated rather than served in a state jail. Some cases can be reduced to a Class A misdemeanor under Penal Code § 12.44. Pretrial intervention and drug court may lead to dismissal. Lab weight and trace-amount issues are also important: very small residue may not support prosecution at all.
""", [('Under 1 gram, Penalty Group 1', 'SJF'), ('If reduced under § 12.44(a)', 'A')]),
S('possession-of-cocaine', 'Possession of Cocaine', 'Cocaine possession charges in Houston and Fort Bend County: Penalty Group 1 weights, penalties and defenses.', """
Cocaine, including crack cocaine, is a Penalty Group 1 controlled substance. Possession of less than a gram is a state jail felony; larger amounts quickly become second- or first-degree felonies.

Common defenses include challenging the traffic stop or search, disputing knowing possession when the drugs were found in a shared space, and testing the lab's identification and weight. Residue in a pipe or baggie may be too small to test or prosecute.
""", PG1),
S('possession-of-methamphetamine', 'Possession of Methamphetamine', 'Methamphetamine possession charges in Harris and Fort Bend County: penalties and defenses.', """
Methamphetamine is a Penalty Group 1 drug. Because meth is often sold mixed with other substances, the aggregate weight used by the lab, which includes those mixtures, can push a charge into a higher category.

We examine the search, the chain of custody, and the lab's methods for weighing and identifying the substance. Clients struggling with addiction may qualify for drug court, which combines treatment with the chance of a dismissal.
""", PG1),
S('possession-of-heroin', 'Possession of Heroin', 'Heroin possession charges in Houston and Fort Bend County: penalties and treatment-based alternatives.', """
Heroin is a Penalty Group 1 controlled substance, carrying the same weight-based ranges as cocaine and methamphetamine. Heroin is also increasingly mixed with fentanyl, which can raise the stakes in delivery cases.

In addition to search and possession defenses, we explore treatment-based resolutions where appropriate. Texas's Good Samaritan law offers a limited defense to possession for someone who calls 911 for an overdose, subject to conditions.
""", PG1),
S('possession-of-fentanyl', 'Possession of Fentanyl', 'Fentanyl charges in Texas: Penalty Group 1-B, enhanced delivery penalties, and fentanyl-related murder charges.', """
In 2023, Texas moved fentanyl into its own Penalty Group 1-B and raised penalties for manufacturing and delivery. Possession of even small amounts is a felony. If fentanyl delivered by someone causes a death, prosecutors can now charge murder.

Many people charged with fentanyl offenses believed they had a different drug, such as a counterfeit pill sold as a prescription medication. Knowledge, identification, and causation are central issues. We retain toxicology and pharmacology experts when the facts require it.
"""),
S('opioid-possession', 'Opioid Possession', 'Defending possession of oxycodone, hydrocodone and other opioid charges in Houston.', """
Most prescription opioids, including oxycodone and hydrocodone, are Penalty Group 1 drugs, so possession without a valid prescription is charged the same way as cocaine or heroin. Pills are weighed in full, not by the amount of active ingredient, which can inflate the weight.

A valid prescription is a defense to possession of your own medication. We also examine whether pills were properly identified by laboratory testing rather than markings alone.
""", PG1),
S('possession-of-xanax', 'Possession of Xanax', 'Possession of Xanax (alprazolam) charges in Texas: Penalty Group 3 penalties and defenses.', """
Alprazolam, sold as Xanax, is a Penalty Group 3 substance. Possession of less than 28 grams, which includes the full weight of the pills, is a Class A misdemeanor. Larger amounts are felonies.

Counterfeit "Xanax" pills sometimes contain fentanyl or other substances, which can change the charge entirely. We review the lab results carefully and raise prescription and knowledge defenses where they apply.
""", PG3),
S('possession-of-adderall', 'Possession of Adderall', 'Possession of Adderall without a prescription in Houston and Fort Bend County: penalties and defenses.', """
Adderall contains amphetamine, which Texas classifies in Penalty Group 2. Possession of less than one gram, including the full pill weight, can be a state jail felony, and a handful of pills can exceed that threshold.

These cases often involve students and young professionals who never thought of a borrowed pill as a felony. Diversion programs are frequently available, and a valid prescription is a defense.
""", PG2),
S('possession-of-ecstasy', 'Possession of Ecstasy', 'Ecstasy and MDMA possession charges in Texas: Penalty Group 2 penalties and defenses.', """
MDMA, commonly called ecstasy or molly, is a Penalty Group 2 controlled substance. Possession of less than one gram is a state jail felony, and amounts from four to 400 grams are a second-degree felony.

Pills and powders sold as MDMA often contain other drugs. The State must prove what the substance actually was through laboratory testing. Arrests at concerts and festivals also raise questions about search procedures and consent.
""", PG2),
S('possession-of-mushrooms', 'Possession of Psilocybin Mushrooms', 'Psilocybin mushroom possession charges in Texas: weight issues and penalties.', """
Psilocybin and psilocin are Penalty Group 2 substances in Texas. Because the State often weighs the entire mushroom rather than the active compound, a modest amount of dried mushrooms can reach serious felony weight ranges.

Weight methodology is a key issue in these cases. We also challenge searches and knowledge, particularly with edibles or products whose contents were not clear.
""", PG2),
S('possession-of-synthetic-marijuana', 'Possession of Synthetic Marijuana', 'Synthetic marijuana (K2, spice) possession charges in Texas: Penalty Group 2-A.', """
Synthetic cannabinoids, often sold as K2 or spice, are in Penalty Group 2-A, which is punished by weight similar to marijuana: two ounces or less is a Class B misdemeanor, and larger quantities climb to felony levels.

Chemical formulas for these products change frequently, so the lab must confirm the specific compound is listed in the statute.
""", [('2 ounces or less', 'B'), ('More than 2 oz, up to 4 oz', 'A'), ('More than 4 oz, up to 5 lbs', 'SJF'), ('More than 5 lbs, up to 50 lbs', 'F3')]),
S('possession-of-a-dangerous-drug', 'Possession of a Dangerous Drug', 'Possession of a dangerous drug without a prescription in Texas: Class A misdemeanor charges and defenses.', """
"Dangerous drugs" are prescription medications that are not controlled substances, such as certain muscle relaxers, antidepressants, and testosterone in some forms. Possessing one without a valid prescription is generally a Class A misdemeanor under Health and Safety Code Chapter 483.

A prescription in your name, or a lawful reason for possession, is a defense. These cases are often good candidates for dismissal or diversion.
""", [('Possession without a prescription', 'A')]),
S('possession-of-drug-paraphernalia', 'Possession of Drug Paraphernalia', 'Drug paraphernalia charges in Houston: Class C possession, Class A delivery, and keeping a clean record.', """
Possession of drug paraphernalia, such as pipes, scales, or baggies intended for use with drugs, is a Class C misdemeanor punishable by a fine only. Delivering or selling paraphernalia is a Class A misdemeanor.

Even a Class C conviction creates a criminal record. Deferred disposition often allows the case to be dismissed and later expunged.
""", [('Possession', 'C'), ('Delivery or sale', 'A')]),
S('possession-in-a-drug-free-zone', 'Drug-Free Zone Enhancements', 'Drug-free zone enhancements in Texas: schools, youth centers and playgrounds.', """
Texas increases punishment for certain drug offenses committed within 1,000 feet of a school, or within 300 feet of a youth center, public pool, or video arcade, and on school buses. Depending on the offense, the enhancement can raise the offense level, increase minimum sentences, or double fines.

The State must prove the location and distance with competent evidence, and the enhancement must be properly pleaded. We frequently find measurement and mapping errors.
"""),
S('possession-with-intent-to-distribute', 'Possession With Intent to Deliver', 'Possession with intent to deliver charges in Harris and Fort Bend County: what the State must prove.', """
Texas charges possession with intent to deliver under the same statute as manufacture and delivery, with higher penalties than simple possession. Prosecutors usually try to prove intent through quantity, packaging, scales, cash, or text messages rather than any observed sale.

Each of those factors has innocent explanations. We challenge the inference of intent and push to reduce the charge to simple possession, which can make a significant difference in exposure.
""", [('Penalty Group 1, less than 1 gram', 'SJF'), ('Penalty Group 1, 1 to less than 4 grams', 'F2'), ('Penalty Group 1, 4 to less than 400 grams', 'F1'), ('Penalty Group 1, 400 grams or more (15 to 99 years)', 'F1')]),
S('drug-trafficking', 'Drug Trafficking', 'Drug trafficking and delivery defense in Houston: state and federal charges along the I-10 and US-59 corridors.', """
Houston's highways and port make it a focus of state and federal trafficking investigations. Large-quantity cases may be charged in state court as manufacture or delivery, or federally under 21 U.S.C. § 841 with mandatory minimum sentences.

These investigations often rely on wiretaps, confidential informants, controlled buys and vehicle searches. We challenge the legality of each technique, the credibility of informants, and the government's proof of knowledge, and we evaluate federal safety-valve and cooperation issues where relevant. See [Federal Crimes](/federal-crimes/).
"""),
S('prescription-drug-fraud', 'Prescription Drug Fraud', 'Prescription fraud charges in Texas: forged prescriptions, doctor shopping and pharmacy cases.', """
Obtaining a controlled substance by fraud, such as through a forged or altered prescription or misrepresentation to a doctor or pharmacy, is a felony in Texas. The level depends on the penalty group of the drug involved.

These cases are document-heavy and often involve pharmacy records and surveillance video. We examine whether the State can prove you knew the prescription was invalid and whether identification is reliable.
"""),
S('diversion-of-controlled-substance', 'Diversion of Controlled Substances', 'Diversion of controlled substances by healthcare professionals in Texas: criminal and licensing exposure.', """
Physicians, nurses, pharmacists, and other registrants can be charged when controlled substances are diverted from lawful medical use. These cases often arise from audits, DEA or state board investigations, or pharmacy inventory discrepancies.

Because licensing and criminal exposure overlap, we coordinate the defense with your professional obligations and engage with investigators early, before charges are filed when possible.
"""),

P(M, 'Marijuana Defense', 'Houston and Fort Bend County marijuana defense lawyer: possession, THC vape and wax, distribution and cultivation charges.', hub=True, cat=M,
  h1='Houston & Fort Bend Marijuana Defense Lawyer', hub_label='Marijuana Topics', body="""
Marijuana remains illegal in Texas outside of the limited Compassionate Use Program, but enforcement varies widely between counties. Harris County has offered a misdemeanor marijuana diversion program for years, while practices in Fort Bend County and surrounding areas have changed over time.

The 2019 legalization of hemp with low delta-9 THC has made marijuana prosecutions more complicated, because the State must prove the THC concentration through laboratory testing. Odor or appearance alone may not distinguish legal hemp from illegal marijuana.

THC concentrates, including vape cartridges, wax, and edibles, are treated far more harshly than plant marijuana because they fall in Penalty Group 2. A single vape pen can be a felony.
""", levels=MJL),
MJ('possession-of-marijuana', 'Possession of Marijuana', 'Marijuana possession charges in Harris and Fort Bend County: penalties, diversion and defenses.', """
Possession of two ounces or less of marijuana is a Class B misdemeanor in Texas, but the penalties grow with weight. Usable marijuana is weighed, not stems or seeds where the lab properly separates them.

In Harris County, eligible people may be offered a diversion program that avoids a conviction. Even where diversion is not offered, we often obtain dismissals by challenging the search, the lab's ability to distinguish hemp, and whether the State can link the marijuana to you.
""", MJL),
MJ('possession-of-thc-oil', 'Possession of THC Oil, Vapes & Edibles', 'THC vape, wax and edible charges in Texas: Penalty Group 2 felony exposure and defenses.', """
Texas classifies THC concentrates, including vape oil, wax, shatter, and many edibles, as Penalty Group 2 substances. Possession of less than one gram is a state jail felony, and because the entire weight of an edible or cartridge contents may be counted, charges can quickly escalate.

Laws governing hemp-derived THC products have been the subject of ongoing legislation and litigation. Many products sold in stores are labeled as hemp. The State must prove the product exceeded the legal delta-9 THC limit through valid testing, and must prove you knew what you possessed.
""", PG2),
MJ('cite-and-release', 'Cite and Release for Marijuana', 'Cite-and-release and marijuana diversion programs in Houston and Fort Bend County.', """
Texas law allows officers to issue a citation instead of making an arrest for certain misdemeanors, including possession of up to four ounces of marijuana, if the county has adopted a policy. A citation still requires you to appear in court and still results in a criminal charge.

Harris County has used a pre-charge diversion approach for small marijuana cases, under which eligible people complete a class instead of being charged. Policies change, so we confirm current options in the county where your case is pending.
"""),
MJ('marijuana-distribution', 'Marijuana Distribution', 'Delivery and distribution of marijuana charges in Texas: penalties and defenses.', """
Delivery of marijuana ranges from a Class B misdemeanor for giving away a quarter ounce or less to a first-degree felony for large quantities. Offering to sell also counts as delivery under Texas law.

Distribution cases often rely on informants, undercover purchases, or text messages. We challenge identification, entrapment and the reliability of the evidence used to prove intent.
""", [('1/4 oz or less, no payment', 'B'), ('1/4 oz or less, for payment', 'A'), ('More than 1/4 oz, up to 5 lbs', 'SJF'), ('More than 5 lbs, up to 50 lbs', 'F2'), ('More than 50 lbs, up to 2,000 lbs', 'F1')]),
MJ('marijuana-cultivation-and-growhouses', 'Marijuana Cultivation & Grow Houses', 'Marijuana cultivation and grow house charges in Houston: weight calculations, searches and defenses.', """
Texas generally prosecutes cultivation as possession, based on the weight of the usable marijuana. Grow-house cases often begin with utility records, thermal observations, informant tips, or odor, and usually involve a search warrant.

We scrutinize the probable cause behind the warrant, the way plants were weighed, and whether occupants of a shared property actually knew about or controlled the grow.
"""),
]
