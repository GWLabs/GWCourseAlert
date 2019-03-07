DROP TABLE IF EXISTS requests;

CREATE TABLE requests (
	id INT PRIMARY KEY,
	email varchar(50),
	crn int	
);

DROP TABLE IF EXISTS classes;

CREATE TABLE classes(
	id SERIAL NOT NULL,
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
