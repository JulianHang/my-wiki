const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // 允许打包的结果，以文件方式访问（允许双击打开）
  publicPath: './',
  // 去掉map文件
  productionSourceMap: false,
  // 打包时，排除哪些
  configureWebpack: {
    externals: {
      // 属性名（包名），window中多了什么
      echarts: 'echarts'
    }
  }
})
