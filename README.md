# markdown-links-replace
平时写博客，会在网上借鉴很多东西，直接复制过来是某些网站不支持直接引用的，比如（微信、语雀），这就有个麻烦了，如果是图片过多一张一张保存，那得多烦，网上也没找到的脚本，自己写了个，有一些小bug，但也没打算改。能满足大部分需求就行了，有部分图片没法替换手动。

本脚本思路：
1、先正在匹配下载图片（正则只能按规则写，如果内容中有其他被匹配上了就难搞了）
![images](https://github.com/mrknow001/markdown-links-replace/blob/main/images/1.png)


2、所以在这一步下载图片这里直接不下载，到后面也不替换它
![images](https://github.com/mrknow001/markdown-links-replace/blob/main/images/1.png)
![images](https://github.com/mrknow001/markdown-links-replace/blob/main/images/1.png)

3、最后看看效果，把原来的网页链接替换成了本地相对路径，使用hexo搭建博客可直接使用。
![images](https://github.com/mrknow001/markdown-links-replace/blob/main/images/1.png)
