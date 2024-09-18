<template>
<div>

 <el-row>
    <el-col :span="10"><div class="grid-content ep-bg-purple-dark" />
    <ul>
    <li v-for="i in mlist" :key="i.id">
    <el-button @click="start(i.id)">{{i.name}}</el-button>
    
    </li>
   
    </ul>
    </el-col>
  <el-col :span="14">
  <div>
  <ul>
  <li v-for="i in askmes">{{i}}</li>

  </ul>
  </div>
  <div class="grid-content ep-bg-purple-dark" />
  名称<el-input v-model="message" placeholder="Please input" />
  <el-button @click="submit">提交</el-button>
  </el-col>
 </el-row>

  
  
</div>
</template>

<script lang="ts" setup>
import {ref,onMounted}  from 'vue'
import roomVue from '../../../../consult-patient-h5-video-main/src/views/Order/room.vue';


//搜索用的
const message = ref('')
const askmes = ref([])
const doctorid = ref(1)
const socket = ref(null)
const asksocket = ref(null)
const clickuserid = ref('')
const mlist=ref([{"id":1,"name":"张三"},{"id":2,"name":"李四"}])
const scoketlist = ref([])
const flag = ref(true)


const submit=()=>{
  alert('23234234')
  asksocket.value.send(JSON.stringify({"message":message.value,"from":JSON.stringify(clickuserid.value)+JSON.stringify(doctorid.value)}))
}



//点击用户
const start=(userid)=>{
    askmes.value=[]
    clickuserid.value=userid
    //获取聊天记录
    var mes = localStorage.getItem(clickuserid.value)
    if(mes){
        mes = JSON.parse(mes)
        askmes.value = mes
    }
    var room = JSON.stringify(clickuserid.value)+JSON.stringify(doctorid.value)
        
    scoketlist.value.forEach(res=>{
        if(res['id'] == room){
            flag.value=false
            asksocket.value = res['conn']
        }
    })
    if(flag.value == true){
        asksocket.value = new WebSocket("ws://localhost:8000/room/"+clickuserid.value+doctorid.value+"/");
        scoketlist.value.push({"id":room,"conn":asksocket.value})
    }
    
    // 当客户端和服务端刚创建好连接(self.accept)之后，自动触发.
    asksocket.value.onopen =  (event)=>{
        console.log("连接成功")
    }

    // 回调函数，客户端接收服务端消息
    asksocket.value.onmessage =  (event)=>{
        alert('33333')
        //获取用户发送的消息
        var data  = JSON.parse(event.data)
        console.log(data)
        //存入localstorage
        //历史消息列表
        var mes = localStorage.getItem(clickuserid.value)
        console.log(mes)
        if(mes){
            alert('1')
            mes = JSON.parse(mes)
            mes.push(data)
            localStorage.setItem(clickuserid.value,JSON.stringify(mes))
        }else{
            alert('2')
            var mesdata = []
            mesdata.push(data)
            localStorage.setItem(clickuserid.value,JSON.stringify(mesdata))
        }
        //把新的消息加入列表
        askmes.value.push(data)
        
    }

}

const initwesockt=()=>{
    socket.value = new WebSocket("ws://localhost:8000/room/doctor"+doctorid.value+"/");

    // 当客户端和服务端刚创建好连接(self.accept)之后，自动触发.
    socket.value.onopen =  (event)=>{
        console.log("连接成功")
    }

    // 回调函数，客户端接收服务端消息
    socket.value.onmessage =  (event)=>{
        
        console.log(event)
        var data  = JSON.parse(event.data)
        //data {"name":'zs',"id":1}
        mlist.value.push(data)
    }

    // // 当断开连接时，触发该函数
    // this.socket.onclose =function (event){
    // let tag = document.createElement("div");
    // tag.innerText = "[连接断开]";
    // document.getElementById("message").appendChild(tag);
    // }


}

onMounted(()=>{
    initwesockt()

})
</script>
