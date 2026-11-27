from mk import P
import data_common as C

SITE = None  # person schema urls filled relative

def bio_html(a_index, body_html, tagline=''):
    name, role, page, local, remote, ini, blurb = C.ATTYS[a_index]
    tg = f'<p class="tagline">{tagline}</p>' if tagline else ''
    return (f'<div class="bio-head" style="margin-top:24px">{C.photo(local, remote, ini)}'
            f'<div><h2 style="margin-top:0;border:0">{name}</h2><div class="atty" style="text-align:left"><span class="role">{role}</span></div>{tg}'
            f'<p><a class="btn btn-grad" href="tel:+18329790882">Call (832) 979-0882</a></p></div></div>')

ISHMAEL = """
Ishmael Gabriel Ali Pink is a Houston trial and transactional attorney carrying forward his grandfather's 50-year legacy in the Texas legal community. A two-time graduate of the University of Texas, where he earned both his undergraduate degree and his Juris Doctor, Mr. Pink combines deep Texas roots with aggressive, results-driven advocacy.

## Complex Litigation & Trial Advocacy
Mr. Pink's practice is built on high-stakes courtroom and commercial experience. He has gone head to head with large defense firms such as Jackson Walker and with major rideshare corporations, while advising startups and privately held companies on SaaS agreements, B2B disputes, and securities matters.

Whether he is litigating complex commercial conflicts, fighting serious criminal and white-collar charges, or holding insurance companies accountable in personal injury cases, he brings disciplined preparation and trial-ready leverage to every file.

## Direct, Strategic Counsel
Legal disputes threaten your livelihood, your freedom, and your financial future. Whether you are structuring a business deal, defending against criminal allegations, or recovering from a serious injury, Ishmael Pink provides clear-eyed strategy without the runaround.

## Practice Focus
- [Business litigation and transactional counsel](https://www.pinkbusiness.com/) at PinkBusiness.com
- [White-collar and fraud defense](/white-collar-crimes/)
- [Criminal defense](/practice-areas/), including [DWI](/dwi-dui/)
- [Personal injury](https://www.pinkinjury.com/) at PinkInjury.com

## Education
- The University of Texas, undergraduate degree
- The University of Texas, Juris Doctor

Contact Ishmael today at (832) 979-0882 or Ishmael@PinkEsquire.com to schedule a consultation.
"""

AUGUSTIN = """
Augustin T. Pink is a partner and the lead strategist for criminal defense in the Pink family of firms. He has practiced law since 1992, building more than 30 years of experience in Texas state courts and federal courts and carrying on the work of his father, civil rights attorney Walter J. Pink.

"When you face the power of the state or federal government, you need a legal powerhouse who views your fight as his own."

## Experience
- More than three decades defending clients in Harris County, Fort Bend County, and courts across Texas.
- Federal criminal defense, including case dismissals, jury acquittals, and sentence reductions.
- Legal matters handled in Africa and South America.

## Practice Focus
- [Criminal defense](/practice-areas/) in state and federal court
- [Violent crimes](/violent-crimes/) and [family violence](/domestic-family-violence/)
- [DWI and intoxication offenses](/dwi-dui/)
- [Federal crimes](/federal-crimes/)

Augustin T. Pink works from 1717 St. James Place, Suite 690, Houston, TX 77056.
"""

OKORO = """
Ikenna Okoro serves as of counsel to PinkDefense. He is the founder of Okoro Law PLLC in Austin, a practice focused on Texas legislative law and policy, and has spent his career in and around the Texas Capitol as an attorney and government relations professional.

## Background
- Served for more than three years as an Assistant Parliamentarian for the Texas House of Representatives.
- Previously practiced in the Austin office of Balch & Bingham as part of its Public Policy & Government Relations practice.
- Regulatory practice focused on electricity and natural gas issues, and a government relations practice representing corporate, non-profit, and trade association clients.

## How He Helps Clients
Mr. Okoro helps clients understand how Texas legislation affects them, monitor bills through the legislative process, advocate for policy changes, and communicate with Texas leadership. For PinkDefense clients, that perspective is valuable when a business or regulatory problem has a legislative or agency dimension.

## Education
- The University of Texas School of Law, J.D. (2019)
- University of Miami, B.S. (2013)

## Recognition and Memberships
- Best Lawyers: Ones to Watch in America, Energy Law and Government Relations Practice (since 2024)
- Thurgood Marshall Legal Society Alumni of the Year Award, University of Texas School of Law (2022)
- Austin Under 40 finalist (2025)
- Member, Austin Bar Association and Austin Black Lawyers Association
"""

FEMI = """
Femi Aborisade serves as of counsel to PinkDefense. A Houston native, he is an attorney with Mesquite Law Group, a personal injury law firm, and he brings that firm's motto to every case: **When you need the smoke, start with Mesquite.**

## Background
Mr. Aborisade's experience includes representing developers, utilities, and project financiers in renewable energy development projects and transactions, with a particular focus on real estate and project finance. That background in complex, document-heavy transactions gives him a practical edge in evaluating commercial and injury claims.

During law school, he interned for the Honorable Vanessa D. Gilmore of the United States District Court for the Southern District of Texas.

## Community
Mr. Aborisade is active in organizations serving Houston's legal and business community, including the Houston Young Lawyers Association and the Houston Young Lawyers Foundation.

## Practice Focus
- [Personal injury](https://www.pinkinjury.com/) at PinkInjury.com
- [Business matters](https://www.pinkbusiness.com/) at PinkBusiness.com
"""

def person(name, page, job, extra=None):
    d = {'name': name, 'jobTitle': job, 'url': page, 'address': {'@type': 'PostalAddress', 'addressLocality': 'Houston', 'addressRegion': 'TX'}}
    if extra: d.update(extra)
    return d

PAGES = [
P('attorneys/ishmael-pink', 'Ishmael G. A. Pink', 'Ishmael Pink: Houston business, white-collar defense and personal injury attorney carrying forward the Walter J. Pink legacy. Call (832) 979-0882.',
  ISHMAEL, kind='info', cat='attorneys', h1='Ishmael Pink: Houston Business, White-Collar Defense & Personal Injury Attorney', schema_type='ProfilePage',
  pre_html=lambda: bio_html(0, ''),
  person=person('Ishmael Gabriel Ali Pink', '/attorneys/ishmael-pink/', 'Attorney', {'@id': '#ishmael', 'alternateName': ['Ishmael G. A. Pink', 'Ishmael Pink', 'Gabriel Pink'],
      'alumniOf': [{'@type': 'CollegeOrUniversity', 'name': 'The University of Texas at Austin'}, {'@type': 'CollegeOrUniversity', 'name': 'The University of Texas School of Law'}],
      'telephone': '+18329790882', 'email': 'Ishmael@PinkEsquire.com',
      'knowsAbout': ['Business litigation', 'SaaS agreements', 'Securities', 'White-collar defense', 'Criminal defense', 'Personal injury'],
      'relatedTo': [{'@type': 'Person', 'name': 'Walter Jerome Pink'}, {'@type': 'Person', 'name': 'Augustin T. Pink'}, {'@type': 'Person', 'name': 'Clement B. Pink'}]})),
P('attorneys/augustin-t-pink', 'Augustin T. Pink', 'Augustin T. Pink: Houston criminal defense attorney and partner with more than 30 years in Texas and federal courts.',
  AUGUSTIN, kind='info', cat='attorneys', h1='Augustin T. Pink: Lead Criminal Defense Strategist', schema_type='ProfilePage',
  pre_html=lambda: bio_html(1, ''),
  person=person('Augustin T. Pink', '/attorneys/augustin-t-pink/', 'Partner', {'alternateName': ['Augustin Pink'], 'image': 'https://walterjpink.com/wp-content/uploads/2024/07/Augustin-T.-Pink.jpg',
      'knowsAbout': ['Criminal defense', 'Federal criminal defense', 'Violent crimes', 'DWI'], 'relatedTo': [{'@type': 'Person', 'name': 'Walter Jerome Pink'}]})),
P('attorneys/ikenna-okoro', 'Ikenna Okoro', 'Ikenna Okoro, of counsel to PinkDefense: Texas government relations and energy regulatory attorney, former Assistant Parliamentarian of the Texas House.',
  OKORO, kind='info', cat='attorneys', h1='Ikenna Okoro: Of Counsel', schema_type='ProfilePage',
  pre_html=lambda: bio_html(3, ''),
  person=person('Ikenna Okoro', '/attorneys/ikenna-okoro/', 'Of Counsel', {'alumniOf': [{'@type': 'CollegeOrUniversity', 'name': 'The University of Texas School of Law'}, {'@type': 'CollegeOrUniversity', 'name': 'University of Miami'}],
      'sameAs': ['https://www.okorolaw.com/'], 'knowsAbout': ['Texas legislative law', 'Government relations', 'Energy regulation']})),
P('attorneys/femi-aborisade', 'Femi Aborisade', 'Femi Aborisade, of counsel to PinkDefense: Houston native and personal injury attorney with Mesquite Law Group. When you need the smoke, start with Mesquite.',
  FEMI, kind='info', cat='attorneys', h1='Femi Aborisade: Of Counsel', schema_type='ProfilePage',
  pre_html=lambda: bio_html(4, '', 'When you need the smoke, start with Mesquite.'),
  person=person('Femi Aborisade', '/attorneys/femi-aborisade/', 'Of Counsel', {'sameAs': ['https://www.mesquitelawgroup.com/'],
      'knowsAbout': ['Personal injury', 'Renewable energy transactions', 'Real estate', 'Project finance']})),
]
