CREATE CONSTRAINT IF NOT EXISTS FOR (n:Node) REQUIRE n.id IS UNIQUE;

MERGE (:Program :Node {id:'PROGRAM_BTECH_AI_ML', label:'B.Tech AI & ML'});
MERGE (:Program :Node {id:'PROGRAM_BE', label:'B.E (General)'});
MERGE (:Program :Node {id:'PROGRAM_MTECH', label:'M.Tech'});
MERGE (:Program :Node {id:'PROGRAM_MBBS', label:'MBBS'});
MERGE (:Program :Node {id:'PROGRAM_MD', label:'MD (Doctor of Medicine)'});
MERGE (:Program :Node {id:'PROGRAM_BBA', label:'BBA'});
MERGE (:Program :Node {id:'PROGRAM_MBA', label:'MBA'});
MERGE (:Program :Node {id:'PROGRAM_BA', label:'Bachelor of Arts'});
MERGE (:Program :Node {id:'PROGRAM_MA', label:'Master of Arts'});
MERGE (:Program :Node {id:'PROGRAM_BCOM', label:'B.Com'});
MERGE (:Program :Node {id:'PROGRAM_MCOM', label:'M.Com'});
MERGE (:Program :Node {id:'PROGRAM_BSC', label:'B.Sc'});
MERGE (:Program :Node {id:'PROGRAM_MSC', label:'M.Sc'});
MERGE (:Program :Node {id:'PROGRAM_BED', label:'B.Ed'});
MERGE (:Program :Node {id:'PROGRAM_LLB', label:'LLB (Bachelor of Laws)'});
MERGE (:Program :Node {id:'PROGRAM_LLM', label:'LLM (Master of Laws)'});
MERGE (:Program :Node {id:'PROGRAM_POLYTECHNIC', label:'Polytechnic Engineering Diploma'});
MERGE (:Program :Node {id:'PROGRAM_BCA', label:'Bachelor of Computer Applications'});
MERGE (:Specialization :Node {id:'SPEC_AI_ML', label:'Artificial Intelligence and Machine Learning'});
MERGE (:Specialization :Node {id:'SPEC_DATA_SCIENCE', label:'Data Science'});
MERGE (:Specialization :Node {id:'SPEC_CSE', label:'Computer Science Engineering'});
MERGE (:Specialization :Node {id:'SPEC_FINANCE', label:'Finance'});
MERGE (:Specialization :Node {id:'SPEC_MARKETING', label:'Marketing'});
MERGE (:Job :Node {id:'JOB_ML_ENGINEER', label:'Machine Learning Engineer'});
MERGE (:Job :Node {id:'JOB_DATA_SCIENTIST', label:'Data Scientist'});
MERGE (:Job :Node {id:'JOB_BUSINESS_ANALYST', label:'Business Analyst'});
MERGE (:Job :Node {id:'JOB_MEDICAL_DOCTOR', label:'Medical Doctor'});
MERGE (:Job :Node {id:'JOB_LAWYER', label:'Lawyer'});
MERGE (:Industry :Node {id:'NIC_6201', label:'Computer programming activities'});
MERGE (:Employer :Node {id:'EMP_TCS', label:'Tata Consultancy Services'});
MERGE (:Employer :Node {id:'EMP_INFOSYS', label:'Infosys'});
MERGE (:Employer :Node {id:'EMP_APOLLO', label:'Apollo Hospitals'});
MERGE (:Region :Node {id:'REG_BANGALORE', label:'Bangalore'});
MERGE (:Region :Node {id:'REG_DELHI', label:'New Delhi'});
MERGE (:Region :Node {id:'REG_MUMBAI', label:'Mumbai'});
MERGE (:Certification :Node {id:'CERT_GOOGLE_ML_ENGINEER', label:'Google ML Engineer'});
MERGE (:Certification :Node {id:'CERT_AWS_SOLUTIONS', label:'AWS Solutions Architect'});
MERGE (:Certification :Node {id:'CERT_PMP', label:'Project Management Professional'});
MERGE (:Skill :Node {id:'SKILL_MACHINE_LEARNING', label:'Machine Learning'});
MERGE (:Skill :Node {id:'SKILL_PYTHON', label:'Python Programming'});
MERGE (:Skill :Node {id:'SKILL_DATA_ANALYSIS', label:'Data Analysis'});
MERGE (:Skill :Node {id:'SKILL_PROJECT_MANAGEMENT', label:'Project Management'});
MERGE (:Skill :Node {id:'SKILL_BUSINESS_ACUMEN', label:'Business Acumen'});
MERGE (:Exam :Node {id:'EXAM_JEE_MAIN', label:'JEE Main'});
MERGE (:Exam :Node {id:'EXAM_NEET', label:'NEET'});
MERGE (:Exam :Node {id:'EXAM_12TH_BOARD', label:'12th Board'});
MERGE (:Exam :Node {id:'EXAM_CLAT', label:'CLAT (Common Law Admission Test)'});
MERGE (:Program :Node {id:'PROGRAM_BDS', label:'Bachelor of Dental Surgery'});
MERGE (:Specialization :Node {id:'SPEC_GENERAL_MEDICINE', label:'General Medicine'});
MERGE (:Specialization :Node {id:'SPEC_LITERATURE', label:'Literature'});
MERGE (:Specialization :Node {id:'SPEC_ACCOUNTING', label:'Accounting'});
MERGE (:Specialization :Node {id:'SPEC_PHYSICS', label:'Physics'});
MERGE (:Specialization :Node {id:'SPEC_CONSTITUTIONAL_LAW', label:'Constitutional Law'});
MERGE (:Specialization :Node {id:'SPEC_CARDIOLOGY', label:'Cardiology'});
MERGE (:Industry :Node {id:'NIC_8620', label:'Other professional, scientific and technical activities'});
MERGE (:Industry :Node {id:'NIC_6910', label:'Legal activities'});
MERGE (:Skill :Node {id:'SKILL_CLINICAL_DIAGNOSIS', label:'Clinical Diagnosis'});
MERGE (:Skill :Node {id:'SKILL_LEGAL_RESEARCH', label:'Legal Research'});
MATCH (a {id:'PROGRAM_BTECH_AI_ML'}),(b {id:'EXAM_JEE_MAIN'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BE'}),(b {id:'EXAM_JEE_MAIN'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BCA'}),(b {id:'EXAM_12TH_BOARD'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_MBBS'}),(b {id:'EXAM_NEET'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BDS'}),(b {id:'EXAM_NEET'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BBA'}),(b {id:'EXAM_12TH_BOARD'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BA'}),(b {id:'EXAM_12TH_BOARD'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BCOM'}),(b {id:'EXAM_12TH_BOARD'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BSC'}),(b {id:'EXAM_12TH_BOARD'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BED'}),(b {id:'EXAM_12TH_BOARD'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_LLB'}),(b {id:'EXAM_CLAT'})
MERGE (a)-[:REQUIRES]->(b);
MATCH (a {id:'PROGRAM_BTECH_AI_ML'}),(b {id:'SPEC_AI_ML'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BTECH_AI_ML'}),(b {id:'SPEC_DATA_SCIENCE'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BE'}),(b {id:'SPEC_CSE'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BCA'}),(b {id:'SPEC_CSE'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_MBBS'}),(b {id:'SPEC_GENERAL_MEDICINE'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BBA'}),(b {id:'SPEC_FINANCE'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BBA'}),(b {id:'SPEC_MARKETING'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BA'}),(b {id:'SPEC_LITERATURE'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BCOM'}),(b {id:'SPEC_ACCOUNTING'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BSC'}),(b {id:'SPEC_PHYSICS'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_LLB'}),(b {id:'SPEC_CONSTITUTIONAL_LAW'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_MTECH'}),(b {id:'SPEC_AI_ML'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_MBA'}),(b {id:'SPEC_FINANCE'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_MBA'}),(b {id:'SPEC_MARKETING'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_MD'}),(b {id:'SPEC_CARDIOLOGY'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_LLM'}),(b {id:'SPEC_CONSTITUTIONAL_LAW'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_AI_ML'}),(b {id:'JOB_ML_ENGINEER'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_AI_ML'}),(b {id:'JOB_DATA_SCIENTIST'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_DATA_SCIENCE'}),(b {id:'JOB_DATA_SCIENTIST'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_CSE'}),(b {id:'JOB_ML_ENGINEER'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_FINANCE'}),(b {id:'JOB_BUSINESS_ANALYST'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_MARKETING'}),(b {id:'JOB_BUSINESS_ANALYST'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_GENERAL_MEDICINE'}),(b {id:'JOB_MEDICAL_DOCTOR'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'SPEC_CONSTITUTIONAL_LAW'}),(b {id:'JOB_LAWYER'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'SPEC_AI_ML'})
MERGE (a)-[:CAN_BE_REACHED_FROM]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'SPEC_DATA_SCIENCE'})
MERGE (a)-[:CAN_BE_REACHED_FROM]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'SPEC_FINANCE'})
MERGE (a)-[:CAN_BE_REACHED_FROM]->(b);
MATCH (a {id:'JOB_MEDICAL_DOCTOR'}),(b {id:'SPEC_GENERAL_MEDICINE'})
MERGE (a)-[:CAN_BE_REACHED_FROM]->(b);
MATCH (a {id:'JOB_LAWYER'}),(b {id:'SPEC_CONSTITUTIONAL_LAW'})
MERGE (a)-[:CAN_BE_REACHED_FROM]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'NIC_6201'})
MERGE (a)-[:BELONGS_TO]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'NIC_6201'})
MERGE (a)-[:BELONGS_TO]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'NIC_6201'})
MERGE (a)-[:BELONGS_TO]->(b);
MATCH (a {id:'JOB_MEDICAL_DOCTOR'}),(b {id:'NIC_8620'})
MERGE (a)-[:BELONGS_TO]->(b);
MATCH (a {id:'JOB_LAWYER'}),(b {id:'NIC_6910'})
MERGE (a)-[:BELONGS_TO]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'SKILL_MACHINE_LEARNING'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'SKILL_PYTHON'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'SKILL_DATA_ANALYSIS'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'SKILL_PYTHON'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'SKILL_PROJECT_MANAGEMENT'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'SKILL_BUSINESS_ACUMEN'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'JOB_MEDICAL_DOCTOR'}),(b {id:'SKILL_CLINICAL_DIAGNOSIS'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'JOB_LAWYER'}),(b {id:'SKILL_LEGAL_RESEARCH'})
MERGE (a)-[:DEMANDS]->(b);
MATCH (a {id:'SKILL_MACHINE_LEARNING'}),(b {id:'JOB_ML_ENGINEER'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'SKILL_PYTHON'}),(b {id:'JOB_ML_ENGINEER'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'SKILL_DATA_ANALYSIS'}),(b {id:'JOB_DATA_SCIENTIST'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'SKILL_PROJECT_MANAGEMENT'}),(b {id:'JOB_BUSINESS_ANALYST'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'SKILL_BUSINESS_ACUMEN'}),(b {id:'JOB_BUSINESS_ANALYST'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'CERT_GOOGLE_ML_ENGINEER'}),(b {id:'SKILL_MACHINE_LEARNING'})
MERGE (a)-[:TEACHES]->(b);
MATCH (a {id:'CERT_GOOGLE_ML_ENGINEER'}),(b {id:'SKILL_PYTHON'})
MERGE (a)-[:TEACHES]->(b);
MATCH (a {id:'CERT_AWS_SOLUTIONS'}),(b {id:'SKILL_PYTHON'})
MERGE (a)-[:TEACHES]->(b);
MATCH (a {id:'CERT_AWS_SOLUTIONS'}),(b {id:'SKILL_PROJECT_MANAGEMENT'})
MERGE (a)-[:TEACHES]->(b);
MATCH (a {id:'CERT_PMP'}),(b {id:'SKILL_PROJECT_MANAGEMENT'})
MERGE (a)-[:TEACHES]->(b);
MATCH (a {id:'CERT_PMP'}),(b {id:'SKILL_BUSINESS_ACUMEN'})
MERGE (a)-[:TEACHES]->(b);
MATCH (a {id:'CERT_GOOGLE_ML_ENGINEER'}),(b {id:'JOB_ML_ENGINEER'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'CERT_GOOGLE_ML_ENGINEER'}),(b {id:'JOB_DATA_SCIENTIST'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'CERT_AWS_SOLUTIONS'}),(b {id:'JOB_ML_ENGINEER'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'CERT_AWS_SOLUTIONS'}),(b {id:'JOB_BUSINESS_ANALYST'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'CERT_PMP'}),(b {id:'JOB_BUSINESS_ANALYST'})
MERGE (a)-[:QUALIFIES_FOR]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'EMP_TCS'})
MERGE (a)-[:HIRED_BY]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'EMP_INFOSYS'})
MERGE (a)-[:HIRED_BY]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'EMP_TCS'})
MERGE (a)-[:HIRED_BY]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'EMP_INFOSYS'})
MERGE (a)-[:HIRED_BY]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'EMP_TCS'})
MERGE (a)-[:HIRED_BY]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'EMP_INFOSYS'})
MERGE (a)-[:HIRED_BY]->(b);
MATCH (a {id:'JOB_MEDICAL_DOCTOR'}),(b {id:'EMP_APOLLO'})
MERGE (a)-[:HIRED_BY]->(b);
MATCH (a {id:'EMP_TCS'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'EMP_TCS'}),(b {id:'REG_DELHI'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'EMP_TCS'}),(b {id:'REG_MUMBAI'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'EMP_INFOSYS'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'EMP_INFOSYS'}),(b {id:'REG_DELHI'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'EMP_APOLLO'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'EMP_APOLLO'}),(b {id:'REG_DELHI'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'EMP_APOLLO'}),(b {id:'REG_MUMBAI'})
MERGE (a)-[:LOCATED_IN]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:TRENDING_IN]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'REG_DELHI'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'REG_DELHI'})
MERGE (a)-[:TRENDING_IN]->(b);
MATCH (a {id:'JOB_ML_ENGINEER'}),(b {id:'REG_MUMBAI'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'JOB_DATA_SCIENTIST'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:TRENDING_IN]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'JOB_BUSINESS_ANALYST'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:TRENDING_IN]->(b);
MATCH (a {id:'JOB_MEDICAL_DOCTOR'}),(b {id:'REG_BANGALORE'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'JOB_LAWYER'}),(b {id:'REG_DELHI'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'JOB_LAWYER'}),(b {id:'REG_MUMBAI'})
MERGE (a)-[:SALARY_IN]->(b);
MATCH (a {id:'PROGRAM_BTECH_AI_ML'}),(b {id:'PROGRAM_MTECH'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BE'}),(b {id:'PROGRAM_MTECH'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_MBBS'}),(b {id:'PROGRAM_MD'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BBA'}),(b {id:'PROGRAM_MBA'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_BA'}),(b {id:'PROGRAM_MA'})
MERGE (a)-[:LEADS_TO]->(b);
MATCH (a {id:'PROGRAM_LLB'}),(b {id:'PROGRAM_LLM'})
MERGE (a)-[:LEADS_TO]->(b);