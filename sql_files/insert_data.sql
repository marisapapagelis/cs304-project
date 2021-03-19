use lmiranda_db; 

INSERT INTO user(username,name,passwd,email) 
VALUES ('mars', 'Marisa', 'cat1234', 'mpapagel');

INSERT INTO user(username,name,passwd,email) 
VALUES ('mehr','Mehar', 'dog657', 'mbhatia');


INSERT INTO user(username,name,passwd,email) 
VALUES ('lu1','Luiza', 'monkey657', 'lmiranda');

INSERT INTO welles_affiliates (username, year, major, gpa, org1, org2, org3)
VALUES ('mars', 2022, 'Economics', 3.98, 'CSClub', 'WNews', 'WIB');

INSERT INTO welles_affiliates (username, year, major, gpa, org1, org2, org3)
VALUES ('mehr', 2022, 'Data Science', 2.2, 'ISOC', 'WNews', 'WIB');

INSERT INTO industry (ind_name)
VALUES ('Financials');

INSERT INTO industry (ind_name)
VALUES ('Technology');

INSERT INTO company (comp_name,iid,locations)
VALUES ('JPMorgan Chase', 1, 'NY, SFO');

INSERT INTO company (comp_name,iid,locations)
VALUES ('Morgan Stanley', 2, 'NY, SFO');


INSERT INTO company_rep(username,name,comp_id)
VALUES ('lu1','Luiza', 1);

INSERT INTO jobs (username, title, qual1, qual2, qual3, 
job_status, app_link, comp_id, iid )
VALUES ('lu1','portfolio analyst', 'BA in Economics', 3.5, 'Familiarity with Excel','applications closed',
NULL, 1, 1);

INSERT INTO experience (username, jid, comp_id , iid, compensation)
VALUES ('mars',1,1,1,100000)

