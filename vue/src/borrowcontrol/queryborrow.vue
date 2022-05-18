<template>
  <div id="all">
	  <div id="aside">
	  	<div id="header">
	  		<h1>查询借阅</h1>
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
	  			<el-input type="password" class="el-input2" placeholder="新密码" v-model="userpwd" show-password></el-input>
	  			<el-input type="password" class="el-input2" placeholder="确认新密码" v-model="userpassword" show-password></el-input>				
	  			<span slot="footer" class="dialog-footer">
	  				<el-button  type="primary" @click="update()">确认</el-button>
	  			</span>
	  		</el-dialog>
	  	</div>
	  </div>
	  
	  <div id="div1">
		  <el-input class="el-input" @click.native="againclick()" placeholder="请输入姓名" v-model="stuname"></el-input>
		  <el-button type="primary" icon="el-icon-search" @click="queryborrow()">搜索</el-button>
	  	<table class="table1">
	  		<tr>
	  			<td>序号</td>
	  			<td>姓名</td>
	  			<td>学号</td>
	  			<td>借阅书本</td>
	  			<td>借阅日期</td>
				<td>归还日期</td>
	  			<td>是否归还</td>
	  		</tr>
	  		<tr v-for="(stu,index) in stus">
	  			<td>{{index+1}}</td>
	  			<td>{{stu.stuname}}</td>
	  			<td>{{stu.sno}}</td>
	  			<td>{{stu.bbook}}</td>
	  			<td>{{stu.timeborrow}}</td>
				<td>{{stu.timereturn}}</td>
	  			<td>{{stu.statu}}</td>
	  		</tr>
	  		<tr>
	  			<td colspan="8">借阅人总数:{{total}}</td>
	  		</tr>
	  	</table>
	  	
	  </div>
	  
  </div>
</template>

<script>
	export default {
		data(){
			return{
				onemenus:[{show:false}],
				twomenus:[{show:false}],
				threemenus:[{show:false}],
				fourmenus:[{show:false}],
				stuname:"",
				stus:[],
				adminVisible:false,
				username:"",
				userpwd:"",
				userpassword:"",
			}
		},
		created(){
			this.getname()
			this.getborrowlist()
		},
		computed:{
			total:function(){
				return this.stus.length;
			}		
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
			getborrowlist(){
				this.$http.get('http://127.0.0.1:9000/borrowlist')
				.then(res => {
					this.stus = res.data.res
				})
			},
			againclick(){
				this.getborrowlist()
			},
			queryborrow(){
			
				var queryborrow = new URLSearchParams();
				if(this.stuname.length != 0){
					queryborrow.append('stuname',this.stuname);
					this.$http.post('http://127.0.0.1:9000/queryborrow',queryborrow)
					.then(res => {
						this.stus = res.data.res;
						this.stuname = "";
						
					})
					.catch(err => {
						console.log(err)
					})
					
				}else{
					alert('请输入')
				}
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
	@import url("../assets/css.css");
</style>
