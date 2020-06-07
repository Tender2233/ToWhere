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
<!--          按钮-->
          <el-row class="btns">
            <el-button type="primary" @click="login">登录</el-button>
            <el-button type="success" @click="register">注册</el-button>
            <el-button type="info" @click="resetLoginForm">重置</el-button>
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
        password: ''
      },
      RegisterForm: {
        username: '',
        password: '',
        repeat_password: ''
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
        ]
      }
    }
  },
  methods: {
    login () {
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) {} else {
          // 登录的地址
          const { data: res } = await this.$http.post('login', this.loginForm)
          console.log(res)
          console.log(res.data.token)
          if (res.status_code !== 200) { return this.$message.error(res.data.message) } else {
            this.$message.success('登陆成功')
            window.sessionStorage.setItem('token', res.data.token)
            await this.$router.push('/')
          }
        }
      })
    },
    register () {
      this.$router.push('/register')
      // this.$refs.loginFormRef.validate(valid => {
      //   if (!valid) {} else {
      //     const { data: res } = this.$http.post('http://121.36.25.3:8080/register', this.loginForm)
      //     console.log(res)
      //     if (res.status_code !== 200) { return this.$message.error('注册失败') } else {
      //       this.$message.success('注册成功')
      //       this.$router.push('/login')
      //     }
      //   }
      // })
    },
    resetLoginForm () {
      this.$refs.loginFormRef.resetFields()
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
  height: 300px;
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
