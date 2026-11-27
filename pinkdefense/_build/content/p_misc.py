from mk import P
def mk(cat):
    def S(slug, title, desc, body, levels=None, faq=None, **kw):
        return P(f'{cat}/{slug}', title, desc, body, levels, faq, cat=cat, **kw)
    return S
T = mk('serious-traffic-offenses'); AL = mk('alcohol-offenses'); AR = mk('arrests'); ST = mk('student-defense')
EX = mk('expunctions-record-sealing'); JR = mk('jail-release'); TP = mk('texas-criminal-process'); MI = mk('misdemeanors'); FE = mk('felonies')

PAGES = [
# ---------------- Serious traffic ----------------
P('serious-traffic-offenses', 'Serious Traffic Offenses', 'Houston and Fort Bend County serious traffic offense lawyer: failure to stop and render aid, evading in a vehicle, racing, reckless driving and suspended license.', hub=True,
  h1='Houston & Fort Bend Serious Traffic Offense Lawyer', hub_label='Traffic Offense Topics', body="""
Some traffic cases are far more than tickets. Leaving the scene of a crash, evading police in a vehicle, street racing, and driving while your license is invalid can lead to jail, felony records, and long license suspensions.

Houston's roads, from the Southwest Freeway to the Grand Parkway, see heavy enforcement by HPD, the Harris County Sheriff's Office, constables, Fort Bend County deputies, and DPS. We obtain dash-camera and body-camera footage, crash reports, and vehicle data to build a defense.
"""),
T('failing-to-stop', 'Failure to Stop and Render Aid', 'Failure to stop and render aid (hit and run) charges in Houston and Fort Bend County.', """
A driver involved in a crash that results in injury or death must stop, return to the scene, give their information, and render reasonable assistance. Failing to do so is a felony under Transportation Code § 550.021, with the most serious penalties when a death results.

The State must prove the driver knew a crash occurred and knew or should have known someone was injured. Darkness, weather, panic, and fear for one's own safety are relevant to that question.
""", hub=True, hub_label='Related Topics'),
T('failing-to-stop/injury-or-death', 'Leaving the Scene: Injury or Death', 'Felony leaving the scene of an accident involving injury or death in Texas.', """
When a crash causes serious bodily injury or death and a driver leaves, prosecutors pursue felony charges and often seek prison time. These cases also bring civil liability, and the person may face separate intoxication or manslaughter charges.

We reconstruct the timeline and investigate what the driver actually perceived. In some cases, the driver did stop or return, or the information given satisfied the statute.
"""),
T('accidents-involving-vehicles', 'Leaving the Scene: Vehicle Damage', 'Leaving the scene of an accident with vehicle damage in Texas: misdemeanor penalties.', """
When a crash damages only an attended vehicle, the driver must stop and exchange information. Failing to do so is a Class C misdemeanor if the damage is under $200 and a Class B misdemeanor if it is $200 or more.

Disputes over the amount of damage, whether the driver knew contact occurred, and whether information was exchanged are common defense issues.
""", [('Damage under $200', 'C'), ('Damage $200 or more', 'B')]),
T('duty-on-striking-unattended-vehicle', 'Striking an Unattended Vehicle', 'Duty on striking an unattended vehicle in Texas: notice requirements and penalties.', """
A driver who hits an unattended vehicle must stop and either locate the owner or leave a written note with their name and address. Failing to do so is a Class C misdemeanor for damage under $200 and a Class B misdemeanor for damage of $200 or more.
""", [('Damage under $200', 'C'), ('Damage $200 or more', 'B')]),
T('duty-on-striking-fixture', 'Striking a Fixture or Highway Landscaping', 'Duty on striking a fixture or highway landscaping in Texas.', """
Drivers who damage fixtures, signs, fences, or landscaping on or near a highway must take reasonable steps to notify the owner and, in some cases, report to police. Penalties depend on the amount of damage, similar to other leaving-the-scene offenses.
""", [('Damage under $200', 'C'), ('Damage $200 or more', 'B')]),
T('motor-vehicle-accidents-involving-injury', 'Crashes Involving Injury', 'Criminal exposure after a car crash involving injury in Houston.', """
A crash that injures someone can lead to criminal charges ranging from failure to stop and render aid, to intoxication assault, to manslaughter, depending on the facts. It also creates civil liability.

If you were involved in a serious crash, speak with a lawyer before giving a recorded statement to police or an insurance company. We coordinate the criminal defense with the insurance and civil issues.
"""),
T('evading-arrest-in-vehicle', 'Evading Arrest in a Vehicle', 'Evading arrest or detention in a vehicle in Texas: felony penalties and defenses.', """
Intentionally fleeing in a vehicle from a person you know is a peace officer attempting a lawful arrest or detention is a felony in Texas, and the penalty increases with prior convictions or if someone is seriously injured or killed.

The State must prove you knew an officer was trying to stop you and that the attempted detention was lawful. Delayed pull-overs to find a safe location are not evading.
"""),
T('racing', 'Street Racing', 'Racing on a highway charges in Houston and Fort Bend County.', """
Racing on a highway, including drag races, speed competitions, and "takeovers," is a Class B misdemeanor. It becomes a Class A misdemeanor with a prior conviction or open container, a state jail or third-degree felony if someone is injured, and a second-degree felony if someone dies. Vehicles can be seized in some cases.

Houston has increased enforcement against street takeovers. Identification of drivers and proof of an actual race are central issues.
""", [('First offense', 'B'), ('Prior conviction or open container', 'A'), ('Serious bodily injury', 'F3'), ('Death', 'F2')]),
T('reckless-driving', 'Reckless Driving', 'Reckless driving charges in Texas: penalties and use as a reduced charge.', """
Reckless driving is driving in wilful or wanton disregard for the safety of persons or property. It is a misdemeanor punishable by up to 30 days in jail and a fine of up to $200. It is sometimes negotiated as a reduction from more serious offenses, including DWI.
"""),
T('driving-while-license-invalid-or-suspended', 'Driving While License Invalid', 'Driving while license invalid or suspended charges in Houston and Fort Bend County.', """
Driving while your license is suspended or invalid is usually a Class C misdemeanor for a first offense. It becomes a Class B misdemeanor with a prior conviction, if you had no insurance at the time, or if the suspension resulted from certain offenses, and it can become more serious if a crash causes injury.

Many people do not know their license was suspended. We help clients resolve the underlying suspension, obtain an occupational license if needed, and resolve the charge.
""", [('First offense, in most cases', 'C'), ('Prior conviction or no insurance', 'B')]),

# ---------------- Alcohol ----------------
P('alcohol-offenses', 'Alcohol Offenses', 'Underage drinking, minor in possession, fake ID and public intoxication defense in Houston and Fort Bend County.', hub=True,
  h1='Houston Alcohol Offense Lawyer', hub_label='Alcohol Offense Topics', body="""
Alcohol-related offenses are common around Houston's nightlife districts, college campuses, concerts, and sporting events. Most are misdemeanors, but they still create a criminal record and, for minors, can mean license suspensions and school discipline.

Most first-time alcohol offenses can be resolved through deferred disposition, classes, or dismissal, followed by expunction. Handling the case correctly the first time matters, because repeat offenses lose those options.
"""),
AL('public-intoxication', 'Public Intoxication', 'Public intoxication charges in Houston: Class C penalties and keeping a clean record.', """
Public intoxication is appearing in a public place while intoxicated to the degree that you may endanger yourself or others. It is a Class C misdemeanor, punishable by a fine. Minors face additional consequences under the Alcoholic Beverage Code.

Officers make these arrests based on judgment calls. We challenge whether the person was actually a danger and pursue dismissal or deferred disposition followed by expunction.
""", [('Public intoxication', 'C')]),
AL('minor-in-possession', 'Minor in Possession', 'Minor in possession of alcohol charges in Texas: penalties and expunction.', """
A person under 21 who possesses alcohol commits a Class C misdemeanor, with exceptions for possession in the presence of a parent, guardian, or spouse who is an adult, and for certain employment. Penalties can include a fine, alcohol awareness classes, community service, and a driver license suspension.

First offenses are often eligible for deferred disposition and later expunction.
""", [('First or second offense', 'C')], hub=True, hub_label='Related Topics'),
AL('minor-in-possession/underage-drinking', 'Underage Drinking', 'Underage drinking charges in Houston and Fort Bend County.', """
Underage drinking charges include possession, consumption, purchase, and driving under the influence by a minor. A third offense can carry jail time and is not eligible for deferred disposition.

Parents should know that these cases can affect scholarships and college admissions. We focus on outcomes that leave no permanent record.
"""),
AL('minor-in-consumption', 'Minor in Consumption', 'Minor in consumption of alcohol charges in Texas.', """
Consuming alcohol under 21 is a Class C misdemeanor, with similar exceptions and consequences as possession. The State must prove the person actually consumed alcohol, often through officer observations or admissions.
""", [('First or second offense', 'C')]),
AL('furnishing-alcohol-to-minors', 'Furnishing Alcohol to Minors', 'Furnishing alcohol to a minor charges in Texas: Class A misdemeanor defense.', """
Purchasing alcohol for or giving alcohol to a person under 21 is a Class A misdemeanor, with an exception for a parent, guardian, or spouse who is visibly present. Making alcohol available at a party can also lead to charges, and to civil liability if someone is hurt.
""", [('Furnishing alcohol to a minor', 'A')]),
AL('misrepresentation-of-age', 'Misrepresentation of Age', 'Misrepresentation of age by a minor to buy alcohol in Texas.', """
A minor who falsely states they are 21 or older, or presents false identification, to obtain alcohol commits a Class C misdemeanor. Using a false ID can also lead to more serious charges.
""", [('Misrepresentation of age', 'C')]),
AL('possession-of-a-fictitious-license', 'Possession of a Fictitious License', 'Possession of a fictitious or altered driver license in Texas.', """
Possessing a fictitious, altered, or borrowed driver license or ID card can be charged under the Transportation Code or the Penal Code. Penalties range from a Class C misdemeanor for some underage cases to a Class A misdemeanor or felony for manufacturing or possessing with intent to use.
"""),
AL('possession-of-fake-id', 'Possession of a Fake ID', 'Fake ID charges in Houston: penalties for students and young adults.', """
Fake ID charges are common near college campuses and bars. Depending on the facts, prosecutors may charge a Class A misdemeanor under the Transportation Code or a more serious offense for manufacturing or selling.

Because a misdemeanor conviction can affect admissions and employment, we work toward dismissal or reduction and expunction.
""", [('Possession of a fake license', 'A')]),

# ---------------- Arrests ----------------
P('arrests', 'Arrests & Police Encounters', 'Your rights during an arrest in Houston and Fort Bend County: searches, resisting arrest, evading and failure to identify charges.', hub=True,
  h1='Arrests & Police Encounters', hub_label='Arrest Topics', body="""
What happens during an arrest often decides the outcome of the case. Unlawful stops, searches without consent or a warrant, and statements taken without proper warnings can all lead to evidence being suppressed.

You have the right to remain silent and the right to refuse consent to a search. Exercise those rights politely, do not physically resist, and ask for a lawyer. Then call us at (832) 979-0882.
"""),
AR('search-and-seizures', 'Searches & Seizures', 'Illegal search and seizure defenses in Texas criminal cases.', """
The Fourth Amendment and Article I, Section 9 of the Texas Constitution protect against unreasonable searches and seizures. Police generally need a warrant to search a home or phone. Vehicle searches require probable cause, consent, or another recognized exception.

When police violate these rules, Article 38.23 of the Code of Criminal Procedure requires exclusion of the evidence, and Texas juries can be instructed to disregard illegally obtained evidence. Motions to suppress are among the most powerful tools in a criminal defense.
"""),
AR('resisting-arrest', 'Resisting Arrest', 'Resisting arrest, search or transport charges in Houston and Fort Bend County.', """
Intentionally preventing or obstructing a peace officer from making an arrest, search, or transport by using force against the officer is a Class A misdemeanor, and a third-degree felony if a deadly weapon is used. It is not a defense that the arrest itself was unlawful, but pulling away or going limp may not amount to force against the officer.
""", [('Resisting arrest', 'A'), ('Using a deadly weapon', 'F3')]),
AR('evading-arrest-or-detention', 'Evading Arrest or Detention', 'Evading arrest on foot in Texas: penalties and defenses.', """
Intentionally fleeing from a person you know is a peace officer attempting a lawful arrest or detention is a Class A misdemeanor when on foot. Fleeing in a vehicle is a felony.

If the officer had no lawful basis to detain you, the State cannot prove this offense. Knowledge that the person was an officer is also required.
""", [('Evading on foot', 'A')]),
AR('fleeing-or-eluding', 'Fleeing a Police Officer', 'Fleeing or attempting to elude a police officer under the Texas Transportation Code.', """
Fleeing or attempting to elude a police officer under Transportation Code § 545.421 involves wilfully failing to stop a vehicle when given a visual or audible signal by a uniformed officer in a marked vehicle. It is generally a Class B misdemeanor, separate from felony evading arrest in a vehicle.
""", [('Fleeing or eluding', 'B')]),
AR('failure-to-identify', 'Failure to Identify', 'Failure to identify and giving false information to police in Texas.', """
In Texas, you are generally not required to identify yourself to an officer unless you have been lawfully arrested. Refusing to give your name, address, or date of birth after a lawful arrest is a Class C misdemeanor. Giving a false name or information to an officer who has lawfully arrested or detained you is a Class B misdemeanor, and more serious if you are a fugitive.
""", [('Refusing after lawful arrest', 'C'), ('Giving false information', 'B')]),
AR('interference-with-public-duties', 'Interference With Public Duties', 'Interference with public duties charges in Houston: what counts and defenses.', """
Interfering with a peace officer, emergency medical worker, or firefighter performing duties is a Class B misdemeanor. Speech alone is a defense under the statute, so arguing with or criticizing an officer is not a crime by itself, and recording police from a reasonable distance is generally protected.
""", [('Interference with public duties', 'B')]),
AR('spring-break-arrests', 'Spring Break Arrests', 'Spring break arrests in Galveston, South Padre and Texas beach towns: what to do from Houston.', """
Every spring, students and young adults from Houston are arrested in Galveston, South Padre Island, and other Texas destinations for public intoxication, minor in possession, drug possession, and DWI. Many leave town assuming the case will go away; it will not, and missed court dates lead to warrants.

We can often handle out-of-town cases with minimal travel for the client. See [Out-of-County Offenders](/out-of-county-offenders/).
"""),

# ---------------- Student ----------------
P('student-defense', 'Student Defense', 'Criminal defense for college students in Houston: UH, TSU, Rice, HCC and campus disciplinary proceedings.', hub=True,
  h1='Houston Student Defense Lawyer', hub_label='Student Defense Topics', body="""
Houston is home to the University of Houston, Texas Southern University, Rice University, Houston Community College, the University of St. Thomas, Houston Christian University, and many other schools, and Fort Bend County families send students across the state. A criminal case can threaten a student's enrollment, scholarships, financial aid, campus housing, and future licensing.

Many students are eligible for diversion and expunction, which allows them to move forward with a clean record. We also guide students and families through campus conduct processes.
"""),
ST('university-disciplinary-hearings', 'University Disciplinary Hearings', 'Student conduct hearings at Houston-area universities: protecting your enrollment and your criminal case.', """
Universities run their own conduct processes for alleged violations of student codes, often at the same time as a criminal case. Statements made in a campus hearing can be used by prosecutors.

We help students prepare, review the evidence, and coordinate the school process with the criminal defense so that one does not damage the other.
"""),
ST('note-to-parents', 'A Note to Parents', 'Guidance for parents of a student arrested in Houston or Fort Bend County.', """
A call that your child has been arrested is frightening. The most important first steps are to help them stay silent about the facts, avoid social media, and get a lawyer involved quickly.

Our attorney-client relationship is with the student, even when parents pay the fee, but with the student's permission we keep families informed and involved.
"""),
ST('hazing', 'Hazing', 'Hazing charges under the Texas Education Code: penalties for students and organizations.', """
Texas criminalizes hazing under the Education Code, including participating in, encouraging, or failing to report hazing. Penalties range from a Class B misdemeanor to a state jail felony when hazing causes death. Organizations can also be prosecuted.

Hazing cases can involve many students and complex group dynamics. Immunity may be available for people who report or cooperate.
""", [('Hazing (most cases)', 'B'), ('Causing bodily injury', 'A'), ('Causing death', 'SJF')]),
ST('false-alarm-or-report', 'False Alarm or Report', 'False alarm, false report and hoax threat charges involving schools in Texas.', """
Knowingly making a false report of a bomb, fire, or other emergency is a Class A misdemeanor, and a state jail felony when it involves a school, public building, or public transportation. Threats posted online can lead to these charges or terroristic threat charges, as well as school discipline.

Context and intent matter. Jokes and misunderstandings are frequently treated as threats, and the response must be measured.
""", [('False alarm or report', 'A'), ('Involving a school or public facility', 'SJF')]),

# ---------------- Expunctions ----------------
P('expunctions-record-sealing', 'Expunctions & Record Sealing', 'Houston and Fort Bend County expunction and nondisclosure lawyer: clear or seal Texas arrest records.', hub=True,
  h1='Houston Expunction & Record Sealing Lawyer', hub_label='Record Clearing Topics', body="""
An old arrest can show up on background checks for jobs, apartments, and professional licenses long after the case ended. Texas offers two remedies: expunction, which destroys records and allows you to deny the arrest in most situations, and an order of nondisclosure, which seals records from most of the public.

## Who May Qualify for Expunction
- Cases that were dismissed, subject to certain conditions.
- Cases that were no-billed by a grand jury.
- Acquittals at trial.
- Completion of a pretrial diversion program.
- Class C deferred disposition.

## Who May Qualify for Nondisclosure
- Many people who completed deferred adjudication.
- Certain first-time misdemeanor convictions, including some first DWIs.

Some offenses, including family violence and many sex offenses, are excluded. We review your complete history and handle filings in Harris County, Fort Bend County, and other Texas counties.
"""),
EX('expunction-process', 'The Expunction Process', 'How the Texas expunction process works in Harris and Fort Bend County.', """
1. We obtain your criminal history and court records to confirm eligibility and waiting periods.
2. We prepare a verified petition listing every agency that holds records of the arrest.
3. The petition is filed in district court and served on the agencies.
4. A hearing is set, and the State may agree or object.
5. The judge signs the order, and agencies must return or destroy the records.

The process usually takes several months. We follow up to confirm compliance by private background-check companies as well.
"""),
EX('expunction-vs-nondisclosure', 'Expunction vs. Nondisclosure', 'The difference between expunction and nondisclosure in Texas.', """
An expunction treats the arrest as though it never happened. Records are destroyed, and you may generally deny the arrest and charge. A nondisclosure order seals records from the public, but law enforcement, courts, and certain licensing agencies can still see them, and you may need to disclose the matter in some applications.

Eligibility differs. Expunction generally requires that the case not result in a conviction or deferred adjudication (other than Class C). Nondisclosure is available after many deferred adjudications and some convictions.
"""),
EX('expunctions-after-a-pretrial-diversion-program', 'Expunction After Pretrial Diversion', 'Expunging your record after completing pretrial intervention in Harris or Fort Bend County.', """
Completing a pretrial diversion or intervention program usually makes the arrest eligible for expunction, often without waiting for the statute of limitations to run. Many people never take this final step, leaving the arrest visible on background checks.

If you completed a program in Harris or Fort Bend County, we can confirm eligibility and handle the filing.
"""),
EX('sealing-criminal-records', 'Sealing Criminal Records', 'Orders of nondisclosure in Texas: who qualifies and waiting periods.', """
An order of nondisclosure under Chapter 411 of the Government Code seals criminal records from public view. Waiting periods range from none for many deferred misdemeanors to five years for felony deferred adjudications, and some offenses are excluded entirely.

Once granted, the order prevents most employers, landlords, and the public from accessing the records through official channels.
"""),
EX('expunging-unlawful-carry-of-a-firearm', 'Expunging Unlawful Carrying Convictions', 'Expunction for older unlawful carrying of a weapon convictions after Texas permitless carry.', """
After Texas adopted permitless carry in 2021, the Legislature created a path for some people convicted of unlawfully carrying a handgun under the old law to seek expunction, when their conduct would no longer be an offense. Eligibility depends on the facts of the original case.

If you have an old UCW conviction from Harris, Fort Bend, or another county, we can evaluate whether it qualifies.
"""),
EX('impact-of-arrest-on-grad-school', 'Arrests and Graduate School', 'How an arrest affects law school, medical school and graduate admissions.', """
Law, medical, nursing, and many graduate programs ask about arrests and charges, not just convictions, and bar and licensing agencies ask even more. Inaccurate answers can be treated as dishonesty.

An expunction can allow you to answer differently in many settings. We advise clients on what their record shows and how to approach disclosure questions accurately.
"""),
EX('expunction-and-record-sealing-faqs', 'Expunction FAQ', 'Frequently asked questions about expunctions and nondisclosure in Texas.', """
Answers to common questions about clearing a Texas record.
""", faq=[
  ('How long does an expunction take?', 'Typically several months from filing to signed order, plus time for agencies to comply.'),
  ('Can I expunge a conviction?', 'Generally no, except in limited situations such as a pardon, actual innocence, or certain older unlawful carrying convictions.'),
  ('Do I have to wait to expunge a dismissed case?', 'Often yes. Waiting periods depend on the offense level and whether the case was dismissed for certain reasons. Some dismissals allow immediate filing.'),
  ('Will an expunction remove my mugshot from websites?', 'An expunction order binds government agencies and certain parties served. Private websites can be more difficult, but an order is a strong tool for removal requests.'),
]),

# ---------------- Jail release ----------------
P('jail-release', 'Jail Release & Bond', 'Getting out of jail in Houston and Fort Bend County: bond hearings, PR bonds and bond conditions.', hub=True,
  h1='Jail Release & Bond in Houston & Fort Bend County', hub_label='Jail Release Topics', body="""
After an arrest in Harris County, people are generally taken to the Joint Processing Center downtown and appear before a magistrate, often by video, who sets bail and conditions. In Fort Bend County, people are booked into the county jail in Richmond and see a magistrate there.

Texas law requires bail to be sufficient to ensure appearance but not to be used as an instrument of oppression. Recent bail-reform legislation restricts personal bonds for some violent offenses and requires certain information to be considered. A lawyer can present employment, family, and residence information to support a lower bond or better conditions.
"""),
JR('loved-one-in-jail', 'A Loved One in Jail', 'What to do when a family member is arrested in Houston or Fort Bend County.', """
1. Find out where they are held and their booking or SPN number.
2. Learn the charges and bond amount.
3. Remind them not to discuss the case on jail phones, which are recorded.
4. Call a lawyer who can contact the jail, check the bond, and seek a reduction if needed.

We can explain the options between cash bond, surety bond through a bondsman, and attorney bonds, and help get your loved one home as soon as possible.
"""),
JR('personal-recognizance-bond', 'Personal Recognizance Bonds', 'Personal recognizance (PR) bonds in Harris and Fort Bend County.', """
A personal bond, often called a PR bond, releases a person on their promise to appear, without paying the full bail amount up front. Eligibility depends on the offense, criminal history, and local practice. Texas law now bars personal bonds for some violent offenses.

When a PR bond is denied, we can request a bond reduction hearing and present information that supports release.
"""),
JR('conditions-of-bond', 'Bond Conditions', 'Common bond conditions in Texas: no contact, interlock, GPS and drug testing.', """
Courts commonly impose conditions such as no contact with the complaining witness, staying away from certain places, ignition interlocks, alcohol monitoring, GPS, drug testing, and curfews. Violating a condition can lead to arrest and revocation of the bond.

If a condition is unreasonable or no longer necessary, we can ask the court to modify it.
"""),

# ---------------- Texas criminal process ----------------
P('texas-criminal-process', 'The Texas Criminal Process', 'How a criminal case works in Harris and Fort Bend County, from arrest to trial and beyond.', hub=True,
  h1='The Texas Criminal Process', hub_label='Process Topics', body="""
1. **Arrest or warrant:** A case starts with an arrest, a citation, or a warrant.
2. **Magistration and bond:** A magistrate informs you of the charge and sets bond.
3. **Charging:** Misdemeanors proceed on an information; felonies require a grand jury indictment.
4. **Arraignment and settings:** The case is set on the court's docket.
5. **Discovery:** The State must produce evidence under the Michael Morton Act, Article 39.14.
6. **Motions and negotiation:** Suppression motions, diversion requests and plea discussions.
7. **Trial:** A jury or judge decides guilt, and in Texas you may choose whether the jury decides punishment.
8. **After the case:** Appeals, probation, early termination, expunction or nondisclosure.
"""),
TP('deferred-adjudication', 'Deferred Adjudication', 'Deferred adjudication in Texas: how it works, benefits and risks.', """
Deferred adjudication is a form of community supervision in which the judge defers a finding of guilt. If you complete the conditions, the case is dismissed and there is no conviction. Many deferred cases qualify for nondisclosure.

The risk is that if you violate conditions, the judge can find you guilty and sentence you anywhere within the full range of punishment. We weigh those trade-offs carefully with every client.
"""),
TP('early-termination-of-probation', 'Early Termination of Probation', 'How to get off probation early in Harris and Fort Bend County.', """
Judges can discharge a person from community supervision early, often after one-third or two years of the term, whichever is less, if the person has complied with conditions and paid what is owed. Some offenses are excluded. Early termination of regular probation can lead to a "judicial clemency" order releasing many penalties.

We prepare motions that show the court your progress and the reasons early discharge is appropriate.
"""),
TP('early-termination-of-deferred-adjudication', 'Early Termination of Deferred Adjudication', 'Early termination of deferred adjudication in Texas.', """
Judges may dismiss a deferred adjudication case early when the person has complied with conditions. Early dismissal can speed eligibility for nondisclosure and remove restrictions sooner. We present compliance records, employment, and other accomplishments in support.
"""),
TP('failure-to-appear', 'Failure to Appear & Bail Jumping', 'Bail jumping and failure to appear charges in Houston and Fort Bend County.', """
Missing court while released on bond can lead to a warrant, bond forfeiture, and a new charge of bail jumping and failure to appear. The new charge is a Class A misdemeanor if the original case was a misdemeanor and a third-degree felony if it was a felony.

A reasonable excuse is a defense. If you missed court, act quickly. We can often resolve the warrant and reinstate the bond.
""", [('Underlying misdemeanor', 'A'), ('Underlying felony', 'F3')]),
TP('perjury', 'Perjury & Aggravated Perjury', 'Perjury and aggravated perjury charges in Texas.', """
Perjury is making a false statement under oath with intent to deceive and knowledge of its meaning. It is a Class A misdemeanor. Aggravated perjury, a false material statement in an official proceeding, is a third-degree felony. Retraction before the falsity becomes manifest can be a defense.
""", [('Perjury', 'A'), ('Aggravated perjury', 'F3')]),
TP('statute-of-limitations', 'Statute of Limitations', 'Statute of limitations for criminal offenses in Texas.', """
Most Texas misdemeanors must be charged within two years. Many felonies have a three-year limitation, while others have longer periods, and some, including murder and many sexual offenses against children, have none. The limitation period can be tolled in some circumstances, such as when the accused is absent from the state.
"""),
TP('walk-through-arrests', 'Walk-Through Arrests', 'Arranging a walk-through or voluntary surrender in Houston and Fort Bend County.', """
If a warrant has been issued, a lawyer can often arrange a voluntary surrender, sometimes called a walk-through, with bond arranged in advance. This reduces time in custody and avoids the embarrassment of an arrest at home or work.
"""),
TP('warrants', 'Warrants', 'Arrest warrants in Harris and Fort Bend County: how to find out and what to do.', """
Warrants can be issued after an investigation, a grand jury indictment, a missed court date, or a probation violation. Officers can make an arrest at any time, including during a traffic stop.

If you think you have a warrant, call us before taking any other step. We can confirm the warrant and plan a surrender with bond in place.
""", hub=True, hub_label='Related Topics'),
TP('warrants/clearing-warrants', 'Clearing Warrants', 'How to clear municipal, county and felony warrants in Houston and Fort Bend County.', """
Municipal warrants for traffic tickets can often be cleared by resolving the underlying ticket. County and district court warrants usually require posting a bond or appearing before the court, which we can often arrange through a walk-through or a motion to reinstate bond.
"""),

# ---------------- Misdemeanors / Felonies ----------------
P('misdemeanors', 'Misdemeanors', 'Misdemeanor defense in Harris and Fort Bend County: Class A, B and C offenses and how to protect your record.', hub=True,
  h1='Houston & Fort Bend Misdemeanor Lawyer', hub_label='Misdemeanor Classes', body="""
Misdemeanors are less serious than felonies, but they can still bring jail time, fines, and a permanent record. In Harris County they are heard in the county criminal courts at law; in Fort Bend County, in the county courts at law in Richmond. Class C offenses are heard in justice and municipal courts.
""", levels=[('Class C', 'C'), ('Class B', 'B'), ('Class A', 'A')]),
MI('class-a-misdemeanor', 'Class A Misdemeanors', 'Class A misdemeanor charges in Texas: up to one year in jail and a $4,000 fine.', """
Class A misdemeanors, the most serious misdemeanor class, carry up to one year in county jail and a fine of up to $4,000. Common examples include assault causing bodily injury, family violence assault, second DWI, DWI with a 0.15 or higher BAC, unlawful carrying of a weapon, and theft between $750 and $2,500.
""", [('Class A', 'A')]),
MI('class-b-misdemeanor', 'Class B Misdemeanors', 'Class B misdemeanor charges in Texas: up to 180 days in jail and a $2,000 fine.', """
Class B misdemeanors carry up to 180 days in county jail and a fine of up to $2,000. Examples include first DWI, possession of two ounces or less of marijuana, theft between $100 and $750, criminal trespass, and harassment.
""", [('Class B', 'B')]),
MI('class-c-misdemeanor', 'Class C Misdemeanors', 'Class C misdemeanor tickets in Texas: fine-only offenses and keeping them off your record.', """
Class C misdemeanors are punishable by a fine of up to $500 and no jail. They include public intoxication, minor in possession, assault by contact, and possession of drug paraphernalia. They still create criminal records, but deferred disposition often allows dismissal and expunction.
""", [('Class C', 'C')]),
P('felonies', 'Felonies', 'Felony defense in Houston and Fort Bend County: state jail, third-, second-, first-degree and capital felonies.', hub=True,
  h1='Houston & Fort Bend Felony Defense Lawyer', hub_label='Felony Levels', body="""
Felonies are punishable by confinement in a state jail or the Texas Department of Criminal Justice. They require a grand jury indictment and are heard in district court. A felony conviction carries lasting consequences, including loss of firearm rights and barriers to employment and housing.

Early representation, even before indictment, can influence how a case is charged.
""", levels=[('State jail felony', 'SJF'), ('Third degree', 'F3'), ('Second degree', 'F2'), ('First degree', 'F1'), ('Capital', 'CAP')]),
FE('state-jail-felony', 'State Jail Felonies', 'State jail felonies in Texas: 180 days to two years and possible reduction to a misdemeanor.', """
State jail felonies carry 180 days to two years in a state jail facility. Judges and prosecutors can sometimes reduce them to Class A misdemeanors under Penal Code § 12.44. Examples include possession of less than a gram of a Penalty Group 1 drug, theft from $2,500 to $30,000, and burglary of a building.
""", [('State jail felony', 'SJF')]),
FE('third-degree-felony', 'Third-Degree Felonies', 'Third-degree felony charges in Texas: two to ten years in prison.', """
Third-degree felonies carry two to ten years in prison. Examples include third DWI, assault by impeding breath against a family member, stalking, possession of a firearm by a felon, and intoxication assault.
""", [('Third-degree felony', 'F3')]),
FE('second-degree-felony', 'Second-Degree Felonies', 'Second-degree felony charges in Texas: two to twenty years in prison.', """
Second-degree felonies carry two to twenty years in prison. Examples include aggravated assault, robbery, burglary of a habitation, sexual assault, and intoxication manslaughter.
""", [('Second-degree felony', 'F2')]),
FE('first-degree-felony', 'First-Degree Felonies', 'First-degree felony charges in Texas: five to ninety-nine years or life.', """
First-degree felonies carry five to ninety-nine years or life in prison. Examples include murder, aggravated robbery, aggravated sexual assault, and possession of large quantities of controlled substances.
""", [('First-degree felony', 'F1')]),

# ---------------- Singles ----------------
P('probation-violations', 'Probation Violations', 'Probation violation and motion to revoke defense in Harris and Fort Bend County.', """
When the State files a motion to revoke probation or adjudicate guilt, the judge decides the case without a jury, and the standard of proof is lower than at trial: a preponderance of the evidence. A warrant often issues, and bond may be limited.

Many violations are technical, such as missed appointments, unpaid fees, or a positive test. Courts frequently modify conditions instead of revoking, especially when a lawyer presents the reasons and a plan. Inability to pay is a defense to revocation based on fees alone.
""", cat='misdemeanors'),
P('first-time-offenders', 'First-Time Offenders', 'Options for first-time offenders in Houston and Fort Bend County: pretrial intervention, deferred adjudication and expunction.', """
If this is your first arrest, you likely have options that can protect your record. Harris and Fort Bend County prosecutors offer pretrial intervention programs for eligible first-time defendants, which lead to dismissal and expunction. Deferred adjudication, followed by nondisclosure, is another path.

The decisions you make early, including what you say and whether you accept the first offer, determine which options remain. Call us before you decide.
""", cat='misdemeanors'),
P('out-of-county-offenders', 'Out-of-County Offenders', 'Arrested in Houston but live elsewhere? How we handle cases for out-of-county and out-of-state clients.', """
Houston draws visitors for business, the Texas Medical Center, concerts, conventions, and sporting events. If you were arrested here but live elsewhere, we can often handle much of the case without requiring you to travel for every setting, though some appearances are mandatory.

We also represent Houston-area residents with cases in other Texas counties and coordinate with local counsel when needed.
""", cat='misdemeanors'),
]
