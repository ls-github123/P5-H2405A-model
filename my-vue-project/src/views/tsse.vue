<template>
  <div>
  请输入问题<el-input v-model="mes"></el-input>
  <el-button @click="submit">提交</el-button>
  {{answer}}
  </div>
</template>

<script lang="ts" setup>  
import { ref } from 'vue'  
import http from "../http";  

const mes = ref('')
const answer = ref('')
const source = ref('')

const submit=()=>{
    source.value = new EventSource("http://localhost:8000/sse/?ask="+mes.value);

    //接收消息
    source.value.onmessage = (event=> {
        answer.value = answer.value + event.data
    });

    source.value.onerror = (error=> {
        console.error('EventSource failed:', error);
        source.value.close();
        source.value = null;
    });
}
</script>

<style>

</style>