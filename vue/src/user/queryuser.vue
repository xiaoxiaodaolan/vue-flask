<template>
	<div id="all">
		<div id="aside">
			<div id="header">
				<h1>用户首页</h1>
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
			<el-input class="el-input" @click.native="againclick()" placeholder="请输入书名" v-model="name"></el-input>
			<el-button type="primary" icon="el-icon-search" @click="querybook()">搜索</el-button>
			<table class="table1">
				<tr>
					<td>序号</td>
					<td>书名</td>
					<td>作者</td>
					<td>位置</td>
					<td>价格</td>
				</tr>
				<tr v-for="(book,index) in books">
					<td>{{index+1}}</td>
					<td>{{book.name}}</td>
					<td>{{book.author}}</td>
					<td>{{book.location}}</td>
					<td>{{book.price}}</td>
				</tr>
				<tr>
					<td colspan="6">书本总数:{{total}}</td>
				</tr>
			</table>
		</div>
		
	</div>
</template>

<script>
	
	export default {
		name:'addbook',
		data(){
			return{
				onemenus:[{show:false}],
				twomenus:[{show:false}],
				threemenus:[{show:false}],
				books:[],
				name:"",
				author:"",
				userVisible:false,
				username:"",
				userpwd:"",
				userpassword:"",
			}
		},
		created(){
			this.getname()
			this.getbook()
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
			exit(){
				this.$session.destroy()
				this.$router.push('/')
			},
			getbook(){
				this.$http.get('http://127.0.0.1:9000/booklist')
				.then(res => {
					this.books = res.data.res
				})
			},

			againclick(){
				this.getbook()
			},
			querybook(){

				var querybook = new URLSearchParams();
				if(this.name.length != 0){
					querybook.append('name',this.name);
					this.$http.post('http://127.0.0.1:9000/querybook',querybook)
					.then(res => {
						this.books = res.data.res;
						this.name = "";
						
					})
					.catch(err => {
						console.log(err)
					})
					
				}else{
					alert('请输入')
				}
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
		},
		computed:{
		    total:function(){
		        return this.books.length;
		    }
		}
	}
</script>

<style>
</style>
