<template>
  <div class="article-page">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item>面经后台</el-breadcrumb-item>
      <el-breadcrumb-item>面经管理</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card shadow="never" border="false">
      <template #header>
        <div class="header">
          <span>共 {{ total }} 条记录</span>
          <el-button
            @click="openDrawer('add')"
            icon="el-icon-plus"
            size="small"
            type="primary"
            round
          >
            添加面经
          </el-button>
        </div>
      </template>
      <!-- 卡片的内容 -->
      <el-table stripe :data="list" style="width: 100%">
        <el-table-column prop="stem" label="标题" width="400">
        </el-table-column>
        <el-table-column prop="creator" label="作者"> </el-table-column>
        <el-table-column prop="likeCount" label="点赞"> </el-table-column>
        <el-table-column prop="views" label="浏览"> </el-table-column>
        <el-table-column prop="createdAt" label="更新日期" width="180">
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template #default="{ row }">
            <div class="actions">
              <i class="el-icon-view" @click="openDrawer('view', row.id)"></i>
              <i
                class="el-icon-edit-outline"
                @click="openDrawer('edit', row.id)"
              ></i>
              <i class="el-icon-delete" @click="del(row.id)"></i>
            </div>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="current"
        :page-sizes="[10, 15, 20, 50]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
    </el-card>
    <!-- 抽屉 -->
    <el-drawer
      :title="drawerTitle"
      :visible.sync="drawer"
      :before-close="handleClose"
      size="50%"
    >
      <!-- 添加、修改操作，抽屉的内容是表单 -->
      <el-form
        v-if="drawerType !== 'view'"
        label-width="80px"
        :model="form"
        :rules="rules"
        ref="form"
      >
        <!-- 一行：标题 -->
        <el-form-item label="标题" prop="stem">
          <el-input v-model="form.stem"></el-input>
        </el-form-item>
        <!-- 一行：内容 -->
        <el-form-item label="内容" prop="content">
          <quill-editor
            v-model="form.content"
            @blur="$refs.form.validateField('content')"
          ></quill-editor>
        </el-form-item>
        <!-- 一行：按钮 -->
        <el-form-item>
          <el-button type="primary" @click="onSubmit">确认</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
      <!-- 预览操作，内容不是表单，就是一个div -->
      <div v-else class="article-preview">
        <h5>{{ form.stem }}</h5>
        <div v-html="form.content"></div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
// require styles
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import { quillEditor } from 'vue-quill-editor'
import {
  ArticleListAPI,
  addArticleAPI,
  deleteArticleAPI,
  articleAPI,
  updateArticleAPI
} from '@/api/article'
export default {
  name: 'article-page',
  components: { quillEditor },
  data () {
    return {
      current: 1, // 页码，默认获取第1页的数据
      pageSize: 10, // 每页10条数据
      list: [], // 存储面经列表数据
      total: 0, // 共有多少条数据
      drawer: false, // false-关闭抽屉；true-打开抽屉
      drawerType: '', // 打开抽屉后 的操作类型
      form: {
        stem: '',
        content: ''
      },
      rules: {
        stem: [{ required: true, message: '标题必填', trigger: 'blur' }],
        content: [{ required: true, message: '内容必填', trigger: 'blur' }]
      }
    }
  },
  created () {
    this.initData() // 调用获取列表数据的方法
  },
  methods: {
    // 获取面经列表数据的方法
    async initData () {
      const res = await ArticleListAPI({
        current: this.current,
        pageSize: this.pageSize
      })
      // console.log(res)
      this.list = res.data.rows
      this.total = res.data.total
    },
    // 删除方法
    async del (id) {
      try {
        console.log(id)
        await deleteArticleAPI(id)
        this.$message.success('删除成功')
        this.initData() // 重新获取数据，更新页面
      } catch (e) {
        if (e.response) {
          this.$message.error(e.response.data.message)
        } else {
          this.$message.error('删除失败')
        }
      }
    },
    // 每页多少条发生变化后触发
    handleSizeChange (val) {
      console.log('每页几条数据', val) // 变化后的每页几条数据
      this.pageSize = val // 修改每页几条数据 10/15/20/50
      this.initData()
    },
    // 页码发生变化后触发
    handleCurrentChange (val) {
      console.log('当前页码', val) // 当前页码
      this.current = val // 修改页码
      this.initData()
    },
    // 打开抽屉的方法
    async openDrawer (type, id) {
      // console.log(type) // add | view | edit
      this.drawerType = type // 将操作类型，存储到变量中
      // 添加不需要获取面经详情的；预览、编辑 需要获取面经详情的
      if (type !== 'add') {
        // 获取面经详情
        const res = await articleAPI(id)
        // console.log(res)
        this.form.content = res.data.content
        this.form.stem = res.data.stem
        this.form.id = res.data.id
      }
      this.drawer = true
    },
    // 关闭抽屉之前执行的方法
    handleClose () {
      console.log('抽屉即将关闭，你有什么事要交待吗？')
      this.$refs.form?.resetFields() // 重置表单  对象?.方法()  ?是 ES6的可选链语法；如果?前面不是false，则调用后面的方法，否则不执行
      this.form = {
        stem: '',
        content: ''
      } // 彻底重置 form 数据
      this.drawer = false
    },
    // 提交表单【可能是添加、可能是修改】
    onSubmit () {
      // 表单.validate(valid => {  /* valid=true验证通过；valid=false验证不通过 */  })
      this.$refs.form.validate(async valid => {
        if (valid) {
          // 验证通过，可以提交数据了
          // 判断是添加还是修改操作
          let msg = ''
          if (this.drawerType === 'add') {
            msg = '添加'
          } else {
            msg = '修改'
          }
          try {
            // console.log(this.form)
            if (this.drawerType === 'add') {
              await addArticleAPI(this.form)
            } else {
              await updateArticleAPI(this.form)
            }
            this.handleClose() // 关闭抽屉 （清空表单）
            this.initData() // 重新渲染页面
            this.$message.success(msg + '成功') // 提示一下
          } catch (e) {
            if (e.response) {
              this.$message.error(e.response.data.message)
            } else {
              this.$message.error(msg + '失败')
            }
          }
        }
      })
    }
  },
  computed: {
    drawerTitle () {
      if (this.drawerType === 'add') {
        return '添加面经'
      } else if (this.drawerType === 'edit') {
        return '编辑面经'
      } else {
        return '面经预览'
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.el-card {
  margin-top: 25px;
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-right: 16px;
  }
  .actions {
    font-size: 18px;
    display: flex;
    justify-content: space-around;
    color: #666;
    > i:hover {
      color: rgba(114, 124, 245, 1);
      cursor: pointer;
    }
  }
}
.el-pagination {
  margin-top: 20px;
  text-align: center;
}
.el-breadcrumb {
  margin-top: 10px;
}
.el-form {
  padding-right: 40px;
}
.quill-editor {
  ::v-deep .ql-editor {
    height: 300px;
  }
}
.el-rate {
  padding: 10px 0;
}
.article-preview {
  padding: 0 40px 40px 40px;
  > h5 {
    font-size: 20px;
    color: #666;
    border-bottom: 1px dashed #ccc;
    padding-bottom: 30px;
    margin: 0 0 20px 0;
  }
}
</style>
