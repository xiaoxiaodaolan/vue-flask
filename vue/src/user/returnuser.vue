<template>
	<div id="all">
		<div id="aside">
			<div id="header">
				<h1>归还记录</h1>
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
		
		<div id="div1">
			<table class="table3">
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
				stuname:"",
				sno:"",
				bbook:"",
				timeborrow:"",
				statu:"",
				stus:[],
				userVisible:false,
				username:"",
				userpwd:"",
				userpassword:"",
			}
		},
		created(){
			this.getname()
			if (this.$session.exists()) {
			  this.getborrowlist()
			}else{
				this.$router.push('/')
			}
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
			getborrowlist(){
				const first = this.$session.get("first")
				console.log(first)
				var jieyue = new URLSearchParams();
				jieyue.append('sno',first)
				this.$http.post('http://127.0.0.1:9000/returnrecord',jieyue)
				.then(res => {
					this.stus = res.data.res
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
