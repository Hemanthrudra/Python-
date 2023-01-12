
Create database Union_DB;

use Union_DB;

Create table Table1 (Name Varchar (100), Age Int)
drop table Table1
insert into Table1(Name,Age)
values ('Hemanth',27);
insert into Table1(Name,Age)
values ('Rajanessh',27),('Sagar',27),('Prem',27),('Uday',27);

Create table Table2 (Name Varchar (100), Age Int)

insert into Table2(Name,Age)
values ('Neeraj',27),('Rahul',27),('Mohan',27),('Naveen',27),('Yogesh',26);

--Union Function

select*from Table1 union select*from Table2;

select * into Table_backup from Table2;
select*from Table_backup;
