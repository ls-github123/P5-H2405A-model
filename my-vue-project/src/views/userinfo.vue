<template>
  <div>
  <el-button @click="myorder">我的订单</el-button>
  <ul>
  <li v-for="i in orderlist">
  {{i.id}}{{i.money}}
  </li>
  </ul>
  <div v-show="show">
  <a :href="ddurl">钉钉</a>
  </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import http from '../http'

const orderlist=ref([])
const show = ref(false)
const ddurl = ref('')
const myorder=()=>{
    var userid = localStorage.getItem('userid')
    if(userid){
        //获取订单列表
        orderlist.value=[{"id":1001,'money':500,"detail":[{"id":1,'name':'python'}]}]
    }else{
        //获取dingdingurl
        http.get('ddurl/').then(res=>{
            ddurl.value = res.data.url
            show.value=true
        })
        
    }
}

</script>

<style>

</style>