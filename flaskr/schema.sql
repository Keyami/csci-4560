DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS checked;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS user;

create table member
(
	fName varchar(15) not null,
        lName varchar(15) not null,
        dob varchar(15) not null,
        phone char(10) not null,
        fees decimal(10,2),
        accountType varchar(15) not null,	/*user, staff, admin*/
        primary key(phone)
);

create table checked
(
	title_of varchar(15) not null,
        dateCheck varchar(6) not null,
        dateDue varchar(6) not null,
        isbn_of char(13) not null,
        copy int not null,
        primary key(isbn_of, copy),
        foreign key(isbn_of) references items(isbn)
);

create table items
(
	title varchar(15) not null,
        author varchar(20) not null,
        publication varchar(20) not null,
        genre varchar(15),
        copies int,		/*number of total copies*/
        availability int,	/*number currently available*/
        isbn char(13) not null,
        image VARCHAR(512)
);
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
