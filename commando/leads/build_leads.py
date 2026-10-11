"""Builds leads-2026-10-11.xlsx + .csv from Google Maps data pulled with Apify (11 Oct 2026).

Data: compass/crawler-google-places, 6 runs (Sheikh Zayed, 6th of October, Hadayek al Ahram/Haram,
New Cairo, Fifth Settlement, Maadi). Education, chains, franchises, hotel restaurants and listings
with no phone were removed. Re-run: python3 commando/leads/build_leads.py
"""
import csv
from pathlib import Path
from urllib.parse import quote_plus

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = Path(__file__).parent

# (name, niche, area, phone, website_on_google, socials_found, rating, reviews, one_star, special_note)
RAW = [
    # --- Sheikh Zayed ---
    ("Eccentric Beauty Salon", "Beauty", "Sheikh Zayed (The Gate Plaza)", "+20 10 31175000", "instagram.com/eccentric_beautysalon", "IG", 3.8, 17, 4, ""),
    ("Sense Beauty Salon", "Beauty", "Sheikh Zayed (El Zohour)", "+20 10 00200210", "", "", 4.7, 113, 6, ""),
    ("Abood Beauty Salon", "Beauty", "Sheikh Zayed (6th district)", "+20 10 98695192", "", "", 4.6, 30, 3, ""),
    ("Alfred & Mina Beauty Salon (Zayed)", "Beauty", "Sheikh Zayed (Isle Promenade mall)", "+20 10 70232319", "", "", 4.0, 190, 44, ""),
    ("Kriss Beauty Salons", "Beauty", "Sheikh Zayed", "+20 10 26566002", "", "", 4.3, 491, 67, ""),
    ("Be Perfect Beauty Salon", "Beauty", "Sheikh Zayed (El Karma entrance)", "+20 10 03774707", "facebook.com (profile page)", "FB", 4.2, 36, 6, ""),
    ("Beauty Station", "Beauty", "Sheikh Zayed (Beverly Hills, Gate Mall)", "+20 10 00148349", "instagram.com/beautybyraniaelbana", "IG", 4.8, 345, 14,
     "Google 'website' button opens a personal Instagram (beautybyraniaelbana), not an account named Beauty Station."),
    ("Padel Beats", "Padel", "Sheikh Zayed (Al Khamayel)", "+20 10 50055855", "padelbeats.com", "", 4.7, 36, 0, ""),
    ("The Padel Club", "Padel", "Sheikh Zayed (26th of July)", "+20 10 01122422", "", "", 3.1, 11, 4, ""),
    ("The Match Padel Tennis", "Padel", "Sheikh Zayed", "+20 11 14999092", "match.skedda.com/booking", "", 4.7, 312, 17,
     "Google 'website' is only a Skedda booking page: no brand site, no packages/coaching page."),
    ("Lets Padel", "Padel", "Sheikh Zayed (Dahshur link)", "+20 11 46817880", "instagram.com/letspadel.eg", "IG", 4.4, 45, 3, ""),
    ("MT Dental Clinic", "Dental", "Sheikh Zayed (16th district)", "+20 15 07050048", "", "", 4.7, 6, 0, ""),
    ("LEVATIO Dental Clinic", "Dental", "Sheikh Zayed (Badr El Din center)", "+20 10 90356639", "", "", 4.9, 47, 1, ""),
    ("Glam Dental Clinic", "Dental", "Sheikh Zayed (A Plaza mall)", "+20 11 16930569", "", "", 5.0, 19, 0, ""),
    ("Alpen Dental Implant Center", "Dental", "Sheikh Zayed (Beverly Hills)", "+20 10 19932335", "alpendentalimplantcenter.com", "", 5.0, 21, 0, ""),
    ("Tooth Time Dental Clinic (Dr Ahmed ElRefaey)", "Dental", "Sheikh Zayed (A Plaza mall)", "+20 10 03885594", "instagram.com/ahmed_elrefaeyy", "IG", 5.0, 18, 0,
     "Google 'website' is the doctor's personal Instagram, not a clinic page."),
    ("Smile Care Dental Clinics", "Dental", "Sheikh Zayed (Badr El Din center)", "+20 12 33323094", "", "", 4.9, 42, 0, ""),
    ("West Dental Clinic (Dr Omar Tarek)", "Dental", "Sheikh Zayed", "+20 11 48722217", "", "", 5.0, 6, 0, ""),
    ("Golden Dental Spa", "Dental", "Sheikh Zayed (Beverly Hills)", "+20 10 11000550", "", "", 5.0, 9, 0, ""),
    ("Dr Mohammed El-Baz Physiotherapy", "Physio", "Sheikh Zayed (Beverly Hills)", "+20 10 25540253", "", "", 4.9, 60, 1, ""),
    ("Peak Motion Therapy", "Physio", "Sheikh Zayed (Fithub Gym)", "+20 10 69494211", "", "", 5.0, 6, 0, ""),
    ("PrimePhysio Clinics", "Physio", "Sheikh Zayed (West Park)", "+20 11 55015489", "", "", 5.0, 6, 0, ""),
    ("PT Squad Clinic", "Physio", "Sheikh Zayed (Al Shabab Rd)", "+20 12 83724881", "", "", 5.0, 41, 0, ""),
    ("Next Move Real Estate", "Real estate", "Sheikh Zayed (Gamal Abdel Nasser)", "+20 10 64644577", "nextmovegypt.com", "", 5.0, 1, 0, ""),
    ("New Way Real Estate", "Real estate", "Sheikh Zayed (Gamal Abdel Nasser)", "+20 10 00847267", "", "", 4.5, 4, 0, ""),
    ("Royal Hills Real Estate", "Real estate", "Sheikh Zayed (Chillout One, Dahshur link)", "+20 10 09005833", "royalhillseg.com", "", 4.8, 26, 1, ""),
    ("Promax Real Estate", "Real estate", "Sheikh Zayed (Gamal Abdel Nasser)", "+20 10 06667805", "promaxeg.com", "FB", 5.0, 1, 0, ""),
    # --- 6th of October ---
    ("Dr Doaa Ibrahim El-Desouky (Derma)", "Dermatology", "6th of October (El Nasr St)", "+20 15 51990964", "", "", 4.4, 16, 2, ""),
    ("Vedette Clinic (Dr Gihan Yehia)", "Dermatology", "6th of October (Magda Square)", "+20 10 12534051", "", "", 4.5, 15, 2, ""),
    ("U Clinic Laser & Skin Care", "Dermatology", "6th of October (October Plaza)", "+20 10 10570712", "", "", 4.4, 67, 9, ""),
    ("Hur Clinic", "Dermatology", "6th of October (October Plaza)", "+20 11 11230124", "", "", 4.9, 41, 1, ""),
    ("SD Skin Clinic (Dr Hadeel Refaat)", "Dermatology", "6th of October (Central Axis)", "+20 12 80364424", "youtube.com/channel/…", "", 4.7, 13, 1,
     "Google 'website' is a YouTube channel."),
    ("Aldermatic (Dr Omar & Dr Mohamed El Ghanam)", "Dermatology", "6th of October (El Hosary)", "+20 10 00954280", "", "", 4.9, 37, 1, ""),
    ("White Coats Dermatology & Cosmetic Center", "Dermatology", "6th of October (American Towers)", "+20 12 20225339", "", "", 5.0, 4, 0, ""),
    ("Perfecta Clinic October", "Dermatology", "6th of October (Central Axis)", "+20 10 80649181", "", "", 4.9, 119, 2, ""),
    ("Queen Secret October", "Dermatology", "6th of October (Central Axis)", "+20 10 50757396", "facebook.com/QueenSecretclinic", "FB", 4.7, 14, 1, ""),
    ("Diamond Dental Clinic", "Dental", "6th of October (Diamond Mall)", "+20 10 97734747", "facebook.com/Diamond.Dental.Clinic1", "FB", 4.8, 27, 1, ""),
    ("Diamora Dental Clinic", "Dental", "6th of October (Diamond Mall, El Hosary)", "+20 10 23389998", "", "", 5.0, 42, 0, ""),
    ("Cure Dental Clinics (Dr Khaled Maher), October", "Dental", "6th of October (Dolphin Mall)", "+20 15 54009155", "curedentalclinics.com", "", 4.5, 44, 6, ""),
    ("DentoCare Dental Clinic", "Dental", "6th of October (Borai Plaza, Central Axis)", "+20 11 14448686", "", "", 5.0, 246, 1, ""),
    ("Dento Lashen (Dr Reham Lashen)", "Dental", "6th of October (Central Axis)", "+20 10 93907239", "dentolashendlc.com", "IG+FB", 4.9, 570, 19,
     "Strong presence already: pitch ads/lead generation or video content, not a new site."),
    ("Enhanced Dental Clinic", "Dental", "6th of October (Westgate Business Hub)", "+20 10 33522085", "forms.gle (Google Form)", "", 5.0, 274, 1,
     "Google 'website' button opens a Google Form, not a website: 274 reviews at 5.0 and nowhere to land."),
    ("911 Dental Clinic (Dr Shereef Azab)", "Dental", "6th of October (Central Axis)", "+20 10 61555988", "m.facebook.com/911DC", "FB", 4.9, 194, 3, ""),
    ("Aura Dental Clinic", "Dental", "6th of October (El Central)", "+20 11 03810006", "auracliniceg.com", "IG", 5.0, 16, 0,
     "The Facebook link on their website is a generic share URL, not their page."),
    ("Bahgat Gym", "Gym", "6th of October", "+20 11 42884444", "", "", 4.1, 84, 9, ""),
    ("Diva Gym & Spa (Ladies Only)", "Gym", "6th of October (Dolphin Mall)", "+20 10 67117444", "facebook.com/divagymandspaforher", "FB", 3.9, 94, 19, ""),
    ("Wolverine Gym", "Gym", "6th of October (El Hosary)", "+20 10 63910840", "", "", 4.9, 18, 0, ""),
    ("Avengers Fitness Gym", "Gym", "6th of October (2nd district)", "+20 10 13603137", "", "", 3.9, 24, 4, ""),
    ("Evolution Fitness Gym", "Gym", "6th of October (Square Mall)", "+20 10 50006974", "", "", 3.8, 31, 7, ""),
    ("Baggi Gym", "Gym", "6th of October", "+20 10 95088111", "", "", 4.6, 146, 8, ""),
    ("New You Gym", "Gym", "6th of October (Central Axis)", "+20 10 11228891", "", "", 4.8, 55, 1, ""),
    ("Star Gym October", "Gym", "6th of October (El Higaz)", "+20 10 05682407", "", "", 4.8, 119, 4, ""),
    ("Gold Gym (October)", "Gym", "6th of October (Generation 2000 School)", "+20 10 91003601", "facebook.com (profile page)", "FB", 4.2, 67, 5, ""),
    ("Pain & Gain Gym", "Gym", "6th of October (2nd district)", "+20 10 10446245", "facebook.com/paingaingymoct", "FB", 3.8, 59, 9, ""),
    ("Corto Lab Cafe", "Cafe", "6th of October", "+20 15 55422268", "", "", 4.3, 74, 10, ""),
    ("Laipari Cafe", "Cafe", "6th of October (West Gate mall)", "+20 10 40554773", "", "", 5.0, 74, 0, ""),
    ("Milana Cafe & More", "Cafe", "6th of October", "+20 10 35363363", "", "", 4.8, 50, 1, ""),
    ("Golden Cup Cafe", "Cafe", "6th of October (Applied Arts St)", "+20 11 04160443", "facebook.com/GoldenCup18", "FB", 4.8, 92, 1, ""),
    ("Ahl Masr Restaurant & Cafe", "Restaurant", "6th of October", "+20 10 00438007", "instagram.com/ahlmasar.eg", "IG", 4.4, 22, 2, ""),
    # --- Hadayek al Ahram / Haram ---
    ("Cure Dental Center (Hadayek)", "Dental", "Hadayek al Ahram (2nd gate)", "+20 2 33808383", "", "", 3.6, 14, 4, ""),
    ("Grand Dental Clinic", "Dental", "Hadayek al Ahram (Ahmose gate)", "+20 10 37073921", "", "", 4.9, 13, 0, ""),
    ("Dr Tamer Emara Dental Clinic", "Dental", "Hadayek al Ahram (old 2nd gate)", "+20 10 18706261", "", "", 4.9, 10, 0, ""),
    ("Smile Lounge Dental Clinic", "Dental", "Hadayek al Ahram (Gardenia St)", "+20 10 14442318", "", "", 4.7, 57, 4, ""),
    ("La Vida Dental Clinic", "Dental", "Hadayek al Ahram (Khafraa gate)", "+20 15 55673212", "instagram.com/the_dentalroom", "IG", 4.9, 99, 2,
     "Google 'website' opens the Instagram of a different name (the_dentalroom). A second Maps listing, 'The Dental Room', has the same phone, so the reviews are split."),
    ("Kingdom Gym", "Gym", "Hadayek al Ahram", "+20 11 18600135", "", "", 4.6, 40, 4, ""),
    ("Boost Gym", "Gym", "Haram (King Faisal St)", "+20 10 02317566", "", "", 4.4, 113, 13, ""),
    ("Power Gym (216 D)", "Gym", "Hadayek al Ahram", "+20 11 18521333", "", "", 4.1, 558, 37, ""),
    ("Rock Gym (CrossFit)", "Gym", "Hadayek al Ahram (Gardenia)", "+20 11 23088885", "facebook.com/Rockcrossfitgym", "FB", 4.6, 113, 10, ""),
    ("Air Gym & Spa / H2O Gym", "Gym", "Haram", "+20 12 74974401", "h2o-gym.com", "IG+FB+TT", 4.3, 525, 34,
     "The Maps listing is called 'Air Gym & Spa' but the website and socials are H2O Gym. People searching either name get confused."),
    ("Fit Miss Gym", "Gym", "Hadayek al Ahram", "+20 11 52866286", "facebook.com (single photo link)", "", 3.0, 11, 2,
     "Google 'website' opens a single Facebook photo."),
    ("S.A Salon", "Beauty", "Hadayek al Ahram", "+20 10 55084709", "", "", 4.9, 105, 2, ""),
    ("Seymour Salon", "Beauty", "Hadayek al Ahram (1st gate)", "+20 12 24079888", "", "", 4.9, 18, 0, ""),
    ("Bondok Beauty Salon", "Beauty", "Hadayek al Ahram", "+20 10 06010089", "facebook.com/BondokBeautySalon", "FB", 4.9, 67, 1, ""),
    ("A One Beauty Salon", "Beauty", "Hadayek al Ahram (4th gate)", "+20 10 98523221", "facebook.com (profile page)", "FB", 4.9, 723, 18, ""),
    ("Sisters Spa & Beauty Salon", "Beauty", "Hadayek al Ahram (Gardenia)", "+20 11 24644407", "linktr.ee/Sistersspaandbeautysalon", "IG+TT", 4.0, 16, 4, ""),
    ("Nomadics Restaurant & Rooftop", "Restaurant", "Haram (King Faisal St)", "+20 11 14111386", "facebook.com/share/… (share link)", "FB", 4.7, 336, 14, ""),
    ("Boom Restaurant", "Restaurant", "Haram (Abou Al Hool St, by the Pyramids)", "+20 11 11201750", "", "", 4.9, 781, 12, ""),
    ("The Grand Pharaoh Restaurant", "Restaurant", "Haram (Pyramids St)", "+20 10 91799977", "", "", 4.6, 154, 5, ""),
    ("Tona Fish Restaurant", "Restaurant", "Hadayek al Ahram (Al Amira Fadia)", "+20 11 20862267", "", "", 4.7, 199, 5, ""),
    ("Sheba Grill Restaurant", "Restaurant", "Haram (Zaghloul)", "+20 10 66523383", "", "", 4.8, 26, 1, ""),
    ("Beds Restaurant", "Restaurant", "Kerdasa (Mansoureya Rd)", "+20 15 55801975", "facebook.com/BedsRestaurant", "FB", 4.2, 41, 4, ""),
    ("Heaven Lounge & Rooftop View", "Restaurant", "Haram (Abou El Hol St)", "+20 10 64789249", "gizapyramidsviewinn.com", "", 3.7, 283, 47, ""),
    ("Pizza King (Hadayek)", "Restaurant", "Hadayek al Ahram (El Lebeny Axis)", "+20 15 00254855", "", "", 3.7, 150, 28, ""),
    # --- New Cairo / Fifth Settlement ---
    ("Town Fit Gym", "Gym", "New Cairo", "+20 11 18186598", "", "", 4.0, 121, 22, ""),
    ("Vein Gym", "Gym", "New Cairo (Street 15)", "+20 12 80693774", "", "", 3.9, 475, 65, ""),
    ("Flex Gym New Cairo", "Gym", "New Cairo (Street 4)", "+20 12 74998232", "", "", 4.8, 26, 1, ""),
    ("Bar and Dumbbell Gym", "Gym", "New Cairo (Street 4)", "+20 10 08866154", "facebook.com/BarAndDumbbell", "FB", 4.3, 101, 7, ""),
    ("Island Gym", "Gym", "New Cairo (Platinum Mall)", "+20 10 16666144", "m.facebook.com/IslandGymEg", "FB", 4.3, 357, 23, ""),
    ("Dr Rehab Zakaria (Derma)", "Dermatology", "New Cairo (Trivium, North 90th)", "+20 10 64022402", "dr-rehabzakaria.com", "IG+FB", 4.9, 79, 2, ""),
    ("A-Touch Clinics (Dr Amr Kotb)", "Dermatology", "New Cairo (Cairo Business Plaza)", "+20 10 22222072", "facebook.com/atouchclinics", "FB", 4.7, 95, 7, ""),
    ("Damas Derma Clinic", "Dermatology", "New Cairo (Elegantry Mall)", "+20 11 48829045", "instagram.com/damas.dermaclinic", "IG", 4.6, 73, 6, ""),
    ("Derma Health Clinics", "Dermatology", "New Cairo (Elegantry Mall)", "+20 10 30272501", "derma-health.com", "", 4.9, 172, 4, ""),
    ("Hebe Skin & Laser (Dr Heba Diab)", "Dermatology", "New Cairo (Street 17)", "+20 11 21271449", "m.facebook.com/SkinCosmetologyCenter", "FB", 3.9, 11, 3, ""),
    ("Habiba Elkeraby (Beautician)", "Beauty", "New Cairo (Elegantry Mall)", "+20 10 17542691", "", "", 4.5, 174, 19, ""),
    ("C Rancho", "Restaurant", "New Cairo (Street 2)", "+20 10 61060662", "", "", 4.8, 24, 1, ""),
    ("Piclama Group (Real Estate)", "Real estate", "New Cairo (Street 48)", "+20 15 00098110", "", "", 5.0, 3, 0, ""),
    ("Jamar Real Estate", "Real estate", "New Cairo (Town Center, Bank District)", "+20 11 11605818", "", "", 5.0, 1, 0, ""),
    # --- Maadi ---
    ("Dr Karim Fawzy (Cosmetic Dentist)", "Dental", "Maadi (Street 221)", "+20 10 15166629", "", "", 5.0, 327, 2, ""),
    ("Smile Me Clinic", "Dental", "Maadi (Degla Square)", "+20 11 44499432", "", "", 4.9, 280, 4, ""),
    ("Dental Care Clinic (Maadi)", "Dental", "Maadi (Street 233)", "+20 10 12055421", "", "", 5.0, 59, 0, ""),
    ("Mira Dental Center", "Dental", "Maadi", "+20 11 11197399", "yellowpages.com.eg profile", "IG+FB", 4.9, 235, 6,
     "Google 'website' opens their Yellow Pages profile, not their own site."),
    ("Degla Dental Clinic (Dr Mina Haroun)", "Dental", "Maadi (Street 208)", "+20 11 15496333", "degladentalclinic.com", "IG+FB", 4.5, 160, 18, ""),
    ("Maadi Dental Center (Prof Dr Amr Azim)", "Dental", "Maadi (Road 209)", "+20 12 28888950", "maadidental.com", "IG", 4.6, 303, 22, ""),
    ("Global Gym (Maadi)", "Gym", "Maadi (Al Mearag Rd)", "+20 10 29597545", "", "", 4.4, 40, 2, ""),
    ("Town Gym Maadi", "Gym", "Maadi (Misr-Helwan Agri Rd)", "+20 10 98982242", "", "", 4.5, 151, 6, ""),
    ("Hermood Lady's Fitness Club", "Gym", "Maadi (near Family Land)", "+20 10 29857223", "", "", 4.8, 99, 4, ""),
    ("Fit Factory (Club One)", "Gym", "Maadi (Club One)", "+20 11 11124561", "facebook.com/FitFactoryEgypt", "FB", 4.8, 88, 1, ""),
    ("Transformers Fitness Club", "Gym", "Maadi (Street 104)", "+20 10 21219000", "facebook.com/Transformersfitnesscenter", "FB", 4.0, 559, 65, ""),
    ("Carmel California", "Restaurant", "Maadi (Street 18)", "+20 15 50067619", "", "", 4.7, 1907, 61, ""),
    ("Lucille's", "Restaurant", "Maadi (Road 9)", "+20 10 92915000", "", "", 4.4, 2866, 85, ""),
    ("Bistro Paris (Maadi)", "Restaurant", "Maadi (Street 18)", "+20 12 89994449", "", "", 4.7, 1267, 52, ""),
    ("Fish Time", "Restaurant", "Maadi (Al Nasser St)", "+20 11 16862555", "", "", 4.9, 419, 9, ""),
    ("Calisto Restaurant & Cafe", "Restaurant", "Maadi (Family Land)", "+20 10 29107026", "facebook.com/calistotegypt", "FB", 4.7, 526, 15, ""),
    ("Bell's Restaurant & Cafe", "Restaurant", "Maadi (Mostafa Kamel Sq)", "+20 10 93077077", "facebook.com/BellsRestaurantandCafe", "FB", 4.3, 2543, 108, ""),
    ("Hair Look Salon", "Beauty", "Maadi (Dmshek)", "+20 12 85885655", "", "", 5.0, 71, 0, ""),
    ("ZOEYA Beauty Lounge (Maadi)", "Beauty", "Zahraa El Maadi", "+20 11 55018818", "", "", 4.5, 555, 47, ""),
    ("Kadoli Nubian Beauty", "Beauty", "Maadi (Street 104)", "+20 10 93344839", "", "", 4.9, 172, 3, ""),
    ("Beauty Salon Josy", "Beauty", "Maadi (Road 206)", "+20 2 25196009", "beautysalonjosycairo.weebly.com", "", 4.5, 288, 19,
     "Website is a free Weebly subdomain."),
    ("Evalee Beauty Salon", "Beauty", "Maadi (Degla, Street 231)", "+20 10 05676444", "", "", 4.7, 263, 18, ""),
    ("La Rosa Beauty Lounge", "Beauty", "Maadi (Al Lasilki)", "+20 11 14033048", "facebook.com/LaRosaEGY", "FB", 4.7, 840, 44, ""),
    ("The One Beauty Salon", "Beauty", "Maadi (Degla Square)", "+20 10 99990940", "instagram.com/theonebeautysalon_", "IG", 4.4, 355, 36, ""),
    ("Maha Farid Beauty Salon", "Beauty", "El Shorouk (Galaxy Mall)", "+20 10 31432463", "instagram.com/mahafarid.beautysalon", "IG", 4.3, 165, 20, ""),
    ("Marko Beauty Salon", "Beauty", "Maadi (Degla Square)", "+20 12 78515334", "instagram.com/marko__hair_dresser", "IG", 5.0, 64, 0, ""),
    ("Stride Clinic (Physio & Rehab)", "Physio", "Zahraa El Maadi", "+20 15 50551291", "", "", 5.0, 128, 0, ""),
    ("Infinity Physio Clinic Maadi", "Physio", "Maadi (Carrefour Rd)", "+20 11 53313513", "", "", 4.8, 171, 7, ""),
    ("Health Physiotherapy Center (Dr Mostafa Galal)", "Physio", "Maadi (Hegaz Grand Plaza)", "+20 15 07333491", "", "", 5.0, 21, 0, ""),
    ("Physio Masr (New Maadi)", "Physio", "New Maadi (Palestine Rd)", "+20 12 08444042", "", "", 4.7, 51, 4, ""),
    ("Physiocure Egypt", "Physio", "Zahraa El Maadi", "+20 11 29736666", "", "", 4.6, 217, 19, ""),
    ("Painless Physiotherapy Center", "Physio", "Maadi (Al Lasilki)", "+20 10 98091589", "facebook.com (profile page)", "FB", 4.8, 220, 8, ""),
    ("Physio Plus Clinic", "Physio", "Maadi (Street 300)", "+20 10 94599366", "physioplusclinic.lovable.app", "IG", 4.8, 50, 1,
     "Website is a free lovable.app subdomain (no own domain); Maps name is stuffed with keywords."),
    ("Dutch Physiotherapy (Royal Dutch Cure)", "Physio", "Maadi", "+20 12 74520212", "royaldutchcure.wordpress.com", "IG+FB", 4.8, 275, 6,
     "Website is a free WordPress.com blog subdomain."),
    ("Physio Egypt (Maadi)", "Physio", "Maadi (Hayat Degla)", "+20 10 09899785", "physioegyptclinics.com", "IG+FB", 4.9, 73, 1, ""),
]

FREE_HOSTS = ("instagram.com", "facebook.com", "linktr.ee", "youtube.com", "forms.gle", "yellowpages", "weebly.com",
              "wordpress.com", "lovable.app", "skedda.com", "web-rack.com")
NICHE_BASE = {"Dental": 6, "Dermatology": 6, "Real estate": 6, "Physio": 5, "Restaurant": 5, "Gym": 4, "Padel": 4, "Beauty": 4, "Cafe": 3}
PREMIUM_AREAS = ("Maadi", "New Cairo", "Sheikh Zayed", "Zahraa El Maadi")

WHY = {
    "Dental": "Patients pick a dentist on Google and Instagram before calling. You build the site and the content together and answer WhatsApp yourself, with no agency account manager in between. You run lead gen with real proof (Grapes Holiday: −62.5% ad spend, 2.5× leads).",
    "Dermatology": "Derma/aesthetic is sold with before/after content and booking ads. You do the website, content and ads in one place, and make in-house motion graphics that explain treatments without breaking medical-ad rules.",
    "Physio": "Physio patients search 'physiotherapy near me' and compare reviews. You turn their strong reviews into a booking site plus Google ranking and short treatment-explainer videos. Most local marketers only post graphics.",
    "Real estate": "Real estate lives on leads and landing pages. You've driven lead campaigns for travel (3,000+ qualified leads, Rihla 350K+ EGP in 2 weeks), so you think in leads and cost per lead, not likes.",
    "Gym": "Gyms sell on transformation videos, offers and fast WhatsApp replies. As a young, gym-going founder you can shoot reels members actually watch, and set up a page where people sign up for a trial.",
    "Padel": "Padel is booming and crowded. You give them a brand site with court booking and coaching, plus reels from the court, built and run by one person.",
    "Beauty": "Salons sell through Instagram reels and reviews. You turn their busy days into before/after reels and fix the booking route (WhatsApp/link), without the price tag of a big agency.",
    "Restaurant": "Restaurants live on video and delivery orders. You're already running a content trial for a Neapolitan pizza place in Pyramids Gardens, and you combine content, review replies and a menu/order site.",
    "Cafe": "Cafés compete on vibe content. You can batch a month of reels in one shoot day and give them a simple menu/location page.",
}


def phone_local(p):
    digits = p.replace("+", "").replace(" ", "")
    return "0" + digits[2:] if digits.startswith("20") else digits


def score(r):
    name, niche, area, phone, web, soc, rating, reviews, one, note = r
    gaps, need = [], 0
    web_l = web.lower()
    if not web:
        need += 4
        gaps.append("No website on their Google Maps listing")
    elif any(h in web_l for h in FREE_HOSTS):
        need += 3
        gaps.append(f"Google 'website' is not a real site ({web})")
    else:
        gaps.append(f"Has a site ({web}): check it on mobile before the call")
    if not soc:
        need += 2
        gaps.append("No Instagram/Facebook/TikTok linked anywhere on Google or their site")
    share = (one / reviews) if reviews else 0
    if reviews and share >= 0.10:
        need += 2
        gaps.append(f"{one} one-star reviews out of {reviews} ({share:.0%}): reputation/review replies needed")
    elif reviews and share >= 0.06:
        need += 1
        gaps.append(f"{one} one-star reviews out of {reviews} ({share:.0%})")
    if rating is not None and rating < 4.0:
        need += 1
        gaps.append(f"Rating {rating}: below the 4.0 people filter by")
    if reviews < 20:
        need += 1
        gaps.append(f"Only {reviews} Google reviews: weak local visibility")
    if note:
        need += 1
        gaps.insert(0, note)
    need = min(need, 10)

    ability = NICHE_BASE[niche]
    if any(a in area for a in PREMIUM_AREAS):
        ability += 1
    ability += 3 if reviews >= 500 else 2 if reviews >= 200 else 1 if reviews >= 50 else 0
    ability = min(ability, 10)
    return need, ability, gaps


def offer(niche, web, soc, reviews, one):
    web_l = web.lower()
    has_site = web and not any(h in web_l for h in FREE_HOSTS)
    parts = []
    if not has_site:
        parts.append("Website with WhatsApp/booking + Google Business Profile setup")
    if not soc or niche in ("Restaurant", "Beauty", "Gym", "Cafe", "Padel"):
        parts.append("monthly social content (reels)")
    if reviews and one / reviews >= 0.06:
        parts.append("review-reply + reputation plan")
    if niche in ("Dental", "Dermatology", "Real estate", "Physio") and has_site:
        parts.append("lead-gen ads + landing page")
    return "; ".join(parts) or "Content + ads audit"


def tier(ability):
    if ability >= 8:
        return "A: High-paying"
    if ability >= 6:
        return "B: Mid"
    return "C: Low / quick win"


DEAL = {
    "A: High-paying": "Website 20–35K EGP + social 10–20K/month (or ads 5K+/month)",
    "B: Mid": "Landing page 12–18K EGP or social 6–12K/month",
    "C: Low / quick win": "Landing page ~12K or Starter social 6K/month, or a one-off shoot",
}

rows = []
for r in RAW:
    name, niche, area, phone, web, soc, rating, reviews, one, note = r
    if not phone:
        continue
    need, ability, gaps = score(r)
    t = tier(ability)
    pl = phone_local(phone)
    rows.append({
        "Business": name, "Niche": niche, "Area": area, "Phone": pl,
        "WhatsApp link (if on WA)": "https://wa.me/2" + pl if pl.startswith("01") else "",
        "Website on Google": web or "none", "Socials found": soc or "none",
        "Rating": rating, "Reviews": reviews, "1★ reviews": one,
        "Gaps (check on your phone first)": " • ".join(gaps),
        "Offer to pitch": offer(niche, web, soc, reviews, one),
        "Tier": t, "Likely deal size": DEAL[t],
        "Why you (not another marketer)": WHY[niche],
        "Need (0–10)": need, "Ability to pay (0–10)": ability, "Score": need * ability,
        "Status": "Not called", "Call notes": "", "Follow-up date": "",
        "Google Maps": "https://www.google.com/maps/search/?api=1&query=" + quote_plus(f"{name} {area.split('(')[0]}"),
    })

rows.sort(key=lambda x: (-x["Score"], -x["Reviews"]))
rows = rows[:100]
# Call order: high-paying first, then by score inside each tier
rows.sort(key=lambda x: (x["Tier"], -x["Score"], -x["Reviews"]))
for i, r in enumerate(rows, 1):
    r["#"] = i

COLS = ["#", "Tier", "Business", "Niche", "Area", "Phone", "WhatsApp link (if on WA)", "Gaps (check on your phone first)",
        "Offer to pitch", "Likely deal size", "Why you (not another marketer)", "Rating", "Reviews", "1★ reviews",
        "Website on Google", "Socials found", "Need (0–10)", "Ability to pay (0–10)", "Score", "Status", "Call notes",
        "Follow-up date", "Google Maps"]

with open(OUT / "leads-2026-10-11.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    for r in rows:
        w.writerow({c: r[c] for c in COLS})

wb = Workbook()
ws = wb.active
ws.title = "Leads"
ws.append(COLS)
for r in rows:
    ws.append([r[c] for c in COLS])
head = PatternFill("solid", fgColor="1F2937")
for c in ws[1]:
    c.font = Font(bold=True, color="FFFFFF")
    c.fill = head
    c.alignment = Alignment(wrap_text=True, vertical="center")
tier_fill = {"A": "D1FAE5", "B": "FEF3C7", "C": "F3F4F6"}
widths = {"#": 5, "Tier": 16, "Business": 34, "Niche": 12, "Area": 28, "Phone": 14, "WhatsApp link (if on WA)": 26,
          "Gaps (check on your phone first)": 70, "Offer to pitch": 40, "Likely deal size": 34,
          "Why you (not another marketer)": 60, "Website on Google": 30, "Call notes": 40, "Google Maps": 30}
for i, col in enumerate(COLS, 1):
    ws.column_dimensions[get_column_letter(i)].width = widths.get(col, 12)
for row in ws.iter_rows(min_row=2):
    t = row[1].value[0]
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    row[1].fill = PatternFill("solid", fgColor=tier_fill[t])
ws.freeze_panes = "D2"
ws.auto_filter.ref = ws.dimensions
dv = DataValidation(type="list", formula1='"Not called,No answer,Call back,Gatekeeper,Interested,Audit sent,Meeting booked,Won,Not interested"')
ws.add_data_validation(dv)
st = COLS.index("Status") + 1
dv.add(f"{get_column_letter(st)}2:{get_column_letter(st)}{len(rows) + 1}")

# Summary sheet
s = wb.create_sheet("Summary")
s.append(["Tier", "Count", "What it means"])
meaning = {"A: High-paying": "Premium niche + area + big review volume. Call first; pitch website + monthly retainer.",
           "B: Mid": "Solid business, smaller. Pitch one clear project (landing page or 3-month content).",
           "C: Low / quick win": "Small or new. Quick wins, referrals and portfolio pieces; don't discount heavily."}
for t in meaning:
    s.append([t, sum(1 for r in rows if r["Tier"] == t), meaning[t]])
s.append([])
s.append(["Niche", "Count"])
for n in sorted({r["Niche"] for r in rows}):
    s.append([n, sum(1 for r in rows if r["Niche"] == n)])
s.append([])
s.append(["Scoring", "Need = no site (+4) / not a real site (+3), no socials linked (+2), 1★ ≥10% (+2) or ≥6% (+1), rating <4 (+1), <20 reviews (+1), specific issue (+1). "
          "Ability = niche base (dental/derma/real estate 6, physio/restaurant 5, gym/padel/beauty 4, cafe 3) + premium area (+1) + reviews ≥50/200/500 (+1/+2/+3). Score = Need × Ability."])
s.append(["Source", "Google Maps via Apify (compass/crawler-google-places), pulled 11 Oct 2026. Excluded: education, chains/franchises, hotel restaurants, listings without a phone."])
s.append(["Caveat", "'No socials linked' means none on the Google listing or website. They may still have an Instagram, so search their name before calling."])
s.column_dimensions["A"].width = 22
s.column_dimensions["B"].width = 12
s.column_dimensions["C"].width = 100
for row in s.iter_rows():
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")

# Playbook sheet (from calling-playbook.md)
p = wb.create_sheet("Call playbook")
p.column_dimensions["A"].width = 140
for line in (OUT / "calling-playbook.md").read_text(encoding="utf-8").splitlines():
    p.append([line])
    if line.startswith("#"):
        p.cell(p.max_row, 1).font = Font(bold=True, size=13 if line.startswith("## ") else 15)

wb.save(OUT / "leads-2026-10-11.xlsx")
print(len(rows), "rows;", {t: sum(1 for r in rows if r["Tier"] == t) for t in meaning})
print({n: sum(1 for r in rows if r["Niche"] == n) for n in sorted({r["Niche"] for r in rows})})
