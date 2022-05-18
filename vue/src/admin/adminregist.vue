<template>
	<div class="login">
		<img :src="imgSrc" />
		  <div class="loginPart">
			<h2>管理员注册</h2>
		  <el-form>
			<div class="inputElement">
				<el-input v-model="username" placeholder="教师编号"></el-input>
			</div>
			<div class="inputElement">
				<el-input type="password" v-model="userpwd" placeholder="密码 "></el-input>
			</div>
			<div>
				<el-button type="primary" @click="regist()">注册</el-button>
			</div>
			<div style="text-align: right;color: white;">
				<div>
					<router-link to="/userregist"><el-link type="warning"><span class="link">切换用户注册</span></el-link></router-link>
				</div>
				<router-link to="/adminlogin"><el-link type="warning"><span class="link">已有账号？去登录</span></el-link></router-link>
			</div>
		  </el-form>
		  </div>
	  </div>
</template>

<script>
	export default{
		data() {
			return {
				admin:[],
				glys:[],
				username:"",
				userpwd:"",
				imgSrc: require("../img/login.jpg"),
			}
		},

		methods: {
			regist(){
				
				if(this.username.length != 0 && this.userpwd.length != 0 ){
					var queryadmin = new URLSearchParams();
					queryadmin.append('username',this.username)
					this.$http.post('http://127.0.0.1:9002/queryadmin',queryadmin)
					.then(res => {
						this.admin = res.data.res
						if(this.admin != 0){
							alert('用户已存在')
						}else{
							var querygly = new URLSearchParams();
							querygly.append('tno',this.username)
							this.$http.post('http://127.0.0.1:9003/querygly',querygly)
							.then(res => {
								this.glys = res.data.res
								if(this.glys != 0){
									var zhuce = new URLSearchParams();
									zhuce.append('username',this.username)
									zhuce.append('userpwd',this.userpwd)
									this.$http.post('http://127.0.0.1:9002/addadmin',zhuce)
									.then(res => {
										alert("注册成功");
										this.$router.push('/adminlogin')
									})
								}else{
									alert('学号不存在')
								}
							})

						}
					})
				}else{
					alert('不能为空')
				}
			}
		},
	}
</script>

<style>

</style>
