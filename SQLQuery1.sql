/*Database creation*/
create database Database1
--Drop database
drop database Database1
--Using the created table as master file instead of system directory
use Database1
/*Creating a table*/
create table Employee_data (Name varchar(100), Age int, Addres varchar(200), Salary float);
/*Selecting table*/
select*from Employee_data
--Drop or deleting the table
drop table Employee_data;
/*Inserting data into table*/
INSERT into Employee_data(Name, Age, Addres, Salary)
Values('Hemanth',27,'Bangalore',350000.15);
--Day 4 Monday 19/9
use Database1;
--Alter Command
/* Alter table table_name
Add Col_Name data*/
Alter table Employee_data
Add Email_id varchar(50);
Select*from Employee_data;
--Email id Col says Null bcz we need to use where command while adding email id to particular row
-- Command to drop a column
Alter table Employee_data drop column Email_id;
--CReate new database Naming Rules
create Database Rules;
--Use the database Rules
Use Rules;
--Using Constraint commands & Rules - By creating 5 different tables
-
-- NOT NULL Constraint
create table Employee_data1 (Name varchar(100) NOT NULL, Age int, Addres varchar(200), Salary float);

--Inserting constraints into created tables
INSERT into Employee_data1(Name, Age, Addres, Salary)
Values('NULL',27,'Bangalore',350000.15);

--UNIQUE Constraint
create table Employee_data2 (Name varchar(100), Age int, Addres varchar(200), Salary float,ID int UNIQUE);

--Inserting constraints into created tables
INSERT into Employee_data2(Name, Age, Addres, Salary,ID)
Values('Hemanth',27,'Bangalore',350000.15,1);



--Primary Key Constraint
create table Employee_data3 (Name varchar(100), Age int, Addres varchar(200), Salary float,ID int Primary Key);

--Inserting constraints into created tables

INSERT into Employee_data3(Name, Age, Addres, Salary,ID)
Values('Hemanth',27,'Bangalore',350000.15,1);

--Check Constraint

create table Employee_data4 (Name varchar(100), Age int CHECK(Age>=18), Addres varchar(200), Salary float);

--Inserting constraints into created tables
INSERT into Employee_data4(Name, Age, Addres, Salary)
Values('Hemanth',17,'Bangalore',350000.15);

--Day 5 -20-09-2022

-- dbo fullform - Database owner

use Rules;
-- Default Constraint

create table Employee_data5 (Name varchar(100), Age int CHECK(Age>=18), Addres varchar(200), Salary float,[Joining date] date default getdate());

INSERT into Employee_data5(Name, Age, Addres, Salary)
Values('Rajaneesh',25,'Bangalore',370000.15);

select*from Employee_data5;

--Create new database for analysis

Create database Data_Analysis;
Use Data_Analysis;	

/*Import data from SQL Import export 2019 -there choose microsoft excel -select import type
-select destination-select database-select the table which you want- then next and open*/

/* Another way of data import - in MS SQL right click on the database in which you want to import-click on tasks-click on import-then select the source as microsoft excel
-then browse the file where it is saved-next check your database file should be in downside 
- then select the destination as ms sql 11.0 server - then check and select the table you want to use without filter data-next-finish*/

select * from Orders;
--Day 6
--Selecting particular columns

select [order Id],[order date],[ship date]
from orders;

Select region
from orders;
--Selecting only distinct values

select distinct region
from orders;

/* Selecting particular city*/
/* select *from table_name
where city_name='Condition' */


select* from orders
where region='Central US';

--Logic Gates
--And logic
select*from orders
where region='Central US' and city='Seattle';

--Or logic
select*from orders
where region='Central US' or city='Seattle';

--Not logic
select * from orders
where not region='Central Us';

select * from orders
where region in ('Cetral Us','Western africa');

select * from orders
where region in ('Cetral Us','Western africa') and [order priority]='high';

--Like command
/* select* from table name
where region like'A%S' */

select *from orders
where region like 'A%S';

select *from orders
where region like 'w%e';

select *from orders
where region like 'w%';

select *from orders
where region like '%A';

select *from orders
where region like '_A%';

select *from orders
where region like '%A_';

select *from orders
where region like '%As%';

--End of Day6 

--Day 7 - Thursday -22-9-22

--Between clause
use Data_Analysis;
select*from Orders
where sales between 500 and 1000;

--Comparison Operators <,>,>=,<=,!=,<>

select*from orders
where sales >12000;

select * from orders
where sales >=12000;

select * from orders
where sales <=12000;

--Order by Command - It does the Ascending and descending order values

--Ascending order ---even if we don't mention ascending the order will be from ascending to descending
select * from orders
order by [Customer Name];

--Descending order
select * from orders
order by [Customer Name] desc;

--NULL Function

select * from orders
where [Postal Code] is NULL;


select * from orders
where [Postal Code] is NOT NULL;

--Update values in Null cells

update Orders set [Postal Code]=560077
where [Postal Code] is NULL;

select* from orders 
where [Postal Code]=560077;

---delete function Justin Ritter

delete from Orders
where [customer name] = 'Justin Ritter';

--Top 10 functions

select top 10 *from orders

--Backup function

select * into Orders_Backup from orders;
select * from Orders_Backup;

--End of day 7

--Day 8
use Data_Analysis
select* from orders

--Group by

select country,sum (sales) from orders
group by country;

-- As or Alias function

select country,sum (sales) as Total_sales
from orders
group by country;

--As with where statement
select country,sum (sales) as Total_sales
from orders
where [Ship Mode]='First Class'
group by country;

-- as with order clause

select country,sum (sales) as Total_sales
from orders
group by country
order by Country;

--As,sum,count,group,order by clause

select country,sum (sales) as Total_sales,
count (quantity) as Total_count
from orders
group by country
order by Country;

--As,sum,count,group,order by clause,with distict values

select country,sum (sales) as Total_sales,
count (distinct quantity) as Total_count
from orders
group by country
order by Country;

--Min,MAx,avg,count,sum,order by,group by commands

select country,sum (sales) as Total_sales,
count (distinct quantity) as Total_count,
min(sales) as Min_sales,
max(sales) as Max_sales,
avg(sales) as Average_sale
from orders
group by country
order by Country;

--Arithmetic operators (+,-,*,/,% )

Select country, Sales-profit as Total_cost
from orders;

Select country, Sales-profit as Total_cost,
(Sales*0.10) as Sales_Commision
from orders;

select top 10 country, Sales % Profit as Total_cost
from orders;

/* End od day 8*/

/*Day 9 - 26 sep 22*/

--Joins Concept
--Creating new database joins

create database Joins;

--Use databse joins

use Joins;

-- creating new tables for joins operator & inserting data into it
---Tbale 1
create table order_data (name varchar (20),Qty Int,unit_price float,Ord_id int);

Insert into order_data (name,Qty,unit_price,Ord_id)
Values ('A',12,25.7,101),('B',18,108.13,120),('C',20,252.18,118),('D',14,170.17,142),('E',17,182.98,198);
---Table 2

create table product_ifo (order_id int,product_name varchar (20),place_of_booking varchar (20));

Insert into product_ifo (order_id,product_name,place_of_booking)
Values (101,'mobile','Bangalore'),(120,'Consumer','Chennai'),(118,'TV','Delhi'),(142,'mobile','Mysore'),(119,'Laptop','Pune');

--table 3

create table Lay_over(Name varchar (20),order_id int,lay_over varchar (20));

insert into Lay_over(Name,order_id,lay_over)
Values ('A',101,'H.K'),('B',120,'Peru'),('C',118,'Mexico'),('F',197,'U.S'),('G',241,'London');

--Table 4
create table [Taxes and charges](Name varchar (20),order_id int,Taxes int,Shipping_cost float,handy int);

insert into [Taxes and charges](Name,order_id,Taxes,Shipping_cost,handy)
 Values('A',101,10,750.00,4),('B',120,20,1000.00,7),('C',138,14,280.00,12),('F',170,17,170.18,10),('G',199,18,170.00,8);

 select *from order_data;
 --updating values in one row bcz i had entered 25.7 instead of 25.17 in row 1
 Update order_data set unit_price=25.17 where unit_price=25.7;

 select*from Lay_over;

 select*from product_ifo
 select*from [Taxes and charges]

 --End of day 9

 -- Day 10

 use Joins;

 select * from order_data

 select * from product_ifo

 --Inner join

 select od.name,
	 od.Qty,
	 od.unit_price,
	 od.ord_id,
	 pi.product_name,
	 pi.place_of_booking
from order_data as od                          ---this is base data table
inner join product_ifo as pi
on od.ord_id=pi.order_id;

--Left join

 select od.name,
	 od.Qty,
	 od.unit_price,
	 od.ord_id,
	 pi.product_name,
	 pi.place_of_booking
from order_data as od                          ---this is base data table
left join product_ifo as pi
on od.ord_id=pi.order_id;

---Right join

 select od.name,
	 od.Qty,
	 od.unit_price,
	 od.ord_id,
	 pi.product_name,
	 pi.place_of_booking
from order_data as od                          ---this is base data table
right join product_ifo as pi
on od.ord_id=pi.order_id;

select * from Lay_over
select * from [Taxes and charges]

---inner join by 3 tables ord table, product ifo & layover

 select od.name,
	 od.Qty,
	 od.unit_price,
	 od.ord_id,
	 pi.product_name,
	 pi.place_of_booking,
	 li.lay_over
from order_data as od                          ---this is base data table
inner join product_ifo as pi
on od.ord_id=pi.order_id
inner join lay_over as li on li.order_id=od.ord_id;

---- inner join for all 4 tables
 select od.name,
	 od.Qty,
	 od.unit_price,
	 od.ord_id,
	 pi.product_name,
	 pi.place_of_booking,
	 li.lay_over
from order_data as od                          ---this is base data table
inner join product_ifo as pi
on od.ord_id=pi.order_id
inner join lay_over as li 
on li.order_id=od.ord_id
inner join [Taxes and charges] as tx
on tx.order_id=od.ord_id;

 select * from order_data

 select * from product_ifo
 select * from Lay_over
select * from [Taxes and charges]

---Find total taxes for orders

use joins;
 select od.qty*od.unit_price*tx.Taxes/100 as total_tax,
 (od.qty*od.unit_price+tx.Shipping_cost)*tx.handy/100 as handling_charges,
     od.name,
	 od.Qty,
	 od.unit_price,
	 od.ord_id,
	 pi.product_name,
	 pi.place_of_booking,
	 li.lay_over
from order_data as od                          ---this is base data table
inner join product_ifo as pi
on od.ord_id=pi.order_id
inner join lay_over as li 
on li.order_id=od.ord_id
inner join [Taxes and charges] as tx
on tx.order_id=od.ord_id;

---end of day 10

---Day 11  -28-09-2022

use Joins

--Finding min & max sales

use Data_Analysis


select min(sales) as Min_sales
from Orders;     ---- min value is 0.444

select max(sales) as Min_sales
from Orders;                      ---Min value is 22638.48

----Case functions/clause
--Query to find & name avg profit as less,poor,good,super

select region,sales,  case
   when sales<5000 then 'Avg profit is less'
   when sales <10000 then 'Avg_profit_is_moderate'
   when sales <15000 then 'Avg_profit_is_good'
   when sales>15000 then 'Avg_profit_is_super'
   end as 'Profit_status'
   from Orders;

   use Data_Analysis

select min("Order Date") as Min_date from Orders;
order by [Order Date] desc;

--Case statement for years in orderdate 

select region,sales,[order date], case
   when [Order Date] like '%2012%' then '2012'
   when [Order Date] like  '%2013%' then '2013'
   when [Order Date] like '%2014%' then '2014'
   when [Order Date] like '%2015%' then '2015'
   end as 'Year'
   from Orders;

   --End of day 11

   --Day 12 --29-09-2022
  /*  CAST  - it Converts the data type   - cast changes the functionality  */
   
  select CAST(1 As float);

   select CAST(1 as varchar);
   
   select CAST(1 as date);

   select cast (1 as decimal);
   
   select cast (1 as decimal(18,4));  --here 18 is the default value in SQL. 0.4 is the decimals we required.

   -- we can give 18.17 but not 18.18 because it again takes default value not decimal
    select cast (1 as decimal(18,18));


	--casting the strings

	select CAST('ABCD' as float);
	
	select CAST('ABCD' as varchar);

	select CAST('ABCD' as date);

	select CAST('ABCD' as decimal);
	select CAST('ABCD' as decimal (18,4));
	----- NUmerical cast
	select CAST('123' as float);
	
	select CAST('123' as varchar);

	select CAST('123' as date);

	select CAST('123' as decimal);
	select CAST('123' as decimal (18,4));

	--Special character
	select CAST('@$' as float);
	
	select CAST('@%' as varchar);

	select CAST('@%' as date);

	select CAST('@%' as decimal);
	select CAST('$@' as decimal (18,4));


	--Get today's date
	select GETDATE()

	select cast (GETDATE() as float);
	
	select cast (GETDATE() as varchar);
	
	select cast (GETDATE() as decimal);
	
	select cast (GETDATE() as decimal(18,4));

	---USing cast in Global value (that is Nvarchar)

	select cast (GETDATE() as nvarchar);

	select CAST('@%' as nvarchar);
	
	select CAST('1234' as nvarchar);
	
	select CAST('ABCD' as nvarchar);

	--Creating sample table for excercise

	create table Sample_table(Name varchar (20),country varchar (20),state varchar (20), city varchar (20),pincode int);

	insert into Sample_table(Name,country,state,city,pincode)
	Values ('HR','India','Kar','BGL',562149),('SS','India','Kar','BGL1',560077),('RR','India','Kar','BGL3',562122);

	select * from Sample_table


	----TRUNCATE  - This function deletes values from table but not deletes the table

	Truncate table sample_table;

	Select*from Sample_table;


	---Creating new table for SUBQUERY FUNCTION PRACTICE

	create table Sample_table1(Name varchar (20),country varchar (20),state varchar (20), city varchar (20),pincode int);

	insert into Sample_table1(Name,country,state,city,pincode)
	Values ('HR','India','Kar','BGL',562149),('SS','India','Kar','BGL1',560077),('RR','India','Kar','BGL3',562122),
	       ('KK','India','Kar','BGL4',562132),('MSD','India','Ranchi','JSr',562222);

	--insert the same values as above into table to create duplicate value

	select* from Sample_table1;
	--Assignment 
	/*Create 4 table having relationship with each other with 5 rows, 
	build right join to these created 4 tables as previously done in inner join concept*/
	use Joins
	select * from lay_over;
	select *from order_data
	select * from product_ifo
	select* from [Taxes and charges]

 use Data_Analysis
 --table 1
 create table Subscription (Names varchar(20),users int,Lhours int,topic int,active_user int);

insert into Subscription values
 ('Coursera',32,196,20,6),('linkedln',295,586,928,2),('Oreily',746,996,260,12),('pluralsight',287,136,54,3),('udemy',141,185,28,4);

 --table 2
 create table Fyear (Names varchar(20),Participation int,Lhours int);

 insert into Fyear values
 ('Coursera',67,196),('linkedln',2031,586),('Oreily',553,916),('pluralsight',168,135),('udemy',829,1852);
 ---table 3
 create table Cdetaila (sales int,price int,Names varchar (20),duration int);

 insert into Cdetaila values
 (225,1544,'pluralsight',8),(342,6644,'Tech',5),(278,1764,'udemy',10),(775,8886,'linkedln',15),(987,6528,'nttf',40);
 --table 4
 create table profit (Names varchar(20),sales int,tax int,gains int);
 insert into profit values
 ('udemy',223,2,632),('pluralsigh',253,7,232),('nttf',322,3,622),('tech',231,8,626);
  use Data_Analysis
  select*from Subscription
  select*from Fyear
  select*from Cdetaila
  select*from profit

  ---Right join

   select a.names,
	 a.users,
	 a.topic,
	 b.participation,
	 b.Lhours
from Subscription as a                         ---this is base data table
right join Fyear as b
on a.Lhours=b.Lhours;

 select a.names,
	 a.participation,
	 a.Lhours,
	 b.sales,
	 b.price,
	 b.duration
from Fyear as a                         ---this is base data table
right join Cdetaila as b
on a.Names=b.Names;

 select a.names,
	 a.users,
	 a.topic,
	 b.participation,
	 b.Lhours,
	 c.price
from Subscription as a                         ---this is base data table
right join Fyear as b
on a.Lhours=b.Lhours
right join cdetaila as c
on b.names=c.names;

 select a.names,
	 a.users,
	 a.topic,
	 b.participation,
	 b.Lhours,
	 c.price,
	 d.tax
from Subscription as a                         ---this is base data table
right join Fyear as b
on a.Names=b.Names
right join cdetaila as c
on b.names=c.names
right join profit as d
on c.Names=d.Names;


update Cdetaila set Names='linkedln' where Names='Tech';
update profit set Names='linkedln' where Names='Tech';
update profit set Names='pluralsight' where Names='pluralsigh';

---Total course hours & t.tax of course

select a.Lhours*a.topic as total_hours,
        c.sales*c.price *d.tax/100 as Total_tax,
     a.names,
	 a.users,
	 a.topic,
	 b.participation,
	 b.Lhours,
	 c.price,
	 d.tax
from Subscription as a                         ---this is base data table
right join Fyear as b
on a.Names=b.Names
right join cdetaila as c
on b.names=c.names
right join profit as d
on c.Names=d.Names;

---day 12 end

--Day 13 -30-12-22

---Subquery statement
---CTE = common table expression

	select* from Sample_table1;

	delete cte
	from(
	select *,name1=ROW_NUMBER() over (
	partition by name
	order by (select name)
	) from sample_table1 
	) as cte
	where name1>1;

--End of Day 13

--Day 14 - 03-10-2022

--Store Procedure
--The stored procedure will caryout same procees all time when it is stored in 

/* Inserting data function  can be used in store procedure ---i.e when we have repititive task

it follows 3 steps  
1.create procedure procedure name As 
2.SQL statement 
3.End     */

use Data_Analysis
create procedure Test as   -- ----Giving name for procedure name                               
create table Bessant (Name varchar (20),Course varchar (20))   ----Creating table
insert into Bessant                                          ---Inserting into table
values ('A','sql'),('B','Python'),('C','Linux')
delete from  Bessant where Name='C'                          ---Deleting data of C
update Bessant                                              ----Updating data into B
Set Name='XYZ' where Name='B'
go

/* Executing the store procedure*/

exec Test

---Checking the table for values affected

select *from Bessant

/* How to know the already created store procedure ---(That is to know what is the procedure stored/written
in store procedure)
Syntax  :   sp_helptext store procedure name*/

sp_helptext Test

create procedure Test as                                  ----Giving name for procedure name  
create table Bessant (Name varchar (20),Course varchar (20))   ----Creating table  
insert into Bessant                                          ---Inserting into table  
values ('A','sql'),('B','Python'),('C','Linux')  
delete from  Bessant where Name='C'                          ---Deleting data of C  
update Bessant                                              ----Updating data into B  
Set Name='XYZ' where Name='B'  
go

/*As the table already created we cannot run the statement again. So just change 'create' as 'Alter' in the 
Statement and remove the create table syntax*/

alter procedure Test as   -- ----Giving name for procedure name                               
insert into Bessant                                          ---Inserting into table
values ('A','sql'),('B','Python'),('C','Linux')
delete from  Bessant where Name='C'                          ---Deleting data of C
update Bessant                                              ----Updating data into B
Set Name='XYZ' where Name='B'
go

---Executing 5 times to check the store procedure working
exec Test
--Checking values

select * from Bessant

---Go to 'Kaggle' website to download the data sets for practicing  

--End of day 15


--Day 16   --06-10-2022
--Functions
use Data_Analysis
select * from Orders

----- American Standard Code for Information Interchange

select [customer name],ASCII([customer name]) 
from orders

--Concatenation function

select CONCAT ([customer name],[ship mode])
from Orders

-- Concat with Separator or Delimiter

select CONCAT ([customer name],'@',[ship mode])
from Orders
--To convert all cases to lowercase

select LOWER([customer name])
from Orders

---To convert to all Uppercase

select upper([customer name])
from Orders

--To select characters from left side/Right side

select LEFT([Customer name],4) from Orders

select Right([Customer name],4) from Orders

---Checking characters length 
select LEN([customer name]) from Orders

---To check the server name to which we have connected to
select @@SERVERNAME

--To check the language

select @@LANGUAGE

---To know how much space the server is utilizing

select @@CPU_BUSY
--Row count check 

Select @@ROWCOUNT

Select @@ROWCOUNT from Orders

select @@TEXTSIZE
--
select @@VERSION

---Reversing string characters
select REVERSE([Customer name]) from Orders

----ABS function gives all negative values as positive values
select ABS(-70)

select COS(10)
---Floor function gives highest least value from the defined numbers
select FLOOR(10.72)

---Ceiling function gives higher value of the defined value
select Ceiling(10.72)

---Power functions
select POWER(10,3)

select ROUND(10.11,1)


select REPLACE([customer name],'aaron','Hemanth') from Orders

select GETDATE()

select DATENAME(Year,Getdate()) as Year


select DATENAME(QUARTER,Getdate()) as Quarter


select DATENAME(MONTH,Getdate()) as Month


select DATENAME(DAY,Getdate()) as day


select DATENAME(WEEK,Getdate()) as week


select DATENAME(WEEKDAY,Getdate()) as weekday


select DATENAME(HOUR,Getdate()) as Hour

select DATENAME(MINUTE,Getdate()) as Minute

select DATENAME(SECOND,Getdate()) as Second

select DATENAME(MICROSECOND,Getdate()) as microsecond

select DATENAME(MILLISECOND,Getdate()) as millisec

select DATENAME(NANOSECOND,Getdate()) as nanosecond

----Assignment

/* Create a database , create a table but dont insert the data
 then create 2 store procedure (only have 2-3 columns in the table)
 Success & Failure as  two different store procedure names*/

 create database Store_Procedure  -----creating database
 use Store_procedure             ---Using database

 create table Table_one(Name varchar (20),Course varchar (20),Score int)   ----Creating table

create procedure Success as   -- ----Giving name for procedure name                               
insert into Table_one                                          ---Inserting into table
values ('A','sql',89),('B','Python',78),('C','Linux',86)
go

create procedure Failure as   -- ----Giving name for procedure name                               

insert into Table_one                                          ---Inserting into table
values ('A','Java',32),('B','Excel',30),('C','Power Bi',28)
go


---Executing the store procedure 
exec Success
exec Failure

--Checking values

select * from Table_one

Alter procedure sp_data
as 
	Begin 
		declare @A as int ,
				@B as int
	Set 
	    @A=10

	If @A>=22
	   Begin
	        Exec Success
    End

 Else 
      Exec Failure
	  End  
	  Go

Exec sp_data

Select * from Table_one

truncate table Table_one

-----SQL Server Procedure 
---We can start run this procedure in the server instead we run 
/* SQL server - Job - New job - Mention the job name as testing-steps (Here
give the store procedure) - Create new - Give step name as 'A' - select databsae name 
store_procedure -  give exec procedure (sp_data)-
now Go to schedule - new - set time and ok .

Alter procedure sp_data
as 
	Begin 
		declare @A as int ,
				@B as int
	Set 
	    @A=10

	If @A>=22
	   Begin
	        Exec Success
    End

 Else 
      Exec Failure
	  End  
	  Go