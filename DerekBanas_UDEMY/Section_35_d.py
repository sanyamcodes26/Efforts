'''
sqlite> select test.date as Date,
   ...> min(test_score.score) as Worst,
   ...> max(test_score.score) as Best
   ...> from test_score, test
   ...> where test_score.test_id = test.id
   ...> group by test.date;
Date        Worst       Best
----------  ----------  ----------
2018-10-4   5           23
2018-3-28   2           20
2018-3-4    1           22
2018-8-8    3           23

sqlite> select test.date as Date,
   ...> avg(test_score.score) as Avg_Score
   ...> from test_score, test
   ...> where test_score.test_id = test.id
   ...> group by test.date;
Date        Avg_Score
----------  ----------
2018-10-4   13.6
2018-3-28   8.6
2018-3-4    11.7
2018-8-8    12.0

sqlite> select f_name || ' ' || l_name as Name,
   ...> test_score.score as Score
   ...> from test_score, student
   ...> where test_score.score > 20
   ...> and test_score.student_id = student.id
   ...> group by Name;
Name             Score
---------------  ----------
Amanda Williams  22
Ashley Williams  22
Matthew Martin   21
Samantha Robins  23

sqlite> create view ScoreOver20 as
   ...> select f_name || ' ' || l_name as Name,
   ...> test_score.score
   ...> from test_score, student
   ...> where test_score.score > 20
   ...> and test_score.student_id = student.id
   ...> group by Name;
sqlite> .table
ScoreOver20  sex          test         test_type
absence      student      test_score
sqlite> select * from ScoreOver20;
Name             score
---------------  ----------
Amanda Williams  22
Ashley Williams  22
Matthew Martin   21
Samantha Robins  23

sqlite> drop view ScoreOver20;
sqlite> .table
absence     sex         student     test        test_score  test_type

sqlite> create table log(
   ...> id int primary key,
   ...> test_id int not null,
   ...> date date not null,
   ...> student_id int not null,
   ...> foreign key(test_id) references test_score(test_id),
   ...> foreign key(student_id) references test_score(student_id));
sqlite> .table
absence     sex         test        test_type
log         student     test_score

sqlite> create trigger test_score_update
   ...> after update of score on test_score
   ...> begin
   ...> insert into log(test_id, date, student_id)
   ...> values(new.test_id, date('now'), new.student_id);
   ...> end;

sqlite> update test_score
   ...> set score = 20
   ...> where test_id = 1 and student_id = 2;
sqlite> select * from log;
id          test_id     date        student_id
----------  ----------  ----------  ----------
            1           2020-01-14  2

sqlite> select l_name, f_name
   ...> from student
   ...> where l_name like 'J%';
l_name      f_name
----------  ----------
Jackson     Daniel
sqlite> select l_name, f_name
   ...> from student
   ...> where l_name like '_____';
l_name      f_name
----------  ----------
Brown       Ashley
Smith       Lauren
sqlite> select l_name, f_name
   ...> from student
   ...> where f_name like 'A%'
   ...> order by l_name asc, f_name limit 5 offset 2;
l_name      f_name
----------  ----------
Williams    Ashley
sqlite> select random();
random()
-------------------
-881169683497305328
sqlite> select abs(random() % 100);
abs(random() % 100)
-------------------
6
sqlite> select lower(f_name),
   ...> upper(l_name)
   ...> from student;
lower(f_name)  upper(l_name)
-------------  -------------
ashley         WILLIAMS
matthew        MARTIN
daniel         JACKSON
matthew        MARTIN
matthew        GARCIA
ashley         BROWN
jennifer       THOMAS
samantha       ROBINSON
lauren         SMITH
amanda         WILLIAMS
sqlite> select length('iron man');
length('iron man')
------------------
8
sqlite> select count(*) from student;
count(*)
----------
10
sqlite> select date();
date()
----------
2020-01-14
sqlite> select time();
time()
----------
10:20:17

sqlite> select datetime();
datetime()
-------------------
2020-01-14 10:21:23
sqlite> select date('now', '-30 days');
date('now', '-30 days')
-----------------------
2019-12-15
sqlite> select date('now', 'weekday 0');
date('now', 'weekday 0')
------------------------
2020-01-19
sqlite> select strftime("%m-%d-%Y");
strftime("%m-%d-%Y")
--------------------
01-14-2020
sqlite> select date('now', 'start of year',
   ...> '10 months', '21 days', 'weekday 4');
date('now', 'start of year',
'10 months', '21 days', 'weekday 4')
-----------------------------------------------------------------
2020-11-26

'''