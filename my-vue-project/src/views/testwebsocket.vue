<template>
  <div>
  <div id="main" style="width:500px;height:300px;"></div>
  <!-- 请输入问题<el-input v-model="mes"></el-input>
  <el-button @click="submit">提交</el-button>
  {{answer}} -->

  </div>
</template>

<script lang="ts" setup>  
import { ref,onMounted } from 'vue'  
import http from "../http";  
import * as echarts from 'echarts';

// const mes = ref('')
// const answer = ref('')
// const source = ref('')
const orderlist = ref([1001,1002,1003])
const countlist = ref([100,200,50])
const websocket =ref()
const userid = route.query.id

const initwebsocket=()=>{
  const room = "user:"+userid.value
    websocket.value = new WebSocket("ws://localhost:8000/room/"+room+"/");
    websocket.value.onopen =  (event)=>{
        alert('连接成功')
    }
    websocket.value.onmessage =  (event)=>{
        console.log(JSON.parse(event.data))
        countlist.value = JSON.parse(event.data) 
        initecharts()
    }
                
}
const initecharts=()=>{
    var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
  xAxis: {
    type: 'category',
    data:orderlist.value
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: countlist.value,
      type: 'line'
    }
  ]
};

option && myChart.setOption(option);
}

onMounted(() => { 
    initwebsocket()
    initecharts() 
}) 

// const submit=()=>{
//     source.value = new EventSource("http://localhost:8000/sse/?ask="+mes.value);
//     //接收消息
//     source.value.onmessage = (event=> {
//         answer.value = answer.value + event.data
//         var totallist = JSON.parse(event.data)
       
//         orderlist.value = totallist.orderlist
//         countlist.value = totallist.countlist
//         initecharts() 
//     });

//     source.value.onerror = (error=> {
//         console.error('EventSource failed:', error);
//         source.value.close();
//         source.value = null;
//     });
// }
</script>

<style>

</style>