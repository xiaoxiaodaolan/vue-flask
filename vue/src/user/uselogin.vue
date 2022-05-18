<template>
	<div class="login">
		<img :src="imgSrc" />
		  <div class="loginPart">
			<h2>用户登录</h2>
		  <el-form>
			<div class="inputElement">
				<el-input v-model="username" placeholder="学号"></el-input>
			</div>
			<div class="inputElement">
				<el-input type="password" v-model="userpwd" placeholder="密码 "></el-input>	
			</div>
			<div>
				<el-button type="primary" @click="userlogin()">登录</el-button>
			</div>
			<div style="text-align: right;color: white;">
				<div>
					<router-link to="/adminlogin"><el-link type="warning"><span class="link">切换管理员登录</span></el-link></router-link>
				</div>
				<router-link to="/userregist"><el-link type="warning"><span class="link">没有账号？去注册</span></el-link></router-link>
			</div>
		  </el-form>
		  </div>
	  </div>
	
</template>

<script>
	export default{
		data(){
			return{
				imgSrc: require("../img/login.jpg"),
				username:'',
				userpwd:''
			}
		},
		created(){
		    if (this.$session.exists()) {
		      this.$router.push('/queryuser')
		    }
		  },
		methods:{
			userlogin(){
				if(this.username != 0 && this.userpwd != 0){
					var denglu = new URLSearchParams();
					denglu.append('username',this.username);
					denglu.append('userpwd',this.userpwd);
					this.$http.post('http://127.0.0.1:9001/loginyonghu',denglu)
					.then(res => {
						this.students = res.data.res
						if(this.students != 0){
							alert('登录成功')
							this.$session.start()
							
							this.$session.set("first",this.username)
							this.$router.push('/queryuser')
						}else{
							alert('账号或者密码错误')
						}
					})
				}else{
					alert('请输入完整的账号和密码')
				}
			},
		}
	}
</script>

<style>

</style>
