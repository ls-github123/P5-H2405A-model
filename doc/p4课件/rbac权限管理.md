权限管理

~~~
教学管理
    考试管理
    班级管理
    考核管理
学生管理
    查综合积分
    缴费
教务管理
    班级管理
    排课管理
    
~~~

1.acl基于用户的权限管理

~~~
用户表
id  name pasword
1    小明
2    张三
3    张老师

资源表
id  name    pid     url
1   教学管理   0
2   考试管理   1      /exam
3   考核管理   1      /aa
4   学生管理   0
5   查综合积分  4     /score


用户资源表
userid  resid
1         5
3         3

当小明登录后
学生管理 
    查综合积分
    
当张老师登录后
教学管理
  考核管理
  
~~~

![image-20241015090705949](Images/image-20241015090705949.png)

![image-20241015091028215](Images/image-20241015091028215.png)

![image-20241015091701045](Images/image-20241015091701045.png)

![image-20241015092911420](Images/image-20241015092911420.png)



2.rbac

  rbac0

rbac1

rbac2

Rbac3

3.abac

