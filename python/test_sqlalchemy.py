# -*- coding=utf-8 -*-
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    db_user = 'lxq'
    db_pass = 'passwd'
    db_host = 'localhost'
    db_name = 'funds_data'
    engine_str = 'postgres://%s:%s@%s/%s' % (db_user,db_pass,db_host,db_name)
    engine = sqlalchemy.create_engine(engine_str)

    metadata = sqlalchemy.Metadata(bind = engine)
    Base = declarative_base(metadata)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 关键在下面这两个类的定义，不需要针对每个数据项单独定义一个类的列，即能
    # 够实现简单的ORM映射。
    class Funds_list(Base):
        __table__ = Table('funds_list', metadata, autoload=True)
    class Funds_value(Base):
        __table__ = Table('funds_value', metadata, autoload = True)

    # 查询操作
    result = session.query(Funds_value.value_data_id).filter(
                Funds_value.fund_code == '350005',
                Funds_value.value_date == '20140714').all()

    # 插入操作
    item = Fund_List(fund_code = '350005', fund_name = u'天治创新先锋')
    session.add(item)
    session.commit()