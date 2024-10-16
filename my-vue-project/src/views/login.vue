<template>

  <ul>
  <li v-for="i in menulist"> {{i.label}}
        <ul>
    <li v-for="s in i.children"> 
    <a :href="s.url"> {{s.label}}</a>
    
    </li>
    </ul>
  </li>
  </ul>
</template>

<script lang="ts" setup>
import { onMounted,ref } from 'vue'
import { useRoute } from 'vue-router'
import http from "../http";
const menulist = ref([])

const login=()=>{
    http.post('login/',{"name":'zs',"pwd":'234'}).then(res=>{
        menulist.value = res.data.menulist
        localStorage.setItem("userid",res.data.userid)
        localStorage.setItem("token",res.data.token)
        localStorage.setItem("menulist",JSON.stringify(res.data.menulist))
        localStorage.setItem("pomitionlist",JSON.stringify(res.data.pomitionlist))
        
    })
}

onMounted(()=>{
   login()
})
</script>

<style>

</style>