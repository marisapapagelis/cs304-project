use mbhatia_db;


drop table if exists experience;
drop table if exists jobs; 
drop table if exists seekers;
drop table if exists worked_for; 
drop table if exists company_rep; 
drop table if exists company; -- done
drop table if exists industry; -- done

drop table if exists viewers; -- worked
drop table if exists courses_taken; -- worked
drop table if exists welles_affiliates; -- worked 
drop table if exists user; -- worked




create table user(
    username varchar(20) not null, 
    name varchar(30), 
    passwd varchar(30),
    email varchar(50),
    primary key(username)
)

ENGINE = InnoDB;

create table welles_affiliates (
    username varchar(20) not null,
    year date, 
    major varchar (20),
    gpa float, 
    org1 varchar (15),
    org2 varchar (15),
    org3 varchar (15),
    foreign key (username) references user(username) 
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;
    

create table courses_taken (
    username varchar(20) not null,
    cid int not null, -- From the wellesley course browser
    course_name varchar (20),
    primary key (username,cid),
    foreign key (username) references welles_affiliates(username)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;

create table industry (
    iid int auto_increment not null ,
    ind_name varchar (15),
    primary key (iid)
)

ENGINE = InnoDB;

create table company (
    comp_id int auto_increment not null,
    comp_name varchar (15),
    iid int not null,
    `desc` varchar (150),
    primary key (comp_id),
    foreign key (iid) references industry(iid)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;


-- create table seekers (
--     username varchar(20) not null,
--     name varchar (15),
--     iid int not null, -- industry that they are interested in
--     primary key (username),
--     foreign key (username) references welles_affiliates(username),
--     foreign key (iid) references industry(iid)
--         on update restrict 
--         on delete restrict
-- )
-- ENGINE = InnoDB;



-- create table viewers (
--     username varchar(20) not null,
--     name varchar (15),
--     primary key (username),
--     foreign key (username) references welles_affiliates(username)
--         on update restrict 
--         on delete restrict
-- )
-- ENGINE = InnoDB;

create table worked_for(
    username varchar(20) not null,
    comp_id int not null,
    comp_culture varchar (100),
    primary key (username,comp_id),
    foreign key (username) references viewers(username),
    foreign key (comp_id) references company(comp_id)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;

create table company_rep (
    username varchar(20) not null,
    name varchar (15),
    comp_id int,
    primary key (username),
    foreign key (comp_id) references company(comp_id),
    foreign key (username) references user(username)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;

create table jobs (
    jid int auto_increment not null,
    username varchar(20) not null,
    title varchar (25),
    qual1 varchar (15),
    qual2 varchar (15),
    qual3 varchar (15),
    job_status enum ('applications open', 'applications closed'),
    app_link varchar (40),
    comp_id int not null,
    iid int not null,
    primary key (jid),
    foreign key (username) references company_rep(username),
    foreign key (iid) references industry(iid)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;

create table experience (
    username varchar(20) not null,
    jid int not null,
    comp_id int not null,
    iid int not null,
    compensation int,
    interview_rating int,
    interview_ques varchar (300),
    hire_date date,
    end_date date,
    primary key (username,jid),
    foreign key (username) references viewers(username),
    foreign key (comp_id) references company(comp_id),
    foreign key (iid) references industry(iid),
    foreign key (jid) references jobs(jid)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;


