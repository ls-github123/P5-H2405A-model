<template>  
  <div id="app">  
    <nav>  
      <!-- <router-link to="/">Home</router-link> |  
      <router-link to="/about">About</router-link>   -->
    </nav>  
    <router-view/> <!-- 这里会显示当前路由对应的组件 -->  
  </div>  
</template>  
  
<script>  
export default {  
  name: 'App'  
}  
</script>