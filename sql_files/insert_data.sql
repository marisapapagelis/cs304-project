-- Luiza, Nina, Marisa, Mehar 
-- CS 304 Final Project 
-- Insert Sample Data 

-- RUN APP.PY TO INSERT USERS ONCE BEFORE RUNNING THIS SQL

use mpapagel_db; 

--inserting dummy row for company 1 and industry 1
INSERT INTO industry (ind_name)
VALUES ('None');

INSERT INTO company (comp_name, iid, locations)
VALUES ('None',1, 'None')

-- insert wellesley affiliates into wellesley affiliate table
INSERT INTO welles_affiliates (username, year, major, gpa, org1, org2, org3)
VALUES ('mars', 2022, 'Economics', 3.98, 'CSClub', 'WNews', 'WIB');

INSERT INTO welles_affiliates (username, year, major, gpa, org1, org2, org3)
VALUES ('mehr', 2022, 'Data Science', 2.2, 'ISOC', 'WNews', 'WIB');

insert into welles_affiliates(username, year, major, gpa)
values('ng', 2022, 'Music', 3.7);

-- insert industries into industry table
INSERT INTO industry (ind_name)
VALUES ('Financials'); 

INSERT INTO industry (ind_name) 
VALUES ('FinTech');

INSERT INTO industry (ind_name) 
VALUES ('Technology');

insert into industry (ind_name) 
values ('Food/Beverage');

-- insert companies into company table
INSERT INTO company (comp_name,iid,locations)
VALUES ('JPMorgan Chase', 2, 'NY, SFO'); 

INSERT INTO company (comp_name,iid,locations)
VALUES ('Morgan Stanley', 2, 'NY, SFO');

insert into company(comp_name, iid, locations)
values ('Apple', 4, 'NY, SFO, CHI'); 
insert into company(comp_name, iid, locations)
values ('Dairy Queen', 5, 'NY, NJ, MA, FL');

-- insert company representative into company rep table
INSERT INTO company_rep(username,name,comp_id)
VALUES ('lu1','Luiza', 2);

insert into company_rep(username, name, comp_id)
values ('styles', 'Harry Styles', 4);

insert into company_rep(username, name, comp_id)
values ('horan', 'Niall Horan', 2);

insert into company_rep(username, name, comp_id)
values ('louis', 'Louis Tomlinson', 3);

insert into company_rep(username, name, comp_id)
values ('liam', 'Liam Payne', 5);

insert into company_rep(username, name, comp_id)
values ('zayn', 'Zayn Malik', 5);

-- insert job for lu1 into jobs table
INSERT INTO jobs (username, title, qual1, qual2, qual3, job_status, app_link, comp_id, iid )
VALUES ('lu1','portfolio analyst', 'BA in Economics', 'Minimum GPA: 3.5', 
'Familiarity with Excel','applications closed', NULL, 2, 2);

insert into jobs(username, title, qual1, qual2, qual3, job_status, app_link, comp_id, iid) 
values ('lu1', 'software engineer', 'BA in computer engineering', 'Minimum GPA: 3.7', 'Java', 'open', NULL, 2, 2);

insert into jobs(username, title, qual1, qual2, qual3, job_status, app_link, comp_id, iid) 
values ('styles', 'Apple Music Licensing', 'MBA', NULL, 'Microsoft Office', 'open', NULL, 4, 4);

insert into jobs(username, title, qual1, qual2, qual3, job_status, app_link, comp_id, iid) 
values ('liam', 'Retail Manager', 'MBA', NULL, 'Microsoft Office', 'closed', NULL, 5, 5);

-- insert experience for mars into experience table
INSERT INTO experience (username, jid, comp_id , iid, compensation)
VALUES ('mars',1,2,2,100000)