import html
esc = html.escape

LEVELS = {
    'C':   ('Class C misdemeanor', 'No jail', '$500'),
    'B':   ('Class B misdemeanor', 'Up to 180 days in county jail', '$2,000'),
    'A':   ('Class A misdemeanor', 'Up to 1 year in county jail', '$4,000'),
    'SJF': ('State jail felony', '180 days to 2 years in state jail', '$10,000'),
    'F3':  ('Third-degree felony', '2 to 10 years in prison', '$10,000'),
    'F2':  ('Second-degree felony', '2 to 20 years in prison', '$10,000'),
    'F1':  ('First-degree felony', '5 to 99 years or life in prison', '$10,000'),
    'CAP': ('Capital felony', 'Life without parole (or death if the State seeks it)', 'N/A'),
}

NAV = [
    ('/practice-areas/', 'Criminal Defense', [
        ('/dwi-dui/', 'DWI / DUI'), ('/drug-charges/', 'Drug Charges'), ('/marijuana-defense/', 'Marijuana Defense'),
        ('/violent-crimes/', 'Assault & Violent Crimes'), ('/domestic-family-violence/', 'Domestic & Family Violence'),
        ('/sex-crimes/', 'Sex Crimes'), ('/theft-property-crimes/', 'Theft & Property Crimes'),
        ('/white-collar-crimes/', 'White-Collar & Fraud'), ('/weapon-firearm-charges/', 'Weapons Charges'),
        ('/federal-crimes/', 'Federal Crimes'), ('/serious-traffic-offenses/', 'Serious Traffic Offenses'),
        ('/expunctions-record-sealing/', 'Expunctions & Record Sealing'), ('/jail-release/', 'Jail Release & Bond')]),
    ('/case-results/', 'Results'),
    ('/testimonials/', 'Reviews'),
    ('/attorneys/', 'Attorneys', [
        ('/attorneys/ishmael-pink/', 'Ishmael G. A. Pink'), ('/attorneys/augustin-t-pink/', 'Augustin T. Pink'),
        ('/attorneys/ikenna-okoro/', 'Ikenna Okoro — Of Counsel'), ('/attorneys/femi-aborisade/', 'Femi Aborisade — Of Counsel'),
        ('/about/', 'About the Firm')]),
    ('/videos/', 'Videos'),
    ('/contact/', 'Contact'),
    ('/other-practices/', 'Other Practices', [
        ('/other-practices/', 'Our Affiliated Practices'),
        ('https://www.pinkinjury.com/', 'Personal Injury: PinkInjury.com'),
        ('https://www.pinkbusiness.com/', 'Business & Transactions: PinkBusiness.com')]),
]

FOOT_PRACTICE = [('/dwi-dui/', 'DWI Defense'), ('/drug-charges/', 'Drug Crimes'), ('/violent-crimes/', 'Violent Crimes'),
                 ('/domestic-family-violence/', 'Family Violence'), ('/white-collar-crimes/', 'White-Collar Defense'),
                 ('/federal-crimes/', 'Federal Crimes'), ('/sex-crimes/', 'Sex Crimes'),
                 ('/theft-property-crimes/', 'Theft & Fraud'), ('/expunctions-record-sealing/', 'Expunctions')]

HOME_PRACTICE = [
    ('/dwi-dui/', 'DWI / DUI Defense', 'First DWIs, felony DWI, intoxication assault and ALR license hearings in Harris and Fort Bend Counties.'),
    ('/drug-charges/', 'Drug Charges', 'Possession, delivery and trafficking cases, from penalty-group charges to fentanyl allegations.'),
    ('/violent-crimes/', 'Assault & Violent Crimes', 'Assault, aggravated assault, robbery, homicide and other serious felony allegations.'),
    ('/domestic-family-violence/', 'Family Violence', 'Domestic assault, strangulation allegations, protective orders and bond conditions.'),
    ('/white-collar-crimes/', 'White-Collar & Fraud', 'Fraud, embezzlement, securities and federal investigations handled with discretion.'),
    ('/federal-crimes/', 'Federal Crimes', 'Defense in the U.S. District Court for the Southern District of Texas.'),
    ('/sex-crimes/', 'Sex Crimes', 'Discreet defense against sexual assault, indecency and online solicitation allegations.'),
    ('/theft-property-crimes/', 'Theft & Property Crimes', 'Shoplifting, burglary, auto theft, forgery and embezzlement charges.'),
    ('/expunctions-record-sealing/', 'Expunctions & Nondisclosure', 'Clear or seal eligible Texas records so an old case stops following you.'),
]

STATS = [('50+', 'Years of family legal practice'), ('3,000+', 'Dismissals as a family of firms'),
         ('600+', 'Trials as a family of firms'), ('340+', 'Five-star client reviews')]

# Excerpts of Google reviews left for Walter J. Pink & Associates, PC (as published on walterjpink.com). Do not edit wording.
REVIEWS = [
    ('Michael D.', "Thanks to his expertise and relentless advocacy, I was acquitted of all charges related to aggravated robbery."),
    ('Taylor T.', "Thanks to Mr. Pink's hard work and dedication, the outcome of my case was far better than I had anticipated."),
    ('Bahira S.', "His dedication and honesty made a huge difference in my case."),
    ('Mongrick S.', "Treated me like family than a client."),
    ('Whitney M.', "Very educated and professional. Book with Pink!"),
    ('Kiundra A.', "Because of Mr. Pink my family has closure and can move on with our lives."),
    ('Lisa D.', "They are not just a remarkable attorney but also a compassionate human being who genuinely cares about their clients."),
    ('Heather B.', "He was always very prompt on answering my calls or texts."),
    ('Nicole S.', "He is simply the best in the business."),
    ('Sophia T.', "He treated my daughter with respect and dignity."),
    ('Lakeisha P.', "He demonstrated an impressive depth of knowledge in juvenile law."),
    ('Shanta W.', "I highly recommend Mr. Walter Pink to anyone in need of a skilled and dedicated criminal defense lawyer."),
    ('Traveon A.', "I am incredibly grateful for the outstanding legal representation provided by Mr. Walter Pink."),
    ('Cohen S.', "I am delighted to share my exceptional experience with Mr. Pink."),
    ('Dajah T.', "His work is extravagantly incomparable to others."),
]

# Results published by Walter J. Pink & Associates, PC. (matter, outcome, detail)
RESULTS = [
    ('Capital Murder', 'Dismissed', ''),
    ('Murder', 'No Bill', 'Grand jury declined to indict.'),
    ('Intoxication Manslaughter', 'Reduced Sentence', '4 years; the State sought 15 years.'),
    ('Aggravated Assault with a Deadly Weapon', 'Dismissed', ''),
    ('Assault on a Peace Officer & Retaliation', 'Both Dismissed', ''),
    ('Domestic Violence — Impeding Breath (Felony)', 'Dismissed', ''),
    ('DWI', 'Dismissed', ''),
    ('Burglary & Domestic Violence', 'Both Dismissed', ''),
    ('Assault on a Peace Officer', 'Deferred Probation', '5 years deferred; prior offer was 2 years TDCJ.'),
    ('Terroristic Threat — Family/Household', 'Dismissed', ''),
    ('Murder', 'No Bill', 'Grand jury declined to indict.'),
    ('Aggravated Assault with a Deadly Weapon', 'Dismissed', ''),
    ('Domestic Violence', 'Dismissed', ''),
    ('DWI', 'Dismissed', ''),
    ('Domestic Violence', 'Dismissed', ''),
    ('DWI', 'Dismissed', ''),
]

DEFAULT_DEFENSE = """
Every charge has elements the State must prove beyond a reasonable doubt. We start by getting the offense report, body-camera and dash-camera video, 911 audio, lab records, and witness statements, then test each piece against the law.

- Was the stop, detention, or search lawful under the Fourth Amendment and Article I, Section 9 of the Texas Constitution?
- Were statements taken in violation of Miranda or Article 38.22 of the Code of Criminal Procedure?
- Can the State actually prove identity, intent, and every other required element?
- Is the client eligible for pretrial intervention, deferred adjudication, or a reduction that protects their record?
"""

LOCAL_CRIM = """
In Houston, most felony and misdemeanor cases are heard at the Harris County Criminal Justice Center at 1201 Franklin Street downtown, and arrests are processed through the Harris County Joint Processing Center. In Fort Bend County, cases are handled at the Fort Bend County Justice Center in Richmond. Arresting agencies include the Houston Police Department, Harris County Sheriff's Office and constables, the Fort Bend County Sheriff's Office, Sugar Land, Missouri City, Rosenberg, Stafford and Katy police, and the Texas Department of Public Safety. Each court and prosecutor's office has its own practices and diversion programs, and knowing them is part of building a strategy.
"""

PI_COMMON = """
Insurance carriers start building their file the day of the incident. We move just as fast: preserving photos and video, getting police and incident reports, identifying every insurance policy that may apply, and documenting medical treatment and lost income.

- **Deadlines:** Most Texas injury claims must be filed within two years (Civil Practice & Remedies Code § 16.003). Claims against government entities can require written notice in as little as six months, and some city charters require less.
- **Shared fault:** Under Texas's proportionate responsibility rule, you can recover if you are 50% or less at fault, reduced by your percentage of fault.
- **Damages:** Medical expenses, lost wages and earning capacity, pain and suffering, mental anguish, physical impairment, disfigurement, and property damage.

Clients in Houston, Sugar Land, Missouri City, Richmond, Rosenberg and Katy can meet with us without paying anything up front to discuss their claim.
"""

CATS = {
 'dwi-dui': {'defense': """
DWI cases are won and lost on details. We review the reason for the stop, the officer's standardized field sobriety test administration against NHTSA standards, the 15-minute observation period before a breath test, Intoxilyzer 9000 maintenance and calibration records, and the chain of custody and lab methods for any blood draw. We also request the ALR hearing within the 15-day deadline so your license is protected and the arresting officer can be cross-examined early.
"""},
 'drug-charges': {'defense': """
Drug prosecutions depend on proving the substance, the amount, and that you knowingly possessed it. We challenge searches of cars and homes, consent that was not truly voluntary, affirmative links in shared spaces, lab weight calculations (including adulterants and dilutants), and the reliability of confidential informants. First-time and lower-level cases may qualify for pretrial intervention or drug-court programs in Harris and Fort Bend Counties.
"""},
 'marijuana-defense': {'defense': """
We look first at how officers claim to have identified marijuana. Because hemp is legal in Texas, odor or appearance alone may not prove an illegal substance, and labs must test THC concentration. We also challenge searches, examine whether possession can be tied to you, and pursue diversion or dismissal programs that keep a conviction off your record.
"""},
 'violent-crimes': {'defense': """
Violent-crime allegations often turn on credibility and context. We gather surveillance and phone video, 911 calls, medical records, and independent witnesses, and we evaluate self-defense, defense of others, and defense of property under Chapter 9 of the Penal Code. When identity is disputed, we scrutinize lineups and forensic evidence.
"""},
 'domestic-family-violence': {'defense': """
Family violence cases move quickly: emergency protective orders, no-contact bond conditions, and pressure to accept a plea. We investigate the full history, preserve texts and social media, interview witnesses, and examine injuries and photographs. We also work to modify bond conditions so clients can return home or see their children when appropriate.
"""},
 'sex-crimes': {'defense': """
Sex-offense allegations carry life-changing consequences, including possible sex-offender registration. We act discreetly and early, before any interview with police, and we examine forensic interviews, SANE exams, digital evidence, delayed-outcry timelines, and motives to fabricate. We retain qualified experts when the science matters.
"""},
 'theft-property-crimes': {'defense': """
Property cases depend on intent and value. We examine whether the State can prove you intended to deprive the owner, whether the claimed value is accurate (value often decides the offense level), and whether restitution or a civil resolution can lead to dismissal. Many first-time theft cases qualify for pretrial intervention.
"""},
 'white-collar-crimes': {'defense': """
White-collar matters are document cases. We get involved before charges whenever possible, communicate with investigators and prosecutors on your behalf, review financial records with forensic accountants, and identify good-faith, authorization, and lack-of-intent defenses. Early intervention can sometimes keep a matter civil rather than criminal.
"""},
 'weapon-firearm-charges': {'defense': """
Texas allows most adults 21 and older to carry a handgun without a license, so many weapons arrests turn on technical questions: Was the person prohibited? Was the location actually off-limits and properly posted? Was the weapon in plain view or found in an unlawful search? We examine each element and the circumstances of the stop.
"""},
 'serious-traffic-offenses': {'defense': """
We obtain dash-camera and body-camera footage, crash reports, event data recorder downloads, and witness statements to reconstruct what happened. Many traffic-related charges turn on whether the State can prove knowledge or recklessness rather than a simple mistake.
"""},
 'alcohol-offenses': {'defense': """
Alcohol cases involving young people often qualify for deferred disposition, alcohol-awareness classes, and later expunction. We focus on protecting the client's record, license, and school or job standing while testing the evidence of possession or consumption.
"""},
 'arrests': {'defense': DEFAULT_DEFENSE},
 'student-defense': {'defense': """
Students face both the court case and school discipline. We coordinate the criminal defense with university conduct proceedings at schools like the University of Houston, Texas Southern University, Rice University, and Houston Community College, so a statement in one does not damage the other.
"""},
 'expunctions-record-sealing': {'defense': """
We review the complete record, including every arrest and disposition, confirm eligibility and waiting periods, prepare and file the petition, and serve every agency that holds your records so the clean-up is complete.
"""},
 'texas-criminal-process': {'defense': DEFAULT_DEFENSE},
 'jail-release': {'defense': """
Speed matters. We contact the jail and the court, gather information about employment, family ties, and residence, and argue for a reasonable bond or personal recognizance release and workable conditions.
"""},
 'misdemeanors': {'defense': DEFAULT_DEFENSE},
 'felonies': {'defense': DEFAULT_DEFENSE},
 'federal-crimes': {'defense': """
Federal cases are investigated for months before charges. We engage early with Assistant U.S. Attorneys and agents, analyze discovery and Sentencing Guidelines exposure, litigate suppression issues, and prepare for trial in the Southern District of Texas, Houston Division.
"""},
}

REDIRECTS = [
    ('/contact-us', '/contact/'), ('/attorney-profile', '/attorneys/'), ('/home/why-us', '/why-us/'),
    ('/results', '/case-results/'), ('/policies', '/frequently-asked-question-faq/'),
    ('/practice-areas/:cat/:sub', '/:cat/:sub/'), ('/blog/:path*', '/resources/'), ('/video-embed/:path*', '/videos/'),
    ('/videos/:slug', '/videos/'), ('/comments/:path*', '/'), ('/feed', '/'), ('/:path*/feed', '/:path*/'),
    ('/wp-admin/:path*', '/'), ('/wp-json/:path*', '/'), ('/wp-content/:path*', '/'),
    ('/dwi-dui/austin-police-department', '/dwi-dui/houston-police-department/'),
    ('/student-defense/ut-student-disciplinary-hearings', '/student-defense/university-disciplinary-hearings/'),
    ('/expunctions-record-sealing/sealing-criminal-record-process-in-texas-austin-lawyer-for-sealing-records', '/expunctions-record-sealing/sealing-criminal-records/'),
    ('/dwi-dui/ignitioninterlock-scramdevice-portablealcoholmonitor', '/dwi-dui/scram-and-alcohol-monitoring/'),
    ('/theft-property-crimes/theft-by-check/forms', '/theft-property-crimes/theft-by-check/'),
    ('/about-houston-attorney-walter-j-pink', '/about/'), ('/augustin-t-pink', '/attorneys/augustin-t-pink/'),
    ('/ishmael-g-a-pink', '/attorneys/ishmael-pink/'), ('/clement-b-pink', '/attorneys/'), ('/faq', '/frequently-asked-question-faq/'),
    ('/review-us', '/testimonials/'), ('/llms-info', '/llms.txt'),
    ('/business-litigation', 'https://www.pinkbusiness.com/'), ('/business-litigation/:path*', 'https://www.pinkbusiness.com/'),
    ('/personal-injury', 'https://www.pinkinjury.com/'), ('/personal-injury/:path*', 'https://www.pinkinjury.com/'),
]

# Attorneys: (name, role, page or None, local photo, remote fallback photo, initials, blurb)
ATTYS = [
    ('Ishmael G. A. Pink', 'Founding Attorney', '/attorneys/ishmael-pink/', '/assets/img/team/ishmael-pink.jpg', '', 'IP',
     'Trial attorney focused on white-collar and criminal defense in state and federal court.'),
    ('Augustin T. Pink', 'Partner', '/attorneys/augustin-t-pink/', '/assets/img/team/augustin-t-pink.jpg',
     'https://walterjpink.com/wp-content/uploads/2024/07/Augustin-T.-Pink.jpg', 'AP',
     'Lead criminal defense strategist with more than 30 years in Texas and federal courts.'),
    ('Clement B. Pink', 'Partner', None, '/assets/img/team/clement-b-pink.jpg',
     'https://walterjpink.com/wp-content/uploads/2024/07/Clement-B.-Pink.jpg', 'CP', ''),
    ('Ikenna Okoro', 'Of Counsel', '/attorneys/ikenna-okoro/', '/assets/img/team/ikenna-okoro.jpg', '', 'IO',
     'Texas government relations and energy regulatory attorney; former Assistant Parliamentarian, Texas House.'),
    ('Femi Aborisade', 'Of Counsel', '/attorneys/femi-aborisade/', '/assets/img/team/femi-aborisade.jpg', '', 'FA',
     'Houston native and personal injury attorney with Mesquite Law Group.'),
]

def photo(local, remote, ini, cls='ph'):
    fb = f' data-fallback="{remote}"' if remote else ' data-fallback=""'
    return f'<div class="{cls}"><span class="mono" aria-hidden="true">{ini}</span><img src="{local}"{fb} alt="" loading="lazy"></div>'

def atty_card(a):
    name, role, page, local, remote, ini, blurb = a
    inner = f'{photo(local, remote, ini)}<h3>{esc(name)}</h3><div class="role">{esc(role)}</div>' + (f'<p>{esc(blurb)}</p>' if blurb else '')
    if page:
        return f'<a class="card pa-card atty" href="{page}">{inner}<span class="more">View profile &rarr;</span></a>'
    return f'<div class="card atty">{inner}</div>'
