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
          <span>删除成功</span>
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
          <el-table
            :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
            style="width: 100%">
            <el-table-column
              label="课程号"
              prop="kh">
            </el-table-column>
            <el-table-column
              label="课程名"
              prop="km">
            </el-table-column>
            <el-table-column
              label="教师名"
              prop="jsm">
            </el-table-column>
            <el-table-column
              label="上课时间"
              prop="sksj">
            </el-table-column>
            <el-table-column
              label="学分"
              prop="xf">
            </el-table-column>
            <el-table-column
              label="学时"
              prop="xs">
            </el-table-column>
            <el-table-column
              align="right">
              <template slot="header" slot-scope="scope">
                <el-input
                  v-model="search"
                  size="mini"
                  placeholder="输入关键字搜索"/>
              </template>
              <template slot-scope="scope">
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)">Delete
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "my_schedule",
    data() {
      return {
        tableData: [],
        search: '',
        name: '',
        stu_number: '',
        centerDialogVisible: false
      }
    },
    methods: {
      handleDelete(index, row) {
        let that = this
        $.ajax({
          url: "/del_course/",
          dataType: "json",
          data: {
            kh: row.kh,
            jsm: row.jsm
          },
          success: function (data) {
            if (data['res'] == 'OK') {
              that.centerDialogVisible = true
            }
          }
        })
      }
    },
    mounted() {
      let that = this;
      this.name = this.COMMON.name
      this.stu_number = this.COMMON.stu_number
      $.ajax({
        url: "/my_schedule/",
        dataType: "json",
        data: {
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
