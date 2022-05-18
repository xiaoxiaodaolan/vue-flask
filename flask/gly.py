from flask import Flask, request, jsonify, render_template, session, url_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from flask_cors import CORS


app = Flask(__name__)
CORS(app, supports_credentials=True)
db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/library'
db = create_engine(db_url, echo=True)


Base = declarative_base()

class Gly(Base):
    __tablename__ = 'Gly'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    glyname = Column('glyname',String)
    tno = Column('tno',String)
    tel = Column('tel',String)
    def __str__(self) -> str:
        return "id: {}, glyname: {}, tno: {},tel: {}".format(
            self.id, self.glyname, self.tno, self.tel
        )

@app.route("/glylist",methods=["GET"])
def glylist():
    session = sessionmaker(bind = db,expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(Gly).filter():
            resp["res"].append({
                "id":rd.id,
                "glyname": rd.glyname,
                "tno": rd.tno,
                "tel": rd.tel,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"
#查阅学生信息
@app.route("/querygly",methods=["POST"])
def querygly():
    glyname = request.form.get("glyname", "default glyname")
    tno = request.form.get("tno", "default tno")
    session = sessionmaker(bind = db,expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(Gly).filter(or_(Gly.glyname == glyname,Gly.tno == tno)):
            resp["res"].append({
                "id":rd.id,
                "glyname": rd.glyname,
                "tno": rd.tno,
                "tel": rd.tel,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"
# 增加学生信息数据
@app.route("/addgly",methods=["POST"])
def addgly():
    glyname = request.form.get("glyname", "default glyname")
    tno = request.form.get("tno", "default tno")
    tel = request.form.get("tel", "default tel")
    rd=Gly(glyname=glyname,tno=tno,tel=tel)
    session=sessionmaker(bind=db,expire_on_commit=False)()
    try:
        session.add(rd)
        session.commit()
    except Exception as e:
        print(e)
        return "addstudent error"

    resp = {
        "id":rd.id,
        "glyname": rd.glyname,
        "tno": rd.tno,
        "tel": rd.tel,
    }
    return jsonify(resp)
#删除学生信息
@app.route("/deletegly",methods=["POST"])
def deletegly():
    tno = request.form.get("tno", "default tno")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Gly).filter(Gly.tno == tno).all():
            session.delete(rd)
            session.commit()
        return "deletestu success"
    except Exception as e:
        print(e)
        return "errorstu"

# 修改学生信息
@app.route("/updategly", methods=["POST"])
def updategly():
    id = request.form.get("id", "default id")
    glyname = request.form.get("glyname", "default glyname")
    tno = request.form.get("tno", "default tno")
    tel = request.form.get("tel", "default tel")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Gly).filter(Gly.id == id).all():
            print(rd)
            rd.glyname = glyname
            rd.tno = tno
            rd.tel = tel
            session.commit()
        return "updatestu success"

    except Exception as e:
        print(e)
        return "update err"

if __name__ == '__main__':
    app.run(port=9003, debug=True)