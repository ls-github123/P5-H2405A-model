<template>
<div>
  名称<el-input v-model="sname" placeholder="Please input" />
  <el-button @click="search">搜索</el-button>
  <el-table :data="tableData" style="width: 100%">
    
    <el-table-column prop="name" label="Name" width="120" />
   
    <el-table-column fixed="right" label="Operations" width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="handleClick"
          >Detail</el-button
        >
        <el-button link type="primary" size="small" @click='show(scope.row.id)'>资源配制</el-button>
      </template>
    </el-table-column>
  </el-table>

   <el-pagination
      v-model:currentPage="currentPage"
      v-model:page-size="pageSize"
      :page-sizes="[1, 2, 3, 4]"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />


<el-dialog
    v-model="dialogVisible"
    title="Tips"
    width="70%"
    :before-close="handleClose"
  >
    
    <el-transfer v-model="value" :data="data" />
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="setresource"
          >Confirm</el-button
        >
      </span>
    </template>
  </el-dialog>
</div>
</template>

<script lang="ts" setup>
import {ref,onMounted}  from 'vue'
import http from '../../http'
const dialogVisible = ref(false)
const handleClick = () => {
  console.log('click')
}
//搜索用的
const sname = ref('')
//分页
const currentPage = ref(1)
const pageSize = ref(2)
const total = ref(10)

const handleSizeChange=(size)=>{
  pageSize.value =size
  getreslist()
}

const search=()=>{
  getreslist()
}

const handleCurrentChange=(page)=>{
  
  currentPage.value = page
  getreslist()
}
//定义roleid
const roleid = ref(0)

interface Option {
  key: number
  label: string
}


const data = ref([])
const value = ref([])


const tableData = ref([])

const show=(rid)=>{
    roleid.value = rid
    http.get('roleresource/?roleid='+rid).then(res=>{
      data.value = res.data.reslist
      value.value = res.data.values
       //发起axios请求获取数据
      dialogVisible.value= true
    })
   
}

const getreslist = ()=>{
  http.get('roles/?sname='+sname.value+"&page_size="+pageSize.value+"&page="+currentPage.value).then(res=>{
    tableData.value = res.data.rlist
    total.value = res.data.total
  })
}

//角色配制资源
const setresource = ()=>{
  http.post('roleresource/',{"roleid":roleid.value,'values':value.value}).then(res=>{
    if(res.data.code == 200){
      alert("添加成功")
      dialogVisible.value= false
      roleid.value=0
    }else{
      alert('添加失败')
    }
  })
}
onMounted(()=>{
    getreslist()
})
</script>
