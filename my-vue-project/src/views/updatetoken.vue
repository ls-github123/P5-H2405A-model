<template>
  
</template>

<script lang="ts" setup>
import { onMounted,ref } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()

const token = ref('')
const userid = ref('')

onMounted(()=>{
   
    token.value = route.query.token
    userid.value = route.query.userid
    localStorage.setItem('userid',userid.value)
    localStorage.setItem('token',token.value)
    // window.location.href='http://localhost:5173/userinfo'
})
</script>

<style>

</style>