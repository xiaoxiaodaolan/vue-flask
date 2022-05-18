<template>
  <div id="all">
	  <div id="aside">
	  	<div id="header">
	  		<h1>修改学生</h1>
	  	</div>
	  	<div id="nav">
	  			<button class="btn"><router-link to="/shouye"><p class="p2">首&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;页</p></router-link></button>
	  			<div v-for="onemenu in onemenus" @click='onemenu.show=!onemenu.show'>
	  				<button class="btn"><p class="p2">借阅管理</p></button>
	  				<div v-show="onemenu.show">
	  					<div>
	  						<button class="btn"><router-link to="/addborrow"><span>添加借阅</span></router-link></button>
	  						<button class="btn"><router-link to="/delborrow"><span>删除借阅</span></router-link></button>
	  						<button class="btn"><router-link to="/queryborrow"><span>查询借阅</span></router-link></button>
	  						<button class="btn"><router-link to="/updateborrow"><span>修改借阅</span></router-link></button>
	  					</div>
	  				</div>
	  			</div>
	  			<div v-for="twomenu in twomenus" @click='twomenu.show=!twomenu.show'>
	  				<button class="btn"><p class="p2">图书管理</p></button>
	  				<div v-show="twomenu.show">
	  					<div>
	  						<button class="btn"><router-link to="/addbook"><span>添加图书</span></router-link></button>
	  						<button class="btn"><router-link to="/deletebook"><span>删除图书</span></router-link></button>
	  						<button class="btn"><router-link to="/querybook"><span>查询图书</span></router-link></button>
	  						<button class="btn"><router-link to="/updatebook"><span>修改图书</span></router-link></button>
	  					</div>
	  				</div>
	  			</div>
	  			<div v-for="threemenu in threemenus" @click='threemenu.show=!threemenu.show'>
	  				<button class="btn"><p class="p2">学生管理</p></button>
	  				<div v-show="threemenu.show">
	  					<div>
	  						<button class="btn"><router-link to="/addstu"><span>添加学生</span></router-link></button>
	  						<button class="btn"><router-link to="/delstu"><span>删除学生</span></router-link></button>
	  						<button class="btn"><router-link to="/querystu"><span>查询学生</span></router-link></button>
	  						<button class="btn"><router-link to="/updatestu"><span>修改学生</span></router-link></button>
							<button class="btn"><router-link to="/querystupwd"><span>查询密码</span></router-link></button>
							<button class="btn"><router-link to="/delstupwd"><span>删除账号</span></router-link></button>
	  					</div>
	  				</div>
	  			</div>
				<div v-for="fourmenu in fourmenus" @click='fourmenu.show=!fourmenu.show'>
					<button class="btn"><p class="p2">教师管理</p></button>
					<div v-show="fourmenu.show">
						<div>
							<button class="btn" @click="enteradd()"><span>添加教师</span></button>
							<button class="btn" @click="enterdel()"><span>删除教师</span></button>
							<button class="btn"><router-link to="/querygly"><span>查询教师</span></router-link></button>
							<button class="btn" @click="enterupd()"><span>修改教师</span></button>
						</div>
					</div>
				</div>
	  			
	  	</div>
	  </div>
	  <div class="top">
	  	<div class="btn-2">
	  		<span class="span2">欢迎 {{this.$session.get("three")}} {{this.$session.get("four")}}</span> 
	  		<button class="btn2"><router-link to="/adminlogin"><span>用户登录</span></router-link></button>
	  		<button class="btn2" @click="adminVisible=true"><span>修改密码</span></button>
	  		<button class="btn2" @click="exit()"><span>退出</span></button>
	  		
	  		<el-dialog
	  		title="修改密码"
	  		center
	  		:visible.sync="adminVisible"
	  		width="30%"
	  		>
	  			<el-input class="el-input2" placeholder="新密码" v-model="userpwd" show-password></el-input>
	  			<el-input class="el-input2" placeholder="确认新密码" v-model="userpassword" show-password></el-input>				
	  			<span slot="footer" class="dialog-footer">
	  				<el-button  type="primary" @click="update()">确认</el-button>
	  			</span>
	  		</el-dialog>
	  	</div>
	  </div>

	  
	  <div id="div1">
	  	<table class="table1">
			
	  		<tr>
	  			<td>序号</td>
	  			<td>姓名</td>
	  			<td>学号</td>
				<td>学院</td>
				<td>年级</td>
	  			<td>班级</td>
				<td>联系电话</td>
				<td>添加修改</td>
	  		</tr>
	  		<tr v-for="(student,index) in students">
	  			<td>{{index+1}}</td>
	  			<td>{{student.stuname}}</td>
	  			<td>{{student.sno}}</td>
				<td>{{student.college}}</td>
				<td>{{student.grade}}</td>
				<td>{{student.cls}}</td>
				<td>{{student.tel}}</td>
	  			<td>
					<el-button type="primary" icon="el-icon-edit" circle @click="updatestudent(student)"></el-button>
	  			</td>
	  		</tr>
	  		<tr>
	  			<td colspan="8">学生总数:{{total}}</td>
	  		</tr>
	  	</table>
		<table class="table2">
			<td>
				<p>修改学生信息</p>
				<!-- <p>ID:<input type="text" v-model="id" /></p> -->
				<p>姓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名:<input type="text" v-model="stuname" /></p>
				<p>学&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号:<input type="text" v-model="sno" /></p>
				<p>学&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;院:<input type="text" v-model="college" /></p>
				<p>年&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;级:<input type="text" v-model="grade" /></p>
				<p>班&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;级:<input type="text" v-model="cls" /></p>
				<p>联系电话:<input type="number" v-model="tel" /></p>
				<p><el-button type="primary" round @click="updstudent()">确定</el-button></p>
			</td>
		</table>
	  </div>
  </div>
</template>

<script>
	export default{
		data(){
			return{
				onemenus:[{show:false}],
				twomenus:[{show:false}],
				threemenus:[{show:false}],
				fourmenus:[{show:false}],
				students:[],
				stuname:"",
				sno:"",
				grade:"",
				college:"",
				cls:"",
				tel:"",
				flag:false,
				adminVisible:false,
				username:"",
				userpwd:"",
				userpassword:"",
			}
		},
		computed:{
			total(){
				return this.students.length;
			}
		},
		created(){
			this.getname()
			this.getstudentlist()
		},
		methods:{
			update(){
				if(this.userpwd != 0 && this.userpassword != 0){
					if(this.userpwd == this.userpassword){
						const three = this.$session.get("three");
						var updateadmin = new URLSearchParams();
						updateadmin.append('username',three);
						updateadmin.append('userpwd',this.userpwd);
						this.$http.post('http://127.0.0.1:9002/updateadmin',updateadmin)
						.then(res => {
							alert('修改成功')
							this.$session.destroy()
							this.$router.push('/adminlogin')
						})
					}else{
						alert('密码不一致')
						this.userpwd="";
						this.userpassword="";
					}
				}else{
					alert('不能为空')
				}
			
			},
			enteradd(){
				const three = this.$session.get("three");
				if(this.$session.get("three") == "2018313370"){
					this.$router.push('/addgly')
				}else{
					alert("权限不够")
				}
			},
			enterdel(){
				const three = this.$session.get("three");
				if(this.$session.get("three") == "2018313370"){
					this.$router.push('/deletegly')
				}else{
					alert("权限不够")
				}
			},
			enterupd(){
				const three = this.$session.get("three");
				if(this.$session.get("three") == "2018313370"){
					this.$router.push('/updategly')
				}else{
					alert("权限不够")
				}
			},
			getstudentlist(){
				this.$http.get('http://127.0.0.1:9000/studentlist')
				.then(res => {
					this.students = res.data.res
				})
			},
			updatestudent(student) {
				this.updatedStudent = student;
				this.id = this.updatedStudent.id;
				this.stuname = this.updatedStudent.stuname;
				this.sno = this.updatedStudent.sno;
				this.college = this.updatedStudent.college;
				this.grade = this.updatedStudent.grade;
				this.cls = this.updatedStudent.cls;
				this.tel = this.updatedStudent.tel;
				this.flag = true;
			},
			updstudent() {
				var updateStudent = new URLSearchParams();
				updateStudent.append('id',this.id);
				updateStudent.append('stuname',this.stuname);
				updateStudent.append('sno',this.sno);
				updateStudent.append('college',this.college);
				updateStudent.append('grade',this.grade);
				updateStudent.append('cls',this.cls);
				updateStudent.append('tel',this.tel);
				this.$http.post('http://127.0.0.1:9000/updatestudent',updateStudent)
				.then(res => {	
					this.updatedStudent.stuname = this.stuname;
					this.updatedStudent.sno = this.sno;
					this.updatedStudent.college = this.college;
					this.updatedStudent.grade = this.grade;
					this.updatedStudent.cls = this.cls;
					this.updatedStudent.tel = this.tel;
					
					this.flag = false;
					this.id = "",
					this.stuname = '';
					this.sno = '';
					this.college ="",
					this.grade = '';
					this.cls = '';
					this.tel = '';
				})
				
				
			},
			getname(){
				var getglyname = new URLSearchParams();
				const three = this.$session.get("three");
				getglyname.append('tno',three);
				this.$http.post('http://127.0.0.1:9003/querygly',getglyname)
				.then(res => {
					this.getglyname = res.data.res[0].glyname
					console.log(this.getglyname)
					this.$session.set("four",this.getglyname)
				})
			},
			exit(){
				this.$session.destroy()
				this.$router.push('/adminlogin')
			},
		}
	}
</script>

<style>
</style>
