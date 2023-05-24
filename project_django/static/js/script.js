// script.js

// 在页面加载完成后执行以下代码
document.addEventListener('DOMContentLoaded', function() {
    // 获取页面中的 <p> 元素
    var paragraph = document.querySelector('p');
    
    // 在 <p> 元素中插入文本
    paragraph.innerHTML = '这是通过 JavaScript 动态插入的文本。';
    
    // 修改 <p> 元素的样式
    paragraph.style.color = 'blue';
  });
  