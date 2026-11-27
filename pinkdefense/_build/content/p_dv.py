from mk import P
D = 'domestic-family-violence'
def S(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{D}/{slug}', title, desc, body, levels, faq, cat=D, **kw)

PAGES = [
P(D, 'Domestic & Family Violence', 'Houston and Fort Bend County domestic violence lawyer: family violence assault, strangulation, protective orders and bond conditions. Call (832) 979-0882.', hub=True, cat=D,
  h1='Houston & Fort Bend Domestic Violence Lawyer', hub_label='Family Violence Topics', body="""
Family violence charges reach far beyond the courtroom. An arrest can come with an emergency protective order that removes you from your home, bond conditions that bar contact with your partner or children, and a lifetime federal firearm prohibition if you are convicted.

Texas defines family violence broadly to include spouses, former spouses, people who share a child, relatives, people living in the same household, and dating partners. In Harris and Fort Bend Counties, prosecutors handle these cases through specialized units and often proceed even when the complaining witness does not want the case to continue.

The Pink family of firms has obtained dismissals in numerous family violence cases, including a felony charge for impeding breath and a combined burglary and family violence case.
"""),
S('domestic-assault', 'Domestic Assault', 'Family violence assault charges in Harris and Fort Bend County: penalties, enhancements and long-term consequences.', """
Assault causing bodily injury to a family or household member or dating partner is a Class A misdemeanor for a first offense. It becomes a third-degree felony if you have a prior family violence conviction or if the State alleges impeding breath or circulation.

## Consequences Beyond the Sentence
- An "affirmative finding" of family violence follows you and enhances future charges.
- A conviction triggers a federal firearm prohibition.
- Deferred adjudication for family violence cannot be sealed by nondisclosure.
- The case can affect custody, immigration status, and professional licenses.

That is why the goal in most cases is dismissal, acquittal, or a resolution that avoids a family violence finding.
""", [('First offense', 'A'), ('Prior family violence conviction or impeding breath', 'F3'), ('Impeding breath with prior conviction', 'F2')]),
S('assault-by-strangulation', 'Assault by Strangulation', 'Impeding breath or circulation (strangulation) charges in Texas: third-degree felony defense.', """
Assault by impeding the normal breathing or circulation of the blood, by applying pressure to the throat or neck or blocking the nose or mouth, is a third-degree felony when committed against a family member, household member, or dating partner, even without any prior record.

These allegations are often made during a heated argument with little physical evidence. We scrutinize photographs, medical findings, the complaining witness's statements over time, and any 911 recording. Our affiliated family firm has obtained the dismissal of a felony impeding-breath charge.
""", [('Impeding breath, family member', 'F3'), ('With prior family violence conviction', 'F2')]),
S('continuous-family-violence', 'Continuous Family Violence', 'Continuous violence against the family charges in Texas: what the State must prove.', """
Continuous violence against the family under Penal Code § 25.11 applies when a person commits two or more family violence assaults within a 12-month period. It is a third-degree felony, and the alleged assaults do not need to have resulted in convictions or even arrests.

Because the State can rely on prior incidents that were never charged, we investigate each alleged event separately and challenge vague or unsupported claims.
""", [('Continuous family violence', 'F3')]),
S('interference-with-emergency-call', 'Interference With an Emergency Call', 'Interference with an emergency request for assistance charges in Texas.', """
Knowingly preventing or interfering with another person's ability to place an emergency call, or request help from a law enforcement agency, medical facility, or family member, when that person reasonably believes they are in danger, is a Class A misdemeanor. It becomes a state jail felony with a prior conviction.

This charge is often added to family violence arrests. It requires proof that the person was trying to call for help and that the interference was knowing, both of which are often disputed.
""", [('First offense', 'A'), ('With prior conviction', 'SJF')]),
S('protective-order-hearings', 'Protective Order Hearings', 'Protective order hearings in Harris and Fort Bend County: emergency orders, final orders and defending your rights.', """
There are two main types of protective orders. A magistrate's order of emergency protection is often issued automatically at a family violence arrest and can last 31 to 61 days, or up to 91 days if a weapon was involved. A protective order under the Family Code requires a hearing and can last up to two years, and longer in serious cases.

A protective order can remove you from your home, restrict contact with your children, and prohibit you from possessing firearms. Anything you say at the hearing can be used in the criminal case. We represent clients at these hearings to protect both their rights and their criminal defense.
"""),
S('violation-of-protective-order', 'Violation of a Protective Order', 'Violation of protective order and bond conditions charges in Houston and Fort Bend County.', """
Violating a protective order or family violence bond condition, such as communicating with the protected person, going near their home or workplace, or possessing a firearm, is a Class A misdemeanor. It becomes a third-degree felony with two prior violations or if the violation involves an assault or stalking.

Contact initiated by the protected person is still a violation for the restrained person, which surprises many clients. If you have questions about what your order allows, ask us before acting.
""", [('Violation', 'A'), ('Two prior convictions, or involving assault or stalking', 'F3')]),
S('dismissing-a-family-violence-charge', 'Dismissing a Family Violence Charge', 'How family violence charges get dismissed in Houston, even when the complaining witness wants to drop charges.', """
Only the prosecutor can dismiss a criminal case. A complaining witness cannot "drop the charges," although their wishes and an affidavit of non-prosecution are often considered. In Harris and Fort Bend Counties, prosecutors may try to proceed using 911 recordings, body-camera video, photographs, and officer testimony.

Many of those pieces of evidence are hearsay that can be excluded unless an exception applies, and the Confrontation Clause limits the use of testimonial statements when the witness does not testify. We build the case for dismissal through investigation, motions practice, and trial preparation.
"""),
S('defending-women-charged-with-domestic-violence', 'Women Charged With Domestic Violence', 'Defending women accused of family violence in Houston and Fort Bend County.', """
Women are increasingly arrested in family violence incidents, sometimes when both parties had injuries or when they acted to defend themselves. Officers responding to a chaotic scene often make quick judgments about who was the primary aggressor.

We examine the history of the relationship, prior incidents, defensive injuries, and self-defense. We also address the practical concerns many of our clients face, such as caregiving responsibilities, custody, and employment.
"""),
S('domestic-violence-faqs', 'Domestic Violence FAQ', 'Frequently asked questions about family violence charges in Harris and Fort Bend County.', """
Here are answers to questions clients often ask after a family violence arrest in Houston, Sugar Land, Richmond or Katy.
""", faq=[
  ('Can my partner drop the charges?', 'No. Only the prosecutor can dismiss the case, although the complaining witness\'s wishes can influence the decision.'),
  ('Can I go home after I bond out?', 'Not if an emergency protective order or bond condition prohibits it. We can ask the court to modify those conditions.'),
  ('Will I lose my right to own guns?', 'A family violence conviction triggers a federal firearm prohibition, and Texas law separately restricts possession for five years after a misdemeanor family violence conviction.'),
  ('Can a family violence case be sealed?', 'If the case is dismissed or you are acquitted, you may qualify for expunction. Deferred adjudication with a family violence finding generally cannot be sealed.'),
  ('Should I talk to the police to explain my side?', 'Not without a lawyer. Statements made to explain can easily become evidence for the State.'),
]),
S('expunging-domestic-violence', 'Expunging a Domestic Violence Arrest', 'When a family violence arrest can be expunged in Texas.', """
A family violence arrest can be expunged if the case was dismissed under qualifying conditions, no-billed by a grand jury, or ended in acquittal. A conviction cannot be expunged, and deferred adjudication involving family violence is excluded from nondisclosure.

Because the options are limited after a plea, the decisions made while the case is pending matter enormously. See [Expunctions & Record Sealing](/expunctions-record-sealing/).
"""),
S('child-abuse-and-injury-to-a-child', 'Injury to a Child', 'Injury to a child and child abuse charges in Houston and Fort Bend County: penalties and defenses.', """
Injury to a child under Penal Code § 22.04 covers causing bodily injury, serious bodily injury, or serious mental deficiency to a child 14 or younger, by act or by omission. The offense level depends on the injury and the mental state, ranging from a state jail felony to a first-degree felony.

These cases often involve medical opinions about how an injury occurred, and those opinions can be wrong. Accidental injuries, medical conditions, and reasonable discipline are possible defenses. CPS investigations usually run alongside the criminal case, and we coordinate both.
""", [('Bodily injury, reckless or negligent', 'SJF'), ('Bodily injury, intentional or knowing', 'F3'), ('Serious bodily injury, reckless', 'F2'), ('Serious bodily injury, intentional or knowing', 'F1')]),
S('injury-to-elderly-or-disabled-individual', 'Injury to an Elderly or Disabled Person', 'Injury to an elderly or disabled individual charges in Texas.', """
Section 22.04 also protects people 65 and older and people with disabilities. Charges often involve caregivers, family members, and healthcare workers, and they may be based on an omission, such as failing to provide care, as well as an act.

The State must prove the person had a legal duty to act and that the injury resulted from the conduct alleged. Medical records and care history are central to the defense.
"""),
S('elder-neglect', 'Elder Neglect', 'Elder neglect charges against family members and caregivers in Harris and Fort Bend County.', """
Neglect cases usually arise when an elderly person is found in poor health or living conditions. Prosecutors must show the accused had a legal duty, such as a statutory, contractual, or assumed caregiving responsibility, and failed to meet it in a way that caused injury.

Many families are doing their best with limited resources and a loved one who refuses help. We gather medical, financial, and care records to show the full picture, and we coordinate with any Adult Protective Services investigation.
"""),
S('abandoning-or-endangering-a-child', 'Abandoning or Endangering a Child', 'Child endangerment and abandonment charges in Texas: penalties and defenses.', """
Endangering a child means intentionally, knowingly, recklessly, or with criminal negligence placing a child younger than 15 in imminent danger of death, bodily injury, or physical or mental impairment. It is generally a state jail felony. Abandonment is leaving a child under 15 in any place without reasonable and necessary care, and ranges from a state jail felony to a second-degree felony.

These charges are sometimes filed alongside DWI or drug cases when a child is present. The danger must be imminent, not speculative.
""", [('Endangering a child', 'SJF')]),
]
