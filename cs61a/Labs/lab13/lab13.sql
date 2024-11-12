.read data.sql


CREATE TABLE average_prices AS
  SELECT category from product, avg(MSRP) from product group by product


CREATE TABLE lowest_prices AS
  SELECT store, item,min(price) from inventory group by item

create table cp_value AS
  select category, name, min(MSRP/rating) from products group by category; 

CREATE TABLE shopping_list AS
  SELECT name, store from cp_value, lowest_prices 
    where name = list;

CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs)
    from stores as a, shopping_list as bread    
      where a.store = b.store;

