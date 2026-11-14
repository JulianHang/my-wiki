# 扩展

## 检测数据类型
```html
<script>
    let num1 = 10;
    console.log(typeof num1);
</script>
```


## null和undefined区别
undefined 表示没有赋值，不存在，null表示赋值了，但是内容为空


## ++放在变量前后的区别
++放在变量前面，先对变量值进行+1，再拿变量的值进行运算；++放在变量后面，先拿变量值进行运算，在对变量的值进行+1

## 遍历数组
```html
<script>
    let a = [1,2,3]
    a.forEach((element, index) => {
        console.log(element, index)
    })
    
</script>
``` 

## 函数声明
Array<any>.forEach(
  callbackfn: (value: any, index: number, array: any[]) => void,
  thisArg?: any
): void

1. callbackfn 这是必填的回调函数。回调函数会接收三个参数：
    - value：当前元素
    - index：当前下标
    - array：正在遍历的原数组
  - => void，表示回调函数不需要返回有效结果
  
2. thisArg?: any。这是可选参数，`?` 表示可以不传，用来指定回调函数中的 this。

3. 末尾的 : void
表示 forEach() 本身没有返回值

4. value is string 是 TypeScript 的类型谓词返回类型，用于告诉编译器：“如果函数返回 true，那么 value 是 string


## new实例化过程
1. 创建新空对象
2. 构造函数this指向新对象
3. 执行构造函数代码
4. 返回新对象

## 内置函数
### Object

- Object.keys()：获取对象中的所有属性，返回的是一个数组
- Object.values()：获取对象中所有属性值，返回的是一个数组
- Object.assign()：用于拷贝对象


## Nodejs

### Node.js执行js代码
在vscode终端中输入：node 01.js 回车即可执行

### fs模块
封装了与本机文件系统进行交互的方法、属性

语法：
1. 加载fs模块
2. 写入文件内容
3. 读取文件内容

```javascript
const fs = require('fs')

fs.writeFile('./text.txt', 'hello world', error => {

})

fs.readFile('./text.txt', (error, data) => {
    console.log(data.toString());
})

```

### path模块
```javascript
const fs = require('fs')
const path = require('path')
const filename = path.join(__dirname,'text.txt')

fs.writeFile(filename, 'hello world', error => {

})


fs.readFile(filename, (error, data) => {
    console.log(data.toString());
})

```

### CommonJS模块化
在nodejs中，每个文件都被视为一个单独的模块。

导出：module.exports = {}
导入：require()

```javascript


// 01.js
const basrURL = ""

module.exports = {
    url: basrURL
}


// 02.js
const one = require('./01.js')
console.log(one.url)
```

### ES导入导出
导出：export default {}
导入：import 变量名 from '模块名或路径'

注意：nodejs默认支持CommonJS标准语法，如需使用es标准语法，在运行模块所在文件夹新键package.json文件，并设置 {type: module}


```javascript
// 01.js
const basrURL = ""

export default {
    url: basrURL
}


// 02.js
import obj from './01.js'

console.log(obj);


```

### ES命名导入导出
导出：export 修饰定义语句
导入：import {同名变量} from '模块名或路径'

按需加载，使用命名导入和导出

```javascript
// 01.js
export const basrURL = "1"


// 02.js
import {basrURL} from './01.js'

console.log(basrURL);


```

## npm

### 包
将模块、代码、其他资料聚合成一个文件夹

分类：
- 项目包：主要用于编写项目和业务逻辑
- 软件包：封装工具和方法进行使用

要求：根目录中，必须有package.json文件（记录包的清单信息）

```json
package.json
{
    "name": "xx", // 软件包名称
    "version": "1.0.0", // 版本
    "main":"index.js", // 软件包入口
}

```

注意：导入软件包时，引入的默认是index.js模块文件/main属性指定的模块文件




## 同源策略
用于限制一个源的文档或者它加载的脚本如何能与另一个源的资源进行交互。网页加载时所在源，和ajax请求时的源（协议、域名、端口号）全部相同即为同源

## 跨域
从一个源的文档/脚本，加载另一个源的资源就产生了跨域

## Webpack
webpack只识别js和json文件内容