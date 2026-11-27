from mk import P
D = 'weapon-firearm-charges'; FED = 'federal-crimes'
def S(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{D}/{slug}', title, desc, body, levels, faq, cat=D, **kw)
def FC(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{FED}/{slug}', title, desc, body, levels, faq, cat=FED, **kw)

PAGES = [
P(D, 'Weapon & Firearm Charges', 'Houston and Fort Bend County gun charge lawyer: unlawful carrying, felon in possession, prohibited places and deadly conduct.', hub=True, cat=D,
  h1='Houston & Fort Bend Weapons Charge Lawyer', hub_label='Weapons Charge Topics', body="""
Since September 2021, most Texans 21 and older who are not otherwise prohibited can carry a handgun without a license. That change did not end weapons prosecutions. It shifted them toward questions about who is prohibited, where a weapon was carried, and how it was displayed or used.

Houston-area weapons cases commonly arise from traffic stops, bar and nightlife incidents, road-rage encounters, and searches incident to other arrests. A weapons conviction can also cost you the right to possess firearms, a License to Carry, and certain jobs. We test the stop, the search, the prohibited-person status, and the location element in every case.
"""),
S('unlawfully-carrying-a-weapon', 'Unlawfully Carrying a Weapon', 'Unlawful carrying of a weapon charges in Texas after permitless carry: who is prohibited and the penalties.', """
Unlawfully carrying a weapon under Penal Code § 46.02 still applies to people younger than 21 (with limited exceptions), people prohibited from possessing firearms, people engaged in criminal activity other than a Class C traffic offense, people who are members of a criminal street gang, and people carrying on premises licensed to sell alcohol. It is generally a Class A misdemeanor, and a third-degree felony on alcohol-licensed premises.

People convicted of unlawful carrying before permitless carry took effect may qualify to have that record expunged. See [Expunging Unlawful Carrying](/expunctions-record-sealing/expunging-unlawful-carry-of-a-firearm/).
""", [('Unlawful carrying', 'A'), ('On premises licensed to sell alcohol', 'F3')]),
S('places-weapons-are-prohibited', 'Places Weapons Are Prohibited', 'Where guns are prohibited in Texas: schools, courts, polling places, airports and posted businesses.', """
Penal Code §§ 46.03 and 46.035 list places where weapons are prohibited, including schools and school events, polling places on election day, courts and court offices, racetracks, secured areas of airports such as Bush Intercontinental and Hobby, and certain other locations. Many of these violations are third-degree felonies.

Private businesses can also prohibit carry through properly worded signs under §§ 30.06 and 30.07. Signs that do not meet the statutory requirements may not provide effective notice. Airport checkpoint cases are common, and many can be resolved without a conviction.
""", [('Most prohibited-place violations', 'F3'), ('Trespass by license holder after proper notice', 'C')]),
S('possession-of-a-weapon-by-a-felon', 'Felon in Possession of a Firearm', 'Unlawful possession of a firearm by a felon: Texas and federal charges in Houston.', """
Under Penal Code § 46.04, a person convicted of a felony cannot possess a firearm until five years after release from confinement or supervision, whichever is later, and after that only at their home. A violation is a third-degree felony. People convicted of misdemeanor family violence are prohibited for five years after supervision ends.

Federal law, 18 U.S.C. § 922(g), imposes a separate and broader prohibition, and federal prosecutors in Houston frequently adopt these cases. We examine the prior conviction, the timing, knowledge of possession, and the legality of the search.
""", [('Unlawful possession by a felon', 'F3')]),
S('firearm-possession-at-a-bar-or-alcohol-establishment', 'Firearms at Bars & 51% Establishments', 'Carrying a gun in a bar or 51% establishment in Texas: felony penalties and defenses.', """
Carrying a handgun on premises that earn 51 percent or more of their income from on-site alcohol sales is a third-degree felony, whether or not the person has a License to Carry. Those businesses must post a red "51%" sign.

Whether the business actually qualified, whether proper signage was displayed, and whether the person knew where they were are all legitimate defense issues. Carrying while intoxicated carries separate consequences.
""", [('Carrying at a 51% establishment', 'F3')]),
S('deadly-conduct-with-a-firearm', 'Deadly Conduct With a Firearm', 'Deadly conduct with a firearm charges in Houston: pointing or discharging a gun.', """
Pointing a firearm at someone, whether or not it is loaded, is presumed to be reckless deadly conduct, a Class A misdemeanor. Knowingly discharging a firearm at or in the direction of people, a house, a building, or a vehicle is a third-degree felony.

Self-defense and defense of property often apply. Texas law justifies the threat of deadly force in situations where deadly force itself would be justified, and creating the apprehension of force is treated differently than using it.
""", [('Pointing a firearm', 'A'), ('Discharging at persons, a habitation, or a vehicle', 'F3')]),
S('discharge-of-firearm-in-certain-municipalities', 'Discharging a Firearm in City Limits', 'Discharge of a firearm in certain municipalities in Texas, including Houston.', """
Recklessly discharging a firearm inside the limits of a municipality with a population of 100,000 or more, such as Houston, is a Class A misdemeanor under Penal Code § 42.12. Many other cities have local ordinances restricting discharge.

Celebratory gunfire on holidays leads to many of these charges. Defenses include self-defense, lawful hunting or range use, and lack of recklessness.
""", [('Reckless discharge in a large city', 'A')]),
S('making-a-firearm-accessible-to-a-child', 'Making a Firearm Accessible to a Child', 'Making a firearm accessible to a child charges in Texas.', """
Texas law makes it an offense to leave a readily dischargeable firearm where a child younger than 17 could access it, when the child does access it. It is a Class C misdemeanor, and a Class A misdemeanor if the child discharges the firearm and causes death or serious bodily injury.

Defenses include that the firearm was secured with a locking device or stored in a locked place, or that the child gained access through unlawful entry. These cases are often tragic accidents and call for careful, compassionate handling.
""", [('Child gains access', 'C'), ('Child discharges, causing death or serious injury', 'A')]),
S('taking-a-peace-officers-firearm', "Taking a Peace Officer's Weapon", "Taking or attempting to take a peace officer's weapon charges in Texas.", """
Intentionally or knowingly taking or attempting to take a firearm, nightstick, stun gun, or similar device from a peace officer who is performing official duties is a state jail felony, and more serious if the weapon is fired or someone is injured.

These charges usually arise from struggles during arrest. Body-camera video is crucial to show whether the contact was intentional or incidental.
""", [('Taking or attempting to take', 'SJF')]),
S('road-rage-incidents-with-weapon-possession-in-texas', 'Road Rage Incidents With a Weapon', 'Road rage gun charges on Houston highways: deadly conduct, aggravated assault and self-defense.', """
Confrontations on I-610, I-45, the Beltway and the Grand Parkway too often involve firearms. Charges can range from disorderly conduct for displaying a weapon, to deadly conduct for pointing it, to aggravated assault with a deadly weapon.

What matters most is what each driver did and reasonably believed. Dash-camera footage, traffic cameras, 911 calls, and independent witnesses often tell a different story than the first report. Self-defense is frequently a strong defense in these cases.
"""),

P(FED, 'Federal Crimes', 'Houston federal criminal defense lawyer: drug conspiracy, firearms, fraud and investigations in the Southern District of Texas.', hub=True, cat=FED,
  h1='Houston Federal Criminal Defense Lawyer', hub_label='Federal Defense Topics', body="""
Federal cases in Houston are prosecuted by the U.S. Attorney's Office for the Southern District of Texas and heard at the Bob Casey U.S. Courthouse downtown. Federal investigations by the FBI, DEA, ATF, HSI, IRS-CI, and the Postal Inspection Service are typically long and thorough, and by the time charges are filed, the government has built its case.

Augustin T. Pink has obtained dismissals, jury acquittals, and sentence reductions in federal court over a career that began in 1992. We engage early, evaluate the discovery and the Sentencing Guidelines exposure, litigate suppression issues, and prepare every case for trial.
"""),
FC('federal-investigations-target-letters', 'Federal Investigations & Target Letters', 'What to do if you receive a federal target letter, grand jury subpoena, or visit from federal agents in Houston.', """
A target letter means federal prosecutors consider you a likely defendant. A grand jury subpoena or a visit from agents may mean you are a witness, a subject, or a target. In every case, it is time to speak with a lawyer before you speak with the government.

Early representation can allow us to present information that changes the government's view, negotiate the terms of any interview, protect privileged documents, and in some cases avoid charges entirely.
"""),
FC('federal-drug-conspiracy', 'Federal Drug Conspiracy', 'Federal drug conspiracy and trafficking defense in Houston: mandatory minimums and safety valve.', """
Federal drug charges under 21 U.S.C. §§ 841 and 846 often carry mandatory minimum sentences of five or ten years depending on the drug and quantity. In a conspiracy, the government may try to hold each person responsible for quantities attributed to the entire group.

Defenses include challenging wiretaps and searches, contesting membership in the conspiracy, disputing drug quantity, and seeking relief under the safety-valve provision, which can allow a sentence below the mandatory minimum for qualifying defendants.
"""),
FC('federal-firearm-charges', 'Federal Firearm Charges', 'Federal gun charges in the Southern District of Texas: felon in possession, 924(c) and straw purchases.', """
Common federal firearm charges include possession by a prohibited person under 18 U.S.C. § 922(g), using or carrying a firearm during a drug trafficking crime or crime of violence under § 924(c), which carries consecutive mandatory minimums, and false statements in firearm purchases (straw purchases).

Many federal gun cases begin as state arrests by HPD or the Harris County Sheriff's Office and are later adopted federally. We evaluate the search, knowledge of possession, and constitutional challenges that continue to develop in the courts.
"""),
FC('federal-sentencing', 'Federal Sentencing', 'How federal sentencing works: the Sentencing Guidelines, departures, variances and mitigation.', """
Federal sentences are calculated under the U.S. Sentencing Guidelines, which assign an offense level and criminal history category. The Guidelines are advisory, and judges must consider the factors in 18 U.S.C. § 3553(a), including the person's history and characteristics.

Effective sentencing advocacy starts long before the hearing. We challenge Guideline enhancements, prepare a detailed mitigation presentation, and address objections to the presentence report. Our family of firms has obtained significant federal sentence reductions.
"""),
FC('federal-fraud', 'Federal Fraud Charges', 'Federal fraud defense in Houston: wire, mail, bank, health care and securities fraud.', """
Federal fraud charges include wire and mail fraud, bank and loan fraud, health care fraud, securities fraud, and conspiracy. Loss amount drives much of the Sentencing Guidelines calculation, so the government's loss figure is often the most important number in the case.

See our [White-Collar & Fraud](/white-collar-crimes/) practice for more detail on these investigations.
"""),
]
