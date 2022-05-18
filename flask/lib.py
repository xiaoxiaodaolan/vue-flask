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

class Lib(Base):
    __tablename__ = 'Lib'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name',String)
    author = Column('author',String)
    location = Column('location',String)
    price = Column('price',String)
    def __str__(self) -> str:
        return "id: {}, name: {}, author: {},location: {},price:{}".format(
            self.id, self.name, self.author, self.location, self.price
        )

class Borrow(Base):
    __tablename__ = 'Borrow'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    stuname = Column('stuname',String)
    sno = Column('sno',String)
    bbook = Column('bbook',String)
    timeborrow = Column('timeborrow',String)
    timereturn = Column('timereturn',String)
    statu = Column('statu',String)
    def __str__(self) -> str:
        return "id: {}, stuname: {}, sno:{}, bbook: {}, timeborrow:{},timereturn:{}, statu:{}".format(
            self.id, self.stuname, self.sno, self.bbook,self.timeborrow,self.timereturn,self.statu
        )

class Student(Base):
    __tablename__ = 'Student'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    stuname = Column('stuname',String)
    sno = Column('sno',String)
    college = Column('college',String)
    grade = Column('grade',String)
    cls = Column('cls',String)
    tel = Column('tel',String)
    def __str__(self) -> str:
        return "id: {}, stuname: {}, sno:{}, college: {}, grade:{},cls:{}, tel:{}".format(
            self.id, self.stuname, self.sno, self.college,self.grade,self.cls,self.tel
        )

class User(Base):
    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    stuname = Column('stuname',String)
    sno = Column('sno',String)
    bbook = Column('bbook',String)
    timeborrow = Column('timeborrow',String)
    approve = Column('approve',String)
    def __str__(self) -> str:
        return "id: {}, stuname: {}, sno: {},bbook: {},timeborrow:{},approve:{}".format(
            self.id, self.stuname, self.sno, self.bbook, self.timeborrow, self.approve
        )
#删除借阅信息
@app.route("/deleteuser",methods=["POST"])
def deleteuser():
    id = request.form.get("id", "default id")

    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(User).filter(User.id == id).all():
            session.delete(rd)
            session.commit()
        return "deletestu success"
    except Exception as e:
        print(e)
        return "erroruser"
# 修改学生信息
@app.route("/updateuser", methods=["POST"])
def updateuser():
    id = request.form.get("id", "default id")
    stuname = request.form.get("stuname", "default stuname")
    sno = request.form.get("sno", "default sno")
    bbook = request.form.get("bbook", "default bbook")
    timeborrow = request.form.get("timeborrow", "default timeborrow")
    approve = request.form.get("approve", "default approve")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(User).filter(or_(User.id == id)).all():
            print(rd)
            rd.stuname = stuname
            rd.sno = sno
            rd.bbook = bbook
            rd.timeborrow = timeborrow
            rd.approve = approve
            session.commit()
        return "updatestu success"

    except Exception as e:
        print(e)
        return "update err"

#学生借书信息
@app.route("/userlist",methods=["GET"])
def userlist():
    session = sessionmaker(bind = db,expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(User).filter():
            resp["res"].append({
                "id":rd.id,
                "stuname": rd.stuname,
                "sno": rd.sno,
                "bbook": rd.bbook,
                "timeborrow": rd.timeborrow,
                "approve": rd.approve,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"

#学生借书信息
@app.route("/queryuserlist",methods=["POST"])
def queryuserlist():
    sno = request.form.get('sno','default sno')
    session = sessionmaker(bind = db,expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(User).filter(User.sno == sno):
            resp["res"].append({
                "id":rd.id,
                "stuname": rd.stuname,
                "sno": rd.sno,
                "bbook": rd.bbook,
                "timeborrow": rd.timeborrow,
                "approve": rd.approve,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"
# 学生借书
@app.route("/adduser",methods=["POST"])
def adduser():
    stuname = request.form.get("stuname", "default stuname")
    sno = request.form.get("sno", "default sno")
    bbook = request.form.get("bbook", "default bbook")
    timeborrow = request.form.get("timeborrow", "default timeborrow")
    # approve = request.form.get("approve", "default approve")

    rd=User(stuname=stuname,sno=sno,bbook=bbook,timeborrow=timeborrow)
    session=sessionmaker(bind=db,expire_on_commit=False)()
    try:
        session.add(rd)
        session.commit()
    except Exception as e:
        print(e)
        return "add error"

    resp = {
        "id":rd.id,
        "stuname": rd.stuname,
        "sno": rd.sno,
        "bbook": rd.bbook,
        "timeborrow": rd.timeborrow,
        # "approve": rd.approve,
    }
    return jsonify(resp)



@app.route('/returnrecord',methods=["POST"])
def returnrecord():
    sno = request.form.get("sno","default sno")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        resp = {
            "res": [],
        }
        for rd in session.query(Borrow).filter(Borrow.sno == sno):
            resp["res"].append({
                "id": rd.id,
                "stuname": rd.stuname,
                "sno": rd.sno,
                "bbook": rd.bbook,
                "timeborrow": rd.timeborrow,
                "timereturn": rd.timereturn,
                "statu": rd.statu,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"
# 以下为管理员的内容
# c查阅全部学生信息
@app.route("/studentlist",methods=["GET"])
def studentlist():
    session = sessionmaker(bind = db,expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(Student).filter():
            resp["res"].append({
                "id":rd.id,
                "stuname": rd.stuname,
                "sno": rd.sno,
                "college": rd.college,
                "grade": rd.grade,
                "cls": rd.cls,
                "tel": rd.tel,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"
#查阅学生信息
@app.route("/querystudent",methods=["POST"])
def querystudent():
    stuname = request.form.get("stuname", "default stuname")
    sno = request.form.get("sno", "default sno")
    session = sessionmaker(bind = db,expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(Student).filter(or_(Student.stuname == stuname,Student.sno == sno)):
            resp["res"].append({
                "id":rd.id,
                "stuname": rd.stuname,
                "sno": rd.sno,
                "college": rd.college,
                "grade": rd.grade,
                "cls": rd.cls,
                "tel": rd.tel,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"
# 增加学生信息数据
@app.route("/addstudent",methods=["POST"])
def addstudent():
    stuname = request.form.get("stuname", "default stuname")
    sno = request.form.get("sno", "default sno")
    college = request.form.get("college", "default college")
    grade = request.form.get("grade", "default grade")
    cls = request.form.get("cls", "default cls")
    tel = request.form.get("tel", "default tel")
    rd=Student(stuname=stuname,sno=sno,college=college,grade=grade,cls=cls,tel=tel)
    session=sessionmaker(bind=db,expire_on_commit=False)()
    try:
        session.add(rd)
        session.commit()
    except Exception as e:
        print(e)
        return "addstudent error"

    resp = {
        "id":rd.id,
        "stuname": rd.stuname,
        "sno": rd.sno,
        "college": rd.college,
        "grade": rd.grade,
        "cls": rd.cls,
        "tel": rd.tel,
    }
    return jsonify(resp)
#删除学生信息
@app.route("/deletestudent",methods=["POST"])
def deletestudent():
    sno = request.form.get("sno", "default sno")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Student).filter(Student.sno == sno).all():
            session.delete(rd)
            session.commit()
        return "deletestu success"
    except Exception as e:
        print(e)
        return "errorstu"

# 修改学生信息
@app.route("/updatestudent", methods=["POST"])
def updatestudent():
    id = request.form.get("id", "default id")
    stuname = request.form.get("stuname", "default stuname")
    sno = request.form.get("sno", "default sno")
    college = request.form.get("college", "default college")
    grade = request.form.get("grade", "default grade")
    cls = request.form.get("cls", "default cls")
    tel = request.form.get("tel", "default tel")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Student).filter(or_(Student.id == id)).all():
            print(rd)
            rd.stuname = stuname
            rd.sno = sno
            rd.college = college
            rd.grade = grade
            rd.cls = cls
            rd.tel = tel
            session.commit()
        return "updatestu success"

    except Exception as e:
        print(e)
        return "update err"



#查阅全部借阅信息
@app.route("/borrowlist",methods=["GET"])
def borrowlist():
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(Borrow).filter():
            resp["res"].append({
                "id":rd.id,
                "stuname": rd.stuname,
                "sno": rd.sno,
                "bbook": rd.bbook,
                "timeborrow": rd.timeborrow,
                "timereturn": rd.timereturn,
                "statu": rd.statu,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "boerror"
# 查询学生借阅数据
@app.route("/queryborrow",methods=["POST"])
def queryborrow():
    stuname = request.form.get("stuname", "default stuname")
    session = sessionmaker(bind = db,expire_on_commit=False)()
    try:
        resp={
            "res":[],
        }
        for rd in session.query(Borrow).filter(Borrow.stuname==stuname):
            resp["res"].append({
                "id":rd.id,
                "stuname": rd.stuname,
                "sno": rd.sno,
                "bbook": rd.bbook,
                "timeborrow": rd.timeborrow,
                "timereturn": rd.timereturn,
                "statu": rd.statu,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"
# 增加学生借阅数据
@app.route("/addborrow",methods=["POST"])
def addborrow():
    stuname=request.form.get("stuname","default stuname")
    sno=request.form.get("sno","default sno")
    bbook=request.form.get("bbook","default bbook")
    timeborrow = request.form.get("timeborrow", "default timeborrow")
    timereturn = request.form.get("timereturn", "default timereturn")
    statu=request.form.get("statu","default statu")
    rd=Borrow(stuname=stuname,sno=sno,bbook=bbook,timeborrow=timeborrow,timereturn=timereturn,statu=statu)
    session=sessionmaker(bind=db,expire_on_commit=False)()
    try:
        session.add(rd)
        session.commit()
    except Exception as e:
        print(e)
        return "addstu error"

    resp = {
        "id": rd.id,
        "stuname": rd.stuname,
        "sno": rd.sno,
        "bbook": rd.bbook,
        "timeborrow": rd.timeborrow,
        "timereturn": rd.timereturn,

        "statu": rd.statu,
    }
    return jsonify(resp)
# 修改学生借阅数据
@app.route("/updateborrow",methods=["POST"])
def updateborrow():
    id = request.form.get("id", "default id")
    stuname = request.form.get("stuname", "default stuname")
    sno = request.form.get("sno", "default sno")
    bbook = request.form.get("bbook", "default bbook")
    timeborrow = request.form.get("timeborrow", "default timeborrow")
    timereturn = request.form.get("timereturn", "default timereturn")
    statu = request.form.get("statu", "default statu")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Borrow).filter(or_(Borrow.id == id)).all():
            print(rd)
            rd.stuname = stuname
            rd.sno = sno
            rd.bbook = bbook
            rd.timeborrow = timeborrow
            rd.timereturn = timereturn
            rd.statu = statu
            session.commit()
        return "updatestu success"

    except Exception as e:
        print(e)
        return "updatestu err"
# 删除学生借阅数据
@app.route("/deleteborrow",methods=["POST"])
def deleteborrow():
    stuname = request.form.get("stuname", "default stuname")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Borrow).filter(Borrow.stuname == stuname).all():
            session.delete(rd)
            session.commit()
        return "deletestu success"
    except Exception as e:
        print(e)
        return "errorstu"

# 删除学生借阅数据
@app.route("/deleteaborrow",methods=["POST"])
def deleteaborrow():
    id = request.form.get("id", "default id")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Borrow).filter(Borrow.id == id).all():
            session.delete(rd)
            session.commit()
        return "deletestu success"
    except Exception as e:
        print(e)
        return "errorstu"




#查询全部图书
@app.route('/booklist',methods=["GET"])
def booklist():
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        resp = {
            "res": [],
        }
        for rd in session.query(Lib).filter().all():
            resp["res"].append({
                "id": rd.id,
                "name": rd.name,
                "author": rd.author,
                "location": rd.location,
                "price": rd.price,
            })
        return jsonify(resp)

    except Exception as e:
        print(e)
        return "error"


# 添加图书
@app.route("/addbook",methods=["POST"])
def addbook():
    name=request.form.get("name","default name")
    author=request.form.get("author","default author")
    location=request.form.get("location","default location")
    price=request.form.get("price","default price")
    rd=Lib(name=name,author=author,location=location,price=price)
    session=sessionmaker(bind=db,expire_on_commit=False)()
    try:
        session.add(rd)
        session.commit()
    except Exception as e:
        print(e)
        return "add error"

    resp = {
        "id": rd.id,
        "name": rd.name,
        "author": rd.author,
        "location": rd.location,
        "price": rd.price,
    }
    return jsonify(resp)
# 修改图书
@app.route("/updatebook",methods=["POST"])
def updatebook():
    id = request.form.get("id", "default id")
    name = request.form.get("name", "default name")
    author = request.form.get("author", "default author")
    location = request.form.get("location", "default location")
    price = request.form.get("price", "default price")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Lib).filter(or_(Lib.id == id)).all():
            print(rd)
            rd.name = name
            rd.author = author
            rd.location = location
            rd.price = price
            session.commit()
        return "update success"

    except Exception as e:
        print(e)
        return "update err"
# 删除图书
@app.route("/deletebook",methods=["POST"])
def deletebook():
    name = request.form.get("name", "default name")
    author = request.form.get("author", "default author")
    location = request.form.get("location", "default location")
    price = request.form.get("price", "default price")

    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Lib).filter(or_(Lib.name == name, Lib.author == author,Lib.location == location ,Lib.price == price)).all():
            session.delete(rd)
            session.commit()
        return "delete success"
    except Exception as e:
        print(e)
        return "error"

# 删除图书
@app.route("/deleteabook",methods=["POST"])
def deleteabook():
    id = request.form.get("id", "default id")

    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        for rd in session.query(Lib).filter(Lib.id == id).all():
            session.delete(rd)
            session.commit()
        return "delete success"
    except Exception as e:
        print(e)
        return "error"
#查询图书
@app.route('/querybook',methods=["post"])
def querybookk():
    name = request.form.get("name","default name")
    author = request.form.get("author","default author")
    session = sessionmaker(bind=db, expire_on_commit=False)()
    try:
        resp = {
            "res": [],
        }
        for rd in session.query(Lib).filter(or_(Lib.name == name, Lib.author == author)).all():
            resp["res"].append({
                "id": rd.id,
                "name": rd.name,
                "author": rd.author,
                "location": rd.location,
                "price": rd.price,
            })
        return jsonify(resp)
    except Exception as e:
        print(e)
        return "error"

if __name__ == '__main__':
    app.run(port=9000, debug=True)
