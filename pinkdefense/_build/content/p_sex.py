from mk import P
D = 'sex-crimes'
def S(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{D}/{slug}', title, desc, body, levels, faq, cat=D, **kw)

PAGES = [
P(D, 'Sex Crimes', 'Confidential sex crime defense in Houston and Fort Bend County: sexual assault, indecency, online solicitation, prostitution and registration issues.', hub=True, cat=D,
  h1='Houston & Fort Bend Sex Crimes Defense Lawyer', hub_label='Sex Offense Topics', body="""
An accusation of a sexual offense can upend your life before any evidence is tested. Many of these offenses carry long prison ranges and sex-offender registration under Chapter 62 of the Code of Criminal Procedure, which can last ten years or a lifetime and restricts where you live and work.

These investigations often begin quietly with a forensic interview, a sexual assault exam, or a request that you "come in and give your side." Do not speak with investigators before talking to a lawyer. Early representation can shape whether charges are filed at all.

We handle these cases with discretion. We examine forensic interviews and medical findings, recover digital evidence, investigate motives and timelines, and retain qualified experts. Every client is presumed innocent, and we defend every case as if it is going to trial.
"""),
S('sexual-assault', 'Sexual Assault', 'Sexual assault and aggravated sexual assault charges in Harris and Fort Bend County: penalties and defenses.', """
Sexual assault under Penal Code § 22.011 involves sexual contact or penetration without consent, as defined by statute. It is a second-degree felony. Aggravated sexual assault under § 22.021, which involves serious bodily injury, threats, weapons, drugs, multiple actors, or certain victims, is a first-degree felony.

Consent, identity, and credibility are the most common issues. We review the timeline of reports, text and social-media communications, SANE examination findings, DNA results, and witness accounts. Conviction requires registration as a sex offender.
""", [('Sexual assault', 'F2'), ('Aggravated sexual assault', 'F1')]),
S('sexual-assault-of-a-child', 'Sexual Assault of a Child', 'Sexual assault of a child charges in Texas: penalties, registration and defenses.', """
Sexual contact with a person under 17 is charged as sexual assault of a child, a second-degree felony, regardless of consent. If the child is under 14, the offense is aggravated sexual assault of a child, a first-degree felony with a 25-year minimum sentence.

These cases often rest on a child's statements in a forensic interview at a children's advocacy center. Interview techniques, delayed outcry, outside influences, and inconsistent accounts are critical areas of investigation. We work with forensic psychologists and other experts when needed.
""", [('Child under 17', 'F2'), ('Child under 14 (25-year minimum)', 'F1')]),
S('statutory-rape', 'Statutory Rape', 'Statutory rape in Texas: age of consent, the close-in-age defense and penalties.', """
Texas does not use the term "statutory rape," but the age of consent is 17. Sexual activity with a person younger than 17 is prosecuted as sexual assault of a child even if the minor agreed.

There is a limited close-in-age affirmative defense when the accused was no more than three years older, the minor was at least 14, and the accused was not a registered sex offender. Other restrictions apply. Many of these cases involve young people in relationships, and early intervention can make a significant difference.
"""),
S('indecency-with-a-child', 'Indecency With a Child', 'Indecency with a child by contact or exposure: Texas penalties and defenses.', """
Indecency with a child involves sexual contact with, or exposure to, a child younger than 17. Indecency by contact is a second-degree felony; indecency by exposure is a third-degree felony. Both generally require sex-offender registration upon conviction or deferred adjudication.

The State must prove specific intent to arouse or gratify sexual desire. Accidental or innocent contact, such as during caregiving or play, is not a crime. These cases are highly fact-specific and require thorough investigation.
""", [('Indecency by exposure', 'F3'), ('Indecency by contact', 'F2')]),
S('indecent-assault', 'Indecent Assault', 'Indecent assault charges in Texas: Class A misdemeanor offense created in 2019.', """
Indecent assault, created in 2019, involves touching or exposure for a sexual purpose without consent, such as touching intimate areas or causing someone to contact bodily fluids. It is a Class A misdemeanor.

Although it is a misdemeanor, a conviction can carry significant collateral consequences. Consent, intent, and identity are frequent defense issues.
""", [('Indecent assault', 'A')]),
S('indecent-exposure', 'Indecent Exposure', 'Indecent exposure charges in Houston and Fort Bend County: penalties and registration risks.', """
Indecent exposure means exposing one's genitals with intent to arouse or gratify sexual desire, while recklessly disregarding whether another person who would be offended or alarmed is present. It is a Class B misdemeanor. A second conviction can trigger sex-offender registration.

Urinating in public, wardrobe malfunctions, and similar situations lack the required intent. We fight to keep these charges from becoming permanent records.
""", [('Indecent exposure', 'B')]),
S('public-lewdness', 'Public Lewdness', 'Public lewdness charges in Texas: Class A misdemeanor defense.', """
Public lewdness involves certain sexual acts in a public place, or in any place where the actor is reckless about whether another person is present who would be offended. It is a Class A misdemeanor.

Many of these cases come from undercover operations in parks, spas, and similar locations. Entrapment, identity, and whether the location qualifies as public are common issues.
""", [('Public lewdness', 'A')]),
S('online-solicitation-of-a-minor', 'Online Solicitation of a Minor', 'Online solicitation of a minor charges and sting operations in Houston and Fort Bend County.', """
Online solicitation of a minor under Penal Code § 33.021 involves communicating online with a person believed to be a minor with the intent to commit a sexual offense, or soliciting a meeting for that purpose. Depending on the conduct and the age involved, it is a third- or second-degree felony.

Many cases come from undercover sting operations in which an adult officer poses as a teenager. We analyze the full chat history, who initiated sexual topics, age representations, and whether law enforcement induced conduct the person was not otherwise disposed to commit.
"""),
S('child-pornography', 'Child Pornography Possession', 'Possession of child sexual abuse material charges: state and federal defense in Houston.', """
Possessing or accessing visual material depicting a child engaged in sexual conduct is a serious felony under Texas law, with higher ranges for larger amounts, very young children, and repeat offenses. Federal prosecutors also bring these cases, often with mandatory minimum sentences.

These investigations typically begin with a cybertip or peer-to-peer monitoring and lead to a search warrant for devices. Key issues include who had access to the device, whether files were knowingly possessed, how files were downloaded, and the reliability of forensic tools. We work with independent digital forensic examiners.
"""),
S('promotion-of-child-pornography', 'Promotion of Child Pornography', 'Promotion and distribution charges involving child sexual abuse material in Texas.', """
Promoting, distributing, or possessing with intent to promote such material is punished more severely than possession, and it is commonly alleged when files are found in shared folders on peer-to-peer networks.

Automatic file sharing does not always prove knowing promotion. Forensic analysis of software settings and user activity is critical. These cases often have parallel federal exposure.
"""),
S('invasive-visual-recording', 'Invasive Visual Recording', 'Invasive visual recording charges in Texas: state jail felony penalties and defenses.', """
Invasive visual recording involves photographing or recording another person's intimate areas without consent, under circumstances where the person had a reasonable expectation of privacy, or recording in a bathroom or changing room. It is a state jail felony.

Defenses focus on intent, consent, and whether the setting carried a reasonable expectation of privacy.
""", [('Invasive visual recording', 'SJF')]),
S('unlawful-disclosure-or-promotion-of-intimate-material-revenge-porn', 'Unlawful Disclosure of Intimate Material', 'Revenge porn and unlawful disclosure of intimate visual material charges in Texas.', """
Texas prohibits disclosing intimate visual material of another person without consent when the material was obtained or created under circumstances in which the person expected it to remain private, and when disclosure causes harm and reveals the person's identity. It is a state jail felony. Threatening to disclose such material can also be a crime.

These cases often grow out of breakups and involve questions about consent, who posted the material, and account security.
""", [('Unlawful disclosure', 'SJF')]),
S('improper-relationship-between-educator-and-student', 'Improper Educator-Student Relationship', 'Improper relationship between educator and student charges in Texas.', """
An employee of a primary or secondary school who engages in sexual contact with a student enrolled in the same district, or with a student they know is enrolled elsewhere and participating in a school activity, commits a second-degree felony, even if the student is an adult.

These charges also bring licensing and employment consequences through the State Board for Educator Certification. Early representation helps manage both.
""", [('Improper relationship', 'F2')]),
S('prostitution', 'Prostitution & Solicitation', 'Prostitution and solicitation of prostitution charges in Houston: penalties after the 2021 law change.', """
Since 2021, Texas has treated buyers more harshly than sellers. Selling sexual conduct is generally a Class B misdemeanor, while soliciting prostitution (buying) is a state jail felony, even for a first offense. Penalties increase with prior convictions or if the person solicited is a minor.

Many arrests come from undercover stings, including online ads. Entrapment, the specific words exchanged, and identification are common defenses.
""", [('Prostitution (selling), first offense', 'B'), ('Solicitation of prostitution (buying)', 'SJF')]),
S('sexually-oriented-businesses', 'Sexually Oriented Business Violations', 'Criminal charges involving sexually oriented businesses in Houston and Harris County.', """
Houston and Harris County regulate sexually oriented businesses through licensing, location, and conduct rules. Owners, managers, and employees can face criminal charges for operating without a permit, violating conduct regulations, or employing minors.

These cases often involve administrative and criminal components. We defend individuals and businesses and help them address regulatory issues to avoid future charges.
"""),
]
