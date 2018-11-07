-- Data prepapred by Davood Rafiei, drafiei@ualberta.ca
-- Published on Sept 27, 2017

-- Let's insert some tuples to our tables (definitly need more data for testing)

insert into stores values (10, 'Canadian Tire', '780-111-2222', 'Edmonton South Common');
insert into stores values (20, 'Canadian Superstore', '780-111-3333', 'Edmonton South Common');

insert into categories values ('dai', 'Dairy');
insert into categories values ('bak', 'Bakery');
insert into categories values ('mea', 'Meat and seafood');

insert into products values ('p10','4L milk 1%','ea', 'dai');
insert into products values ('p20','dozen large egg','ea', 'dai');

insert into carries values (20, 'p10', 100, 4.70);
insert into carries values (20, 'p20', 80, 2.60);

insert into customers values ('c10', 'davood', 'CS Dept,University of Alberta');
insert into customers values ('c20', 'john', '111-222 Ave');

insert into orders values (100, 'c10', '2017-09-26', 'Athabasca Hall, University of Alberta');
insert into orders values (120, 'c20', '2017-09-26', '111-222 Ave');

insert into olines values (100, 20, 'p20', 2, 2.80);
insert into olines values (120, 20, 'p10', 1, 4.70);

insert into deliveries values (1000,100,datetime(), null);
insert into deliveries values (1002,120,datetime('now','-4 hours'), datetime('now'));

