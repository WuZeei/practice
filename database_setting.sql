CREATE TABLE login (
	id int NOT NULL AUTO_INCREMENT,
    account varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    primary key (`id`)
    );
CREATE TABLE tasks (
    id int NOT NULL AUTO_INCREMENT,
    task varchar(255) NOT NULL,
    status char(30),
    PRIMARY KEY (`id`)
);
INSERT INTO tasks (task, status) VALUES ("task no.1" , "Todo");
INSERT INTO tasks (task, status) VALUES ("task no.2" , "Todo");
