### 1.动态表单

~~~vue
<template>
  <div>
    <div v-for="(i,index) in list" :key='index'>
    <div v-for="(j,ind) in i" :key='ind'>
       <el-input v-model="values[index]" v-if="j['name'] == 'title'"/>
    <el-input v-model="vvalues[index]" v-if="j['name'] == 'value'"/>
    </div>
    
    </div>
    <el-button @click="add">+</el-button>
    <el-button @click="submit">提交</el-button>
  </div>
</template>

<script>
export default {
    data(){
        return{
            values:[],
            typevalues:[],
            vvalues:[],
            list:[[{"name":"title"},{"name":"value"}]],
            number:1
        }
    },
    methods: {
        add(){
            this.number++
            this.list.push([{"name":"title"},{"name":"value"}])
        },
        submit(){
            var valueslist=[]
            for(var i=0;i<this.number;i++){
                var vv = this.vvalues[i]
                if (vv !=""){
                    vv = JSON.stringify(vv)
                }
                valueslist.push({"title":this.values[i],"values":vv})
            }
            var data = {"wid":this.$route.query.id,"params":JSON.stringify(valueslist)}
          
            this.axios.post("updateparams",data).then(res=>{

            })
        }
    },
}
</script>

<style>

</style>
~~~

### 2.动态工作流

~~~
OA系统中
我要请假-》姓名，开始时间，结束时间，事由，类型（1.产假 2事假）
财务报销-》姓名，出差地点，天数，费用，发票上传


管理员登录
创建工作流-》名称 字段


~~~

<img src="../images/20.png">

#### 数据库字典

workflow(工作流表)

<table>
  <tr><td>字段名</td><td>类型</td><td>中文名</td><td>描述</td></tr>
  <tr><td>name</td><td>varchar(30)</td><td>名称</td><td>唯一约束</td></tr>
  <tr><td>params</td><td>text</td><td>字段属性</td><td>序列化</td></tr>
  <tr><td>status</td><td>int</td><td>状态</td><td>1启用 2关闭</td></tr>
</table>

work_roles(工作流角色表)

<table>
  <tr><td>字段名</td><td>类型</td><td>中文名</td><td>描述</td></tr>
  <tr><td>workid</td><td>int</td><td>工作流id</td><td></td></tr>
  <tr><td>roles_id</td><td>int</td><td>角色id</td><td></td></tr>
</table>

user_work（用户工作流）

<table>
  <tr><td>字段名</td><td>类型</td><td>中文名</td><td>描述</td></tr>
  <tr><td>userid</td><td>int</td><td>提交人</td><td></td></tr>
  <tr><td>workid</td><td>int</td><td>工作流id</td><td></td></tr>
  <tr><td>title</td><td>varchar(255)</td><td>标题</td><td></td></tr>
  <tr><td>params</td><td>text</td><td>字段属性</td><td>序列化</td></tr>
  <tr><td>status</td><td>int</td><td>状态</td><td>1新建 2审批中 3结束</td></tr>
  <tr><td>nextuserid</td><td>int</td><td>下一审批人</td><td></td></tr>
</table>

代码

~~~vue
<template>
  <div>
<el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="基本信息" name="first">
    <el-input  v-model="form.proname"/>
    <el-input  v-model="form.username"/>
    <el-input  v-model="form.url"/>

    <el-button @click="save">保存</el-button>
    </el-tab-pane>
    <el-tab-pane label="全局参数" name="second">
    <div>
  <el-button @click="add">+</el-button>
  </div>
  <div v-for="(i,index) in reslist" :key="index">
  <el-row>
  <el-col :span="6"><div class="grid-content bg-purple">
  <el-input v-model="v1[index]" />
  </div></el-col>
  <el-col :span="6"><div class="grid-content bg-purple-light">
   <el-input v-model="v2[index]" />
  </div></el-col>
  <el-col :span="6"><div class="grid-content bg-purple">
   <el-input v-model="v3[index]" />
  </div></el-col>
  <el-col :span="6"><div class="grid-content bg-purple-light">
   <el-button @click="del(index)">删除</el-button>
  </div></el-col>
</el-row>
  </div>
  <div>
   <el-button @click="submit">提交</el-button>
  </div>


展示信息
<div v-for="(i,index) in showreslist" :key="index">
<div v-if="i.value=='input'">
{{i.key}} <el-input v-model="valueform[i.key]"></el-input>
</div>

<div v-if="i.value=='select'">
{{i.key}} 
<select v-model="valueform[i.key]">
<option v-for="k,v in i.descip" :value="v" :key="k">{{k}}</option>

</select>
</div>

<el-button @click='getvalue'>提交</el-button>
</div>
  
    </el-tab-pane>
    <el-tab-pane label="头部" name="third">角色管理</el-tab-pane>
   
  </el-tabs>



  
  </div>
</template>

<script>
export default {
    data(){
        return{
            form:{'params':'','headers':''},
            v1:[],
            v2:[],
            v3:[],
            reslist:[{}],
            activeName: 'first',
            showreslist:[],
            valueform:[],
        }
    },
    methods: {
        add(){
            this.reslist.push({})
        },
        submit(){
            var rlist=[]
            var len= this.v1.length
            for(var i=0;i<len;i++){
                var descip = ''
                if(this.v3[i]){
                    descip = JSON.parse(this.v3[i])
                }
                
                rlist.push({"key":this.v1[i],'value':this.v2[i],'descip':descip})
            }
           
            var rrlist = JSON.stringify(rlist)
            this.form.params = rrlist

            this.showreslist = JSON.parse(rrlist)
           

        },
        del(index){
            this.reslist.splice(index,1)
            this.v1.splice(index,1)
            this.v2.splice(index,1)
            this.v3.splice(index,1)
        },
        save(){
            this.axios.post("",this.form).then(res=>{})
        },
        getvalue(){
            console.log(this.valueform)
        }
    },

}
</script>

<style>

</style>
~~~

