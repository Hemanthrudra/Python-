create procedure Test as                                  ----Giving name for procedure name  
create table Bessant (Name varchar (20),Course varchar (20))   ----Creating table  
insert into Bessant                                          ---Inserting into table  
values ('A','sql'),('B','Python'),('C','Linux')  
delete from  Bessant where Name='C'                          ---Deleting data of C  
update Bessant                                              ----Updating data into B  
Set Name='XYZ' where Name='B'  

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