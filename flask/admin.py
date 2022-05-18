from flask import Flask, request, jsonify,render_template,session,url_for
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

class Admin(Base):
    __tablename__ = 'Admin'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username',String)
    userpwd = Column('userpwd',String)
    def __str__(self) -> str:
        return "id: {}, username: {}, userpwd: {}".format(
            self.id, self.username, self.userpwd
        )

#登录
@app.route('/loginadmin',methods=["POST"])
def loginadmin():
    username = request.form.get("username","default username")
    userpwd = request.form.get("userpwd","default userpwd")

    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        resp = {
            "res": [],
        }
        for rd in session.query(Admin).filter(Admin.username == username, Admin.userpwd == userpwd).all():
            resp["res"].append({
                "id": rd.id,
                "username": rd.username,
                "userpwd": rd.userpwd,
            })
        return jsonify(resp)

    except Exception as e:
        print(e)
        return "error"
# 查询登录
@app.route('/queryadmin',methods=["POST"])
def queryadmin():
    username = request.form.get("username","default username")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        resp = {
            "res": [],
        }
        for rd in session.query(Admin).filter(Admin.username == username).all():
            resp["res"].append({
                "id": rd.id,
                "username": rd.username,
                "userpwd": rd.userpwd,
            })
        return jsonify(resp)

    except Exception as e:
        print(e)
        return "error"
# 注册
@app.route("/addadmin",methods=["POST"])
def addadmin():
    username=request.form.get("username","default username")
    userpwd=request.form.get("userpwd","default userpwd")
    rd=Admin(username=username,userpwd=userpwd)
    session=sessionmaker(bind=db,expire_on_commit=False)()
    try:
        session.add(rd)
        session.commit()
    except Exception as e:
        print(e)
        return "addyonghu error"

    resp={
        "id":rd.id,
        "username":rd.username,
        "userpwd":rd.userpwd,
    }
    return jsonify(resp)

# 修改
@app.route("/updateadmin", methods=["POST"])
def updateadmin():
    # id = request.form.get("id", "default id")
    username = request.form.get("username", "default username")
    userpwd = request.form.get("userpwd", "default userpwd")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Admin).filter(Admin.username == username).all():
            print(rd)
            rd.username = username
            rd.userpwd = userpwd
            session.commit()
        return "updatestu success"

    except Exception as e:
        print(e)
        return "update err"

if __name__ == '__main__':
    app.run(port=9002,debug=True)
