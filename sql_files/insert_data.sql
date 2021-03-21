-- Luiza, Nina, Marisa, Mehar 
-- CS 304 Final Project 
-- Insert Sample Data 

use mbhatia_db; 

-- insert users into user table
INSERT INTO user(username,name,passwd,email) 
VALUES ('mars', 'Marisa', 'cat1234', 'mpapagel');

INSERT INTO user(username,name,passwd,email) 
VALUES ('mehr','Mehar', 'dog657', 'mbhatia');

INSERT INTO user(username,name,passwd,email) 
VALUES ('lu1','Luiza', 'monkey657', 'lmiranda');

-- insert wellesley affiliates into wellesley affiliate table
INSERT INTO welles_affiliates (username, year, major, gpa, org1, org2, org3)
VALUES ('mars', 2022, 'Economics', 3.98, 'CSClub', 'WNews', 'WIB');

INSERT INTO welles_affiliates (username, year, major, gpa, org1, org2, org3)
VALUES ('mehr', 2022, 'Data Science', 2.2, 'ISOC', 'WNews', 'WIB');

-- insert industries into industry table
INSERT INTO industry (ind_name)
VALUES ('Financials');

INSERT INTO industry (ind_name)
VALUES ('FinTech');

INSERT INTO industry (ind_name)
VALUES ('Technology');

-- insert companies into company table
INSERT INTO company (comp_name,iid,locations)
VALUES ('JPMorgan Chase', 1, 'NY, SFO');

INSERT INTO company (comp_name,iid,locations)
VALUES ('Morgan Stanley', 2, 'NY, SFO');

-- insert company representative into company rep table
INSERT INTO company_rep(username,name,comp_id)
VALUES ('lu1','Luiza', 1);

-- insert job for lu1 into jobs table
INSERT INTO jobs (username, title, qual1, qual2, qual3, job_status, app_link, comp_id, iid )
VALUES ('lu1','portfolio analyst', 'BA in Economics', 'Minimum GPA: 3.5', 
'Familiarity with Excel','applications closed', NULL, 1, 1);

-- insert experience for mars into experience table
INSERT INTO experience (username, jid, comp_id , iid, compensation)
VALUES ('mars',1,1,1,100000)

