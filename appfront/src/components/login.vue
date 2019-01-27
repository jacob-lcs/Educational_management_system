<template>
  <div class="all">
    <el-row class="title">
      <p>教务管理系统</p>
    </el-row>
    <el-row>
      <el-input
        placeholder="请输入学号"
        v-model="stu_number"
        clearable
        class="in_name">
      </el-input>
    </el-row>
    <el-row>
      <el-input
        placeholder="请输入密码"
        v-model="stu_password"
        type="password"
        clearable
        class="in_pass">
      </el-input>
    </el-row>
    <el-row>
      <el-button round class="btn_login" @click="login_in">登陆</el-button>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: "login",
    data() {
      return {
        stu_number: '',
        stu_password: ''
      }
    },
    methods: {
      login_in() {
        let that = this

        $.ajax({
          url: "/login/",
          dataType: "json",
          data: {
            name: this.stu_number,
            psw: this.stu_password
          },
          success: function (data) {
            if (data['info'] == "no") {
              that.$message({
                message: '用户名或密码错误',
                type: 'warning'
              });
            } else {
              that.$router.push({
                name: "home",
                params: {
                  stu_number: that.stu_number
                }
              });
            }
          }
        })

      }
    }
  }
</script>

<style scoped>

  .in_name {
    width: 20vw;
    margin-top: 5vh;
  }

  .in_pass {
    width: 20vw;
    margin-top: 5vh;
  }

  .btn_login {
    margin-top: 2vh;
  }

  .title {
    margin-top: 23vh;
    font-size: 30px;
  }

</style>
