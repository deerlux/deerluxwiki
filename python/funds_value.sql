
CREATE TABLE IF NOT EXISTS funds_list (
      fund_code varchar(6) NOT NULL ,
      type_id int DEFAULT NULL,
      fund_name varchar(32)   NOT NULL ,
      fund_origin_date date DEFAULT NULL,
      funds_company_id int DEFAULT NULL,
      comment varchar(256)   DEFAULT NULL,
      PRIMARY KEY (fund_code)
);

CREATE TABLE IF NOT EXISTS funds_value (
      value_data_id bigserial,
      fund_code varchar(6) NOT NULL ,
      value_date date NOT NULL,
      value_curr float DEFAULT NULL ,
      PRIMARY KEY (value_data_id),
      UNIQUE (fund_code, value_date)
);
--
--  外键约束 funds_value
--
ALTER TABLE funds_value
    ADD CONSTRAINT funds_value_ibfk_2 FOREIGN KEY (fund_code) REFERENCES funds_list (fund_code) ON DELETE CASCADE ON UPDATE CASCADE;

