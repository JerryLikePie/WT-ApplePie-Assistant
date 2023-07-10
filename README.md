# War Thunder ApplePie Naval Assistant
 - This is a dumb little script I wrote for the summer classes of image recongnition. First of all, it can't farm. Also, it's not a cheat. The main point of this whole project is to intergrate games with OpenCV, and being able to click on respective buttons when in different pages of a game. I modified the code a bit so that it works for War Thunder naval.
 - You can view it as a bot script or whatever, I don't really care, but trust me when I say it doesn't work like a bot. Tried it, pretty unefficiant. Bot scripts these days are not dumb anymore, they use much more advanced image recongition algorithms with machine learning involved, for example, locating the little green indicator then read the distance off the scrren, or auto pilot avoiding the terrans by reading off the map, that I'm still struggling to learn. The days of switching to antiair, rush, die, and hope the main guns gets someone are over, often times you would find most bot accounts having much better stats than humans now. But then again, those kind of bots costs like 30 bucks a month.   
 - If you are that desperate to use this, by all means. If too many people complains about it, I'll private this repository.

## 战争雷霆-苹果派-简约海战助手
### 前言
 - 本软件脱胎于大学暑期图像识别基础课课上实践作业，主要的点为在游戏中根据不同页面点击对应的图标。没有用到什么高深技术，现结课后根据规定修改后免费公开，请勿售卖本软件，造成的后果概不负责。  
 - 可以用于战争雷霆海战挂机。没有自动寻路，没有自瞄，需要玩家设定键位绑定。效率肯定不如市面上要钱的战雷海战脚本，毕竟是免费的嘛。
 - 虽然但是，该说的话还是得说的：你手打的效率比脚本高多了。如果你游戏打得银狮掉得只能用脚本了，那想拿去用就拿去咯。反正我话放在这里了，出了事也别找我，被骂了也别找我，我这边骂的人多起来我就把这个repo给private掉。  
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
#### 其他可能的问题
    Q：适配了哪些船？
    A：做的时候适配的是墨菲特。但是根据实现原理，绝大部分驱逐和一部分轻巡都可以。
       因为进入游戏后会转弯使得更多火炮对准敌人，那个弯转不过来的船都不适配。
       注：1.8版本之后已经适配驱逐，轻巡，重巡。为了效率更高尽量选择低级驱逐，距离近，投射量足，命中率高。

    Q：可以用银币船吗？
    A：尽量不要。使用墨菲特测试下来是平均一局1万3，最高一局达到了6万5，但是银币收益比金船低维修费还高。
       当然你有高账的话就没事（收益不会为负数）
       注：1.9版本已经支持了银币船自动购买配件，
           但依然不建议在没有高账的情况下使用高BR高维修费（大于7000）的银币船
           打配件的话当我没说，具体看效率参考表里面的银币载具

    Q：出现了bug，脚本卡死了！
    A：如果有报错请发在issue里面。目前的解决办法是重启然后继续挂

    Q：杀毒软件报警了？
    A：那就把这脚本删了

    Q：为什么脚本突然点这点那的？
    A：应该时不时会有识别错误吧，只要没有卡死就不是大问题。我写的时候没有让脚本点击任何“购买”按钮。

    Q：脚本半天打不中人，怎么办？
    A：十分正常，想要高效率的话建议手操。挂机就是低效率长时间来获得收益。

    Q：市面上的脚本有这些这些功能，我想要提议一些功能，可以加吗？
    A：不打算加什么功能，抱歉，没打算耗太多精力在这上面。

    Q：涨收益了为啥还要写脚本啊？
    A：说实话，我认为随着收益上涨，会主动使用脚本的人也会变少，因为手打几局就是一百万，效率比脚本高不是一点半点。
       而海战改版，NavyAce停更之后，一眼望去全都是脚本一个月卖大几百的脚本商，就，那缺的免费脚本这一块谁给玩家补啊？
#### 目前的效率是？
    仅供参考。效率有太多因素了。有高账。
| 版本  | 使用船只 | 运行时间 | 运行结果 | 场数 | 总收益| 场均耗时 | 场均收益 | 收益/小时 |
| --- | --- | ---|---|---|---|---|---|---|
| v1.3  | 墨菲特| 3小时 | 崩溃 | 15场 | 27万 | 12分钟 | 1.8万 | 9万/小时 |
| v1.5  | 墨菲特| 10小时 | 掉线 | 39场 | 73万 | 15.3分钟 | 1.87万 | 7.3万/小时 |
| v1.6  | 墨菲特| 9小时 | 正常 | 40场 | 76万 | 13.5分钟 | 1.9万 | 8.4万/小时 |
|-|-|-|-|-|-|-|-|-|
| v1.6  | 工兵| 1.5小时 | 正常 | 6场 | 7万 | 15分钟 | 1.16万 | 4.7万/小时 |
| v1.7  | 工兵 | 5小时 | 卡死 | 25场 | 31万 | 12分钟 | 1.24万 | 6.2万/小时 |
| v1.9  | 工兵 | 9小时 | 正常 | 39场 | 57万 | 13.8分钟 | 1.46万 | 6.3万/小时 |
| v1.9  | 工兵 | 4小时 | 正常 | 18场 | 32万 | 13.3分钟 | 1.78万 | 8万/小时 |
|-|-|-|-|-|-|-|-|-|
| v1.7  | 海伦娜 | 3小时 | 正常 | 11场 | 24万 | 16.4分钟 | 2.18万 | 8万/小时 |
| v1.8  | 海伦娜 | 2小时 | 正常 | 9场 | 17万 | 13.3分钟 | 1.89万 | 8.5万/小时 |
|-|-|-|-|-|-|-|-|-|
| 未测试  | 加的斯 | - | - | - | - | - | - | - |
|-|-|-|-|-|-|-|-|-|
| 未测试  | 欧根亲王 | - | - | - | - | - | - | - |
|-|-|-|-|-|-|-|-|-|
| v1.8  | 豹（无高账） | 6小时 | 正常 | 22场 | 14万 | 16.4分钟 | 0.64万 | 2.3万/小时 |

    目前市面上贩卖的脚本声称用海伦娜1小时30万，我们希望做到付费脚本的四分之一，即平均1小时收益7.5万以上
    现在我们倒是可以说，完美达到指标。
    同时注意“收益”计算的是毛收益，即挂完后的银狮数量-挂之前的银狮数量，不是纯收益
#### 有做更高级版本的打算吗
    有，自动提前量的版本已经有思路了，但是再过几个月做吧，毕竟是副业。
#### 为啥叫苹果派助手啊？
    个人习惯作品号用26个英文字母开头的水果+Pie，理所当然的放在这里的第一个版本就是ApplePie。
    所以第二个版本是蓝莓还是香蕉呢……
