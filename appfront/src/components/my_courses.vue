<template>
  <div>
    <el-container style="height: 100vh; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: white">
        <el-menu :default-openeds="['1', '2']" router>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>学生信息</template>
            <el-menu-item-group>
              <el-menu-item index="1-1">姓名： {{name}}</el-menu-item>
              <el-menu-item index="1-2">学号： {{stu_number}}</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>常用功能</template>
            <el-menu-item-group>
              <el-menu-item index="/Course_information">课程信息</el-menu-item>
              <el-menu-item index="/departments_informations">院系信息</el-menu-item>
              <el-menu-item index="2-3">我的课程</el-menu-item>
              <el-menu-item index="2-4">教学评估</el-menu-item>
              <el-menu-item index="2-5">海外交流</el-menu-item>
              <el-menu-item index="2-6">学分抵充</el-menu-item>
              <el-menu-item index="2-7">试读警告</el-menu-item>
              <el-menu-item index="2-8">学分完成情况</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>

      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>安全退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span style="color: white">欢迎，{{name}}</span>
        </el-header>

        <el-main>
          <el-table :data="tableData">
            <el-table-column prop="xh" label="学号" width="100">
            </el-table-column>
            <el-table-column prop="kh" label="课程号" width="100">
            </el-table-column>
            <el-table-column prop="km" label="课程名" width="100">
            </el-table-column>
            <el-table-column prop="jsm" label="教师名" width="100">
            </el-table-column>
            <el-table-column prop="pscj" label="平时成绩" width="100">
            </el-table-column>
            <el-table-column prop="kscj" label="考试成绩" width="100">
            </el-table-column>
            <el-table-column prop="zpcj" label="总评成绩" width="100">
            </el-table-column>
            <el-table-column prop="xq" label="学期" width="120">
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "my_courses",
    data() {
      return {
        tableData: [],
        name: '',
        stu_number: ''
      }
    },
    mounted() {
      let that = this;
      this.name = this.COMMON.name
      this.stu_number = this.COMMON.stu_number
      $.ajax({
          url: "/my_courses/",
          dataType: "json",
          data:{
            xh: that.stu_number
          },
          success: function (data) {
            console.log(data[0]);
            that.tableData = data
          }
        })

    }
  }
</script>

<style scoped>
  .el-header {
    background-color: #307C91;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #307C91;
  }

  .row-aside {
    margin-top: 20px;
    font-size: 15px;
  }
</style>
