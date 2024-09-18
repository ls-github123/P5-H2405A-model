import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import router from './router' // 导入路由器实例 

//element ui配制
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

app.use(router) // 使用路由器  


app.use(ElementPlus)
app.mount('#app')