import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../views/HelloWorld.vue'
import tsse from '../views/tsse.vue'


const routes = [{
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    }, {
        path: '/tsse',
        name: 'tsse',
        component: tsse
    }
    // 其他路由...  
]

const router = createRouter({
    history: createWebHistory(""),
    routes
})



export default router