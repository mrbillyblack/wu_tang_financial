CREATE DATABASE member;
use member;

CREATE TABLE members(
    MemberID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    LastName varchar(100) NOT NULL,
    Address varchar(100) NOT NULL,
    City varchar(100) NOT NULL,
    State varchar(100) NOT NULL,
    Zip varchar(100) NOT NULL,
    Country varchar(100) NOT NULL,
    Valid boolean,
    PRIMARY KEY (MemberID)
);

INSERT INTO members (FirstName, LastName, Address, City, State, Zip, Country)
values
    ('George', 'Washington', '69 Young St.', 'Mount Juliet', 'TN', '37122', 'USA'),
    ('Thomas', 'Jefferson', '8430 Lake Ln.', 'Phoenixville', 'PA', '19460', 'USA'),
    ('Abraham', 'Lincoln', '67 Snake Hill Dr.', 'Dallas', 'GA', '30132', 'USA'),
    ('John', 'Adams', '241 N. Victoria Ave.', 'Dorchester Center', 'MA', '02124', 'USA'),
    ('Theodore', 'Roosevelt', '731 Brickyard St.', 'Worcester', 'MA', '01604', 'USA'),
    ('Franklin', 'Roosevelt', '9115 Sycamore Cir.', 'Portage', 'IN', '46368', 'USA'),
    ('John', 'Kennedy', '231 Kent Dr.', 'Cincinnati', 'OH', '45211', 'USA'),
    ('Lyndon', 'Johnson', '9125 Hudson St.', 'Orange Park', 'FL', '32065', 'USA'),
    ('Jimmy', 'Carter', '622 Bayberry Rd.', 'Tuscaloosa', 'AL', '35405', 'USA'),
    ('Ronald', 'Reagan', '80 White Ave.', 'Riverview', 'FL', '33569', 'USA'),
    ('Barack', 'Obama', '57 Young Dr.', 'Cary', 'NC', '27511', 'USA'),
    ('Donald', 'Trump', '659 South Country Club St.', 'Stone Mountain', 'GA', '30083', 'USA');



