<template>
  <div class="common-layout">
    <el-container>
      <!-- 左侧边栏 -->
      <el-aside width="200px" class="sidebar">
        <el-button @click="newConversation">新建会话</el-button>
        <el-input v-model="input" placeholder="搜索会话" style="margin-top: 16px; width: 100%;" />
        <ul class="conversation-list" style="margin-top: 16px;">
          <li v-for="(item, index) in conversations" :key="index">{{ item }}33333</li>
        </ul>
      </el-aside>
      <!-- 主要内容区域 -->
      <el-main class="main-content">
        <ul class="message-list">
          <li v-for="(msg, index) in messages" :key="index">
            {{ msg['qustion'] }} </br>
            {{ msg['answer'] }}
          </li>
        </ul>
        <el-form>
          <el-input
            v-model="textarea"
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 4}"
            placeholder="请输入消息"
            style="margin-bottom: 8px;"
          ></el-input>
          <el-button type="primary" @click="submitMessage">发送</el-button>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import http from '../../http'

// 示例数据
const conversations = ['会话1', '会话2'];
const messages = ref([]);

const textarea = ref('');
const input = ref('');
const cateid=ref('')
const catename=ref('')

const newConversation=()=>{
  // 新建会话逻辑
  http.post('cateManager/',{"userid":1}).then(res=>{
        if(res.data.code == 200){
            alert("添加成功")
            cateid.value = res.data.cateid
        }
    })
}

const submitMessage=()=> {
  // 提交消息逻辑
  http.post('newsManager/',{"userid":1,'cateid':cateid.value,'message':textarea.value}).then(res=>{
        if(res.data.code == 200){
            alert("添加成功")
            // var message = {"qustion":textarea.value,'answer':res.data.mes}
            messages.value.push({"qustion":textarea.value,'answer':res.data.mes})
            if(res.data.cname){
                catename.value= res.data.cname
            }
        }
    })
}
</script>

<style scoped>
.common-layout {
  height: 100%;
  background-color: #ebeef2;
}

.sidebar {
  background-color: #efe7e7;
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.main-content {
  padding: 16px;
  background-color: #dcd7d7;
  height: calc(100vh - 32px);
  overflow-y: auto;
}

.conversation-list,
.message-list {
  list-style-type: none;
  padding-left: 0;
}

.conversation-list li,
.message-list li {
  padding: 8px;
  border-bottom: 1px solid red;
  color:rgb(20, 7, 7);
}

.conversation-list li:last-child,
.message-list li:last-child {
  border-bottom: none;
}
</style>