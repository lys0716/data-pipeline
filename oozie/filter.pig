A = LOAD  '/data' using PigStorage() as (line:chararray); 
B = FILTER A BY (line matches '.*facebook.*');
STORE B INTO '/data_hive' USING PigStorage();

