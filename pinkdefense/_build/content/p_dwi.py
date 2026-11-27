from mk import P
D = 'dwi-dui'
def S(slug, title, desc, body, levels=None, faq=None, **kw):
    return P(f'{D}/{slug}', title, desc, body, levels, faq, cat=D, **kw)

PAGES = [
P(D, 'DWI / DUI Defense', 'Houston and Fort Bend County DWI defense lawyer. First and repeat DWI, felony DWI, intoxication assault, ALR hearings and license protection. Call (832) 979-0882.', hub=True, cat=D,
  h1='Houston & Fort Bend County DWI Lawyer', hub_label='DWI Topics', body="""
A driving while intoxicated arrest starts two cases at once: a criminal case in Harris County or Fort Bend County court, and an administrative license suspension through the Texas Department of Public Safety. You generally have **15 days** from the arrest to request an Administrative License Revocation (ALR) hearing, so the clock starts immediately.

Under Texas Penal Code § 49.04, a person is intoxicated if they have lost the normal use of their mental or physical faculties because of alcohol, drugs, or a combination, or if they have a blood or breath alcohol concentration of 0.08 or more. The State can try to prove either theory, which means a DWI can be charged even when a test result is below 0.08 or when no test was taken.

## How a Houston DWI Case Unfolds
Arrests on I-610, I-10, I-69/US-59, Beltway 8, the Grand Parkway and SH-6 are made by HPD, the Harris County Sheriff's Office, county constables, Fort Bend County deputies, Sugar Land and Missouri City police, and DPS troopers. Most cases involve a breath test on an Intoxilyzer 9000 or a blood draw under a search warrant, especially during "no refusal" enforcement periods.

## Our DWI Defense
We review the legal basis for the stop, the officer's field sobriety testing, the breath-test operator's certification and the instrument's records, and the blood-draw warrant and lab analysis. Our goal is a dismissal, an acquittal, or a reduction that protects your license, job and record.
""", levels=[('First DWI', 'B'), ('First DWI with BAC 0.15 or more', 'A'), ('Second DWI', 'A'), ('Third or more DWI', 'F3')], kind='criminal'),

S('first-dwi', 'First DWI', 'What a first DWI means in Houston and Fort Bend County: penalties, license suspension, deferred adjudication and how to fight the charge.', """
A first DWI in Texas is usually a Class B misdemeanor. Even so, it carries a mandatory minimum of 72 hours in jail if jail is imposed (six days if an open container was in the vehicle), a fine of up to $2,000, a possible license suspension, and a state traffic fine of $3,000 after conviction ($6,000 if the alcohol concentration was 0.16 or more).

## Options for First-Time Offenders
Many first-time clients avoid jail entirely. Depending on the facts and the court, outcomes can include dismissal, reduction to a non-DWI offense such as obstructing a highway, community supervision, or deferred adjudication, which became available for most DWIs in 2019. A first DWI conviction or deferred adjudication may later qualify for an order of nondisclosure.

## Do Not Miss the ALR Deadline
Your license can be suspended for 90 days for a failed test or 180 days for a refusal unless you request an ALR hearing within 15 days of arrest. That hearing also gives us an early chance to question the arresting officer under oath.
""", levels=[('BAC under 0.15', 'B'), ('BAC 0.15 or more', 'A')]),

S('second-dwi', 'Second DWI', 'Second DWI charges in Houston and Fort Bend County: Class A penalties, mandatory jail, ignition interlock and defense strategies.', """
A second DWI is a Class A misdemeanor under Penal Code § 49.09(a), punishable by 30 days to one year in county jail and a fine of up to $4,000. Judges must require an ignition interlock device as a condition of bond, and a conviction triggers a longer license suspension and a higher state traffic fine.

The State has to prove the prior conviction with proper records, and it must still prove the new DWI beyond a reasonable doubt. We examine both. A second arrest is also not automatically a "second DWI" if the earlier case ended in dismissal or acquittal.

Probation is possible for a second offense, often with conditions such as an interlock, alcohol monitoring, counseling and community service. When the evidence is weak, we push for dismissal or a reduction that avoids the repeat-offender penalties.
""", levels=[('Second DWI', 'A')]),

S('third-or-subsequent-dwi', 'Third or Subsequent DWI', 'Felony third DWI charges in Harris and Fort Bend County: prison ranges, probation eligibility, and how we challenge prior convictions.', """
A third DWI, or any DWI with two prior DWI convictions, is a third-degree felony under Penal Code § 49.09(b). The punishment range is two to ten years in prison and a fine of up to $10,000. A conviction is a permanent felony record.

Felony DWI cases are filed in district court. The State must prove both prior convictions with certified judgments and fingerprints or other identity evidence. Defects in those records are a common and powerful defense. We also test the new arrest itself: the stop, the field sobriety tests, and the chemical testing.

Probation is available in many felony DWI cases, frequently with an ignition interlock, continuous alcohol monitoring, treatment, and a period of jail time as a condition. Specialty treatment courts may also be an option for eligible clients.
""", levels=[('Third DWI', 'F3')]),

S('felony-dwi', 'Felony DWI', 'Felony DWI charges in Houston: third DWI, DWI with a child passenger, intoxication assault and intoxication manslaughter.', """
Several situations turn a DWI into a felony in Texas:

- **Two or more prior DWI convictions** (third-degree felony).
- **A passenger younger than 15** (state jail felony under § 49.045).
- **Serious bodily injury to another person** (intoxication assault, third-degree felony).
- **A death** (intoxication manslaughter, second-degree felony).

Felony DWI cases are indicted by a grand jury and heard in district court. Before indictment, we can sometimes present information to prosecutors or the grand jury that changes the charging decision. After indictment, we examine accident reconstruction, blood evidence, and causation, which are often the weakest links in the State's case.
""", levels=[('DWI with child passenger', 'SJF'), ('Third DWI / Intoxication assault', 'F3'), ('Intoxication manslaughter', 'F2')]),

S('dwi-with-0-15-bac', 'DWI With a 0.15 BAC or Higher', 'High-BAC DWI in Texas: Class A charges for 0.15 BAC or more, ignition interlock requirements, and challenging blood and breath results.', """
Since 2015, a first DWI with an alcohol concentration of 0.15 or more at the time of testing has been a Class A misdemeanor, carrying up to one year in jail and a $4,000 fine. If probation is granted, the court must require an ignition interlock. Deferred adjudication is not available when the result is 0.15 or higher.

Because the enhancement depends entirely on the number, the reliability of that number matters. We examine whether the breath instrument was properly maintained and operated, whether the two breath samples agreed, and, for blood, whether the sample was correctly collected, preserved, stored and analyzed. Retrograde extrapolation, or estimating BAC at the time of driving, is often scientifically unsupported.
""", levels=[('BAC 0.15 or more', 'A')]),

S('dwi-with-child-passenger', 'DWI With a Child Passenger', 'DWI with a child passenger under 15 is a state jail felony in Texas. Learn the penalties, CPS concerns, and defenses.', """
Driving while intoxicated with a passenger younger than 15 is a state jail felony under Penal Code § 49.045, even on a first arrest. It carries 180 days to two years in a state jail facility, a fine of up to $10,000, and a license suspension. Officers in these cases can seek a mandatory blood draw.

These arrests often bring a report to the Department of Family and Protective Services. Coordinating the criminal defense with any CPS investigation protects both your freedom and your family. We challenge the intoxication evidence, the child's age documentation, and the legality of the stop and any blood draw.
""", levels=[('DWI with child under 15', 'SJF')]),

S('intoxication-assault', 'Intoxication Assault', 'Intoxication assault charges in Houston and Fort Bend County: third-degree felony penalties, causation defenses and accident reconstruction.', """
Intoxication assault under Penal Code § 49.07 is causing serious bodily injury to another person by accident or mistake while intoxicated in a vehicle, boat, or aircraft, or while operating an amusement ride. It is a third-degree felony, and the penalty increases when the injured person is a peace officer, firefighter, or emergency medical worker on duty or when the injury causes a traumatic brain injury leading to a persistent vegetative state.

"Serious bodily injury" is a legal term meaning a substantial risk of death, serious permanent disfigurement, or protracted loss or impairment of a bodily function. Many injuries do not meet that definition. The State must also prove the intoxication caused the injury. We hire accident reconstruction experts, obtain vehicle data, and review medical records closely.
""", levels=[('Intoxication assault', 'F3'), ('Victim is first responder, or TBI resulting in vegetative state', 'F2')]),

S('dui-manslaughter', 'Intoxication Manslaughter', 'Intoxication manslaughter defense in Houston and Fort Bend County: second-degree felony penalties, causation and blood evidence.', """
When a death results from a crash involving an intoxicated driver, the charge is intoxication manslaughter under Penal Code § 49.08, a second-degree felony punishable by two to twenty years in prison. It becomes a first-degree felony if the person who died was an on-duty peace officer, firefighter, or emergency medical worker.

These cases are emotional and heavily investigated. The strongest defenses often involve causation: whether another driver's conduct, road conditions, or the deceased person's actions actually caused the collision. We retain reconstruction and toxicology experts early. Our affiliated family firm has obtained a four-year sentence in an intoxication manslaughter case where the State sought fifteen.
""", levels=[('Intoxication manslaughter', 'F2'), ('Victim was an on-duty first responder', 'F1')]),

S('administrative-license-revocation-hearing', 'ALR Hearings', 'How to save your driver license after a Houston DWI arrest: the 15-day ALR deadline, suspension lengths and hearing strategy.', """
After a DWI arrest where you refused or failed a breath or blood test, DPS will suspend your license unless you request an Administrative License Revocation hearing within **15 days** of receiving notice. The hearing is held before an administrative law judge with the State Office of Administrative Hearings.

## Suspension Lengths
- Failed test, no prior alcohol contacts: 90 days.
- Refused test, no prior alcohol contacts: 180 days.
- With prior alcohol-related contacts in the past ten years: up to one year for a failure and two years for a refusal.

## Why the Hearing Matters
At the hearing, DPS must prove reasonable suspicion for the stop, probable cause for the arrest, and either a refusal or a result of 0.08 or more. We can subpoena the arresting officer and question them under oath, which often produces valuable testimony for the criminal case. If the suspension is upheld, an occupational license may let you keep driving.
"""),

S('houston-police-department', 'HPD & Fort Bend DWI Arrests', 'How DWI arrests work with the Houston Police Department, Harris County deputies, Fort Bend County Sheriff and local police.', """
In Houston, DWI stops are made by the Houston Police Department, including officers assigned to traffic and DWI enforcement, as well as Harris County Sheriff's deputies, constable precincts, METRO police, and DPS troopers. In Fort Bend County, they are made by the Fort Bend County Sheriff's Office, constables, Sugar Land, Missouri City, Stafford, Rosenberg and Richmond police, and DPS.

Both counties run "no refusal" enforcement, where on-call judges sign blood search warrants when a driver declines a breath test. That means blood evidence is common, and the warrant affidavit itself becomes a target for challenge. Agencies differ in equipment, video retention, and testing practices, so we request records specific to the arresting department.

After arrest, people are typically booked through the Harris County Joint Processing Center downtown or the Fort Bend County Jail in Richmond before seeing a magistrate and being released on bond.
"""),

S('breathalyzers', 'Breath Tests in DWI Cases', 'How Texas DWI breath tests work, Intoxilyzer 9000 reliability, and challenging breath results in Harris and Fort Bend Counties.', """
Texas uses the Intoxilyzer 9000 for evidentiary breath testing. The test requires two samples that agree within 0.02, and a certified operator must observe the subject for at least 15 minutes beforehand to make sure nothing could contaminate the result, such as burping, vomiting, or placing something in the mouth.

Portable roadside devices are a different tool and their numbers are generally not admissible to prove a specific concentration. Breath testing assumes an average relationship between breath and blood alcohol that does not fit everyone. Conditions such as acid reflux, dental work, and residual mouth alcohol can skew results.

We obtain the instrument's maintenance, inspection and calibration records, the operator's certification, and the full test record to identify problems.
"""),

S('dwi-blood-tests', 'DWI Blood Tests', 'Challenging blood test evidence in Houston DWI cases: warrants, collection, lab analysis and chain of custody.', """
Blood tests are often treated as the gold standard, but every step creates room for error. Since the U.S. Supreme Court's decision in Missouri v. McNeely, police generally need a warrant or valid consent to draw blood. In Harris and Fort Bend Counties, warrants are often obtained quickly from on-call judges.

## Where Blood Evidence Breaks Down
- The warrant affidavit may rely on boilerplate or inaccurate observations.
- The person drawing blood must be qualified and use proper technique.
- Tubes must contain the correct preservative and anticoagulant and be stored properly.
- Lab analysis by gas chromatography requires calibration, controls, and clean batch data.
- Chain of custody must be documented from the draw to the lab.

We request the full lab file, not just the summary report, and work with independent toxicologists when needed. You may also be entitled to have the sample retested.
"""),

S('field-sobriety-test', 'Field Sobriety Tests', 'Standardized field sobriety tests in Texas DWI cases: HGN, walk-and-turn and one-leg stand, and why officers get them wrong.', """
Officers are trained to administer three standardized field sobriety tests developed by the National Highway Traffic Safety Administration: horizontal gaze nystagmus (HGN), the walk-and-turn, and the one-leg stand. Those tests are only considered reliable when given exactly as trained, on a suitable surface, to a person without conditions that affect balance.

Common problems include uneven or sloped roadside surfaces, flashing emergency lights during HGN, poor footwear, injuries, weight, age, nervousness, and instructions given incorrectly or too quickly. Body-camera and dash-camera footage often shows a different picture than the officer's report. You are not legally required to perform field sobriety tests in Texas.
"""),

S('dwi-test-refusal-and-implied-consent', 'Test Refusal & Implied Consent', 'Texas implied consent law: what happens if you refuse a breath or blood test after a DWI arrest in Houston or Fort Bend County.', """
Under Transportation Code § 724.011, anyone arrested for DWI is considered to have consented to a breath or blood test. You can still refuse, but a refusal leads to a 180-day license suspension for a first offense, can be used as evidence at trial, and often results in police seeking a blood search warrant anyway.

Officers must read the statutory warning (form DIC-24) before requesting a specimen. A refusal obtained without proper warnings, or a "consent" obtained through misleading statements, may be challenged. In certain cases, such as crashes involving serious injury or a child passenger, the law directs officers to obtain a specimen, though constitutional warrant requirements still apply.
"""),

S('dwi-penalties', 'DWI Penalties in Texas', 'Texas DWI penalties: jail ranges, fines, license suspensions, state traffic fines and ignition interlock requirements.', """
DWI penalties in Texas depend on prior convictions, the alcohol concentration, and whether anyone was injured or a child was in the vehicle. Beyond jail and fines, a conviction can bring:

- **State traffic fine:** $3,000 for a first conviction within 36 months, $4,500 for subsequent convictions, or $6,000 if the concentration was 0.16 or more.
- **License suspension:** 90 days to one year for a first conviction, longer for repeat offenses (often avoidable with an occupational license or interlock).
- **Ignition interlock:** required in many repeat and high-BAC cases.
- **Classes and community service:** DWI education, a victim impact panel, and community service hours.
- **Insurance:** SR-22 filing and higher premiums.
""", levels=[('First DWI', 'B'), ('Open container, first DWI', 'B'), ('BAC 0.15+ / Second DWI', 'A'), ('Child passenger under 15', 'SJF'), ('Third DWI / Intoxication assault', 'F3'), ('Intoxication manslaughter', 'F2')]),

S('cost-of-a-dwi', 'The Cost of a DWI', 'What a DWI really costs in Houston: bond, fines, state traffic fines, interlock, insurance and legal fees.', """
The financial impact of a DWI reaches far beyond the court fine. Typical costs include bond, towing and impound fees, fines and court costs, the state traffic fine of $3,000 to $6,000 after conviction, ignition interlock installation and monthly monitoring, DWI education classes, higher insurance premiums with an SR-22 filing, and time away from work for court settings.

A conviction can also affect employment, professional licenses, and travel. That is why a strong defense often costs less in the long run than a quick plea. We quote a flat fee for most DWI cases after a free consultation, so you know your legal cost from the start.
"""),

S('dwi-process', 'The DWI Process', 'Step-by-step guide to the DWI process in Harris and Fort Bend County, from arrest and bond to trial.', """
1. **Stop and investigation:** The officer observes driving, makes contact, and may request field sobriety tests.
2. **Arrest and testing:** You are asked for a breath or blood specimen, or a warrant is sought.
3. **Booking and magistration:** A magistrate sets bond and conditions, which may include an interlock or alcohol monitoring.
4. **ALR deadline:** You have 15 days to request an ALR hearing.
5. **First court setting:** The case is filed in a county court at law (misdemeanor) or district court (felony).
6. **Discovery and investigation:** We obtain video, reports, and test records under Article 39.14.
7. **Motions:** Suppression motions can eliminate evidence obtained unlawfully.
8. **Resolution or trial:** Dismissal, reduction, a negotiated outcome, or a jury or bench trial.
"""),

S('misdemeanor-dwi-process', 'Misdemeanor DWI Process', 'How a misdemeanor DWI moves through the Harris County and Fort Bend County court-at-law system.', """
Misdemeanor DWIs in Harris County are heard in the county criminal courts at law at the Criminal Justice Center downtown. In Fort Bend County, they are heard in the county courts at law at the Justice Center in Richmond. Cases typically take several months, with multiple settings while discovery is exchanged and lab results are completed.

Bond conditions can include reporting, no alcohol, and an interlock. We often handle routine settings without the client needing to miss work, though you must appear when the court requires. Throughout the case we evaluate suppression motions, diversion eligibility, and whether a trial gives you the best result.
"""),

S('dwi-reduction-and-dismissal', 'DWI Reduction & Dismissal', 'How DWI charges get reduced or dismissed in Houston and Fort Bend County.', """
DWI cases are dismissed or reduced when the evidence does not hold up. Common reasons include an unlawful stop, an arrest without probable cause, field sobriety tests that were improperly given, breath-test procedure failures, blood-draw or lab problems, and video that contradicts the report.

Reductions may include obstructing a highway, reckless driving, or other non-DWI offenses that avoid the state traffic fine, the DWI label, and enhancement for future cases. Each prosecutor's office has its own policies, so knowing the local practices in Harris and Fort Bend Counties matters.
"""),

S('dwi-deferred-adjudication', 'DWI Deferred Adjudication', 'Deferred adjudication for DWI in Texas: eligibility, interlock requirements and nondisclosure.', """
Since September 1, 2019, judges may grant deferred adjudication in many DWI cases. With deferred, there is no conviction if you complete the terms, and the case is dismissed.

Deferred is not available to people who held a commercial driver's license at the time of the offense or who had an alcohol concentration of 0.15 or more. The court must require an ignition interlock as a condition. A deferred DWI still counts as a prior if you are arrested again, and it may qualify for an order of nondisclosure after a waiting period.
"""),

S('dwi-pre-trial-diversion-program', 'DWI Pretrial Diversion', 'DWI pretrial diversion and intervention programs in Harris and Fort Bend Counties: eligibility and benefits.', """
Pretrial diversion, sometimes called pretrial intervention, is an agreement with the prosecutor that pauses the case while you complete conditions such as classes, community service, and monitoring. If you complete the program, the case is dismissed and may be eligible for expunction.

Eligibility and availability for DWI cases vary by county and change with prosecutor policy. Generally, first-time arrests without an accident, a high BAC, or aggravating factors are the strongest candidates. We assess whether you qualify and advocate for admission.
"""),

S('dwi-probation', 'DWI Probation', 'What DWI probation (community supervision) looks like in Harris and Fort Bend County.', """
Community supervision lets you serve a sentence in the community instead of jail. For a misdemeanor DWI, probation may last up to two years. Common conditions include reporting to a probation officer, fees, a DWI education program, a victim impact panel, community service, alcohol evaluation and treatment, and in many cases an ignition interlock.

Violations can lead to a motion to revoke and jail time. If you are struggling with conditions, contact us early. Courts are often willing to modify terms when a lawyer explains the situation before a violation is filed.
"""),

S('dwi-court-program', 'DWI Specialty Courts', 'DWI and sobriety specialty court programs in Harris and Fort Bend Counties for eligible repeat offenders.', """
Harris and Fort Bend Counties operate specialty treatment courts designed for people whose cases are connected to substance use. These programs combine intensive supervision, treatment, frequent testing, and regular appearances before a judge.

For eligible clients, especially those facing a repeat DWI, a specialty court can offer a path that avoids long jail or prison sentences and addresses the underlying issue. Programs are demanding, so we discuss whether one fits your circumstances before you apply.
"""),

S('occupational-drivers-license', 'Occupational Driver License', 'How to get an occupational driver license in Texas after a DWI suspension in Houston or Fort Bend County.', """
An occupational driver license (sometimes called an essential need license) lets you drive during a suspension for work, school, and household duties. It is obtained by filing a petition in court and then submitting the order to DPS with proof of SR-22 insurance.

Orders typically limit driving to certain hours and purposes and may require an ignition interlock. When an interlock is ordered, many time-of-day restrictions do not apply, and in many cases the usual waiting period can be avoided. We prepare and file petitions as part of our DWI representation.
"""),

S('ignition-interlock-devices', 'Ignition Interlock Devices', 'When Texas courts require an ignition interlock after a DWI and how to comply.', """
An ignition interlock is a breath-testing device installed in your vehicle that prevents it from starting if it detects alcohol, and that requires periodic retests while driving. Texas law requires an interlock as a bond condition for repeat DWI and intoxication assault or manslaughter charges, as a condition of DWI deferred adjudication, and for probation in high-BAC cases. Judges may order one in other cases too.

Violations, including missed retests or readings from mouthwash or food, are reported to the court. We help clients understand the reporting rules and respond quickly when a reading is disputed.
"""),

S('scram-and-alcohol-monitoring', 'SCRAM & Alcohol Monitoring', 'SCRAM ankle monitors and portable alcohol monitors as DWI bond and probation conditions in Houston.', """
Courts may order continuous alcohol monitoring through a transdermal ankle device, or a portable breath device that requires tests at scheduled times. These conditions are common in repeat DWI cases and when a high BAC is alleged.

Monitoring can be costly and invasive. After a period of compliance, we can ask the court to remove or reduce monitoring conditions. When a reading is alleged, we review the raw data, because environmental alcohol and device errors can produce false alerts.
"""),

S('dwi-terms', 'DWI Terms Glossary', 'Glossary of common Texas DWI terms: BAC, ALR, SFST, HGN, DIC-24, interlock, nondisclosure and more.', """
- **BAC:** Blood or breath alcohol concentration. The per se limit is 0.08.
- **ALR:** Administrative License Revocation, the DPS license suspension process.
- **DIC-24:** The statutory warning read before requesting a breath or blood specimen.
- **SFSTs:** Standardized field sobriety tests: HGN, walk-and-turn and one-leg stand.
- **HGN:** Horizontal gaze nystagmus, an involuntary jerking of the eyes.
- **Loss of normal use:** The non-numeric definition of intoxication.
- **Interlock:** A breath device that prevents a vehicle from starting after alcohol consumption.
- **Occupational license:** A restricted license to drive during a suspension.
- **Deferred adjudication:** Supervision without a conviction if completed.
- **Nondisclosure:** An order sealing certain records from public view.
- **Retrograde extrapolation:** Estimating BAC at the time of driving from a later test.
"""),

S('dwi-faq', 'DWI FAQ', 'Answers to frequently asked questions about DWI arrests in Houston and Fort Bend County.', """
Here are answers to questions DWI clients in Houston, Sugar Land, Richmond and Katy ask most often.
""", faq=[
  ('Will I lose my license after a DWI arrest?', 'Possibly, unless you request an ALR hearing within 15 days. Even if a suspension is upheld, you may qualify for an occupational license.'),
  ('Can I get a DWI if I was under 0.08?', 'Yes. Texas also defines intoxication as losing the normal use of your mental or physical faculties, so a DWI can be charged below 0.08.'),
  ('Should I have refused the breath test?', 'A refusal carries a longer license suspension and can be used as evidence, but it may also limit the State\'s scientific evidence. Every case is different; what matters now is reviewing what actually happened.'),
  ('Is jail mandatory for a first DWI?', 'The law sets a 72-hour minimum if jail is imposed, but many first-time clients receive probation, deferred adjudication, or a reduction instead.'),
  ('Can a DWI be expunged?', 'Only if the case is dismissed, no-billed or results in acquittal. A first DWI that ends in conviction or deferred may qualify for nondisclosure instead.'),
]),

S('dwi-and-unlawful-possession-of-a-weapon', 'DWI and Carrying a Weapon', 'DWI arrests involving a handgun in Texas: unlawful carrying charges and License to Carry consequences.', """
Texas permits most adults 21 and older to carry a handgun without a license, but carrying a handgun in a vehicle while committing another offense, such as DWI, can result in a separate Class A charge for unlawfully carrying a weapon. License to Carry holders who carry while intoxicated face their own Class A offense and possible suspension or revocation of the license.

When a weapon is involved, prosecutors often treat the DWI more seriously. Defeating or reducing the DWI can also defeat the weapons charge, so we defend the two together.
""", levels=[('Unlawful carrying while committing DWI', 'A')]),

S('drug-related-dwi', 'Drug-Related DWI', 'DWI charges based on prescription drugs, marijuana or other substances in Houston and Fort Bend County.', """
A DWI does not require alcohol. Texas law covers intoxication by any controlled substance, drug, dangerous drug, or combination. Unlike alcohol, there is no per se legal limit for most drugs, so the State must prove you lost the normal use of your faculties.

Drug-DWI cases often rely on a Drug Recognition Expert evaluation and a blood test. Blood results can show a substance was present without showing impairment at the time of driving. We challenge the DRE protocol, the lab's methods, and the link between the substance and the driving.
"""),

S('marijuana-dwi', 'Marijuana DWI', 'Defending DWI charges based on marijuana or THC in Houston and Fort Bend County.', """
THC can remain in blood long after any impairment has worn off, especially in regular users. Because Texas has no per se THC limit for driving, the State must prove marijuana actually caused a loss of normal use. Field sobriety tests designed for alcohol are not validated for marijuana impairment.

Hemp-derived products, which are legal in Texas when they meet the THC limits, add another layer: lab reports may not distinguish legal from illegal sources. We examine the officer's observations, any DRE evaluation, and the toxicology carefully.
"""),

S('prescription-dwi', 'Prescription Drug DWI', 'DWI charges involving lawfully prescribed medication in Texas and how to defend them.', """
Having a valid prescription is not a defense to DWI by itself, but it often explains behavior officers misread as impairment. Many medications, including sleep aids, anxiety medications, and pain relievers, are taken safely at therapeutic doses.

We gather the prescription history, physician input, and pharmacology expertise to show whether the level detected was consistent with normal use and whether it plausibly caused impairment. Medical conditions such as diabetes, neurological issues, and fatigue can also mimic intoxication.
"""),

S('under-the-limit-dwi', 'Under-the-Limit DWI', 'Can you be charged with DWI under 0.08 in Texas? How loss-of-normal-use cases are defended.', """
Yes. When a breath or blood result comes back below 0.08, prosecutors may still proceed on the theory that you lost the normal use of your mental or physical faculties. These cases rely almost entirely on the officer's observations and video.

That makes them very defensible. A low test result is strong evidence in your favor, and video often shows clear speech and steady movement that contradict the report. We use the officer's own training standards to expose subjective conclusions.
"""),

S('auto-brewery-syndrome-in-texas-dwi-cases', 'Auto-Brewery Syndrome', 'Auto-brewery syndrome as a defense in Texas DWI cases: what it is and how it is proven.', """
Auto-brewery syndrome is a rare medical condition in which yeast in the digestive tract ferments carbohydrates into alcohol, raising a person's alcohol level without drinking. It has been documented in medical literature and raised in DWI cases.

The defense requires credible medical evidence, usually testing and diagnosis by a physician, along with toxicology that fits the explanation. We evaluate whether the facts support it and work with medical experts when they do. Other conditions, including GERD and diabetes, can also affect breath testing.
"""),

S('dwi-with-property-damage', 'DWI With an Accident or Property Damage', 'DWI arrests after a crash in Houston: property damage, restitution and enhanced investigation.', """
A crash does not change the basic DWI offense level when no one is seriously hurt, but it changes how the case is investigated and negotiated. Officers often arrive after the fact, so they did not see the driving, and injuries from the collision can mimic signs of intoxication. Airbag deployment, shock, and head injuries affect field sobriety testing.

Prosecutors may seek restitution for damage and may be less willing to offer diversion. We review crash reports, scene photos, vehicle data, and timing to test whether the State can prove you were intoxicated when you were driving.
"""),

S('obstruction-of-a-highway', 'Obstruction of a Highway', 'Obstructing a highway as a reduced charge in Texas DWI cases.', """
Obstructing a highway or other passageway under Penal Code § 42.03 is a Class B misdemeanor that is sometimes negotiated in place of a DWI. Although the offense level matches a first DWI, it avoids the DWI label, the state traffic fine, automatic license consequences, and use as a DWI enhancement in the future.

Whether this reduction is realistic depends on the evidence and the prosecutor's policies. A strong defense investigation is what creates the leverage to obtain it.
""", levels=[('Obstructing a highway', 'B')]),

S('commercial-dwi', 'Commercial Driver DWI', 'DWI charges for CDL holders in Texas: 0.04 limits, disqualification and protecting your livelihood.', """
Commercial drivers face stricter rules. The alcohol limit while operating a commercial motor vehicle is 0.04. A DWI conviction or a test refusal, even in a personal vehicle, can disqualify a CDL holder for one year (three years if transporting hazardous materials), and a second offense can lead to lifetime disqualification.

CDL holders are also not eligible for DWI deferred adjudication and cannot obtain an occupational license to drive a commercial vehicle. Because the stakes are a career, we fight both the ALR suspension and the criminal case aggressively.
"""),

S('bwi', 'Boating While Intoxicated', 'Boating while intoxicated charges on Lake Houston, Galveston Bay and other Texas waters.', """
Boating while intoxicated under Penal Code § 49.06 applies to operating a watercraft while intoxicated. It is a Class B misdemeanor for a first offense and is enhanced like DWI with prior convictions. Texas Parks and Wildlife game wardens and local marine units patrol Lake Houston, Lake Conroe, Clear Lake, and Galveston Bay.

Sun, wind, wave motion, and fatigue all affect balance and appearance on the water, which makes standard field sobriety tests unreliable. Officers sometimes use seated tests that are not standardized. We challenge the stop, the testing, and whether the person was actually operating the vessel.
""", levels=[('First BWI', 'B'), ('BWI with prior', 'A')]),

S('flying-while-intoxicated', 'Flying While Intoxicated', 'Flying while intoxicated charges in Texas and FAA consequences for pilots.', """
Operating an aircraft while intoxicated is an offense under Penal Code § 49.05, a Class B misdemeanor for a first offense. Federal rules separately prohibit acting as a crew member within eight hours of drinking or with a concentration of 0.04 or more.

Pilots also face FAA reporting obligations and certificate actions, so the criminal and regulatory issues must be handled together. See our page on [pilot license consequences](/dwi-dui/professional-licenses/pilot-license-revocation/).
""", levels=[('First FWI', 'B')]),

S('underage-dwi', 'Underage DWI', 'DUI and DWI charges for drivers under 21 in Texas: zero tolerance, license suspension and record protection.', """
Texas has a zero-tolerance policy for drivers under 21. A minor who operates a vehicle with any detectable amount of alcohol can be charged with Driving Under the Influence by a Minor (DUI) under the Alcoholic Beverage Code, a Class C offense that still carries a license suspension, alcohol education, and community service.

If the State believes the minor was intoxicated, it may instead file a DWI, which carries adult penalties. A first DUI by a minor may be expunged if certain conditions are met. Early defense protects school, scholarships and future employment.
""", levels=[('DUI by a minor (first)', 'C'), ('DWI by a person under 21', 'B')]),

S('student-dwi', 'Student DWI', 'DWI defense for college students at UH, TSU, Rice, HCC and other Houston-area schools.', """
A DWI arrest can affect enrollment, scholarships, campus housing, study-abroad plans, and professional school applications. Students at the University of Houston, Texas Southern University, Rice University, Houston Community College, and other schools may also face campus discipline.

We work toward outcomes that keep a conviction off the record, such as dismissal, diversion, or a reduction, and we advise on how to answer application questions about arrests honestly and accurately.
"""),

S('defending-women', 'Defending Women Charged With DWI', 'DWI defense considerations for women in Houston and Fort Bend County.', """
Women charged with DWI face the same law, but some practical factors deserve attention. Footwear such as heels or sandals can affect walk-and-turn and one-leg-stand performance, and many officers do not offer an alternative. Medications, hormonal changes and medical conditions can influence how alcohol is absorbed and how breath tests read.

Many of our clients are also balancing careers and caregiving. We focus on resolutions that protect licenses, employment, and family responsibilities, and we handle routine settings to reduce time away from home.
"""),

S('expunging-dwi-records', 'Expunging DWI Records', 'When a Texas DWI arrest can be expunged and how the process works in Harris and Fort Bend County.', """
An expunction erases the arrest record and allows you to deny it in most situations. A DWI arrest can be expunged if the case was dismissed (subject to certain conditions and waiting periods), no-billed by a grand jury, or ended in acquittal, or after completing a pretrial diversion program.

A DWI that ended in conviction or deferred adjudication cannot be expunged, but may qualify for nondisclosure. See [Sealing DWI Records](/dwi-dui/sealing-dwi-records/) and [Expunctions & Record Sealing](/expunctions-record-sealing/).
"""),

S('sealing-dwi-records', 'Sealing DWI Records', 'Orders of nondisclosure for first-time DWI convictions and deferred adjudication in Texas.', """
Texas allows certain first-time DWI offenders to seal their records with an order of nondisclosure. Generally, the offense must have been a first DWI with a concentration below 0.15, without an accident involving another person, and the person must have completed their sentence and the required waiting period. The waiting period is shorter if an ignition interlock was used for at least six months.

A nondisclosure order prevents most private employers and landlords from seeing the record through public databases, although law enforcement and certain licensing agencies can still access it.
"""),

S('professional-licenses', 'DWI & Professional Licenses', 'How a DWI affects nurses, doctors, teachers, pilots and military members in Texas.', """
For licensed professionals, the consequences of a DWI can be more serious than the court sentence. Many licensing boards require self-reporting, review arrests as well as convictions, and evaluate substance-use concerns.

We coordinate the criminal defense with licensing strategy so that the outcome of the case, and how it is described to your board, protects your career. See the pages below for specific professions.
""", hub=True, hub_label='Professions'),
S('professional-licenses/nursing-license-revocation', 'DWI and Nursing Licenses', 'How a DWI affects Texas nursing licenses and Board of Nursing reporting.', """
The Texas Board of Nursing considers criminal history in licensing and renewal and asks nurses about arrests and convictions. Alcohol-related offenses can lead to board inquiries, peer assistance referrals, or conditions on a license.

Answering board questions accurately is critical; incomplete answers can create more trouble than the underlying case. We pursue outcomes, such as dismissal or diversion, that minimize what must be reported.
"""),
S('professional-licenses/medical-license-revocation', 'DWI and Medical Licenses', 'DWI consequences for physicians and Texas Medical Board licensure.', """
Physicians licensed by the Texas Medical Board may face questions about alcohol-related arrests at renewal and in hospital credentialing. A pattern of alcohol offenses can prompt evaluation or monitoring through physician health programs.

We work to resolve the criminal case in a way that limits professional fallout and advise on accurate disclosures to the board and employers.
"""),
S('professional-licenses/teaching-certification-revocation', 'DWI and Teaching Certificates', 'How DWI arrests affect Texas educator certification and school employment.', """
Texas educators are subject to criminal history review by the State Board for Educator Certification and their districts. Districts in Houston ISD, Fort Bend ISD, Katy ISD and elsewhere may receive notice of arrests through fingerprint-based monitoring.

An alcohol offense on its own does not always threaten certification, but how the case is resolved and reported matters. We focus on outcomes that keep your record and career intact.
"""),
S('professional-licenses/pilot-license-revocation', 'DWI and Pilot Certificates', 'FAA reporting requirements for pilots after a DWI arrest or license suspension.', """
Pilots must report alcohol-related motor vehicle actions, including DWI convictions and administrative license suspensions, to the FAA's Security and Investigations Division within 60 days. Medical certificate applications also ask about these events.

Failing to report can itself lead to certificate action. We help pilots meet reporting deadlines while defending the criminal case and the ALR suspension.
"""),
S('professional-licenses/active-military-members-charged-with-dwi', 'Military Members Charged With DWI', 'DWI defense for active-duty service members and veterans in Houston and Fort Bend County.', """
Service members arrested off base are prosecuted in civilian court, but a DWI may also be reported to the command and affect security clearances, promotions, and base driving privileges. Veterans may be eligible for veterans treatment court programs in Harris or Fort Bend County.

We coordinate with clients on command reporting and pursue resolutions that limit both civilian and military consequences.
"""),
]
