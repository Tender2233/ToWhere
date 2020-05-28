<template>
  <div class="login_container">
    <div class="login_box">
      <!--        头像-->
      <div class="avator_box">
        <img src="../assets/avator.png" alt="">
      </div>
      <!--        登录区-->
      <el-form ref="loginFormRef" label-width="0px" :rules="rules" class="login_form" :model="loginForm">
        <!--          用户名-->
        <el-form-item prop="username">
          <el-input prefix-icon="el-icon-user-solid" v-model="loginForm.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <!--          密码-->
        <el-form-item prop="password">
          <el-input prefix-icon="el-icon-lock" placeholder="请输入密码" v-model="loginForm.password" show-password></el-input>
        </el-form-item>
<!--        重复密码-->
        <el-form-item prop="re_password">
          <el-input prefix-icon="el-icon-lock" placeholder="请重复密码" v-model="loginForm.re_password" show-password></el-input>
        </el-form-item>
        <!--          按钮-->
        <el-row class="btns">
          <el-button type="success" @click="register">注册</el-button>
          <el-button type="info" @click="resetLoginForm">重置</el-button>
          <el-button type="danger" @click="quit">取消</el-button>
        </el-row>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loginForm: {
        username: '',
        password: '',
        re_password: ''
      },
      rules: {
        username: [
          {
            required: true,
            message: '请输入用户名',
            trigger: 'blur'
          },
          {
            min: 3,
            max: 10,
            message: '用户名长度在 3 到 10 个字符',
            trigger: 'blur'
          }
        ],
        password: [
          {
            required: true,
            message: '请输入密码',
            transform: value => value,
            trigger: 'blur'
          },
          {
            type: 'string',
            message: '请输入不包含空格的字符',
            trigger: 'blur',
            transform (value) {
              if (value && value.indexOf(' ') === -1) {
                return value
              } else {
                return false
              }
            }
          },
          {
            trigger: 'blur',
            validator: (rule, value, callback) => {
              var passwordreg = /(?=.*\d)(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).{6,16}/
              if (!passwordreg.test(value)) {
                callback(new Error('密码必须由数字、字母、特殊字符组合,请输入6-16位'))
              } else {
                callback()
              }
            }
          }
        ],
        re_password: [
          {
            required: true,
            message: '请输入密码',
            transform: value => value,
            trigger: 'blur'
          },
          {
            trigger: 'blur',
            validator: (rule, value, callback) => {
              if (this.loginForm.password === this.loginForm.re_password) {
                callback()
              } else {
                callback(new Error('两次输入的密码不一致'))
              }
            }
          }
        ]
      }
    }
  },
  methods: {
    register () {
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) {} else {
          const { data: res } = await this.$http.post('register', this.loginForm)
          console.log(res)
          if (res.status_code !== 200) { return this.$message.error(res.data.message) } else {
            this.$message.success('注册成功')
            await this.$router.push('/login')
          }
        }
      })
    },
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
    },
    quit () {
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="less" scoped>
  .login_container{
    background-image: url("../assets/6.jpg");
    height: 100%;
    padding: 0;
    background-size: cover;
  }
  .login_box{
    width: 450px;
    height: 400px;
    background-color: #fff;
    border-radius: 3px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    opacity: 90%;

    .avator_box {
      height: 150px;
      width: 150px;
      border: 1px solid #eee;
      border-radius: 50%;
      padding: 10px;
      box-shadow: 0 0 10px #ddd;
      position: absolute;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: #fff;
      img {
        height: 100%;
        width: 100%;
        border-radius: 50%;
        background-color: #eee;
      }
    }
  }

  .login_form {
    position: absolute;
    bottom: 0;
    height: 65%;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
  }
  .btns{
    display: flex;
    justify-content: flex-end;
  }
</style>
