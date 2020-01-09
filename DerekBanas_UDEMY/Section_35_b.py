import random

f_names = ["Michael", "Christopher", "Joshua", "Matthew", "David", "Daniel", "Andrew", "Joseph", "Justin", "James",
           "Jessica", "Ashley", "Brittany", "Amanda", "Melissa", "Stephanie", "Jennifer", "Samantha", "Sarah", "Megan",
           "Lauren"]

l_names = ["Smith", "Johnson", "Williams", "Jones", "Brown","Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
           "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]


def create_students(how_many):
    for i in range(how_many):
        f_name = f_names[random.randint(0, len(f_names) - 1)]
        l_name = l_names[random.randint(0, len(l_names) - 1)]

        sex = random.choice(['M', 'F'])
        print("INSERT INTO student( f_name, l_name, sex) VALUES ('{}', '{}', '{}');".format(f_name, l_name, sex))
        '''
        sqlite> .mode column
        sqlite> .header on
        sqlite> select * from student;
        f_name      l_name      sex         id
        ----------  ----------  ----------  ----------
        Ashley      Williams    M           1
        Matthew     Martin      F           2
        Daniel      Jackson     M           3
        Matthew     Martin      M           4
        Matthew     Garcia      F           5
        Ashley      Brown       F           6
        Jennifer    Thomas      M           7
        Samantha    Robinson    F           8
        Lauren      Smith       F           9
        Amanda      Williams    M           10
        '''
        return


def create_tests(how_many):
    for i in range(how_many):
        month = random.randrange(1, 13)
        day = random.randrange(1, 31)
        test_type = random.randrange(1, 3)
        if month == 2 and day > 28:
            day = 28
        print("INSERT INTO test VALUES ('2018-{}-{}', {}, NULL);".format(month, day, test_type))
    '''
    sqlite> select * from test;
    date        test_type   id
    ----------  ----------  ----------
    2018-10-4   1           1
    2018-3-28   2           2
    2018-3-4    2           3
    2018-8-8    2           4
    '''
    return


def create_test_scores(n_tests, n_students):
    for i in range(1, n_tests + 1):
        for j in range(1, n_students + 1):
            score = random.randrange(1, 26)
            print("INSERT INTO test_score VALUES( {}, {}, {});".format(j, i, score))
    '''
    sqlite> select * from test_score;
    student_id  test_id     score
    ----------  ----------  ----------
    1           1           15
    2           1           9
    3           1           12
    4           1           21
    5           1           6
    6           1           18
    7           1           5
    8           1           23
    9           1           5
    10          1           22
    1           2           2
    2           2           3
    3           2           4
    4           2           10
    5           2           20
    6           2           8
    7           2           6
    8           2           2
    9           2           18
    10          2           13
    1           3           22
    2           3           10
    3           3           7
    4           3           6
    5           3           1
    6           3           14
    7           3           19
    8           3           15
    9           3           9
    10          3           14
    1           4           17
    2           4           10
    3           4           11
    4           4           13
    5           4           17
    6           4           3
    7           4           3
    8           4           23
    9           4           17
    10          4           6
    '''
    return


def create_absences(how_many):
    for i in range(how_many):
        student_id = random.randrange(1, 11)
        month = random.randrange(1, 13)
        day = random.randrange(1, 31)
        if month == 2 and day > 28:
            day = 28
        print("INSERT INTO absence VALUES({}, '2018-{}-{}');".format(student_id, month, day))
    '''
sqlite> select * from absence;
student_id  date
----------  ----------
4           2018-6-17
2           2018-4-16
4           2018-8-23
6           2018-2-7
8           2018-3-9
2           2018-5-27
9           2018-11-29
4           2018-1-21
2           2018-7-19
2           2018-12-22
5           2018-7-27
1           2018-12-21
1           2018-12-26
2           2018-7-27
8           2018-2-3
6           2018-5-8
6           2018-1-18
6           2018-2-6
4           2018-2-8
10          2018-6-20
5           2018-4-6
1           2018-2-16
4           2018-10-13
5           2018-9-23
8           2018-9-1
9           2018-5-20
6           2018-9-17
9           2018-1-28
3           2018-4-27
3           2018-2-19
8           2018-1-30
5           2018-4-22
9           2018-1-16
10          2018-9-6
5           2018-6-22
10          2018-8-5
2           2018-9-18
7           2018-12-4
2           2018-11-22
4           2018-9-17
8           2018-6-5
9           2018-7-5
7           2018-9-2
4           2018-12-26
8           2018-4-22
2           2018-8-1
4           2018-1-19
9           2018-11-14
8           2018-8-12
4           2018-8-20
1           2018-10-30
1           2018-7-3
5           2018-3-10
9           2018-2-28
7           2018-6-1
5           2018-10-13
9           2018-12-22
1           2018-7-30
4           2018-8-1
9           2018-8-9
5           2018-1-4
6           2018-7-24
3           2018-8-13
3           2018-7-8
4           2018-10-6
8           2018-12-18
6           2018-9-4
8           2018-7-2
9           2018-9-10
8           2018-8-17
4           2018-8-26
7           2018-8-18
7           2018-5-24
8           2018-5-14
9           2018-10-4
7           2018-3-17
4           2018-1-28
7           2018-12-20
1           2018-2-12
5           2018-7-6
6           2018-2-13
1           2018-6-16
4           2018-6-8
2           2018-3-16
5           2018-1-29
7           2018-10-30
8           2018-11-23
5           2018-1-19
1           2018-7-28
10          2018-1-8
8           2018-12-13
4           2018-2-4
10          2018-9-23
6           2018-2-21
8           2018-2-15
3           2018-1-7
2           2018-3-2
9           2018-2-4
9           2018-9-4
8           2018-12-15
1           2018-5-21
1           2018-2-17
3           2018-2-22
5           2018-11-17
8           2018-11-3
1           2018-3-16
8           2018-11-27
8           2018-3-27
2           2018-11-25
9           2018-4-5
10          2018-8-24
7           2018-4-2
6           2018-12-14
2           2018-10-8
8           2018-7-6
3           2018-3-25
1           2018-9-2
7           2018-10-20
7           2018-7-3
5           2018-10-16
2           2018-3-10
9           2018-9-7
6           2018-4-1
9           2018-10-26
7           2018-12-7
1           2018-10-21
7           2018-4-30
3           2018-10-27
2           2018-3-21
5           2018-2-17
9           2018-9-5
5           2018-6-8
5           2018-4-13
6           2018-6-1
1           2018-1-11
2           2018-3-28
8           2018-9-8
1           2018-5-14
10          2018-1-6
1           2018-4-8
1           2018-12-11
4           2018-6-12
4           2018-2-12
4           2018-5-24
10          2018-3-4
1           2018-12-5
3           2018-8-23
7           2018-8-3
10          2018-3-6
9           2018-9-26
4           2018-1-24
8           2018-8-10
6           2018-5-19
2           2018-2-26
3           2018-6-20
10          2018-11-5
1           2018-2-8
3           2018-11-7
5           2018-11-6
8           2018-1-3
4           2018-4-10
5           2018-6-25
9           2018-12-6
3           2018-7-6
3           2018-3-7
5           2018-7-29
5           2018-3-23
6           2018-5-27
7           2018-8-7
9           2018-8-10
9           2018-4-28
9           2018-12-16
3           2018-10-7
1           2018-4-13
10          2018-8-26
6           2018-11-28
9           2018-7-3
10          2018-5-2
8           2018-7-4
10          2018-9-16
    '''
    return


if __name__ == "__main__":
    '''
    create table student( f_name varchar(29) not null, l_name varchar(29) not null, sex character(1) not null, id integer primary key autoincrement, foreign key(sex) references sex(id));
    create table test_type( id integer primary key not null, type text not null);
    create table test( date date not null, test_type int not null, id integer primary key autoincrement, foreign key (test_type) references test_type(id));
    create table test_score( student_id integer not null, test_id integer not null, score integer not null, foreign key (test_id) references test(id), foreign key (student_id) references student(id), primary key (test_id, student_id));
    create table absence( student_id integer not null, date date not null, primary key (student_id, date), foreign key (student_id) references student(id));
    '''
    # create_students(10)
    # create_tests(4)
    # create_test_scores(4, 10)
    # create_absences(365//2)
