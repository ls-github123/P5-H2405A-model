<template>
  <div class="common-layout">
    <el-container>
      <!-- 左侧边栏 -->
      <el-aside width="200px" class="sidebar">
        <el-button @click="newConversation">新建会话</el-button>
        <el-input v-model="sname" placeholder="搜索会话" style="margin-top: 16px; width: 100%;" />
        <el-button @click="search">搜索</el-button>
        <ul class="conversation-list" style="margin-top: 16px;">
          <li v-for="(item, index) in conversations" :key="index">
          <el-button @click="getask(item.id)">{{item['name']}} </el-button>
          </li>
        </ul>
        <el-button @click="showdialog">管理消息</el-button>
      </el-aside>
      <!-- 主要内容区域 -->
      <el-main class="main-content">
        <ul class="message-list" v-for="(i,index) in messages" :key="index">
          <li>{{i['ask']}}</li>
          <li>{{i['answer']}}</li>
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


    <el-dialog v-model="dialogTableVisible" width="800">
   <el-row>
    <el-col :span="12"><div class="grid-content ep-bg-purple" />一共有10条记录</el-col>
    <el-col :span="12"><div class="grid-content ep-bg-purple-light" />
    <el-input  placeholder="搜索会话" style="width: 100%;" />
       
    </el-col>
  </el-row>

   <el-table :data="tableData" style="width: 100%">
    <el-table-column type="selection" width="55" />
    <el-table-column label="Date" width="120">
      <template #default="scope">{{ scope.row.date }}</template>
    </el-table-column>
    <el-table-column property="name" label="Name" width="120" />
    <el-table-column
      property="address"
      label="use show-overflow-tooltip"
      width="240"
      show-overflow-tooltip
    />
    <el-table-column property="address" label="address" />
     <el-table-column fixed="right" label="Operations" min-width="120">
      <template #default>
        <el-button link type="primary" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <el-row>
    <el-col :span="12"><div class="grid-content ep-bg-purple" />
    <el-pagination background layout="prev, pager, next" :total="1000" />
    </el-col>
    <el-col :span="12"><div class="grid-content ep-bg-purple-light" />
    <el-button>删除所有</el-button>
    </el-col>
  </el-row>

   

  </el-dialog>

  </div>
</template>

<script lang="ts" setup>
import { ref,onMounted } from 'vue'
import http from '../http'

// 示例数据
const conversations = ref([])
const messages = ref([]);

const textarea = ref('');
const sname = ref('');
const cateid=ref('')
const catename=ref('')
const dialogTableVisible=ref(false)
const tableData=ref([
  {
    date: '2016-05-04',
    name: 'Aleyna Kutzner',
    address: 'Lohrbergstr. 86c, Süd Lilli, Saarland',
  },
  {
    date: '2016-05-03',
    name: 'Helen Jacobi',
    address: '760 A Street, South Frankfield, Illinois',
  }])

const newConversation=()=>{
  messages.value =[]
  textarea.value = ''
  // 新建会话逻辑
  http.post('cates/').then(res=>{
        if(res.data.code == 200){
            cateid.value = res.data.cateid
        }
    })
}

//获取每个分类下的对话，点击分类是调用
const getask=(cid)=>{
    http.get('questions/?cateid='+cid).then(res=>{
      messages.value=res.data.qlist
    })
}

//获取所有分类
const getcates=()=>{
   http.get('cates/').then(res=>{
      conversations.value=res.data.clist
    })
}

//定义一个搜索的方法
const search=()=>{
  http.get('cates/?sname='+sname.value).then(res=>{
      conversations.value=res.data.clist
  })
}

onMounted(()=>{
  newConversation()
  getcates()
})

const submitMessage=()=> {
  messages.value.push({"ask":textarea.value,'answer':''})
  // 提交消息逻辑
  http.post('questions/',{'cateid':cateid.value,'ask':textarea.value}).then(res=>{
        if(res.data.code == 200){
            var index = messages.value.length -1
            messages.value[index]['answer'] = res.data.answer
            // var message = {"qustion":textarea.value,'answer':res.data.mes}
            // messages.value.push({"qustion":textarea.value,'answer':res.data.mes})
            if(res.data.catename){
                catename.value= res.data.catename
                conversations.value.unshift({"id":cateid.value,'name':res.data.catename})
            }
        }
    })
}

//点击管理对话记录方法
const showdialog=()=>{
  dialogTableVisible.value=true
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