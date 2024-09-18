<template>
<div>
  
</div>
</template>

<script lang="ts" setup>
import {ref,onMounted}  from 'vue'
import http from '../../http'

const login=()=>{
    http.post('login/').then(res=>{
        let data = res.data.menulist
        localStorage.setItem('menulist',JSON.stringify(data))
        localStorage.setItem('token',res.data.token)
        localStorage.setItem('mpromition',JSON.stringify(res.data.mpromition))
        window.location.href="http://localhost:5173/admin"
    })
}
onMounted(()=>{
    login()
})
</script>