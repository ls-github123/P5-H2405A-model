<template>  
<div>
<el-upload :before-upload="upload">
<el-icon  class="avatar-uploader-icon">上传</el-icon>
</el-upload>
</div>
 
</template>  
  
<script lang="ts" setup>  
// import { reactive, ref, onMounted } from 'vue'  
import http from "../http"; 
const upload = (file)=>{
    alert("into")
    const fdata = new FormData()
    fdata.append('file',file)
    console.log(fdata)
    http.post('upload/',fdata).then(res=>{
        alert("success")
    })

    return false;
}
</script>