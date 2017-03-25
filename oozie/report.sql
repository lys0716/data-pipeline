CREATE EXTERNAL TABLE IF NOT EXISTS words(word STRING) LOCATION '/data_hive';
MSCK REPAIR TABLE words;
INSERT OVERWRITE LOCAL DIRECTORY '/home/hadoop/report' 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
SELECT word, count(*) FROM words GROUP BY word;
