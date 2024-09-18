<template>
  <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">
        <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-sub-menu :index="index"  v-for="(i,index) in menulist" :key="index">
          <template #title>
            <el-icon><location /></el-icon>
            <span>{{i.name}}</span>
          </template>
        
            <el-menu-item index="1-1" v-for="j,ind in i.son" :key="ind">
            <router-link :to="{'path':j.url}">{{j.name}}</router-link>
            </el-menu-item>
        </el-sub-menu>
       
      </el-menu>
        
        </el-aside>
        <el-main>
        
        <router-view/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script lang="ts" setup>
import {ref,onMounted}  from 'vue'
const menulist = ref([])

onMounted(()=>{
    menulist.value = JSON.parse(localStorage.getItem('menulist'))
})
</script>