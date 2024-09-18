import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../views/HelloWorld.vue'


const routes = [{
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    }
    // 其他路由...  
]

const router = createRouter({
    history: createWebHistory(""),
    routes
})



export default router