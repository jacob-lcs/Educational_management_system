<template>
  <div>
    <el-container style="height: 100vh; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: white">
        <el-menu :default-openeds="['1', '2']" router>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>个人信息</template>
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
              <el-menu-item index="/grade_manage">成绩管理</el-menu-item>
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
              <el-dropdown-item @click.native="quit_login">安全退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span style="color: white">欢迎，{{name}}</span>
        </el-header>

        <el-main>
          <el-row>
            <el-select v-model="value" placeholder="请选择课程班级" @change="in_change">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
            <el-input v-model="input4" placeholder="请输入考试成绩占比,数字即可" @change="zhanbi" type="number"
                      style="width: 250px; padding-left:20px"></el-input>

          </el-row>
          <el-table
            :data="tableData2"
            stripe
            style="width: 100%">
            <el-table-column
              prop="xh"
              label="学号"
              width="180">
            </el-table-column>
            <el-table-column
              prop="xm"
              label="姓名"
              width="180">
            </el-table-column>
            <el-table-column
              prop="nscore"
              label="平时成绩"
              width="180">
              <template slot-scope="scope">
                <el-input v-model="scope.row.nscore" @change="pscj(scope)"></el-input>
              </template>
            </el-table-column>
            <el-table-column
              prop="tscore"
              label="考试成绩"
              width="180">
              <template slot-scope="scope">
                <el-input v-model="scope.row.tscore" @change="kscj(scope)"></el-input>
              </template>
            </el-table-column>
            <el-table-column
              prop="zscore"
              label="总评成绩"
              width="180">
            </el-table-column>
          </el-table>

        </el-main>

        <el-footer>
          <el-button type="primary" @click="onSubmit">提交成绩</el-button>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  let that = this
  export default {
    name: "grade_manage",
    methods: {
      onSubmit() {
        for (var i = 0; i < this.tableData2.length; i++) {
          $.ajax({
            url: "/input_geade/",
            dataType: "json",
            data: {
              xh: this.tableData2[i].xh,
              gh: this.stu_number,
              kh: this.kh,
              pscj: this.tableData2[i].nscore,
              kscj: this.tableData2[i].tscore,
              zpcj: this.tableData2[i].zscore
            },
            success: function (data) {
              console.log(data);

            }
          })


        }
      },
      quit_login() {
        console.log("用户点击退出登录");
        sessionStorage.clear();
        console.log("SessionStorage：", sessionStorage.getItem('person_id'))
        this.$router.push('/')
      },
      in_change: function (e) {
        let that = this;
        console.log(e);
        this.kh = e;

        $.ajax({
          url: "/find_student_course/",
          dataType: "json",
          data: {
            kh: e,
            gh: sessionStorage.getItem('person_id')
          },
          success: function (data) {
            console.log(data);
            that.tableData2 = []
            for (var i = 0; i < data.length; i++) {
              that.tableData2.push({
                'xm': data[i].xm,
                'xh': data[i].xh,
                'nscore': data[i].pscj,
                'tscore': data[i].kscj,
                'zscore': data[i].zpcj
              })
            }
          }
        })
      },
      zhanbi(e) {
        let that = this;
        console.log(e)
        for (var i = 0; i < that.tableData2.length; i++) {
          that.tableData2[i].zscore = String.valueOf(that.tableData2[i].nscore * (100 - parseInt(e)) * 0.01 + that.tableData2[i].tscore * parseInt(e) * 0.01);
        }
      },
      pscj(row) {
        let that = this;
        console.log(row);

        function ks(a) {
          var k1 = ''
          if (a == '')
            k1 = '0'
          else
            k1 = a
          if (a == '')
            k1 = '0'
          else
            k1 = a
          return k1;
        }

        var kscj = ks(that.tableData2[row.$index].tscore);
        var pscj = ks(that.tableData2[row.$index].nscore);
        var bili = ks(that.input4)
        that.tableData2[row.$index].zscore = parseInt(pscj) * (100 - parseInt(bili)) * 0.01 + parseInt(kscj) * parseInt(bili) * 0.01;
        console.log("成绩结果：", kscj, pscj)
        console.log("成绩结果：", that.tableData2[row.$index].zscore)

      },
      kscj(row) {
        let that = this;
        console.log(row);

        function ks(a) {
          var k1 = ''
          if (a == '')
            k1 = '0'
          else
            k1 = a
          if (a == '')
            k1 = '0'
          else
            k1 = a
          return k1;
        }

        var kscj = ks(that.tableData2[row.$index].tscore);
        var pscj = ks(that.tableData2[row.$index].nscore);
        var bili = ks(that.input4)
        that.tableData2[row.$index].zscore = parseInt(pscj) * (100 - parseInt(bili)) * 0.01 + parseInt(kscj) * parseInt(bili) * 0.01;
        console.log("成绩结果：", kscj, pscj)
        console.log("成绩结果：", that.tableData2[row.$index].zscore)
      }
    },
    mounted() {
      let that = this;
      $.ajax({
        url: "/find_course_teacher/",
        dataType: "json",
        data: {
          gh: sessionStorage.getItem('person_id')
        },
        success: function (data) {
          console.log(data);
          for (var i = 0; i < data.length; i++) {
            that.options.push({'value': data[i].kh, 'label': data[i].km})
          }
        }
      })
      this.name = sessionStorage.getItem('person_name');
      this.stu_number = sessionStorage.getItem('person_id');
    },
    data() {
      return {
        tableData: [],
        name: '',
        stu_number: '',
        options: [],
        tableData2: [],
        input4: '',
        value: '',
        kh: ''
      }
    }

  }

</script>

<style scoped>
  .el-header {
    background-color: #307C91;
    color: #333;
    line-height: 60px;
  }

  .row-aside {
    margin-top: 20px;
    font-size: 15px;
  }

</style>
