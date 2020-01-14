'''
C:\Users\Akash_PC\Documents\sqlite3>sqlite3 Student.db
SQLite version 3.30.1 2019-10-10 20:19:45
sqlite> create table sex( id text primary key not null, sex_type integer not null);
sqlite> insert into sex(id, sex_type) values ('M', 1);
sqlite> insert into sex(id, sex_type) values ('F', 2);

sqlite> .mode column
sqlite> .header on

sqlite> select * from sex;
id          sex_type
----------  ----------
M           1
F           2

sqlite> .schema sex
CREATE TABLE sex(
id text primary key not null,
sex_type integer);

sqlite> create table student( f_name varchar(29) not null, l_name varchar(29) not null, sex character(1) not null, id integer primary key autoincrement, foreign key(sex) references sex(id));
sqlite> create table test_type( id integer primary key not null, type text not null);
sqlite> create table test( date date not null, test_type int not null, id integer primary key autoincrement, foreign key (test_type) references test_type(id));
sqlite> create table test_score( student_id integer not null, test_id integer not null, score integer not null, foreign key (test_id) references test(id), foreign key (student_id) references student(id), primary key (test_id, student_id));
sqlite> create table absence( student_id integer not null, date date not null, primary key (student_id, date), foreign key (student_id) references student(id));

sqlite> .tables
absence     sex         student     test        test_score  test_type

'''