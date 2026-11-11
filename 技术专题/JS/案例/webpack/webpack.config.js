const path = require('path')

module.exports = {
    entry: path.resolve(__dirname, 'src/main.js'), // 入口
    output: { // 出口
        path: path.resolve(__dirname, "dist"),
        filename: 'app.js',
        clean: true // 先清空dist，然后再输出最新内容
    }

}