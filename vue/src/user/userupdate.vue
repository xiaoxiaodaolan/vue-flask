<template>
	<div class="box">
			<h1>欢迎 {{this.$session.get("first")}} {{this.$session.get("two")}}</h1>
			<div class="table">
				<div class="item">
				   <input type="text" placeholder="新密码" v-model="userpwd">	   
				</div>
				<div class="item">
				   <input type="text" placeholder="确认新密码" v-model="userpassword">		   
				</div>
			</div>
			<button class="login" @click="update()">确认</button>
			<router-link to="/queryuser"><button class="login">返回</button></router-link>
		</div>
</template>

<script>
	export default{
		data(){
			return{
				username:"",
				userpwd:"",
				userpassword:"",
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

			}
		}
	}
</script>

<style>
</style>