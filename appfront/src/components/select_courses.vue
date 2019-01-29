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
              <el-menu-item index="/my_courses">我的历史课程</el-menu-item>
              <el-menu-item index="/select_courses">选课管理</el-menu-item>
              <el-menu-item index="/my_schedule">我的课表</el-menu-item>
              <el-menu-item index="2-6">学分抵充</el-menu-item>
              <el-menu-item index="2-7">试读警告</el-menu-item>
              <el-menu-item index="2-8">学分完成情况</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>

      </el-aside>

      <el-container>
        <el-dialog
          title="提示"
          :visible.sync="centerDialogVisible"
          width="30%"
          center>
          <span>选课成功，请查看课表</span>
          <span slot="footer" class="dialog-footer">
    <el-button @click="centerDialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="centerDialogVisible = false">确 定</el-button>
  </span>
        </el-dialog>
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
          <el-row class="xk">
            课程号:
            <el-input
              placeholder="请输入课程号"
              v-model="kh_1"
              clearable
              style="width: 250px">
            </el-input>
            &emsp;&emsp;教师号:
            <el-input
              placeholder="请输入教师号"
              v-model="gh_1"
              clearable
              style="width: 250px">
            </el-input>
          </el-row>
          <el-row class="xk">
            课程号:
            <el-input
              placeholder="请输入课程号"
              v-model="kh_2"
              clearable
              style="width: 250px">
            </el-input>
            &emsp;&emsp;教师号:
            <el-input
              placeholder="请输入教师号"
              v-model="gh_2"
              clearable
              style="width: 250px">
            </el-input>
          </el-row>
          <el-row class="xk">
            课程号:
            <el-input
              placeholder="请输入课程号"
              v-model="kh_3"
              clearable
              style="width: 250px">
            </el-input>
            &emsp;&emsp;教师号:
            <el-input
              placeholder="请输入教师号"
              v-model="gh_3"
              clearable
              style="width: 250px">
            </el-input>
          </el-row>
          <el-row class="xk">
            课程号:
            <el-input
              placeholder="请输入课程号"
              v-model="kh_4"
              clearable
              style="width: 250px">
            </el-input>
            &emsp;&emsp;教师号:
            <el-input
              placeholder="请输入教师号"
              v-model="gh_4"
              clearable
              style="width: 250px">
            </el-input>
          </el-row>
          <el-row>
            <el-button type="primary" plain class="confirm" @click="tijiao">确认选课</el-button>
          </el-row>
          <el-table :data="tableData">
            <el-table-column prop="kh" label="课程号" width="120">
            </el-table-column>
            <el-table-column prop="km" label="课程名" width="120">
            </el-table-column>
            <el-table-column prop="gh" label="教师号" width="120">
            </el-table-column>
            <el-table-column prop="jsm" label="教师名" width="120">
            </el-table-column>
            <el-table-column prop="sksj" label="上课时间" width="120">
            </el-table-column>
            <el-table-column prop="xf" label="学分" width="120">
            </el-table-column>
            <el-table-column prop="xs" label="学时" width="120">
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "select_courses",
    data() {
      return {
        tableData: [],
        name: '',
        stu_number: '',
        kh_1: '',
        gh_1: '',
        kh_2: '',
        gh_2: '',
        kh_3: '',
        gh_3: '',
        kh_4: '',
        gh_4: '',
        centerDialogVisible: false
      }
    },
    methods: {
      tijiao() {
        var suc = 'NO'
        let that = this
        if (that.kh_1 != '' && that.gh_1 != '') {
          $.ajax({
            url: '/add_course/',
            dataType: "json",
            data: {
              kh: that.kh_1,
              gh: that.gh_1,
              xh: that.COMMON.stu_number
            },
            success: function (data) {
              console.log("data['res']:", data['res'])
              if (data['res'] == 'OK') {
                that.centerDialogVisible = true
              }
            }
          })
        }
        if (that.kh_2 != '' && that.gh_2 != '') {
          $.ajax({
            url: '/add_course/',
            dataType: "json",
            data: {
              kh: that.kh_2,
              gh: that.gh_2,
              xh: that.COMMON.stu_number
            },
            success: function (data) {
              if (data['res'] == 'OK') {
                that.centerDialogVisible = true
              }
            }
          })
        }
        if (that.kh_3 != '' && that.gh_3 != '') {
          $.ajax({
            url: '/add_course/',
            dataType: "json",
            data: {
              kh: that.kh_3,
              gh: that.gh_3,
              xh: that.COMMON.stu_number
            },
            success: function (data) {
              if (data['res'] == 'OK') {
                that.centerDialogVisible = true
              }
            }
          })
        }
        if (that.kh_4 != '' && that.gh_4 != '') {
          $.ajax({
            url: '/add_course/',
            dataType: "json",
            data: {
              kh: that.kh_4,
              gh: that.gh_4,
              xh: that.COMMON.stu_number
            },
            success: function (data) {
              if (data['res'] == 'OK') {
                that.centerDialogVisible = true
              }
            }
          })
        }
      }
    },
    mounted() {
      let that = this;
      $.ajax({
        url: "/open_schedule/",
        dataType: "json",
        data: {},
        success: function (data) {
          that.tableData = data
        }
      })
      this.name = this.COMMON.name
      this.stu_number = this.COMMON.stu_number
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

  .xk {
    text-align: left;
    margin-top: 20px;
  }

  .confirm {
    margin-top: 30px;
    margin-bottom: 50px;
    float: left;
  }
</style>
