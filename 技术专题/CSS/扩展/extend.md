# 扩展

## 技巧

- 垂直居中：text-height行高属性等于盒子高度属性值，只适合单行文字，行高小于盒子高度，则文字偏上，行高大于盒子高度，文字偏下


## 注意
- 块级元素可以控制里面的行内元素或行内块元素左中右对齐，块级元素不能控制里面的块级元素对齐
- 行内元素设置margin-top和margin-bottom没效果


## align-items 和 align-content的区别
- align-items：控制每一行中的子元素如何对齐，注意控制的是一行中的子元素对齐方式
- align-conten：控制的是行与行之间的对齐方式

## 设置图片和文字垂直居中对齐的属性
vertical-align: middle;


## 想让span垂直方向往下移动，加了line-height后发现整体会往下移，头像也会跟着往下移，这是怎么回事？
```html
<a href="#">
    <img src="./uploads/user.png" alt="">
    <span>波仔学前端</span>
</a>
```
行内元素会共同参与同一个"行盒"的计算。line-height 调整的是整行文字的高度和基线，不只是把文字单独往下挪：
- span 的行高变大；
- 行盒高度和基线发生变化；
- img 默认也按基线对齐；
- 因此头像和整行都会跟着移动

## 通栏
CSS 中的"通栏"通常指横向铺满整个页面或父容器宽度的区域。


## hegith不会继承父级
height的默认值是auto，子元素会根据自身内容、盒模型和布局规则计算高度。
很多块级元素虽然没有继承 width，但默认 width: auto，会自动占满父元素可用宽度，所以看起来像是"继承"了宽度。但是子级若设置了高度，父级是默认值，则会撑开父级的盒子。

## 隐藏a标签中的title值
```html
<style>
    a {
        text-indent: -9999em;
        overflow: hidden;
    }
</style>


<style>
    a {
        font-size: 0;
    }
</style>
```


## 修改planholder样式
```html
<style>
    input::placeholder {
        color: #ccc
    }   
</style>
```




## 文字溢出使用省略号
```html
<style>
    .box {
        width: 200px;
        height: 200px;
        border:1px solid pink;
        /* 不允许文字换行，强制文字一行显示 */
        white-space: nowrap;
        /* 溢出隐藏 */
        overflow: hidden;
        /* 文字溢出用省略号代替 */
        text-overflow: ellipsis;

    }
</style>

<div class="box">里面多的文字123要显示省略号哦</div>

```

## flexible.js
flexible.js是手淘开发出来的一个用来适配移动端的js库。核心原理就是根据不同的视口宽度给网页中html根节点设置不同的font-size。


## less文件
.less 是 Less 样式预处理器文件，本质上是 CSS 的扩展写法，Less 支持变量、嵌套、函数、混合等功能。

## img标签设置宽度100%
表示图片的宽度设置为父元素内容区域宽度的 100%，也就是尽量和父元素一样宽


## object-fit
用于控制图片或视频在指定宽高的盒子中如何缩放和裁剪
