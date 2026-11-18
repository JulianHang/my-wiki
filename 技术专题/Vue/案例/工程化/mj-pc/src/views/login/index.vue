<template>
  <div class="login-page">
    <el-card>
      <!-- 卡片标题，使用具名插槽 -->
      <template #header>黑马面经后台管理系统</template>
      <!-- 卡片内容，默认插槽，不用嵌套template -->
      <el-form ref="form" label-width="60px" :model="user" :rules="rules">
        <!-- 第一项：账号 -->
        <el-form-item label="账号" prop="username">
          <el-input v-model="user.username"></el-input>
        </el-form-item>
        <!-- 第二项：密码 -->
        <el-form-item label="密码" prop="password">
          <el-input show-password v-model="user.password"></el-input>
        </el-form-item>
        <!-- 第三项：按钮 -->
        <el-form-item>
          <el-button type="primary" @click="login">登录</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { loginAPI } from '@/api/user'

export default {
  name: 'LoginIndex',
  data () {
    return {
      // 提交的数据
      user: {
        username: 'admin',
        password: 'admin'
      },
      // 验证规则对象
      rules: {
        username: [
          // required必填；message验证不通过时的提示；trigger触发时机
          {
            required: true,
            message: '请输入账号',
            trigger: ['blur', 'change']
          },
          {
            min: 3,
            max: 6,
            message: '长度在 3 到 6 个字符',
            trigger: ['blur', 'change']
          }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 3, max: 6, message: '长度在 3 到 6 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    login () {
      // 进行完整的校验
      this.$refs.form.validate(async valid => {
        // console.log(valid) // 验证通过-true； 验证不通过-false
        if (valid) {
          // 进入这个if区间，表示验证通过，此时可以提交数据了
          try {
            // console.log(this.user)
            const res = await loginAPI(this.user)
            // console.log('组件中', res)
            // console.log(res)
            // 存token
            // localStorage.setItem('mj-pc-token', res.data.token)
            this.$store.commit('user/updateToken', res.data.token)
            this.$message.success('登录成功')
            this.$router.push('/dashboard')
          } catch (e) {
            if (e.response) {
              this.$message.error(e.response.data.message)
            } else {
              this.$message.error('登录错误')
            }
          }
        }
      })
    },
    reset () {
      this.$refs.form.resetFields()
    }
  }
}
</script>

<style lang="scss" scoped>
.login-page {
  height: 100vh;
  background: url(@/assets/login-bg.svg) no-repeat center;
  background-size: cover;
  // 使用element-ui，组件名，就是类名
  .el-card {
    width: 420px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    // 样式穿透，用于修改子组件元素的样式
    ::v-deep .el-card__header {
      text-align: center;
      background-color: #727cf5;
      color: #fff;
      height: 80px;
      line-height: 40px;
    }
    .el-form {
      padding: 0 20px;
    }
  }
}
</style>
