<template>
  <div>
  <el-upload
    class="avatar-uploader"
    :show-file-list="false"
    :before-upload="beforeAvatarUpload"
  >
   
    <el-icon  class="avatar-uploader-icon">上传</el-icon>
  </el-upload>
  
  </div>
</template>

<script lang="ts" setup>  
// import { ref,onMounted } from 'vue'  
import http from "../http";  
const beforeAvatarUpload = (file)=>{
    const formdata = new FormData()
    formdata.append('file',file)
    http.post('fileUpload/',formdata).then(res=>{
        alert('上传成功')
    })
    return false;
}
</script>

<style>

</style>