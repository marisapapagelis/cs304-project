

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

INSERT INTO courses_taken (username, cid, course_name) -- course numbers are taken from wellesley course browser
VALUES ('mars', 21134, 'ECON101');

INSERT INTO courses_taken (username, cid, course_name)
VALUES ('mehr', 21136, 'ECON102');

INSERT INTO industry (ind_name)
VALUES ('Investment Management');

INSERT INTO industry (ind_name)
VALUES ('Sales & Trading');

INSERT INTO company (comp_name,iid,`desc`)
VALUES ('JPMorgan Chase', 1, 'JPMorgan Chase & Co. is an American 
multinational investment bank and financial services holding company 
headquartered in New York City.');

INSERT INTO company (comp_name,iid,`desc`)
VALUES ('Morgan Stanley', 2, 'Morgan Stanley is an American multinational investment bank and 
financial services company headquartered at 1585 Broadway');

-- INSERT INTO seekers (username, name, iid)
-- VALUES ('mehr','Mehar', 1);

-- INSERT INTO viewers (username, name)
-- VALUES ('mars','Marisa');

INSERT INTO worked_for (username, comp_id, comp_culture)
VALUES ('mars',1, 'JPMorgan encourages people to work together and you can find great mentors here');

INSERT INTO company_rep(username,name,comp_id)
VALUES ('lu1','Luiza', 1);

INSERT INTO jobs (username, title, qual1, qual2, qual3, 
job_status, app_link, comp_id, iid )
VALUES ('lu1','portfolio analyst', 'BA in Economics', 'Minimum GPA: 3.5', 'Familiarity with Excel','applications closed',
NULL, 1, 1);


INSERT INTO experience (username, jid, comp_id , iid, compensation, interview_rating, interview_ques,
    hire_date,end_date)
VALUES ('mars',1,1,1,100000,4,'Tell me about yourself, What are your top strengths?', '2020-07-20', NULL); -- null for end date because she is still working there









