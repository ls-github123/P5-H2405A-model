<template>
  <div>
  <el-button @click="myorder">我的订单</el-button>
  <ul>
  <li v-for="i in orderlist">
  {{i.id}}{{i.money}}
  <ul>
    <li v-for="j in i.detail">
    {{j.id}}
     {{j.name}}
    <p v-if="i.pay_status==2 & j.status==1"><el-button>评价</el-button></p>
    <p v-if="j.status==2">已评论</p>
    <p v-else></p>
    </li>
  </ul>
  </li>
  </ul>
  <div v-show="show">
  <a :href="ddurl">钉钉</a>
  </div>

  <div>
  <el-upload
    class="avatar-uploader"
    :before-upload="upload"
  >
   <el-icon  class="avatar-uploader-icon">上传</el-icon>
  </el-upload>

  </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import http from '../http'

const orderlist=ref([])
const show = ref(false)
const ddurl = ref('')

const upload=(file)=>{
  const fd = new FormData()
  fd.append("file",file)
  http.post('test/',fd).then(res=>{

  })
}
const myorder=()=>{
    var userid = localStorage.getItem('userid')
    if(userid){
        //获取订单列表
        orderlist.value=[{"id":1001,'money':500,"pay_status":2,"detail":[{"id":1,'name':'python','status':1}]},
        {"id":1002,'money':300,"pay_status":2,"detail":[{"id":1,'name':'python','status':2}]}]
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