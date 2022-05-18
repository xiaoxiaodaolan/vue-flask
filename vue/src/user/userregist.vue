<template>
	<div class="login">
		<img :src="imgSrc" />
		  <div class="loginPart">
			<h2>用户注册</h2>
		  <el-form>
			<div class="inputElement">
				<el-input v-model="username" placeholder="学号"></el-input>
			</div>
			<div class="inputElement">
				<el-input type="password" v-model="userpwd" placeholder="密码 "></el-input>
			</div>
			<div>
				<el-button type="primary" @click="regist()">注册</el-button>
			</div>
			<div style="text-align: right;color: white;">
				<div>
					<router-link to="/adminregist"><el-link type="warning"><span class="link">切换管理员注册</span></el-link></router-link>
				</div>
				<router-link to="/"><el-link type="warning"><span class="link">已有账号？去登录</span></el-link></router-link>
			</div>
		  </el-form>
		  </div>
	  </div>
</template>

<script>
	export default{
		data() {
			return {
				students: [],
				yonghu:[],
				username:"",
				userpwd:"",
				imgSrc: require("../img/login.jpg"),
			}
		},

		methods: {
			regist(){				
				if(this.username.length != 0 && this.userpwd.length != 0 ){
					var queryyonghu = new URLSearchParams();
					queryyonghu.append('username',this.username)
					this.$http.post('http://127.0.0.1:9001/queryyonghu',queryyonghu)
					.then(res => {
						this.yonghu = res.data.res
						if(this.yonghu != 0){
							alert('用户已存在')
						}else{
							var querystudent = new URLSearchParams();
							querystudent.append('sno',this.username);
							this.$http.post('http://127.0.0.1:9000/querystudent',querystudent)
							.then(res => {
								this.students = res.data.res
								if(this.students != 0){
									var zhuce = new URLSearchParams();
									zhuce.append('username',this.username)
									zhuce.append('userpwd',this.userpwd)
									this.$http.post('http://127.0.0.1:9001/addyonghu',zhuce)
									.then(res => {
										alert("注册成功");
										this.$router.push('/')
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
