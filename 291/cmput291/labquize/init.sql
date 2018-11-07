drop table if exists courses;
drop table if exists students;
drop table if exists professors;
drop table if exists enroll;

create table courses (
  courseID			int,
  courseName		text,
  professorID		text,
  seatsAvailable	int,
  credits			int,
  primary key (courseID),
  foreign key (professorID) references professors (professorID));

create table professors (
	professorID		text, 
	professorName	text,
	department		text,
	primary key (professorID));

create table students(
	studentID		int, 
	studentName		text, 
	program			text, 
	primary key (studentID));

create table enroll(
	studentID		int,
	courseID		int,
	grade			int,
	term			text,
	foreign key (studentID) references students (studentID),
	foreign key (courseID) references courses (courseID));

INSERT INTO professors VALUES('1293730194', 'Charles Smith', 'Computing Science');
INSERT INTO professors VALUES('9184951751', 'George Jones', 'Computing Science');
INSERT INTO professors VALUES('8194174951', 'Sandra Williams', 'Computing Science');
INSERT INTO professors VALUES('7193710486', 'Michael Taylor', 'Computing Science');
INSERT INTO professors VALUES('8710391845', 'Steven Brown', 'Computing Science');
INSERT INTO professors VALUES('6194015391', 'Michelle Davies', 'Computing Science');
INSERT INTO professors VALUES('8704187390', 'Laura Evans', 'Computing Science');
INSERT INTO professors VALUES('1720391858', 'Kevin Wilson', 'Biological Sciences');
INSERT INTO professors VALUES('6182910491', 'Sarah Thomas', 'Biological Sciences');
INSERT INTO professors VALUES('7192048193', 'Deborah Johnson', 'Earth and Atmospheric Sciences');
INSERT INTO professors VALUES('8102913918', 'Jeff Wright', 'Earth and Atmospheric Sciences');

INSERT INTO courses VALUES(1, 'Database Systems', '1293730194', 200, 3);
INSERT INTO courses VALUES(2, 'Ethics in Computer Science', '9184951751', 50, 3);
INSERT INTO courses VALUES(3, 'Operating Systems', '8194174951', 100, 3);
INSERT INTO courses VALUES(4, 'Software Engineering', '7193710486', 250, 3);
INSERT INTO courses VALUES(5, 'Advanced Topics in Machine Learning', '8710391845', 50, 6);
INSERT INTO courses VALUES(6, 'Introduction to Computing', '9184951751', 50, 1);
INSERT INTO courses VALUES(7, 'Introduction to Computer Graphics', '6194015391', 50, 3);
INSERT INTO courses VALUES(8, 'Computer Networks', '8704187390', 200, 3);
INSERT INTO courses VALUES(9, 'Introduction to Molecular Genetics Techniques', '1720391858', 200, 3);
INSERT INTO courses VALUES(10, 'Bioinformatics I', '6182910491', 200, 3);
INSERT INTO courses VALUES(11, 'Earth Surface Processes and Landforms', '7192048193', 100, 3);
INSERT INTO courses VALUES(12, 'Introduction to Global Change', '8102913918', 40, 3);


INSERT INTO students VALUES(1, 'Patricia Smith', 'Computing Science');
INSERT INTO students VALUES(2, 'Mary Jones', 'Computing Engineering');
INSERT INTO students VALUES(3, 'Robert Talylor', 'Electrical Engineering');
INSERT INTO students VALUES(4, 'David Willians', 'Computing Science');
INSERT INTO students VALUES(5, 'Richard Brown', 'Earth Science');
INSERT INTO students VALUES(6, 'Linda Davies', 'Computing Science');
INSERT INTO students VALUES(7, 'Paul Evans', 'Computing Science');
INSERT INTO students VALUES(8, 'Karen Wilson', 'Computing Science');
INSERT INTO students VALUES(9, 'Daniel Thompson', 'Systems Engineering');
INSERT INTO students VALUES(10, 'Donald White', 'Computing Science');
INSERT INTO students VALUES(11, 'Ronald Cooper', 'Chemical Engineering');
INSERT INTO students VALUES(12, 'Jennifer Martin', 'Computing Science');
INSERT INTO students VALUES(13, 'Jason Moore', 'Computing Science');




INSERT INTO enroll VALUES(1, 1, 4, 'Fall 2016');
INSERT INTO enroll VALUES(3, 1, 1, 'Winter 2015');
INSERT INTO enroll VALUES(8, 1, 2, 'Summer 2016');
INSERT INTO enroll VALUES(8, 1, 3, 'Winter 2017');
INSERT INTO enroll VALUES(9, 1, 2, 'Summer 2016');
INSERT INTO enroll VALUES(10, 1, 4, 'Fall 2016');
INSERT INTO enroll VALUES(7, 1, 4, 'Fall 2016');
INSERT INTO enroll VALUES(10, 6, 4, 'Summer 2016');
INSERT INTO enroll VALUES(11, 4, 4, 'Winter 2015');
INSERT INTO enroll VALUES(2, 1, 0, 'Winter 2015');
INSERT INTO enroll VALUES(3, 1, 1, 'Fall 2016');
INSERT INTO enroll VALUES(11, 1, 3, 'Summer 2016');
INSERT INTO enroll VALUES(12, 1, 4, 'Fall 2016');
INSERT INTO enroll VALUES(13, 1, 0, 'Fall 2016');
INSERT INTO enroll VALUES(11, 4, 4, 'Summer 2016');
INSERT INTO enroll VALUES(12, 3, 3, 'Fall 2016');
INSERT INTO enroll VALUES(1, 5, 4, 'Summer 2016');
INSERT INTO enroll VALUES(2, 4, 4, 'Fall 2016');
INSERT INTO enroll VALUES(7, 8, 4, 'Winter 2017');
INSERT INTO enroll VALUES(8, 7, 4, 'Fall 2016');
INSERT INTO enroll VALUES(9, 6, 3, 'Fall 2016');
INSERT INTO enroll VALUES(12, 3, 4, 'Summer 2016');
INSERT INTO enroll VALUES(13, 2, 1, 'Fall 2016');
INSERT INTO enroll VALUES(2, 1, 3, 'Winter 2017');
INSERT INTO enroll VALUES(1, 12, 3, 'Fall 2016');
INSERT INTO enroll VALUES(4, 1, 2, 'Winter 2017');
INSERT INTO enroll VALUES(5, 1, 3, 'Fall 2016');
INSERT INTO enroll VALUES(6, 1, 4, 'Fall 2016');
INSERT INTO enroll VALUES(10, 10, 1, 'Summer 2016');
INSERT INTO enroll VALUES(7, 5, 0, 'Fall 2016');
INSERT INTO enroll VALUES(9, 7, 0, 'Fall 2016');
INSERT INTO enroll VALUES(4, 1, 4, 'Winter 2015');
INSERT INTO enroll VALUES(5, 5, 1, 'Fall 2016');
INSERT INTO enroll VALUES(6, 1, 2, 'Fall 2016');
INSERT INTO enroll VALUES(3, 12, 1, 'Summer 2016');
INSERT INTO enroll VALUES(4, 11, 1, 'Fall 2016');
INSERT INTO enroll VALUES(5, 10, 4, 'Fall 2016');
INSERT INTO enroll VALUES(6, 9, 1, 'Winter 2017');
INSERT INTO enroll VALUES(13, 2, 1, 'Fall 2016');







