# Python code to extra user/project/hours used information 
# from second half of CHTC daily (weekly/monthly/yearly) reports
# input is a single tsv file in the "data" directory
# output is written to "reports" directory
# can be run in the ipython notebook (replace the "filename" string in cell 4)
# or on the command line as: 
# $python chtc_sheets data/spreadsheet.tsv

# dictionary for assigning projects -> departments
dept_dictionary = {
    'Economics_Roys':'Economics',
    'BMRB':'Biochemistry',
    'ECE_VanVeen':'Electrical and Computer Engineering',
    'CMS':'Physics',
    'Physics_Knezevic':'Physics',
    'Statistics_YazhenWang':'Statistics',
    'Cs_Ron':'Computer Sciences',
    'Math_Boston':'Mathematics',
    'IceCube':'Physics',
    'WID_Biology_Vetsigian':'Biology',
    'Economics_Gandhi':'Economics',
    'Statistics_Tsui':'Statistics',
    'ERC':'Mechanical Engineering',
    'Zoology_Lee':'Zoology',
    'MaterialScience_Morgan':'Materials Science and Engineering',
    'OSG':'off-campus',
    'Economics_Gregory':'Economics',
    'CAE':'multi-departmental',
    'Statistics_Ane':'Statistics',
    'WID_Biology_Roy':'Biostatistics and Medical Informatics',
    'Biostat_Broman':'Biostatistics and Medical Informatics',
    'LMCG':'Genetics',
    'WID':'multi-departmental',
    'MedPhysics_Bednarz':'Medical Physics',
    'BME_Williams':'Biomedical Engineering',
    'SSEC':'Atmospheric Sciences',
    'Botany_Spalding':'Botany',
    'Biochem_Mitchell':'Biochemistry',
    'ChemE_Mavrikakis':'Chemical and Biological Engineering',
    'BMI_Craven':'Biostatistics and Medical Informatics',
    'Astronomy_Heinz':'Astronomy',
    'MSE_Szlufarska':'Materials Science and Engineering',
    'Cs_Re':'Computer Sciences',
    'AnimalSciences_Berres':'Animal Sciences',
    'Purdue':'off-campus',
    'Genetics_Pool':'Genetics',
    'Physics_Friesen':'Physics',
    'Chemistry_Schmidt':'Chemistry',
    'Chemistry_Yethiraj':'Chemistry',
    'MechE_Trujillo':'Mechanical Engineering',
    'Physics_Bai':'Physics',
    'EarthCube':'Geoscience',
    'Economics_Freyberger':'Economics',
    'CS':'Computer Sciences',
    'Ece_Hagness':'Electrical and Computer Engineering',
    'AnimalSciences_Wu':'Animal Sciences',
    'CHTC':'Computer Sciences',
    'Entomology_Zhu':'Entomology',
    'Medicine_Johnson':'Medicine',
    'ChE_dePablo':'Chemical and Biological Engineering',
    'CEE_Loheide':'Civil and Environmental Engineering',
    'Botany_Givnish':'Botany',
    'Genetics_Payseur':'Genetics',
    'MechE_Rutland':'Mechanical Engineering',
    'Waisman_Alexander':'Psychiatry',
    'EngrPhysics_Wilson':'Engineering Physics',
    'MSE_Voyles':'Materials Science and Engineering',
    'SOAR':'Computer Sciences',
    'Chemistry_Cui':'Chemistry',
    'Physics_Sarff':'Physics',
    'Biostat':'Biostatistics and Medical Informatics',
    'Waisman_Center':'multi-departmental',
    'Math_Thiffeault':'Mathematics',
    'Astronomy_DOnghia':'Astronomy',
    'WID_Biology_Vestigian':'Bacteriology',
    'Physics_Knutson':'Physics',
    'Physics_Perkins':'Physics',
    'Oncology_Hill':'Oncology',
    'UWEC_Ma':'off-campus',
    'Oncology_Sugden':'Oncology',
    'ECE_Ramanathan':'Electrical and Computer Engineering',
    'Statistics_Zhang':'Statistics',
    'Geoscience_DeMets':'Geoscience',
    'NucEngr_Schmitz':'Engineering Physics',
    'Biostat_Wang':'Biostatistics and Medical Informatics',
    'MedPhysics_Bender':'Medical Physics',
    'Business_Gofman':'Finance',
    'Economics_Sorensen':'Economics',
    'MedPhysics_Campagnola':'Medical Physics',
    'Astronomy_Townsend':'Astronomy',
    'Business_Levine':'Finance',
    'Cs_Sohi':'Computer Sciences',
    'Biochem_Fox':'Biochemistry',
    'SmallMolecule_Hoffman':'Oncology',
    'Physics_Joynt':'Physics',
    'MechE_Kokjohn':'Mechanical Engineering',
    'Economics_Kennan':'Economics',
    'Cs_Hill':'Computer Sciences',
    'Biostat_Zhao':'Biostatistics and Medical Informatics',
    'Physics_Forest':'Physics',
    'EngrPhysics_Sovinec':'Engineering Physics',
    'Chemistry_Coon':'Chemistry',
    'Pharmacy_Kwan':'Pharmaceutical Sciences',
    'Biostat_Singh':'Biostatistics and Medical Informatics',
    'Psychology_Rogers':'Pyschology',
    'Statistics_Shao':'Statistics',
    'Waisman_Vorperian':'multi-departmental',
    'UCSB':'off-campus',
    'AnimalSciences_Rosa':'Animal Sciences',
    'Math_Spagnolie':'Mathematics',
    'Neurology_Hermann':'Neurology',
    'EngrPhysics_Anderson':'Engineering Physics',
    'GLBRC_WEI':'multi-departmental',
    'EngrPhysics_Hegna':'Engineering Physics',
    'BMI_Pack':'Biostatistics and Medical Informatics',
    'MechE_Thelen':'Mechanical Engineering',
    'History_Chowkwanyun':'History',
    'Cs_Sankaralingam':'Computer Sciences',
    'Statistics_Hanlon':'Statistics',
    'other':'other',
    'Botany_Sytsma':'Botany',
    'EdPsychology_Kaplan':'Educational Psychology',
    'UWPlatt_Haasl':'off-campus',
    'MedPhysics_Varghese':'Medical Physics',
    'Page_Learn':'Biostatistics and Medical Informatics',
    'Psychiatry_Tononi':'Psychiatry',
    'Zoology_Turner':'Zoology',
    'Astronomy_Bershady':'Astronomy',
    'Primate_Oconnor':'Pathology and Laboratory Medicine',
    'Psychiatry_Koenigs':'Psychiatry',
    'OSG-SS':'off-campus',
    'Economics_Shi':'Economics',
    'Arizona_iPlant':'off-campus',
    'WID_LEL':'multi-departmental',
    'Bacteriology_Rey':'Bacteriology',
    'Botany_Cameron':'Botany',
    'Math_Stechmann':'Mathematics',
    'Medicine_Pepperell':'Medicine',
    'EdPsychology_Steiner':'Educational Psychology',
    'BotanyMath_Staff':'multi-departmental',
    'Psychiatry_Kalin':'Psychiatry',
    'BMI_Gitter':'Biostatistics and Medical Informatics',
    'MIR_Mackie':'Medical Physics',
    'CEE_Wu':'Civil and Environmental Engineering',
    'Geoscience_Feigl':'Geoscience',
    'BME_Ashton':'Biomedical Engineering',
    'Surgery_Jiang':'Surgery',
    'Biochemistry_Denu':'Biochemistry',
    'GLBRC_Benton':'multi-departmental',
    'Botany_Gilroy':'Botany',
    'Astronomy_Tremonti':'Astronomy',
    'Math':'Mathematics',
    'Biochem':'Biochemistry',
    'Economics_Atalay':'Economics',
    'CsBanerjee':'Computer Sciences',
    'Wempec_Jahns':'Electrical and Computer Engineering',
    'Marschfield_Hebbring':'off-campus',
    'Bacteriology_McMahon':'Bacteriology',
    'Statistics_Yu':'Statistics',
    'Psychiatry_Abercrombie':'Psychiatry',
    'Radiology_Brace':'Radiology',
    'Neurology_Gallagher':'Neurology',
    'Geoscience_Cardiff':'Geoscience',
    'CEE_hedegaard':'Civil and Environmental Engineering',
    'UWMilwaukee':'off-campus',
    'Atlas':'Physics',
    'MechE_Pfotenhauer':'Mechanical Engineering',
    'CEE_GinderVogel':'Civil and Environmental Engineering',
    'CEE_Hedegaard':'Civil and Environmental Engineering',
    'StatisticsYazhenWang':'Statistics',
    'Pathobio_Friedrich':'Pathobiological Sciences',
    'Loci_Eliceiri':'Biomedical Engineering',
    'ChemBioEngr_Graham':'Chemical and Biological Engineering',
    'Oncology_Ahlquist':'Oncology',
    'AnimalSciences':'Animal Sciences',
    'backfill':'other',
    'Statistics_Keles':'Statistics',
    'Botany_Graham':'Botany',
    'Psychiatry_Cirelli':'Psychiatry',
    'UWEC':'off-campus',
    'Pathology_Oconnor':'Pathology and Laboratory Medicine',
    'CBE_Yin':'Chemical and Biological Engineering',
    'Geoscience_Staff':'Geoscience',
    'History_Chowkanyun':'History',
    'AgAplliedEcon_Grainger':'Agricultural and Applied Economics',
    'DoIT':'Computer Sciences',
    'MedPhysics_DeWerd':'Medical Physics',
    'EdPsychology_Wollack':'Educational Psychology',
    'OSG-People':'off-campus',
    'GeoDeepDive':'Geoscience',
    'SCO_Wiscland':'Geography',
    'Bionates_Saha':'Biomedical Engineering',
    'AAE_NETS':'Agricultural and Applied Economics',
    'ECE_Sethares':'Electrical and Computer Engineering',
    'BME_Chesler':'Biomedical Engineering',
    'MechE_Qian':'Mechanical Engineering',
    'Physics_Barger':'Physics',
    'MechE_Negrut':'Mechanical Engineering',
    'Astronomy_Stanimirovic':'Astronomy',

# dictionary for assigning depts -> colleges
college_dictionary = {
    'Statistics':'Letters and Sciences',
    'Genetics':'Agricultural and Life Sciences',
    'Biochemistry':'Agricultural and Life Sciences',
    'Pharmaceutical Sciences':'Pharmacy',
    'Psychiatry':'Medicine and Public Health',
    'Radiology':'Medicine and Public Health',
    'Civil and Environmental Engineering':'Engineering',
    'Medicine':'Medicine and Public Health',
    'Mathematics':'Letters and Sciences',
    'Biology':'Letters and Sciences',
    'multi-departmental':'other',
    'Finance':'Business',
    'Mechanical Engineering':'Engineering',
    'Biomedical Engineering':'Engineering',
    'Entomology':'Agricultural and Life Sciences',
    'Engineering Physics':'Engineering',
    'Electrical and Computer Engineering':'Engineering',
    'other':'other',
    'Biostatistics and Medical Informatics':'Medicine and Public Health',
    'Astronomy':'Letters and Sciences',
    'Medical Physics':'Medicine and Public Health',
    'Economics':'Letters and Sciences',
    'Computer Sciences':'Letters and Sciences',
    'Materials Science and Engineering':'Engineering',
    'Agricultural and Applied Economics':'Agricultural and Life Sciences',
    'Pathology and Laboratory Medicine':'Medicine and Public Health',
    'Bacteriology':'Agricultural and Life Sciences',
    'Chemistry':'Letters and Sciences',
    'Physics':'Letters and Sciences',
    'Geoscience':'Letters and Sciences',
    'History':'Letters and Sciences',
    'Botany':'Letters and Sciences',
    'Oncology':'Medicine and Public Health',
    'Atmospheric Sciences':'Letters and Sciences',
    'Animal Sciences':'Agricultural and Life Sciences',
    'Educational Psychology':'Education',
    'off-campus':'off-campus',
    'Chemical and Biological Engineering':'Engineering',
    'Pyschology':'Letters and Sciences',
    'Neurology':'Medicine and Public Health',
    'Zoology':'Letters and Sciences',
    'Pathobiological Sciences':'Veterinary Medicine',
    'Surgery':'Medicine and Public Health',
    'Geography':'Letters and Sciences'
}

import sys
import pandas

#set filename and extract useful pieces for creating output file names
filename = sys.argv[1]
base_fn = filename.split('/')[1].split('.')[0]
date_fn = base_fn.split('_')[1]+'_'+base_fn.split('_')[2]

#read in data and a list of headers
data = pandas.read_csv(filename, delimiter='\t', skiprows=[1,2], thousands=',')
headers = list(data.columns.values)
date = headers[1]

#extract data 
#(usernames, depts, colleges, #submit point#, total hours, broken down into htc, hpc, osg, non-chtc)
# as individual lists

# list of usernames
def username(row):
    if row[date].split('_')[0] == 'nu':
        return row[date].split('_')[0]+"_"+row[date].split('_')[1]
    else: 
        return row[date].split('_')[0]
usernames = list(data.apply(username, axis=1))

# list of Projects
projects = list(data["Project"])

# list of departments
def dept(row):
    proj_dept = row['Project']
    return dept_dictionary[proj_dept]
depts = list(data.apply(dept, axis=1))

# list of colleges
def college(row):
    proj_dept = row['Project']
    dept = dept_dictionary[proj_dept]
    return college_dictionary[dept]
colleges = list(data.apply(college, axis=1))

# list of submit points
#def submit(row):
#    return row[date].split('_')[-1]
#submit_point = list(data.apply(submit, axis=1))

# lists of hours (non chtc, chtc (htc), slurm (hpc), and osg)
slurm = list(data["SLURM"])
chtc = list(data["CHTC"])
osg = list(data["OSG"])
total = list(data["Total"])

def nonchtc(row):
    return row['Total'] - row['CHTC'] - row['SLURM'] - row['OSG']
outside = list(data.apply(nonchtc, axis=1))

#make user_data table from all lists above
user_data = pandas.DataFrame.from_items( [('username', usernames), ('project_name',projects),
                                         ('dept', depts), ('college', colleges),
                                         ('total', total), ('htc', chtc), 
                                         ('hpc', slurm), ('osg', osg), ('other', outside)])

# save all reorganized data
cleaned_fn = 'reports/'+date_fn+'_cleaned.tsv'
cleaned_file = open(cleaned_fn, 'w')
user_data.to_csv(cleaned_file, sep='\t', index=False)
cleaned_file.close()

# get chtc users with more than 0 hours
# this includes all people with hours on chtc supported hardware
# (which necessarily includes everyone submitting from a CHTC submit point)

chtc_users = user_data[((user_data.osg > 0) | 
                        (user_data.htc > 0) | 
                        (user_data.hpc > 0)) & (user_data.total > 0)]

# save chtc specific data
chtc_fn = 'reports/'+date_fn+'_chtc.tsv'
chtc_file = open(chtc_fn, 'w')
chtc_users.to_csv(chtc_file, sep='\t', index=False)
chtc_file.close()



