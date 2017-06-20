import sqlalchemy
from sqlalchemy import create_engine
import os, sys


SQLALCHEMY_DATABASE_URI = 'sqlite:///' +'app.db'
print('\n\n'+str(sys.argv)+'\n\n')
target_name = sys.argv[1]
db = create_engine(SQLALCHEMY_DATABASE_URI)

db.connect()
with open(target_name+'.txt') as _:
    lines = _.readlines()
for line in lines:
    db.engine.execute('insert into photo values (null,(select id from target where url == "{}"),"{}")'.format(target_name,line.rsplit('\n')[0]))

