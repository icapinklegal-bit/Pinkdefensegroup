from mk import P
D = 'violent-crimes'
def S(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{D}/{slug}', title, desc, body, levels, faq, cat=D, **kw)

PAGES = [
P(D, 'Assault & Violent Crimes', 'Houston and Fort Bend County violent crime defense lawyer: assault, aggravated assault, robbery, murder, kidnapping and terroristic threat charges.', hub=True, cat=D,
  h1='Houston & Fort Bend Violent Crimes Lawyer', hub_label='Violent Crime Topics', body="""
Violent-crime charges carry the most serious consequences in Texas law, and many come with a "deadly weapon" finding that limits probation and parole. These cases also tend to move fast, with high bonds and protective conditions set at the first appearance.

Our family of firms has secured dismissals in aggravated assault with a deadly weapon cases, no-bills in murder investigations, and the dismissal of a capital murder charge. We investigate independently, interview witnesses before memories fade, collect surveillance video before it is overwritten, and evaluate self-defense from day one.

## Self-Defense in Texas
Texas law justifies force when a person reasonably believes it is immediately necessary to protect against another's unlawful force, and deadly force in narrower circumstances, including to prevent certain violent felonies. In many situations there is no duty to retreat. When the evidence raises self-defense, the State must disprove it beyond a reasonable doubt.
"""),
S('assault-by-contact', 'Assault by Contact', 'Class C assault by contact charges in Houston and Fort Bend County and how to keep them off your record.', """
Assault by offensive or provocative contact is the least serious form of assault in Texas: intentionally or knowingly causing physical contact that the person knows the other will regard as offensive. It is usually a Class C misdemeanor punishable by a fine, but it becomes a Class A misdemeanor if the victim is elderly or disabled.

Even a fine-only offense can appear on background checks and, when it involves a family member, can lead to an affirmative finding of family violence. We pursue dismissal or deferred disposition so the record can later be expunged.
""", [('Standard', 'C'), ('Elderly or disabled complainant', 'A')]),
S('assault-causing-bodily-injury', 'Assault Causing Bodily Injury', 'Assault causing bodily injury charges in Harris and Fort Bend County: Class A penalties and enhancements.', """
Assault causing bodily injury under Penal Code § 22.01(a)(1) means intentionally, knowingly, or recklessly causing bodily injury, which Texas defines broadly as physical pain, illness, or any impairment of physical condition. It is typically a Class A misdemeanor.

The charge becomes a third-degree felony when the complainant is a public servant, a security officer, emergency services personnel, or a family or household member in certain circumstances, such as a prior family violence conviction or impeding breath. Self-defense, mutual combat, and lack of injury are common defenses.
""", [('Standard', 'A'), ('Public servant or certain family violence cases', 'F3')]),
S('assault-with-serious-bodily-injury', 'Aggravated Assault', 'Aggravated assault charges in Houston and Fort Bend County: serious bodily injury, deadly weapons and defenses.', """
Aggravated assault under Penal Code § 22.02 is an assault that causes serious bodily injury or involves using or exhibiting a deadly weapon. It is generally a second-degree felony. It becomes a first-degree felony in certain cases, such as when a deadly weapon is used against a family member causing serious bodily injury or against a public servant.

A deadly weapon finding has major consequences: judges cannot place you on regular probation, and parole eligibility is delayed. Anything can be a deadly weapon depending on how it was used, which makes the specific facts critical. Our affiliated family firm has obtained multiple dismissals of aggravated assault with a deadly weapon charges.
""", [('Serious bodily injury or deadly weapon', 'F2'), ('Certain public servant or family violence cases', 'F1')]),
S('deadly-weapon', 'Deadly Weapon Findings', 'What a deadly weapon finding means in Texas criminal cases and how to fight it.', """
A deadly weapon is a firearm, anything designed to cause death or serious injury, or anything that in its manner of use or intended use is capable of causing death or serious bodily injury. Vehicles, bats, and even shod feet have qualified.

When a jury or judge makes an affirmative deadly weapon finding, the case becomes a "3g" offense: the judge cannot grant regular community supervision, and a person sentenced to prison must generally serve half the sentence before becoming parole eligible. Contesting the finding can matter as much as contesting guilt.
"""),
S('disorderly-conduct-deadly-conduct', 'Disorderly Conduct & Deadly Conduct', 'Disorderly conduct and deadly conduct charges in Texas: penalties and defenses.', """
Disorderly conduct covers behavior such as offensive language or gestures in public, fighting, making unreasonable noise, or displaying a firearm in a manner calculated to alarm. Most forms are Class C misdemeanors, while firearm-related forms are Class B.

Deadly conduct is more serious. Recklessly placing another in imminent danger of serious bodily injury, including pointing a gun at someone, is a Class A misdemeanor. Knowingly discharging a firearm at or in the direction of people, a home, or a vehicle is a third-degree felony.
""", [('Disorderly conduct (most forms)', 'C'), ('Disorderly conduct involving a firearm', 'B'), ('Deadly conduct, reckless', 'A'), ('Deadly conduct, discharging a firearm at persons or habitation', 'F3')]),
S('public-servant', 'Assault on a Public Servant', 'Assault on a public servant or peace officer charges in Houston and Fort Bend County.', """
Assault causing bodily injury to a person the actor knows is a public servant lawfully discharging an official duty, or in retaliation for that duty, is at least a third-degree felony. Public servants include police officers, jailers, teachers, and government employees.

These cases often arise from chaotic arrests where officers' accounts differ from video. We examine whether the officer was acting lawfully, whether the contact was intentional, and whether injuries are documented. Our affiliated family firm has obtained dismissals of assault on a peace officer and retaliation charges, and deferred probation in another case where the prior offer was prison time.
""", [('Assault on a public servant', 'F3')]),
S('harassment-of-a-public-servant', 'Harassment of a Public Servant', 'Harassment of a public servant charges in Texas involving bodily fluids: third-degree felony defense.', """
Harassment by persons in certain facilities, and harassment of a public servant, involve causing a public servant to contact blood, saliva, urine, or other bodily fluids with intent to assault, harass, or alarm. It is a third-degree felony.

These charges often arise during arrest or in jail. Intent is central. Coughing, sneezing, or accidental contact during a struggle is not the same as an intentional act.
""", [('Harassment of a public servant', 'F3')]),
S('robbery', 'Robbery & Aggravated Robbery', 'Robbery and aggravated robbery charges in Houston: second- and first-degree felony defense.', """
Robbery is committing theft while intentionally, knowingly, or recklessly causing bodily injury, or threatening or placing someone in fear of imminent injury or death. It is a second-degree felony. Aggravated robbery, which involves serious bodily injury, a deadly weapon, or an elderly or disabled victim, is a first-degree felony and a "3g" offense.

Identification is often the central issue. Eyewitness identification is error-prone, especially under stress and when a weapon is present. We examine lineup procedures, video, cell-site data, and forensic evidence. A client of our affiliated family firm was acquitted of all aggravated robbery charges.
""", [('Robbery', 'F2'), ('Aggravated robbery', 'F1')]),
S('kidnapping', 'Kidnapping', 'Kidnapping and aggravated kidnapping charges in Harris and Fort Bend County.', """
Kidnapping is intentionally or knowingly abducting another person, which requires restraint plus intent to prevent liberation by secreting them or by using or threatening deadly force. It is a third-degree felony. Aggravated kidnapping involves additional intent, such as holding someone for ransom or to facilitate another felony, and is a first-degree felony, reduced to second-degree if the defendant voluntarily released the victim in a safe place.

Many kidnapping allegations grow out of domestic disputes or custody disagreements, where intent and context are crucial.
""", [('Kidnapping', 'F3'), ('Aggravated kidnapping, released in a safe place', 'F2'), ('Aggravated kidnapping', 'F1')]),
S('unlawful-restraint', 'Unlawful Restraint', 'Unlawful restraint charges in Texas: misdemeanor and felony levels and defenses.', """
Unlawful restraint means intentionally or knowingly restricting another person's movements without consent by force, intimidation, or deception, or by confining them. It is generally a Class A misdemeanor, a state jail felony when the person restrained is a child under 17, and a third-degree felony when the actor recklessly exposes the victim to a substantial risk of serious bodily injury or restrains a public servant.

A relative of a child who restrains them without force or intent to harm may have a defense.
""", [('Standard', 'A'), ('Child under 17', 'SJF'), ('Substantial risk of serious bodily injury', 'F3')]),
S('terroristic-threats', 'Terroristic Threat', 'Terroristic threat charges in Houston and Fort Bend County: what counts and how to defend.', """
A terroristic threat is threatening violence against a person or property with intent to cause a reaction by emergency officials, place someone in fear of imminent serious bodily injury, or disrupt a building, public place, or public service. A basic threat against a person is a Class B misdemeanor, a Class A misdemeanor when made against a family member or public servant, and a felony when it disrupts public services or a school.

Words spoken in anger, sarcasm, or jest, especially online, are often treated as threats after the fact. Context, intent, and the First Amendment all matter. Our affiliated family firm has obtained the dismissal of a family-household terroristic threat charge.
""", [('Threat against a person', 'B'), ('Family member or public servant', 'A'), ('Disrupting a public place or service', 'SJF')]),
S('stalking', 'Stalking', 'Stalking charges in Texas: third-degree felony penalties, protective orders and defenses.', """
Stalking under Penal Code § 42.072 requires conduct on more than one occasion, directed at a specific person, that the actor knows the other will regard as threatening and that would cause a reasonable person to fear harm or feel harassed. It is a third-degree felony, and a second-degree felony with a prior stalking conviction.

Stalking cases usually involve a history between the parties, and the evidence often consists of texts, call logs, and social media. We collect the full communication record, which frequently shows mutual contact or context that undercuts the allegation.
""", [('Stalking', 'F3'), ('With prior conviction', 'F2')]),
S('cyberstalking', 'Online Harassment & Cyberstalking', 'Online harassment, cyberbullying and cyberstalking charges in Texas.', """
Texas prosecutes electronic harassment under Penal Code § 42.07, including repeated electronic communications meant to harass, annoy, alarm, abuse, torment, or embarrass. Most forms are Class B misdemeanors. When the conduct is repeated and threatening, prosecutors may charge stalking, a felony, based on online behavior.

Digital evidence can be spoofed, misattributed, or taken out of context. We examine account ownership, IP data, and the complete message history, and we evaluate free-speech issues.
""", [('Harassment', 'B'), ('Stalking through electronic means', 'F3')]),
S('manslaughter', 'Manslaughter', 'Manslaughter and criminally negligent homicide charges in Harris and Fort Bend County.', """
Manslaughter is recklessly causing the death of another person and is a second-degree felony. Criminally negligent homicide, causing death through criminal negligence, is a state jail felony. The difference turns on the person's mental state: whether they consciously disregarded a substantial risk or failed to perceive it.

These cases often arise from accidents, firearms mishandling, or vehicle collisions. Expert analysis and careful attention to the facts can mean the difference between a felony conviction and a dismissal or reduced charge.
""", [('Criminally negligent homicide', 'SJF'), ('Manslaughter', 'F2')]),
S('murder', 'Murder & Homicide', 'Murder and capital murder defense in Houston and Fort Bend County from a trial-tested family of firms.', """
Murder under Penal Code § 19.02 is a first-degree felony punishable by five to ninety-nine years or life. If the jury finds the defendant acted under the immediate influence of sudden passion arising from adequate cause, the punishment drops to the second-degree range. Capital murder, which includes killings of peace officers, multiple victims, or murder during certain felonies, carries life without parole or the death penalty.

Homicide investigations begin long before an arrest, and early representation can influence whether a grand jury indicts. Our affiliated family firm has obtained no-bills in two murder investigations and the dismissal of a capital murder charge. We retain investigators and forensic experts, examine self-defense, and prepare every case for trial.
""", [('Murder', 'F1'), ('Murder with sudden passion found', 'F2'), ('Capital murder', 'CAP')]),
]
