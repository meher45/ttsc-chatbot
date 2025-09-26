
from flask import Flask, render_template, request

app = Flask(__name__)

qna = {
    # lower
    "hi": "hello student, welcome to our ttsc smartbot / how can I help you",
    "class9 syllabus": "subject??",
    "math syllabus": "chapter-1,2,3,4,6,7,9,10",
    "math": "chapter-1,2,3,4,6,7,9,10",
    "physics syllabus": "chapter-1,2,3,4,5,6,7",
    "physics": "chapter-1,2,3,4,5,6,7",
    "chemistry syllabus": "chapter-1,2,3,4,5,6",
    "chemistry": "chapter-1,2,3,4,5,6",
    "agriculture syllabus": "chapter-1,2,3,4",
    "agriculture": "chapter-1,2,3,4",
    "religion syllabus": "chapter-1,2,3,4,5",
    "religion": "chapter-1,2,3,4,5",
    "bangladesh and global studies syllabus": "chapter-1,3,6,7,10,12,13",
    "bgs syllabus": "chapter-1,3,6,7,10,12,13",
    "trade1 syllabus": "chapter-1,2,3,4",
    "trade1": "chapter-1,2,3,4",
    "trade2 syllabus": "chapter-1,2,3,4",
    "trade2": "chapter-1,2,3,4",
#sirdata
    "principal": "md. tofazzal hoque / mobile : 01711045755 / phone (office) : 02589931204 / email : tscthak38@gmail.com / joining date : 13 november 2023",
    "md. tofazzal hoque": "md. tofazzal hoque / mobile : 01711045755 / phone (office) : 02589931204 / email : tscthak38@gmail.com / joining date : 13 november 2023",
    "chief instructor farm machinery": "engr. ajoy kumar singha / mobile : 01721216006 / phone (office) : 02589931204 / email : ajoy20362@gmail.com / joining date : 20 august 2016",
    "ajoy kumar singha": "engr. ajoy kumar singha / mobile : 01721216006 / phone (office) : 02589931204 / email : ajoy20362@gmail.com / joining date : 20 august 2016",
    "frm mchinery": "engr. ajoy kumar singha / mobile : 01721216006 / phone (office) : 02589931204 / email : ajoy20362@gmail.com / joining date : 20 august 2016",
    "instructor1": "md. abu taher / mobile : 01714624549 / phone (office) : 02589931204 / email : abu.tahertsc@gmail.com / joining date : 28 september 2018",
    "md. abu taher": "md. abu taher / mobile : 01714624549 / phone (office) : 02589931204 / email : abu.tahertsc@gmail.com / joining date : 28 september 2018",
    "instructor mathematics": "md. hamidur rahmanv / mobile : 01717728340 / phone (office) : 02589931204 / email : hamidurtsc06@gmail.com / joining date : 08 july 2018",
    "mathematics": "md. hamidur rahmanv / mobile : 01717728340 / phone (office) : 02589931204 / email : hamidurtsc06@gmail.com / joining date : 08 july 2018",
    "md. hamidur rahmanv": "md. hamidur rahmanv / mobile : 01717728340 / phone (office) : 02589931204 / email : hamidurtsc06@gmail.com / joining date : 08 july 2018",
    "instructor2": "md. muktadir kabir / mobile : 01714537159 / phone (office) : 02589931204 / email : muktadirkabir97@gmail.com / joining date : 16 october 2021",
    "md. muktadir kabir": "md. muktadir kabir / mobile : 01714537159 / phone (office) : 02589931204 / email : muktadirkabir97@gmail.com / joining date : 16 october 2021",
    "instructor mathmatics2": "samanta kumar sen / mobile : 01913802817 / phone (office) : 02589931204 / email : samantasen1451976@gmail.com / joining date : 03 october 2021",
    "samanta kumar sen": "samanta kumar sen / mobile : 01913802817 / phone (office) : 02589931204 / email : samantasen1451976@gmail.com / joining date : 03 october 2021",
    "instructor farm machinary": "md. monzurul islam / instructor (farm machinary) / mobile : 01715412031 / phone (office) : 02589931204 / email : monzurul460@gmail.com / joining date : 08 may 2023",
    "md. monzurul islam": "md. monzurul islam / instructor (farm machinary) / mobile : 01715412031 / phone (office) : 02589931204 / email : monzurul460@gmail.com / joining date : 08 may 2023",
    "instructor dress making": "prokash kumar day / instructor (dress making) / mobile : 01717016008 / phone (office) : 02589931204 / email : prokashkumardey@gmail.com / joining date : 30 april 2008",
    "dress making": "prokash kumar day / instructor (dress making) / mobile : 01717016008 / phone (office) : 02589931204 / email : prokashkumardey@gmail.com / joining date : 30 april 2008",
    "prokash kumar day": "prokash kumar day / instructor (dress making) / mobile : 01717016008 / phone (office) : 02589931204 / email : prokashkumardey@gmail.com / joining date : 30 april 2008",
    "instructor computer": "md. dabirul islam / mobile : 01723093434 / phone (office) : 02589931204 / email : dabirulttsc29@gmail.com / joining date : 10 march 2010",
    "md. dabirul islam": "md. dabirul islam / mobile : 01723093434 / phone (office) : 02589931204 / email : dabirulttsc29@gmail.com / joining date : 10 march 2010",
    "instructor1 farm machinery": "md. masud rana / mobile : 01718170546 / phone (office) : 02589931204 / email : masudranattsc@gmail.com / joining date : 11 february 2024",
    "md. masud rana": "md. masud rana / mobile : 01718170546 / phone (office) : 02589931204 / email : masudranattsc@gmail.com / joining date : 11 february 2024",
    "kapil dev ray": "instructor (english) / mobile: 01722251523 / phone (office): 0258993120 / email: analogym@gmail.com",
    "mst. mina parveen instructor (chemistry)": "mina parveen / instructor (chemistry) / mobile: 01751549538 / phone (office): 0258993120 / email: minapervin50@gmail.com",
    "instructor (chemistry)": "mina parveen / instructor chemistry / mobile: 01751549538 / phone (office): 0258993120 / email: minapervin50@gmail.com",
    "mst. mina parveen": "mina parveen / instructor chemistry / mobile: 01751549538 / phone (office): 0258993120 / email: minapervin50@gmail.com",
    "mohammad fazlur rahman": "mohammad fazlur rahman / instructor bengla / mobile no: 01785279378 / phone (office): 02589931204 / email: fazlurss215@gmail.com",
    "borsa rani bina": "borsa rani bina / instructor bengla / mobile no: 01705899851 / phone (office): 02589931204 / email: barsharanibina7@gmail.com",
    "instructor bengla": "borsa rani bina / instructor bengla / mobile no: 01705899851 / phone (office): 02589931204 / email: barsharanibina7@gmail.com",
    "ismat ara begum": "ismat ara begum / instructor (it support and iot basics) / mobile no: 01750317044 / phone (office): 02589931204 / email: ismot.hstu60@gmail.com / date of joining: 15 january 2024",
    "instructor (it support and iot basics)": "ismat ara begum / instructor (it support and iot basics) / mobile no: 01750317044 / phone (office): 02589931204 / email: ismot.hstu60@gmail.com / date of joining: 15 january 2024",
    "md. inzam haqueamul": "md. inzam haqueamul / instructor (electrical) / mobile no: 01718787566 / phone (office): 02589931204 / email: injamam.bd@gmail.com",
    "md. raihan habib piyal": "md. raihan habib piyal / instructor (apparel manufacturing basics tech) / mobile no: 01751493830 / phone (office): 02589931204 / email: piyalhabib@gmail.com / joining date: 07 july 2025",
    "md. saddam hossain": "md. saddam hossain / junior instructor (tech/it support & iot basics) / mobile no: 01793870215 / phone (office): 02589931204 / email: saddamcse18@gmail.com",
    "md. limon hasan": "md. limon hasan / junior instructor (tech) general electrical works / mobile no: 01773125460 / phone (office): 02589931204 / email: nahidrejasumon@gmail.com",
    "md. ashraful islam": "md. ashraful islam / junior instructor (apparel manufacturing basics) / mobile no: 01765963838 / phone (office): 02589931204 / email: asa.te2012@gmail.com",
    "taslima khatun": "taslima khatun / junior instructor (tech/it support & iot basics) / mobile no: 01748544504 / phone (office): 02589931204 / email: mtaslima17@gmail.com",
    "liton chandra roy": "liton chandra roy / junior instructor (tech) general electrical works / mobile no: 01706844707 / phone (office): 02589931204 / email: slbarman3@gmail.com",
    "kalesh chandra": "kalesh chandra / junior instructor (tech/it support & iot basics) / mobile no: 01744407128 / phone (office): 02589931204 / email: kalesh77.kr@gmail.com",
    "md. zulker nayem": "md. zulker nayem / junior instructor (tech/it support & iot basics) / mobile no: 01677334185 / phone (office): 02589931204 / email: zulkernayem2@gmail.com",
    "mst. nurista parvin": "mst. nurista parvin / junior instructor (tech/apparel manufacturing basics) / mobile no: 01757374067 / phone (office): 02589931204 / email: nuristaparvin23@gmail.com",
    "md. ali hasan": "md. ali hasan / junior instructor (tech/apparel manufacturing basics) / mobile no: 01763111079 / phone (office): 02589931204 / email: alihasan.private@gmail.com",
    "md. masud rana junior": "md. masud rana / junior instructor (tech) general electrical works / mobile no: 01799481005 / phone (office): 02589931204 / email: prvsmsd@gmail.com",
    # ----- Daily Routine -----

    # Diploma (d-)
    'd-sunday': 'Sunday = TP1, TT1, Religion, Math, Chemistry, Bangla',
    'd-monday': 'Monday = Physics/Chemistry Lab, BGS, Math, Agriculture, Computer Application (Drawing), Electrical-Farm = Computer Application',
    'd-tuesday': 'Tuesday = TP1, Chemistry, English, Math, TT1',
    'd-wednesday': 'Wednesday = TP2, English, Agriculture, Physics, Bangla, TT2',
    'd-thursday': 'Thursday = TP2, Physics, Computer Application (Drawing), Electrical-Farm = Computer Application, English, TT2',

    # Mid-level (m-)
    'm-sunday': 'Sunday = TP2, TT, Tiffin, Math, Chemistry, Religion, Physics',
    'm-monday': 'Monday = TP2, TT1, Tiffin, Bangla, Religion, Physics/Chemistry Practical/Science Lab',
    'm-tuesday': 'Tuesday = TP1, TT1, Tiffin, Agriculture, English, IT-AP = Drawing, Electrical-Farm = Computer Application',
    'm-wednesday': 'Wednesday = TP1, TT1, Tiffin, English, Math, IT-AP = Computer Application, Electrical-Farm = Drawing',
    'm-thursday': 'Thursday = Religion, Bangla, Physics, Math, Tiffin, Chemistry, BGS, English, Agriculture',


   # ----- Upper Case Keywords -----

    'HI': 'HELLO STUDENT, WELCOME TO OUR TTSC SMARTBOT / HOW CAN I HELP YOU',
    'CLASS9 SYLLABUS': 'SUBJECT??',
    'MATH SYLLABUS': 'CHAPTER-1,2,3,4,6,7,9,10',
    'MATH': 'CHAPTER-1,2,3,4,6,7,9,10',
    'PHYSICS SYLLABUS': 'CHAPTER-1,2,3,4,5,6,7',
    'PHYSICS': 'CHAPTER-1,2,3,4,5,6,7',
    'CHEMISTRY SYLLABUS': 'CHAPTER-1,2,3,4,5,6',
    'CHEMISTRY': 'CHAPTER-1,2,3,4,5,6',
    'AGRICULTURE SYLLABUS': 'CHAPTER-1,2,3,4',
    'AGRICULTURE': 'CHAPTER-1,2,3,4',
    'RELIGION SYLLABUS': 'CHAPTER-1,2,3,4,5',
    'RELIGION': 'CHAPTER-1,2,3,4,5',
    'BANGLADESH AND GLOBAL STUDIES SYLLABUS': 'CHAPTER-1,3,6,7,10,12,13',
    'BGS SYLLABUS': 'CHAPTER-1,3,6,7,10,12,13',
    'TRADE1 SYLLABUS': 'CHAPTER-1,2,3,4',
    'TRADE1': 'CHAPTER-1,2,3,4',
    'TRADE2 SYLLABUS': 'CHAPTER-1,2,3,4',
    'TRADE2': 'CHAPTER-1,2,3,4',

    
    #sirdata
    'PRINCIPAL': 'MD. TOFAZZAL HOQUE / MOBILE: 01711045755 / PHONE (OFFICE): 02589931204 / EMAIL: TSCTHAK38@GMAIL.COM / JOINING DATE: 13 NOVEMBER 2023',
    'MD. TOFAZZAL HOQUE': 'MD. TOFAZZAL HOQUE / MOBILE: 01711045755 / PHONE (OFFICE): 02589931204 / EMAIL: TSCTHAK38@GMAIL.COM / JOINING DATE: 13 NOVEMBER 2023',

    'CHIEF INSTRUCTOR FARM MACHINERY': 'ENGR. AJOY KUMAR SINGHA / MOBILE: 01721216006 / PHONE (OFFICE): 02589931204 / EMAIL: AJOY20362@GMAIL.COM / JOINING DATE: 20 AUGUST 2016',
    'AJOY KUMAR SINGHA': 'ENGR. AJOY KUMAR SINGHA / MOBILE: 01721216006 / PHONE (OFFICE): 02589931204 / EMAIL: AJOY20362@GMAIL.COM / JOINING DATE: 20 AUGUST 2016',
    'FRM MACHINERY': 'ENGR. AJOY KUMAR SINGHA / MOBILE: 01721216006 / PHONE (OFFICE): 02589931204 / EMAIL: AJOY20362@GMAIL.COM / JOINING DATE: 20 AUGUST 2016',

    'INSTRUCTOR1': 'MD. ABU TAHER / MOBILE: 01714624549 / PHONE (OFFICE): 02589931204 / EMAIL: ABU.TAHERTSC@GMAIL.COM / JOINING DATE: 28 SEPTEMBER 2018',
    'MD. ABU TAHER': 'MD. ABU TAHER / MOBILE: 01714624549 / PHONE (OFFICE): 02589931204 / EMAIL: ABU.TAHERTSC@GMAIL.COM / JOINING DATE: 28 SEPTEMBER 2018',

    'INSTRUCTOR MATHEMATICS': 'MD. HAMIDUR RAHMAN / MOBILE: 01717728340 / PHONE (OFFICE): 02589931204 / EMAIL: HAMIDURTSC06@GMAIL.COM / JOINING DATE: 08 JULY 2018',
    'MD. HAMIDUR RAHMAN': 'MD. HAMIDUR RAHMAN / MOBILE: 01717728340 / PHONE (OFFICE): 02589931204 / EMAIL: HAMIDURTSC06@GMAIL.COM / JOINING DATE: 08 JULY 2018',

    'INSTRUCTOR2': 'MD. MUKTADIR KABIR / MOBILE: 01714537159 / PHONE (OFFICE): 02589931204 / EMAIL: MUKTADIRKABIR97@GMAIL.COM / JOINING DATE: 16 OCTOBER 2021',
    'MD. MUKTADIR KABIR': 'MD. MUKTADIR KABIR / MOBILE: 01714537159 / PHONE (OFFICE): 02589931204 / EMAIL: MUKTADIRKABIR97@GMAIL.COM / JOINING DATE: 16 OCTOBER 2021',

    'INSTRUCTOR MATHEMATICS2': 'SAMANTA KUMAR SEN / MOBILE: 01913802817 / PHONE (OFFICE): 02589931204 / EMAIL: SAMANTASEN1451976@GMAIL.COM / JOINING DATE: 03 OCTOBER 2021',
    'SAMANTA KUMAR SEN': 'SAMANTA KUMAR SEN / MOBILE: 01913802817 / PHONE (OFFICE): 02589931204 / EMAIL: SAMANTASEN1451976@GMAIL.COM / JOINING DATE: 03 OCTOBER 2021',

    'INSTRUCTOR FARM MACHINERY': 'MD. MONZURUL ISLAM / MOBILE: 01715412031 / PHONE (OFFICE): 02589931204 / EMAIL: MONZURUL460@GMAIL.COM / JOINING DATE: 08 MAY 2023',
    'MD. MONZURUL ISLAM': 'MD. MONZURUL ISLAM / MOBILE: 01715412031 / PHONE (OFFICE): 02589931204 / EMAIL: MONZURUL460@GMAIL.COM / JOINING DATE: 08 MAY 2023',

    'INSTRUCTOR DRESS MAKING': 'PROKASH KUMAR DEY / MOBILE: 01717016008 / PHONE (OFFICE): 02589931204 / EMAIL: PROKASHKUMARDEY@GMAIL.COM / JOINING DATE: 30 APRIL 2008',
    'PROKASH KUMAR DEY': 'PROKASH KUMAR DEY / MOBILE: 01717016008 / PHONE (OFFICE): 02589931204 / EMAIL: PROKASHKUMARDEY@GMAIL.COM / JOINING DATE: 30 APRIL 2008',
    'DRESS MAKING': 'PROKASH KUMAR DEY / MOBILE: 01717016008 / PHONE (OFFICE): 02589931204 / EMAIL: PROKASHKUMARDEY@GMAIL.COM / JOINING DATE: 30 APRIL 2008',

    'INSTRUCTOR COMPUTER': 'MD. DABIRUL ISLAM / MOBILE: 01723093434 / PHONE (OFFICE): 02589931204 / EMAIL: DABIRULTTSC29@GMAIL.COM / JOINING DATE: 10 MARCH 2010',
    'MD. DABIRUL ISLAM': 'MD. DABIRUL ISLAM / MOBILE: 01723093434 / PHONE (OFFICE): 02589931204 / EMAIL: DABIRULTTSC29@GMAIL.COM / JOINING DATE: 10 MARCH 2010',

    'INSTRUCTOR1 FARM MACHINERY': 'MD. MASUD RANA / MOBILE: 01718170546 / PHONE (OFFICE): 02589931204 / EMAIL: MASUDRANATTSC@GMAIL.COM / JOINING DATE: 11 FEBRUARY 2024',
    'MD. MASUD RANA': 'MD. MASUD RANA / MOBILE: 01718170546 / PHONE (OFFICE): 02589931204 / EMAIL: MASUDRANATTSC@GMAIL.COM / JOINING DATE: 11 FEBRUARY 2024',

    'KAPIL DEV RAY': 'INSTRUCTOR (ENGLISH) / MOBILE: 01722251523 / PHONE (OFFICE): 02589931204 / EMAIL: ANALOGYM@GMAIL.COM',

    'MST. MINA PARVEEN': 'MST. MINA PARVEEN / INSTRUCTOR (CHEMISTRY) / MOBILE: 01751549538 / PHONE (OFFICE): 02589931204 / EMAIL: MINAPERVIN50@GMAIL.COM',

    'MOHAMMAD FAZLUR RAHMAN': 'MOHAMMAD FAZLUR RAHMAN / INSTRUCTOR (BANGLA) / MOBILE: 01785279378 / PHONE (OFFICE): 02589931204 / EMAIL: FAZLURSS215@GMAIL.COM',
    'BORSA RANI BINA': 'BORSA RANI BINA / INSTRUCTOR (BANGLA) / MOBILE: 01705899851 / PHONE (OFFICE): 02589931204 / EMAIL: BARSHARANIBINA7@GMAIL.COM',
    'INSTRUCTOR BANGLA': 'BORSA RANI BINA / INSTRUCTOR (BANGLA) / MOBILE: 01705899851 / PHONE (OFFICE): 02589931204 / EMAIL: BARSHARANIBINA7@GMAIL.COM',

    'ISMAT ARA BEGUM': 'ISMAT ARA BEGUM / INSTRUCTOR (IT SUPPORT AND IOT BASICS) / MOBILE: 01750317044 / PHONE (OFFICE): 02589931204 / EMAIL: ISMOT.HSTU60@GMAIL.COM / JOINING DATE: 15 JANUARY 2024',

    'MD. INZAM HAQUEAMUL': 'MD. INZAM HAQUEAMUL / INSTRUCTOR (ELECTRICAL) / MOBILE: 01718787566 / PHONE (OFFICE): 02589931204 / EMAIL: INJAMAM.BD@GMAIL.COM',
    'MD. RAIHAN HABIB PIYAL': 'MD. RAIHAN HABIB PIYAL / INSTRUCTOR (APPAREL MANUFACTURING BASICS) / MOBILE: 01751493830 / PHONE (OFFICE): 02589931204 / EMAIL: PIYALHABIB@GMAIL.COM / JOINING DATE: 07 JULY 2025',
    'MD. SADDAM HOSSAIN': 'MD. SADDAM HOSSAIN / JUNIOR INSTRUCTOR (TECH/IT SUPPORT & IOT BASICS) / MOBILE: 01793870215 / PHONE (OFFICE): 02589931204 / EMAIL: SADDAMCSE18@GMAIL.COM',
    'MD. LIMON HASAN': 'MD. LIMON HASAN / JUNIOR INSTRUCTOR (TECH) GENERAL ELECTRICAL WORKS / MOBILE: 01773125460 / PHONE (OFFICE): 02589931204 / EMAIL: NAHIDREJASUMON@GMAIL.COM',
    'MD. ASHRAFUL ISLAM': 'MD. ASHRAFUL ISLAM / JUNIOR INSTRUCTOR (APPAREL MANUFACTURING BASICS) / MOBILE: 01765963838 / PHONE (OFFICE): 02589931204 / EMAIL: ASA.TE2012@GMAIL.COM',
    'TASLIMA KHATUN': 'TASLIMA KHATUN / JUNIOR INSTRUCTOR (TECH/IT SUPPORT & IOT BASICS) / MOBILE: 01748544504 / PHONE (OFFICE): 02589931204 / EMAIL: MTASLIMA17@GMAIL.COM',
    'LITON CHANDRA ROY': 'LITON CHANDRA ROY / JUNIOR INSTRUCTOR (TECH) GENERAL ELECTRICAL WORKS / MOBILE: 01706844707 / PHONE (OFFICE): 02589931204 / EMAIL: SLBARMAN3@GMAIL.COM',
    'KALESH CHANDRA': 'KALESH CHANDRA / JUNIOR INSTRUCTOR (TECH/IT SUPPORT & IOT BASICS) / MOBILE: 01744407128 / PHONE (OFFICE): 02589931204 / EMAIL: KALESH77.KR@GMAIL.COM',
    'MD. ZULKER NAYEM': 'MD. ZULKER NAYEM / JUNIOR INSTRUCTOR (TECH/IT SUPPORT & IOT BASICS) / MOBILE: 01677334185 / PHONE (OFFICE): 02589931204 / EMAIL: ZULKERNAYEM2@GMAIL.COM',
    'MST. NURISTA PARVIN': 'MST. NURISTA PARVIN / JUNIOR INSTRUCTOR (TECH/APPAREL MANUFACTURING BASICS) / MOBILE: 01757374067 / PHONE (OFFICE): 02589931204 / EMAIL: NURISTAPARVIN23@GMAIL.COM',
    'MD. ALI HASAN': 'MD. ALI HASAN / JUNIOR INSTRUCTOR (TECH/APPAREL MANUFACTURING BASICS) / MOBILE: 01763111079 / PHONE (OFFICE): 02589931204 / EMAIL: ALIHASAN.PRIVATE@GMAIL.COM',
   # ---------------- LOWER CASE ----------------
    'hi': 'hello student, welcome to our ttsc smartbot / how can i help you',
    'class9 syllabus': 'subject??',
    'math syllabus': 'chapter-1,2,3,4,6,7,9,10',
    'math': 'chapter-1,2,3,4,6,7,9,10',
    'physics syllabus': 'chapter-1,2,3,4,5,6,7',
    'physics': 'chapter-1,2,3,4,5,6,7',
    'chemistry syllabus': 'chapter-1,2,3,4,5,6',
    'chemistry': 'chapter-1,2,3,4,5,6',
    'agriculture syllabus': 'chapter-1,2,3,4',
    'agriculture': 'chapter-1,2,3,4',
    'religion syllabus': 'chapter-1,2,3,4,5',
    'religion': 'chapter-1,2,3,4,5',
    'bangladesh and global studies syllabus': 'chapter-1,3,6,7,10,12,13',
    'bgs syllabus': 'chapter-1,3,6,7,10,12,13',
    'trade1 syllabus': 'chapter-1,2,3,4',
    'trade1': 'chapter-1,2,3,4',
    'trade2 syllabus': 'chapter-1,2,3,4',
    'trade2': 'chapter-1,2,3,4',

    # ---------------- DAILY ROUTINE ----------------
    'd-sunday': 'sunday = tp1, tt1, rel, math, che, bang',
    'd-monday': 'monday = phy/che lab, bgs, math, agri, com-ap=drawing, electrical-farm=computer application',
    'd-tuesday': 'tuesday = tp1, che, eng, math, tt1',
    'd-wednesday': 'wednesday = tp2, eng, agri, phy, bang, tt2',
    'd-thursday': 'thursday = tp2, phy, com-ap=drawing, electrical-farm=computer application, eng, tt2',

    # ---------------- MAIN ROUTINE ----------------
    'm-sunday': 'sunday = tp-2, tt, tiffin, math, che, rel, phy',
    'm-monday': 'monday = tp-2, tt-1, tiffin, bangla, rel, phy/che.pr./sc.lab',
    'm-tuesday': 'tuesday = tp-1, tt-1, tiffin, agri, eng, it-ap=drawing, elec-fm=ca',
    'm-wednesday': 'wednesday = tp-1, tt-1, tiffin, eng, math, it-ap=ca, elec-farm=drawing',
    'm-thursday': 'thursday = rel, bangla, phy, math, tiffin, che, bgs, eng, agri',

    # ---------------- UPPER CASE ----------------
    'HI': 'HELLO STUDENT, WELCOME TO OUR TTSC SMARTBOT / HOW CAN I HELP YOU',
    'CLASS9 SYLLABUS': 'SUBJECT??',
    'MATH SYLLABUS': 'CHAPTER-1,2,3,4,6,7,9,10',
    'MATH': 'CHAPTER-1,2,3,4,6,7,9,10',
    'PHYSICS SYLLABUS': 'CHAPTER-1,2,3,4,5,6,7',
    'PHYSICS': 'CHAPTER-1,2,3,4,5,6,7',
    'CHEMISTRY SYLLABUS': 'CHAPTER-1,2,3,4,5,6',
    'CHEMISTRY': 'CHAPTER-1,2,3,4,5,6',
    'AGRICULTURE SYLLABUS': 'CHAPTER-1,2,3,4',
    'AGRICULTURE': 'CHAPTER-1,2,3,4',
    'RELIGION SYLLABUS': 'CHAPTER-1,2,3,4,5',
    'RELIGION': 'CHAPTER-1,2,3,4,5',
    'BANGLADESH AND GLOBAL STUDIES SYLLABUS': 'CHAPTER-1,3,6,7,10,12,13',
    'BGS SYLLABUS': 'CHAPTER-1,3,6,7,10,12,13',
    'TRADE1 SYLLABUS': 'CHAPTER-1,2,3,4',
    'TRADE1': 'CHAPTER-1,2,3,4',
    'TRADE2 SYLLABUS': 'CHAPTER-1,2,3,4',
    'TRADE2': 'CHAPTER-1,2,3,4',
    
    # Sir Data
'Sir Principal': 'Md. Tofazzal Hoque / Mobile: 01711045755 / Phone (Office): 02589931204 / Email: tscthak38@gmail.com / Joining Date: 13 November 2023',
'Md. Tofazzal Hoque': 'Md. Tofazzal Hoque / Mobile: 01711045755 / Phone (Office): 02589931204 / Email: tscthak38@gmail.com / Joining Date: 13 November 2023',

'Chief Instructor Farm Machinery': 'Engr. Ajoy Kumar Singha / Mobile: 01721216006 / Phone (Office): 02589931204 / Email: ajoy20362@gmail.com / Joining Date: 20 August 2016',
'Ajoy Kumar Singha': 'Engr. Ajoy Kumar Singha / Mobile: 01721216006 / Phone (Office): 02589931204 / Email: ajoy20362@gmail.com / Joining Date: 20 August 2016',
'Farm Machinery': 'Engr. Ajoy Kumar Singha / Mobile: 01721216006 / Phone (Office): 02589931204 / Email: ajoy20362@gmail.com / Joining Date: 20 August 2016',

'Instructor1': 'Md. Abu Taher / Mobile: 01714624549 / Phone (Office): 02589931204 / Email: abu.tahertsc@gmail.com / Joining Date: 28 September 2018',
'Md. Abu Taher': 'Md. Abu Taher / Mobile: 01714624549 / Phone (Office): 02589931204 / Email: abu.tahertsc@gmail.com / Joining Date: 28 September 2018',

'Instructor Mathematics': 'Md. Hamidur Rahman / Mobile: 01717728340 / Phone (Office): 02589931204 / Email: hamidurtsc06@gmail.com / Joining Date: 08 July 2018',
'Mathematics': 'Md. Hamidur Rahman / Mobile: 01717728340 / Phone (Office): 02589931204 / Email: hamidurtsc06@gmail.com / Joining Date: 08 July 2018',

'Instructor2': 'Md. Muktadir Kabir / Mobile: 01714537159 / Phone (Office): 02589931204 / Email: muktadirkabir97@gmail.com / Joining Date: 16 October 2021',
'Md. Muktadir Kabir': 'Md. Muktadir Kabir / Mobile: 01714537159 / Phone (Office): 02589931204 / Email: muktadirkabir97@gmail.com / Joining Date: 16 October 2021',

'Instructor Mathematics2': 'Samanta Kumar Sen / Mobile: 01913802817 / Phone (Office): 02589931204 / Email: samantasen1451976@gmail.com / Joining Date: 03 October 2021',
'Samanta Kumar Sen': 'Samanta Kumar Sen / Mobile: 01913802817 / Phone (Office): 02589931204 / Email: samantasen1451976@gmail.com / Joining Date: 03 October 2021',

'Instructor Farm Machinery': 'Md. Monzurul Islam / Mobile: 01715412031 / Phone (Office): 02589931204 / Email: monzurul460@gmail.com / Joining Date: 08 May 2023',
'Md. Monzurul Islam': 'Md. Monzurul Islam / Mobile: 01715412031 / Phone (Office): 02589931204 / Email: monzurul460@gmail.com / Joining Date: 08 May 2023',

'Instructor Dress Making': 'Prokash Kumar Day / Mobile: 01717016008 / Phone (Office): 02589931204 / Email: prokashkumardey@gmail.com / Joining Date: 30 April 2008',
'Dress Making': 'Prokash Kumar Day / Mobile: 01717016008 / Phone (Office): 02589931204 / Email: prokashkumardey@gmail.com / Joining Date: 30 April 2008',
'Prokash Kumar Day': 'Prokash Kumar Day / Mobile: 01717016008 / Phone (Office): 02589931204 / Email: prokashkumardey@gmail.com / Joining Date: 30 April 2008',

'Instructor Computer': 'Md. Dabirul Islam / Mobile: 01723093434 / Phone (Office): 02589931204 / Email: dabirulttsc29@gmail.com / Joining Date: 10 March 2010',
'Md. Dabirul Islam': 'Md. Dabirul Islam / Mobile: 01723093434 / Phone (Office): 02589931204 / Email: dabirulttsc29@gmail.com / Joining Date: 10 March 2010',

'Instructor1 Farm Machinery': 'Md. Masud Rana / Mobile: 01718170546 / Phone (Office): 02589931204 / Email: masudranattsc@gmail.com / Joining Date: 11 February 2024',
'Md. Masud Rana': 'Md. Masud Rana / Mobile: 01718170546 / Phone (Office): 02589931204 / Email: masudranattsc@gmail.com / Joining Date: 11 February 2024',

'Instructor English': 'Kapil Dev Ray / Mobile: 01722251523 / Phone (Office): 02589931204 / Email: analogym@gmail.com',

'Instructor Chemistry': 'Mst. Mina Parveen / Mobile: 01751549538 / Phone (Office): 02589931204 / Email: minapervin50@gmail.com',
'Mst. Mina Parveen': 'Mst. Mina Parveen / Mobile: 01751549538 / Phone (Office): 02589931204 / Email: minapervin50@gmail.com',

'Instructor Bengali': 'Mohammad Fazlur Rahman / Mobile: 01785279378 / Phone (Office): 02589931204 / Email: fazlurss215@gmail.com',
'Mohammad Fazlur Rahman': 'Mohammad Fazlur Rahman / Mobile: 01785279378 / Phone (Office): 02589931204 / Email: fazlurss215@gmail.com',

'Instructor Bengali2': 'Borsa Rani Bina / Mobile: 01705899851 / Phone (Office): 02589931204 / Email: barsharanibina7@gmail.com',
'Borsa Rani Bina': 'Borsa Rani Bina / Mobile: 01705899851 / Phone (Office): 02589931204 / Email: barsharanibina7@gmail.com',

'Instructor IT Support & IoT Basics': 'Ismat Ara Begum / Mobile: 01750317044 / Phone (Office): 02589931204 / Email: ismot.hstu60@gmail.com / Joining Date: 15 January 2024',
'Ismat Ara Begum': 'Ismat Ara Begum / Mobile: 01750317044 / Phone (Office): 02589931204 / Email: ismot.hstu60@gmail.com / Joining Date: 15 January 2024',

'Instructor Electrical': 'Md. Inzam Haqueamul / Mobile: 01718787566 / Phone (Office): 02589931204 / Email: injamam.bd@gmail.com',
'Md. Inzam Haqueamul': 'Md. Inzam Haqueamul / Mobile: 01718787566 / Phone (Office): 02589931204 / Email: injamam.bd@gmail.com',

'Instructor Apparel Manufacturing Basics': 'Md. Raihan Habib Piyal / Mobile: 01751493830 / Phone (Office): 02589931204 / Email: piyalhabib@gmail.com / Joining Date: 07 July 2025',
'Md. Raihan Habib Piyal': 'Md. Raihan Habib Piyal / Mobile: 01751493830 / Phone (Office): 02589931204 / Email: piyalhabib@gmail.com / Joining Date: 07 July 2025',

'Junior Instructor IT Support & IoT Basics': 'Md. Saddam Hossain / Mobile: 01793870215 / Phone (Office): 02589931204 / Email: saddamcse18@gmail.com',
'Md. Saddam Hossain': 'Md. Saddam Hossain / Mobile: 01793870215 / Phone (Office): 02589931204 / Email: saddamcse18@gmail.com',

'Junior Instructor Electrical': 'Md. Limon Hasan / Mobile: 01773125460 / Phone (Office): 02589931204 / Email: nahidrejasumon@gmail.com',
'Md. Limon Hasan': 'Md. Limon Hasan / Mobile: 01773125460 / Phone (Office): 02589931204 / Email: nahidrejasumon@gmail.com',

'Junior Instructor Apparel Manufacturing Basics': 'Md. Ashraful Islam / Mobile: 01765963838 / Phone (Office): 02589931204 / Email: asa.te2012@gmail.com',
'Md. Ashraful Islam': 'Md. Ashraful Islam / Mobile: 01765963838 / Phone (Office): 02589931204 / Email: asa.te2012@gmail.com',

'Junior Instructor IT Support & IoT Basics2': 'Taslima Khatun / Mobile: 01748544504 / Phone (Office): 02589931204 / Email: mtaslima17@gmail.com',
'Taslima Khatun': 'Taslima Khatun / Mobile: 01748544504 / Phone (Office): 02589931204 / Email: mtaslima17@gmail.com',

'Junior Instructor Electrical2': 'Liton Chandra Roy / Mobile: 01706844707 / Phone (Office): 02589931204 / Email: slbarman3@gmail.com',
'Liton Chandra Roy': 'Liton Chandra Roy / Mobile: 01706844707 / Phone (Office): 02589931204 / Email: slbarman3@gmail.com',

'Junior Instructor IT Support & IoT Basics3': 'Kalesh Chandra / Mobile: 01744407128 / Phone (Office): 02589931204 / Email: kalesh77.kr@gmail.com',
'Kalesh Chandra': 'Kalesh Chandra / Mobile: 01744407128 / Phone (Office): 02589931204 / Email: kalesh77.kr@gmail.com',

'Junior Instructor IT Support & IoT Basics4': 'Md. Zulker Nayem / Mobile: 01677334185 / Phone (Office): 02589931204 / Email: zulkernayem2@gmail.com',
'Md. Zulker Nayem': 'Md. Zulker Nayem / Mobile: 01677334185 / Phone (Office): 02589931204 / Email: zulkernayem2@gmail.com',

'Junior Instructor Apparel Manufacturing Basics2': 'Mst. Nurista Parvin / Mobile: 01757374067 / Phone (Office): 02589931204 / Email: nuristaparvin23@gmail.com',
'Mst. Nurista Parvin': 'Mst. Nurista Parvin / Mobile: 01757374067 / Phone (Office): 02589931204 / Email: nuristaparvin23@gmail.com',

'Junior Instructor Apparel Manufacturing Basics3': 'Md. Ali Hasan / Mobile: 01763111079 / Phone (Office): 02589931204 / Email: alihasan.private@gmail.com',
'Md. Ali Hasan': 'Md. Ali Hasan / Mobile: 01763111079 / Phone (Office): 02589931204 / Email: alihasan.private@gmail.com',

   # D-Routine

    "D-Sunday": "Sunday = Tp1, Tt1, Rel, Math, Che, Bang",
    "D-Monday": "Monday = Phy/Che Lab, Bgs, Math, Agri, Com-Ap (Drawing), Electrical-Farm (Computer Application)",
    "D-Tuesday": "Tuesday = Tp1, Che, Eng, Math, Tt1",
    "D-Wednesday": "Wednesday = Tp2, Eng, Agri, Phy, Bang, Tt2",
    "D-Thursday": "Thursday = Tp2, Phy, Com-Ap (Drawing), Electrical-Farm (Computer Application), Eng, Tt2",

    # M-Routine
    "M-Sunday": "Sunday = Tp2, Tt, Tiffin, Math, Che, Rel, Phy",
    "M-Monday": "Monday = Tp2, Tt1, Tiffin, Bangla, Rel, Phy/Che.Pr./Sc.Lab",
    "M-Tuesday": "Tuesday = Tp1, Tt1, Tiffin, Agri, Eng, IT-Ap (Drawing), Elec-Fm (CA)",
    "M-Wednesday": "Wednesday = Tp1, Tt1, Tiffin, Eng, Math, IT-Ap (CA), Elec-Farm (Drawing)",
    "M-Thursday": "Thursday = Rel, Bangla, Phy, Math, Tiffin, Che, Bgs, Eng, Agri",


}
@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_message = request.form["message"].lower()

        # --- Search in dictionary ---
        reply = qna.get(user_message, "Sorry, I do not understand that yet.")

    return render_template("index.html", reply=reply)
if __name__ == "__main__":
    app.run(debug=True)
