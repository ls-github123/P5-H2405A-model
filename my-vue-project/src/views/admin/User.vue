<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
      <!-- <router-link to="/user">用户列表</router-link>  <br>
     
      <router-link :to="{ name: 'UserEdit', params: { id: 123 }}">编辑用户</router-link>
      <br>
     
      <router-link :to="{ name: 'UserEdit', params: { id: 123 }}">添加用户</router-link> -->
      
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-sub-menu index="1">
          <template #title>
            <el-icon><location /></el-icon>
            <span>Navigator One</span>
          </template>
          <el-menu-item-group title="Group One">
            <el-menu-item>
            <router-link to="UserEdit">编辑用户</router-link> 
            </el-menu-item>
            <el-menu-item index="1-2">item one</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="Group Two">
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-4">
            <template #title>item four</template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="2">
          <el-icon><icon-menu /></el-icon>
          <span>Navigator Two</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <el-icon><document /></el-icon>
          <span>Navigator Three</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>Navigator Four</span>
        </el-menu-item>
      </el-menu>

      
      </el-aside>
      <el-main>
       <router-view></router-view>  
      </el-main>
    </el-container>
  </div>
</template>
