-- Luiza, Nina, Marisa, Mehar 
-- CS 304 Final Project 
-- DDL's for database 

use mpapagel_db;

-- drop existing tables
drop table if exists user_resumes;
drop table if exists experience;
drop table if exists jobs; 
drop table if exists company_rep; 
drop table if exists company; 
drop table if exists industry; 
drop table if exists welles_affiliates; 
drop table if exists user; 

-- create user table
create table user(
    username varchar(20) not null, 
    name varchar(30), 
    passwd varchar(30),
    email varchar(50),
    primary key(username)
)

ENGINE = InnoDB;

-- create wellesley affiliates table
create table welles_affiliates (
    username varchar(20) not null,
    primary key (username),
    year int(4), 
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
    
-- create industry table
create table industry (
    iid int auto_increment not null ,
    ind_name varchar (30),
    primary key (iid)
)

ENGINE = InnoDB;

-- create company table
create table company (
    comp_id int auto_increment not null,
    comp_name varchar (150),
    iid int not null,
    locations varchar (150),
    primary key (comp_id),
    foreign key (iid) references industry(iid)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;

-- create company rep table
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

-- create jobs table
create table jobs (
    jid int auto_increment not null,
    username varchar(20) not null,
    title varchar (25),
    qual1 varchar (30),
    qual2 float,
    qual3 varchar (50), 
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

-- create experience table
create table experience (
    username varchar(20) not null,
    jid int not null,
    comp_id int not null,
    iid int not null,
    compensation int,
    primary key (username,jid),
    foreign key (username) references welles_affiliates(username),
    foreign key (comp_id) references company(comp_id),
    foreign key (iid) references industry(iid),
    foreign key (jid) references jobs(jid)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;


create table user_resumes (
    username varchar(20) not null,
    filename varchar(50),
    primary key (username),
    foreign key (username) references welles_affiliates(username)
        on update restrict 
        on delete restrict
)
ENGINE = InnoDB;


