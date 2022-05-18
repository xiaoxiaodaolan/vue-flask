import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'
import VueSession from 'vue-session'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import shouye from './components/shouye.vue'

import addbook from './components/addbook.vue'
import deletebook from './components/deletebook.vue'
import querybook from './components/querybook.vue'
import updatebook from './components/updatebook.vue'


import addborrow from './borrowcontrol/addborrow.vue'
import delborrow from './borrowcontrol/delborrow.vue'
import queryborrow from './borrowcontrol/queryborrow.vue'
import updateborrow from './borrowcontrol/updateborrow.vue'

import addstu from './stucontrol/addstu.vue'
import delstu from './stucontrol/delstu.vue'
import querystu from './stucontrol/querystu.vue'
import updatestu from './stucontrol/updatestu.vue'
import querystupwd from './stucontrol/querystupwd'
import delstupwd from './stucontrol/delstupwd'


import stuborrow from './user/stuborrow.vue'
import queryuser from './user/queryuser.vue'
import returnuser from './user/returnuser.vue'
import uselogin from './user/uselogin.vue'
import userregist from './user/userregist.vue'
import userupdate from './user/userupdate.vue'
import yonghu from './user/yonghu.vue'

import adminlogin from './admin/adminlogin.vue'
import adminregist from './admin/adminregist.vue'
import adminupdate from './admin/adminupdate'

import addgly from './admincontrol/addgly.vue'
import deletegly from './admincontrol/deletegly.vue'
import querygly from './admincontrol/querygly.vue'
import updategly from './admincontrol/updategly.vue'

Vue.use(Router)
Vue.use(VueSession)
Vue.use(ElementUI)
// Vue.use(Button)
// axios.defaults.baseURI = 'http://127.0.0.1:9000'
Vue.prototype.$http = axios;



const router = new Router({
	routes: [
		{
			path: '/adminregist',
			component: adminregist
		},
		{
			path: '/adminlogin',
			component: adminlogin
		},
		{
			path: '/adminupdate',
			component: adminupdate
		},
		// 学生界面
		{
			path: '/yonghu',
			component: yonghu
		},
		{
			path: '/',
			component: uselogin,
			// meta:{
			// 	needlogin:true
			// }
		},
		{
			path: '/userregist',
			component: userregist
		},
		{
			path: '/stuborrow',
			component: stuborrow
		},
		{
			path: '/queryuser',
			component: queryuser
		},
		{
			path: '/returnuser',
			component: returnuser
		},
		{
			path: '/userupdate',
			component: userupdate
		},
		// 图书管理
		{
			path: '/shouye',
			name:'/shouye',
			component: shouye
		},
		{
			path: '/addbook',
			component: addbook
		},
		{
			path: '/deletebook',
			component: deletebook
		},
		{
			path: '/querybook',
			component: querybook
		},
		{
			path: '/updatebook',
			component: updatebook
		},
		// 借阅管理

		{
			path: '/addborrow',
			component: addborrow
		},
		{
			path: '/delborrow',
			component: delborrow
		},
		{
			path: '/queryborrow',
			component: queryborrow
		},
		{
			path: '/updateborrow',
			component: updateborrow
		},
		// 学生信息管理
		{
			path: '/addstu',
			component: addstu
		},
		{
			path: '/delstu',
			component: delstu
		},
		{
			path: '/querystu',
			component: querystu
		},
		{
			path: '/updatestu',
			component: updatestu
		},
		{
			path: '/querystupwd',
			component: querystupwd
		},
		{
			path: '/delstupwd',
			component: delstupwd
		},
		// 管理员管理界面
		{
			path: '/addgly',
			component: addgly
		},
		{
			path: '/deletegly',
			component: deletegly
		},
		{
			path: '/querygly',
			component: querygly
		},
		{
			path: '/updategly',
			component: updategly
		},
	]
})
export default router