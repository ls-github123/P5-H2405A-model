import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../views/HelloWorld.vue'
import tsse from '../views/tsse.vue'
import echartstest from '../views/echartstest.vue'
import rag from '../views/rag.vue'
import userinfo from '../views/userinfo.vue'
import updatetoken from '../views/updatetoken.vue'


const routes = [{
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



export default router