---
Title: Setting Up Blogs With Pelican and GitHub Pages
Slug: Setup-blogs
Date: 2016-05-02 22:00
Tags: zh, Pelican, Git
Category: Software System 
---


書寫-也是試了很多方式，國中時的日記，高中時的作文式筆記，無名小站，[Google Blogger][Blogger] ，BBS，Facebook，漸漸習慣以鍵盤滑鼠代替紙筆

> 為什麼書寫呢，以什麼主題書寫呢，述說的對象是誰呢? 或許曾經一度的找到答案，想留下些什麼的心情，無論答案是什麼，只要確定仍在就好

再次提筆時，已是多年以後，於是訂下一些方向，靜態網頁Markdown書寫方式

[TOC]

開始-如何架呢? 向網路上眾多的資源和大大學習，遙想以前會找些免費空間用Wordpress, Joomla等套件軟體達到方便又可以前後台控制的方式，後來也用過完全書寫為主的像無名 Google Blogger。

現在呢? 最近一陣子很喜歡Python，於是發現了[Pelican][Pelican]這個可以自動轉換Markdown語言成靜態網頁的部落格套件。另一件很喜歡戮力追求的是open source，於是便轉向[GitHub Pages][GitPage]，

[Blogger]:http://phonchi.blogspot.tw/
[Pelican]:https://github.com/getpelican/pelican
[GitPage]:https://pages.github.com/

### GIT Basics
來簡單複習一下git，版本控制在多人協作時很有用，他可以設下很多存檔點

> [存檔點....][Save] 見此(x

能用的軟體很多，早期的subversion系列到近期的主流Git, 見[tutorial][Gittutorial] (據說校內計結等開課也開始用了XD)

> Git 會在你的專案（repo）底下建一個 .git 的資料夾來管理這些「進度點」，而不會去動專案其他路徑裡的東西。這些進度點可以傳到 server 上，別人下載下來的時候就可以除了得到現在的 code 以外，還能看到過去開發的記錄；而別人上傳了他的更新進度點之後，你抓下來就可以得到他更改的進度。這個就是「同步」的概念，多人之間能彼此共享、更新彼此開發的成果。
> 能夠處理 Git 同步操作的伺服器就叫做 git server。Github 就是一間公司提供免費的 git server 讓大家同步公開的 Git 專案。很多 Linux 的工具都使用 git 來讓大家合作開發，也有不少工具已經把 git server 轉到了 Github 上面。所以非常多人在用,在open source的趨勢下，現在許許多多的小程式都可以在上面找到!!

怎麼開始呢? 從github教學開始吧(https://try.github.io/) 順便創帳號~~


Linux系統網路上很多資源，在windows上面可以用mobaxterm 他自帶cygwin的環境 (應該說他功能很多...)，不用等ubuntu bash出來。 新的版本中直接當debian系列的linux操作就好了。
```
apt-get install git
```

#### Adding SSH Keys
如果已創好帳號你會需要用Openssl產生key pair，然後把public key加到git server，這樣就可以在你熟悉的電腦跟git server用ssh溝通了[教學][SSHKey]

> Server會random產生challenge並用你的public key加密，收到加密的challenge後可以用private key解回來然後回傳給server，server藉由比對你回傳的challenge和當時的challenge來認證你(單方認證)

#### Key Git Command
記錄一些主要的command，比較常見的做法是創建兩個repository一個當source一個link到轉檔之後的output，後者必須依據你的使用者名稱來當名字

```
git config --global user.name "John Cena"
git config --global user.email johncena@example.com
git config --global core.editor vi
git clone git@github.com:username/username.github.io-src ghpages
git remote -v
git submodule add git@github.com:username/username.github.io.git output
```

有時可以用來處理檔案exist的問題
```
git init
git rm --cached [file]
```

### Set up the blog with Pelican


#### Installation

你會需要一些主要的python套件
```
apt-get install ghp-import
apt-get install pelican
apt-get install Markdown
```

然後theme 和 plugin
```
git clone --recursive https://github.com/getpelican/pelican-themes themes
git clone --recursive https://github.com/getpelican/pelican-plugins plugins

```

其他的script或theme可能會需要額外的檔案或套件

#### Initialized Pelican
可以用官方的script來建template
```
pelican-quickstart
```
當然也可以找網路上大大們的template
```
git clone others template
```

主要的設定檔為pelicanconf.py，基本上設定好他即可
```
pelican -s pelicanconf.py
```


### Publish WebSite
做git的push流程吧
```
cd output
git add .
git commit -m "First post."
git push -u origin master
cd ..
echo '*.pyc' >> .gitignore #don't need pyc files
git add .
git commit -m "First commit."
git push -u origin master
```

然後在http://username.github.io 下就可以看到囉~



[Save]: https://www.facebook.com/RSR.lol/videos/vb.1587235684873434/1693237897606545/?type=2&theater
[Gittutorial]: http://dylandy.github.io/Easy-Git-Tutorial/
[SSHKey]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
