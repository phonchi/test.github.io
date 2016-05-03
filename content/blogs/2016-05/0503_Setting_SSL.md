---
Title: SSL Basics And Setting SSL
Slug: Setup-SSL
Date: 2016-05-03 16:00
Tags: zh, SSL
Category: Software System

---

SSL(Secure Sockets Layer) 是一個重要的網路安全協定, 越來越多網站會使用SSL來進行與使用者互動或機密資料傳輸，用瀏覽器(Chrome)連入主留網站大多可看到網址列左方有一個鎖，這個鎖即表明此網站會用HTTP over SSL來跟瀏覽器對話。
<div class="figure">
  <img src="pics/HTTPS.png"/>
  <p class="caption center">HTTPS Example</p>
</div>
如果有經營網站的朋友們要如何讓網站啟用此項功能呢，我們會先從Basics說起，然後說明如何透過免費CA(Certificate Authority)來取得憑證，之後以XAMPP這個架站框架來說明如何將透過憑證開啟HTTPS的功能~

[TOC]



### SSL Basics
SSL由 上古時代的大公司Netscape開發，其1.0版並未公開釋出，第一個公開版本為1995年問市的2.0版，不過由於2.0版有些許安全性缺陷，因此隔年Netscape就推出SSL 3.0。

> IETF（Internet Engineering Task Force，網際網路工程任務組）在1999年制定RFC2246，並將其稱為TLS（Transport Layer Security），將其視為SSL的升級版，並於2006與2008年推出TLS 1.1與1.2版。

因此SSL和TLS可以當作交互使用的協定，絕大部分的瀏覽器都支援SSL、TLS，且已預先安裝了各大CA（Certificate Authority，電子證書認證機構）的相關憑證檔案，會在使用者進入支援SSL、TLS的網頁時，自動建立加密連線。再交握的過程中憑證是很重要的，因此我們先轉向CA的說明

基本上一般CA對申請網站的鑑別方式可以分為3種，最簡易的驗證方式為網域驗證（Domain Validation），CA只會簡單地鑑別網域所有權，個人也可申請，等級最低也最便宜甚至免費。第二種稱為機構驗證（Organization Validation），申請網站需要提出政府所發的正式文件，向CA證明自己是合法登記設立的公司行號、機關團體。最為嚴謹的是延伸驗證（Extended Validation），根據經電子商務交易安全整合平台提供的資料，申請延伸驗證需要有合法文件證明商業實體的設立與運作，以及合法文件證明合法擁有登記的網域名稱，並能夠完整掌控該網域名稱之運用等條件，可以確保該網站的擁有者就是一般人所認定的同一公司或組織，安全性更加可靠。

> CA的運作方式為階層式的組成，基本上可以把CA想成第三方憑證中心在認證後用他的公鑰簽署你的公鑰的文件(不同於PGP的信任網)，詳細規格可看X.509文件，因此如果你不相信底層CA你可以去驗證底層CA的公鑰有沒有經過更高層CA驗證簽署，以此類推，最後回溯到你可以信任的CA為指(可能是Root CA)

### Createing Certificate
好的，那要準備哪些文件來取的Certificate呢?流程又是如何呢? 我們以實作SSL的函式庫OpenSSL為例，我們可簡單的分為幾個步驟:

> OpenSSL一直有些爭議，有興趣的讀者可以搜尋參考[Heartbleed事件][Heart Bleed]

#### 產生private key 和 CSR(Certificate Singning Request)

````
openssl req -nodes -newkey rsa:2048 -keyout example.key -out example.csr
# req: openssl command to manage CSRs, -nodes: set the passphrase of the private key to blank (private keys of TLS may have passphrases)
````
過程中會問一些相關資訊，其中domain name是必要的, 另外你也可以用 `subj` 引數傳入相關資訊，2048 bit 也可根據需求再調[參考][Keylength]
```
openssl req -nodes -newkey rsa:2048 -keyout example.key -out example.csr -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=example.com”
```
注意上述傳key為private key，如果你已經有private key 你可以用
```
openssl req -new -key private.key -out example.csr
```
程式會推出你的public key然後製作出CSR, 你也可以自己去簽他XD

```
openssl x509 -req -in example.csr -signkey private.key -out example.crt -days 365
```

預設certificate是base64 encode的(這麼做 跟以前網路協定有關)，你可以decode他
```
openssl x509 -in example.crt -text -noout
```

####  選定CA然後將CSR給CA
目前免費的CA最有名為[Let's Encrypt][LE], 他們使用 AMCE (Automated Certificate Management Environment) protocol 去驗証你是否擁有你欲簽証的 domain。簡單來說，LE 會要求你的 server 在特定的 path 加入特定的檔案，如果你做得到，就代表你擁有這個 domain。這樣的簽証第一次要在 LE server 上註冊，之後最長每 90 天認証一次。(歸於Domain Validation類的簽證)。

你可以參考[用script][ACME]或用[網頁端script][SSLFree][或這個][SSLWeb]來拿到你的簽證。

> 選用工具的時候，如果不那麼信任，請不要隨便交出private key~

####  將certificate和private key 放入你的網站
以Xampp 來說基本上只要去`apache/conf/extra/httpd-ssl.conf` 檔照此template放入你對應的certificate和private key路徑就可以囉。

另外如果要把http 80 port的流量也導向https 443的話，apache官方目前查到的做法如下(用Redirect指令)在上述檔案再加入
```
<VirtualHost *:80> 
    ServerName www.example.com
    DocumentRoot "C:/xampp/htdocs" 
	## If we can get trust certificate uncomment below
	## Redirect / https://www.example.com
</VirtualHost> 
```

### 測試SSL
用瀏覽器開啟對應的網站來測試，要注意的是有些防毒軟體或防火牆(如Avast)可能會改過你的CA 發證單位

> 遇到這種情況也可以暫時關閉網也防護，來看發證單位，不過就看個人衡量了~

[Heart Bleed]: http://devco.re/blog/2014/04/11/openssl-heartbleed-how-to-hack-how-to-protect/
[Keylength]: https://www.keylength.com/
[LE]: https://letsencrypt.org/
[ACME]: https://blog.liang2.tw/posts/2016/02/pydoctw-https/
[SSLFree]: https://free.com.tw/ssl-for-free/
[SSLWeb]: https://gethttpsforfree.com/