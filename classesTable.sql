/*conatins all classes, unsure if i need to make id for example: INT(10) UNSIGNED or if int is fine*/ 

/*DROP TABLE IF EXISTS request, classes;*/

CREATE TABLE request(
	id int NOT NULL AUTO_INCREMENT,
	email varchar(50),
	crn int,
	primary key (id)
);

/*for alert requests, has emails, id, CRN.*/
CREATE TABLE classes(
	id int NOT NULL AUTO_INCREMENT,
	crn int,
	term varchar(50),
	name varchar(75),
	dept varchar(75),
	status varchar(50),
	day varchar(50),
	time varchar(50),
	weblink varchar(75),
	primary key (id),
	foreign key (id) references request(id)
);
