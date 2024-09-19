<template>  
  <div class="form-container">  
    <el-form  
      :label-position="labelPosition"  
      label-width="100px"  
      :model="formLabelAlign"  
      class="form-style"  
    >  
      <el-form-item label="Name">  
        <el-input v-model="formLabelAlign.askmes" placeholder="请输入名称" />  
      </el-form-item>  
  
      <el-form-item>  
        <el-button type="primary" @click="onSubmit">提交</el-button>  
        <el-button>取消</el-button>  
      </el-form-item>  
  
      <div class="message-container">{{ mes }}</div>  
    </el-form>  
  </div>  
</template>  
  
<script lang="ts" setup>  
import { reactive, ref, onMounted } from 'vue'  
import http from "../http";  
  
const labelPosition = ref('left')  
const mes = ref("")  
  
const formLabelAlign = reactive({  
  name: '',  
})  
  
  
const onSubmit = () => {  
  http.post('ask/', formLabelAlign).then(res => {  
    // 可以添加一些处理响应的逻辑  
    console.log(res)  
    mes.value = res.data.mes  
  })  
}  
  
// onMounted(() => {  
//   test()  
// })  
</script>  
  
<style scoped>  
.form-container {  
  padding: 20px;  
  border: 1px solid #ccc;  
  border-radius: 8px;  
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);  
  max-width: 500px;  
  margin: auto;  
}  
  
.form-style {  
  margin-bottom: 20px;  
}  
  
.message-container {  
  color: #666;  
  font-size: 14px;  
  margin-top: 10px;  
}  
  
.el-form-item__label {  
  font-weight: bold;  
}  
  
.el-input
{  
  width: 100%; /* 让输入框和按钮充满表单项的空间 */  
}  
  
.el-button + .el-button {  
  margin-left: 10px; /* 给按钮之间添加一些间距 */  
}  
</style>