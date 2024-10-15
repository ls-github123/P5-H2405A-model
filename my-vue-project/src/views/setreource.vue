
<template>
<div>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column fixed prop="date" label="Date" width="150" />
    <el-table-column prop="name" label="Name" width="120" />
    <el-table-column prop="state" label="State" width="120" />
    <el-table-column prop="city" label="City" width="120" />
    <el-table-column prop="address" label="Address" width="600" />
    <el-table-column prop="zip" label="Zip" width="120" />
    <el-table-column fixed="right" label="Operations" min-width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="handleClick(scope.row.id)">
          资源配制
        </el-button>
        <el-button link type="primary" size="small">Edit</el-button>
      </template>
    </el-table-column>
  </el-table>

 <el-dialog
    v-model="dialogVisible"
    title="Tips"
    width="900"
  >
    
<el-transfer v-model="value" :data="data" />

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="submit">
          Confirm
        </el-button>
      </div>
    </template>
  </el-dialog>

</div>
</template>

<script lang="ts" setup>
import { ref,onMounted } from 'vue'  
import http from "../http"; 
const dialogVisible=ref(false)
const userid = ref('')
const data = ref([{"key":2,'label':'考试管理'},{'key':3,'label':'查看积分'},{'key':5,'label':'查看积分'}])
const value = ref([])
const handleClick = (id) => {
    userid.value = id
    //axios去获取所有的资源,获取用户已经选中的资源id
    // data.value = res.data.reslist
    // value.value = res.data.checked
    dialogVisible.value = true
}

const submit=()=>{
    http.post('resource/',{"userid":userid.value,'res':value.value}).then(res=>{
            dialogVisible.value = false
    })
}

onMounted(()=>{

})

const tableData = [
  {
    id:1,
    date: '2016-05-03',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Home',
  },
  {
    id:2,
    date: '2016-05-02',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Office',
  },
  
]
</script>
