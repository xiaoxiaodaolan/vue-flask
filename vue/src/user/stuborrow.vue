<template>
	<div id="all">
		<div id="aside">
			<div id="header">
				<h1>借阅图书</h1>
			</div>
			<div id="nav">
				<button class="btn"><router-link to="/queryuser"><span><p class="p2">用户首页</p></span></router-link></button>
				<button class="btn"><router-link to="/stuborrow"><span><p class="p2">借阅图书</p></span></router-link></button>
				<button class="btn"><router-link to="/returnuser"><span><p class="p2">归还记录</p></span></router-link></button>
			</div>
		</div>
		<div class="top">
			<div class="btn-2">
				<span class="span2">欢迎 {{this.$session.get("first")}} {{this.$session.get("two")}}</span> 
				<button class="btn2" @click="userVisible=true"><span>修改密码</span></button>
				<button class="btn2" @click="exit()"><span>退出</span></button>
				<el-dialog
				title="修改密码"
				center
				:visible.sync="userVisible"
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
		<fieldset class="fieldset1">
			<legend class="legend1">借阅书籍</legend>
			<div class="table">
				<!-- <p>姓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名:<input type="text" v-model="stuname" /></p>
				<p>学&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号:<input type="text" v-model="sno" /></p> -->
				<p>借阅书籍:<input type="text" v-model="bbook" /></p>
				<p>借阅时间:<input type="date" v-model="timeborrow" /></p>
				<p>
					<button class="btn1" type="button" @click="submit()">确认</button>
				</p>
			</div>
		</fieldset>
		
			<table class="table3">
				<th colspan="7">借阅申请</th>
				<tr>
					<td>序号</td>
					<td>姓名</td>
					<td>学号</td>
					<td>借阅书籍</td>
					<td>借阅时间</td>
					<td>待批准</td>
					<!-- <td>操作</td> -->
				</tr>
				<tr v-for="(user,index) in users">
					<td>{{index+1}}</td>
					<td>{{user.stuname}}</td>
					<td>{{user.sno}}</td>
					<td>{{user.bbook}}</td>
					<td>{{user.timeborrow}}</td>
					<td>{{user.approve}}</td>
					<!-- <td>
						<button class="button1" @mouseup="adddel(user)" @click="deluser()">取消</button>
					</td> -->
				</tr>
			</table>
	</div>
</template>

<script>
		export default {
			name:"stuborrow",
			data(){
				return{
					flag:false,
					stuname:"",
					sno:"",
					bbook:"",
					timeborrow:"",
					approve:"",
					users:[],
					userVisible:false,
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
				this.getuserlist()
				this.getname()
			},
			methods:{
				update(){
					if(this.userpwd != 0 && this.userpassword != 0){
						if(this.userpwd == this.userpassword){
							const first = this.$session.get("first");
							var updateyonghu = new URLSearchParams();
							updateyonghu.append('username',first);
							updateyonghu.append('userpwd',this.userpwd);
							this.$http.post('http://127.0.0.1:9001/updateyonghu',updateyonghu)
							.then(res => {
								alert('修改成功')
								this.$session.destroy()
								this.$router.push('/')
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
				submit(){
					if(this.bbook.length !=0 && this.timeborrow.length !=0){
						const first = this.$session.get("first");
						var newuser = new URLSearchParams();
						newuser.append('stuname', this.getstuname);
						newuser.append('sno', first);
						newuser.append('bbook', this.bbook);
						newuser.append('timeborrow', this.timeborrow);

						this.$http.post('http://127.0.0.1:9000/adduser',newuser)
						.then(res => {
							newuser.stuname = this.getstuname;
							newuser.sno = first;
							newuser.bbook = this.bbook;
							newuser.timeborrow = this.timeborrow;
							this.users.push(newuser);
							this.stuname="";
							this.sno="";
							this.bbook="";
							this.timeborrow="";

						})
					}else{
						alert("不能为空")
					}
				},
				getuserlist(){
					const first = this.$session.get("first")
					console.log(first)
					var userlist = new URLSearchParams();
					userlist.append('sno',first)
					this.$http.post('http://127.0.0.1:9000/queryuserlist',userlist)
					.then(res => {
						this.users = res.data.res
					})
				},
				getname(){
					var getstuname = new URLSearchParams();
					const first = this.$session.get("first");
					getstuname.append('sno',first);
					this.$http.post('http://127.0.0.1:9000/querystudent',getstuname)
					.then(res => {
						this.getstuname = res.data.res[0].stuname
						console.log(this.getstuname)
						this.$session.set("two",this.getstuname)
					})
				},
				exit(){
					this.$session.destroy()
					this.$router.push('/')
				},
			}
		}
	</script>

<style>
</style>
