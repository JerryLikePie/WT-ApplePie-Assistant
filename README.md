# War Thunder ApplePie Naval Assistant
 - This is a dumb little script I wrote for the summer classes of image recongnition. First of all, it can't farm. Also, it's not a cheat. The main point of this whole project is to intergrate games with OpenCV, and being able to click on respective buttons when in different pages of a game. I modified the code a bit so that it works for War Thunder naval.
 - You can view it as a bot script or whatever, I don't really care, but trust me when I say it doesn't work like a bot. Tried it, pretty unefficiant. Bot scripts these days are not dumb anymore, they use much more advanced image recongition algorithms with machine learning involved, for example, locating the little green indicator then read the distance off the scrren, or auto pilot avoiding the terrans by reading off the map, that I'm still struggling to learn. The days of switching to antiair, rush, die, and hope the main guns gets someone are over, often times you would find most bot accounts having much better stats than humans now. But then again, those kind of bots costs like 30 bucks a month.   
 - If you are that desperate to use this, by all means. If too many people complains about it, I'll private this repository.

## 战争雷霆-苹果派-简约海战助手
### 前言
 - 本软件脱胎于大学暑期图像识别基础课课上实践作业，主要的点为在游戏中根据不同页面点击对应的图标。没有用到什么高深技术，现结课后根据规定修改后免费公开，请勿售卖本软件，造成的后果概不负责。  
 - 可以用于战争雷霆海战挂机。没有自动寻路，没有自瞄，需要玩家设定键位绑定。效率肯定不如市面上要钱的战雷海战脚本，毕竟是免费的嘛。
   - 目前效果是稳定运行3小时后卡死，30万银狮，共15局，其中1局为消极局。
   - 7月7日更新，已经做到稳定运行7个小时了，还在运行中。
 - 虽然但是，该说的话还是得说的：你手打的效率比脚本高多了，而广泛的使用脚本只会让游戏更快死亡。如果你游戏打得银狮掉得只能用脚本了，那……想拿去用就拿去咯。反正我话放在这里了，出了事也别找我，被骂了也别找我，我这边骂的人多起来我就把这个repo给private掉。  
#### 使用方法
    1.下载，解压缩，双击运行文件
    2.按照设置好键位，点击开始
    3.开始运行后，选中战争雷霆窗口，会自动探测到
    4.运行途中不要遮挡或移动战争雷霆游戏窗口，不要选定其他窗口
    5.如要停止，点击停止按钮，脚本会自动退出
#### 注意事项
    1.事先说好，这是挂机脚本，效率远低于手打，而且会占用电脑（脚本操作时不能使用电脑）
    2.挂机中的收益都会存在battlelog文件夹里，最多存储150局，请按需查看和删除
    3.写脚本不是我的主业，是学习之余做出来的一个玩意儿，所以不会经常更新。这边看着能挂12小时不崩就宣告完成了。
    4.不支持敌人识别，不含AI寻路，不包含自瞄和提前量
    5.永久免费，别拿去卖
#### 有做更高级版本的打算吗
    有，自动提前量的版本已经有思路了，但是再过几个月做吧，毕竟是副业。
#### 其他可能的问题
    Q：适配了哪些船？
    A：做的时候适配的是墨菲特。但是根据实现原理，绝大部分驱逐和一部分轻巡都可以。
       因为进入游戏后会转弯使得更多火炮对准敌人，那个弯转不过来的船都不适配。

    Q：可以用银币船吗？
    A：尽量不要。使用墨菲特测试下来是平均一局1万3，最高一局达到了6万5，但是银币收益比金船低维修费还高。
       当然你有高账的话就没事（收益不会为负数）

    Q：出现了bug，脚本卡死了！
    A：如果有报错请发在issue里面。目前的解决办法是重启然后继续挂

    Q：杀毒软件报警了？
    A：那就把这脚本删了

    Q：为什么脚本突然点这点那的？
    A：应该时不时会有识别错误吧，只要没有卡死就不是大问题。我写的时候没有让脚本点击任何“购买”按钮，也不会摁空格和回车。

    Q：脚本半天打不中人，怎么办？
    A：十分正常，想要高效率的话建议手操。

    Q：市面上的脚本有这些这些功能，我想要提议一些功能，可以加吗？
    A：不打算加什么功能，抱歉，没打算耗太多精力在这上面。

    Q：涨收益了为啥还要写脚本啊？
    A：说实话，我认为随着收益上涨，会主动使用脚本的人也会变少，因为手打几局就是一百万的，效率比脚本高出去不是一点半点。
       但是随着海战改版，上一个免费脚本Navy_Ace最近也没看到更新之后，一眼望去市面上就全都是付费脚本了。那缺的免费的这一块谁给我补啊？
#### 为啥叫苹果派助手啊？
    个人习惯作品号用26个英文字母开头的水果+Pie，理所当然的放在这里的第一个版本就是ApplePie。
    所以第二个版本是蓝莓还是香蕉呢……
