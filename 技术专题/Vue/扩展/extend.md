# 扩展

## 事件对象

如果在模板中（页面中）使用事件对象，可以使用 $event（固定写法）；如果在 js 中使用事件对象，还是事件处理函数的形参 e，如果除了事件对象还有其他参数的话，就需要手动传入参数 e

## v-model 拆解

v-model 可以拆解成 :vlaue + @input。父组件传递的属性名：`value`，子组件触发的事件名：`input`

## .sync

.sync 用于 Vue 2 中让子组件请求更新父组件传入的某个属性，常见于弹窗显示状态、面板展开状态、分页参数等需要由父子双方修改的值

## 路由模式

- Hash 模式：地址带 #，例如 http://example.com/#/users。不需要服务器配置，兼容性好。
- History 模式：地址不带 #，例如 http://example.com/users。页面更干净，但部署时服务器要把未匹配的地址回退到应用入口（通常是 index.html）

History 模式直接访问深层地址会 404，通常是因为服务器找不到对应的实际文件。例如直接打开 /users/1 时，服务器按文件路径查找，但 Vue 单页应用只有一个入口文件。需要把应用路由之外的请求回退到 index.html；具体配置方式取决于部署服务器，如 Nginx、Apache 或静态托管平台。

Hash 模式把路由放在 # 后面，例如 example.com/#/users/1。浏览器不会把 # 后的部分发送给服务器，因此服务器只收到 /，一般无需配置路由回退

## SPA

单页面应用，指的是所有页面都写在同一个页面下

## $nextTick

当数据更新，等 DOM 也更新后，才会触发执行此方法里的函数体。数据是同步更新，视图是异步更新。

```javascript
this.$nextTick(() => {})
```

## 组件库

- PC 端
  1. Element UI
  2. Ant Design
- 移动端
  1. Vant
  2. mint-ui

## 移动端工程化

1. 创建项目
2. 配置代码风格-ESLint
3. 引入组件库
4. 项目适配
5. 项目路由配置

## 配置文件

vue.config.js：vue-cli（vue2）脚手架的配置文件，用来修改项目的构建及开发配置
webpack.config.js：原生 webpack 的打包配置
vite.config.js：vite 的打包配置
