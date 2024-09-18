<template>
<div>
  资源名称<el-input v-model="resform.name"></el-input>
  资源地址<el-input v-model="resform.url"></el-input>
  <select v-model="resform.pid">
    <option value="0">顶级菜单</option>
    <option :value="i.id" v-for="(i,index) in reslist" :key="index">{{i.name}}</option>
  </select>
  <el-button @click="addres">提交</el-button>
<el-button @click="add">增加一条</el-button>
</div>
</template>

<script lang="ts" setup>
import {ref,onMounted} from 'vue'
import http from '../../http'
import {addMes} from '../../http'

const resform=ref({"name":'','url':''})
const reslist = ref([])

const addres=()=>{
    //axios请求resform
    http.post('resourse/',resform.value).then(res=>{
        if(res.data.code == 200){
            alert("添加成功")
        }
    })

}

const getreslist=()=>{
    //axios请求resform
    // http.get('resourse/').then(res=>{
    //     if(res.data.code == 200){
    //         reslist.value=res.data.list
    //     }
    // })
    reslist.value=[{"id":1,'name':'权限管理'},{"id":2,'name':'订单管理'}]
}

const add=()=>{
    reslist.value.push({"id":3,'name':'ssdsd'})
}

const getmes=()=>{
    const mes = addMes()
    alert(mes['code'])
}

onMounted(()=>{
    getreslist()
    getmes()
})

</script>
