<template>
	<div class="login">
		<img :src="imgSrc" />
		  <div class="loginPart">
			<h2>管理员登录</h2>
		  <el-form>
			<div class="inputElement">
				<el-input v-model="username" placeholder="教师编号"></el-input>
			</div>
			<div class="inputElement">
				<el-input type="password" v-model="userpwd" placeholder="密码 "></el-input>
			</div>
			<div>
				<el-button type="primary" @click="userlogin()">登录</el-button>
			</div>
			<div style="text-align: right;color: white;">
				<div>
					<router-link to="/"><el-link type="warning"><span class="link">切换用户登录</span></el-link></router-link>
				</div>
				<router-link to="/adminregist"><el-link type="warning"><span class="link">没有账号？去注册</span></el-link></router-link>
			</div>
		  </el-form>
		  </div>
	  </div>	
</template>

<script>
	export default{
	    name:"uselogin",
	    data(){
			return{
				username: '',
				userpwd: '',
				mimas:[],
				imgSrc: require("../img/login.jpg"),
			}
	    },
	    methods: { 
	        userlogin(){
	        	if(this.username != 0 && this.userpwd != 0){
	        		var denglu = new URLSearchParams();
	        		denglu.append('username',this.username);
	        		denglu.append('userpwd',this.userpwd);
	        		this.$http.post('http://127.0.0.1:9002/loginadmin',denglu)
	        		.then(res => {
	        			this.admins = res.data.res
	        			if(this.admins != 0){
	        				alert('登录成功')
	        				this.$session.start()
	        				
	        				this.$session.set("three",this.username)
	        				this.$router.push('/shouye')
	        			}else{
	        				alert('账号或者密码错误')
	        			}
	        		})
	        	}else{
	        		alert('请输入完整的账号和密码')
	        	}
	        },
			
	    },
	}
</script>

<style>
	
</style>
