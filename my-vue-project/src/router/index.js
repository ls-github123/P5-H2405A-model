import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../views/HelloWorld.vue'
import tsse from '../views/tsse.vue'
import echartstest from '../views/echartstest.vue'
import rag from '../views/rag.vue'
import userinfo from '../views/userinfo.vue'
import updatetoken from '../views/updatetoken.vue'
import fileupload from '../views/fileupload.vue'
import testsse from '../views/testsse.vue'
import fupload from '../views/fupload.vue'
import setreource from '../views/setreource.vue'
import login from '../views/login.vue'

const routes = [{
        path: '/login',
        name: 'login',
        component: login
    }, {
        path: '/setreource',
        name: 'setreource',
        component: setreource
    }, {
        path: '/fupload',
        name: 'fupload',
        component: fupload
    }, {
        path: '/testsse',
        name: 'testsse',
        component: testsse
    }, {
        path: '/fileupload',
        name: 'fileupload',
        component: fileupload
    }, {
        path: '/updatetoken',
        name: 'updatetoken',
        component: updatetoken
    }, {
        path: '/userinfo',
        name: 'userinfo',
        component: userinfo
    }, {
        path: '/rag',
        name: 'rag',
        component: rag
    }, {
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    }, {
        path: '/tsse',
        name: 'tsse',
        component: tsse
    }, {
        path: '/etest',
        name: 'echartstest',
        component: echartstest
    },
    // 其他路由...  
]

const router = createRouter({
    history: createWebHistory(""),
    routes
})

router.beforeEach((to, from, next) => {
    //定义一个白名单
    var reslist = ['/login', '/register']
    if (reslist.indexOf(to.path) == -1) {
        //获取token
        var token = localStorage.getItem('token')
            //验证token
        if (token) {
            //查看权限列表是否存在
            var mlist = localStorage.getItem('pomitionlist')
            if (mlist) {
                mlist = JSON.parse(mlist)
                if (mlist.indexOf(to.path) == -1) {
                    alert("无权操作")
                    return false;
                } else {
                    next()
                }
            } else {
                alert("没获取到请登录后面操作")
                next({ "name": "login" })
            }

        } else {
            alert("请登录后面操作")
            next({ "name": "login" })
        }



        // var token = localStorage.getItem('token')
        // if (token) {
        //     //验证是否在权限列表中
        //     var menulist = localStorage.getItem('mpromition')
        //     var mlist = JSON.parse(menulist)
        //     if (mlist.indexOf(to.path) >= 0) {
        //         next()
        //     } else {
        //         alert("无权访问此页面")
        //         next({ "name": 'Login' })
        //     }
        // } else {
        //     next({ "name": 'Login' })
        // }
    }
    next()
})


export default router