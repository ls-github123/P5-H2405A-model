<template>
  <div>
  <div id="main" style="width:600px;height:300px;"></div>
 {{errormes}}
  </div>
</template>

<script lang="ts" setup>  
import { ref,onMounted } from 'vue'  
// import http from "../http";  
import * as echarts from 'echarts';
const xlist = ref(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
const ylist = ref([120, 200, 150, 80, 70, 110, 130])
const errormes=ref('')
const source=ref('')

const initecharts = ()=>{
    var chartDom = document.getElementById('main');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
    xAxis: {
        type: 'category',
        data: xlist.value
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
        data: ylist.value,
        type: 'bar'
        }
    ]
    };

    option && myChart.setOption(option);
}

const getmes=()=>{
    //建立sse连接
    //获取数据,更新xlist和ylist和errormes
    // initecharts()
    source.value = new EventSource("http://localhost:8000/echartssse/");
    //接收消息
    source.value.onmessage = (event=> {
        var edata = JSON.parse(event.data)
        console.log(edata)
        xlist.value = edata.orderlist
        ylist.value = edata.numberlist
        errormes.value = edata.errormes
        
         initecharts()
    });
   

    // source.value.onerror = (error=> {
    //     console.error('EventSource failed:', error);
    //     source.value.close();
    //     source.value = null;
    // });
}

onMounted(()=>{
    getmes()
    
})

</script>

<style>

</style>