FV的打怪向模组包 `FV's PVE modpack`
=====

Encoding = UTF-8

Modpack Version: %{version}

MC version: 1.12.2

Forge Version: 14.23.5.2847

需要手动导入

~~前期很难，真的很难！`(说的好像后期不难一样)`~~

这个包一点也不难:D

建议用火狐浏览器/谷歌浏览器打开本文档的.md版本

- [FV的打怪向模组包 `FV's PVE modpack`](#fv%e7%9a%84%e6%89%93%e6%80%aa%e5%90%91%e6%a8%a1%e7%bb%84%e5%8c%85-fvs-pve-modpack)
  - [安装方法](#%e5%ae%89%e8%a3%85%e6%96%b9%e6%b3%95)
  - [一些小程序](#%e4%b8%80%e4%ba%9b%e5%b0%8f%e7%a8%8b%e5%ba%8f)
  - [加入服务器](#%e5%8a%a0%e5%85%a5%e6%9c%8d%e5%8a%a1%e5%99%a8)
  - [建议配置](#%e5%bb%ba%e8%ae%ae%e9%85%8d%e7%bd%ae)
  - [模组列表](#%e6%a8%a1%e7%bb%84%e5%88%97%e8%a1%a8)
  - [重要说明](#%e9%87%8d%e8%a6%81%e8%af%b4%e6%98%8e)
  - [前排提示](#%e5%89%8d%e6%8e%92%e6%8f%90%e7%a4%ba)
  - [未来版本计划](#%e6%9c%aa%e6%9d%a5%e7%89%88%e6%9c%ac%e8%ae%a1%e5%88%92)
  - [鸣谢](#%e9%b8%a3%e8%b0%a2)

安装方法
-------

安装前, **请清空游戏目录中的mods文件夹**

进入游戏目录, 将本Modpack中的文件夹复制到游戏目录中. Modpack中的其他文件是一些相关数据文档~~或者是作者不小心放进去的无关紧要的文件~~, 仅供玩家参考, 不需要复制到游戏目录中.

~~对于服务器, 请删除Mod列表中Client下的所有mod.~~
请选择 server 模式

一些小程序
----------

ModpackModeSelector.sh / ModpackModeSelector.bat
- - - -
用于选择 Modpack 模式的脚本, bat版本和sh版本功能一致

第一次下载后请务必运行此脚本

对于 Windows 系统, 请双击 ModpackModeSelector.bat 使用

对于 Linux 内核系统, 请直接运行 ModpackModeSelector.sh 脚本, 或使用 sh ./ModpackModeSelector.sh <模式代码>

有以下几个模式选项:(模式代码为冒号后面的字母序列)

- 服务器: s
  - 开服务器请务必选这个模式
- 客户端: c
  - 只玩使用这个包的服务器, 请选这个模式
  - 只是为了减少游戏启动时间而做的这个模式
- 单机端(默认选项): sp
  - 完整体验这个包的所有内容, 请选这个模式
  - 可以加入使用这个包的服务器
  - 可以离线模式联机
- 开发端: d
  - 如果想查看 KubeJS 文档, 请选择这个模式
- 核心(初始状态): o
  - 你下载到这个包时候的模式, 仅仅用于打包
  - 可用于加入这个包对应的服务器
  - 当然, 和客户端模式比, 少了许多辅助的 mod, 比如小地图

restart.sh
- - - -

服务器使用的小程序, 可以在服务器崩溃时自动重启服务器.

使用方法, 将启动脚本命名为`run.sh`并和此脚本置于同一文件夹下, 启动此脚本即可.

```shell
sh ./restart.sh <min_stable_running_time>
```

min_stable_running_time: 所启动程序稳定运行的最短时间, 若所启动的程序在最短稳定运行时间内停止运行, 则停止自动重启.

get_whitelist.sh
- - - -

用于自动从远端 git 同步白名单, 还在开发当中, 需要提前设置 git remote

加入服务器
-------

加入使用此包的服务器, 请使用客户端模式或单机端模式

建议配置
---------

64-bit CPU, Java 8

RAM 6G(4G+) for 单机, 4G(3G+) for 玩服务器, 8G(6G+) for 开服务器

模组列表
-------

- 工具装备向
  - Tinkers' Construct
    - plus TiC
    - Construct Armory
      - Armory Expansion
    - Tinkers' Tool Levelling
  - Abyssal Craft
    - Abyssal Integration
  - Cyberware
  - Immersive Engineering
  - Ice and Fire
  - Apotheosis
- 冒险向
  - Ice and Fire
  - Abyssal Craft
  - Extra Utilities 2
  - Twilight Forest
  - Bountiful
- 饮食向
  - Spice of Life
  - Pam's Harvestcraft
    - Pam's Cookables
  - Cooking For Blockheads
  - Nutrition
- 难度向
  - Epic Siege
  - Inferno Mobs
  - Ice and Fire
  - Spice of Life
  - Nutrition
  - Craft Tweaker2
  - Scaling Health
  - Tinkered Hegemony
- 科技向
  - Immersive Engineering
  - Project Red
  - Open Computers
    - Open Screens
  - Open Modular Turrets
  - Extra Utilities 2
  - OpenBlocks
- 魔法
  - Electroblob's Wizardry
- 装饰
  - Immersive Engineering
  - Chinese Workshop
  - Biomes'O Plenty
  - Cosmetic Armor Reworked
  - Armourer's Workshop
  - Architechture Craft
  - Waystones
  - Sign Post
  - Chisels & Bits
  - Baubles
- 存储
  - Ender Storage
  - Colossal Chest
- 实用
  - Akashic Tome
  - Better Builder Wands
  - FTB Quests
  - FTB Utilities
  - Waystones
  - Sign Post
  - Equal Dragons
  - Admin Shop
  - Simple Login
  - Pet Bat
  - Hunting Dim
- 辅助
  - JEI
    - JECH
    - JEHC
    - Just Enough Calculation
  - Classic Bars
  - Better HUD
  - Journey Map
  - Craft Tweaker2
    - Content Tweaker
  - The One Probe
  - Smooth Font
  - Surge
  - Foamfix
  - I18n Update Mod
  - Custom Skin Loader
  - Custom Starting Gear
  - Inventory Tweaks
  - No More Recipe Conflict
  - Dynmap
- Client Only
  - Better HUD
  - JourneyMap
  - JECH
  - Smooth Font
  - Foamfix
  - I18n Update Mod
  - Optifine (**高危**)
  - Classic Bars
  - Neat
- LIBs 懒得写了

**高危**: 如果游戏崩溃, 请删除mod或更换mod版本, 如果删除后问题没有解决, 请联系作者

重要说明
-------

`你可能觉得不太习惯...`

- 合成配方修改
  - 原版配方修改
    - 原版+匠魂熔炉冶炼矿物产率从1锭/矿降为3粒/矿
    - ~~删除了原版工具的工具特性, 仅保留合成功能~~
      - ~~删除了原版工具和盔甲, 仅保留皮质盔甲~~
      - 原版工具被保留
  - 匠魂冶炼炉矿物产率从2锭/矿降为1锭/矿
  - OpenComputers
    - OpenComputers 中的 OpenOS 系统盘需要使用深渊中物品守门人的精华进行合成
    - 删去 OpenComputers 中的因特网卡的合成表
  - 更多实用设备2
    - 将更多实用设备2的墨鱼指环配方中的黑色染料替换为深渊的珊瑚珍珠
    - 将更多使用设备2的彩虹发电机的上下部分配方中的共振红石水晶替换为深渊的守门人的精华
    - ~~删除了量子采石场相关方块的合成表~~
      - 直接移除了量子采石场
      - 甚至连量子采石场维度也移除了
  - 消除了一部分合成表冲突
    - ~~深渊国度的铁盘 vs 沉浸工程的铁棒~~
    - ~~开放式电脑的磁盘 vs 冰与火的铁链~~
    - 使用了 NoMoreRecipeConflict 模组消除合成冲突
  - 盆栽mod中的盆栽现在需要用砖块而不是砖头来合成了

- 游戏性修改
  - 关闭 Epic Siege Mod 中 Creeper Jockey 的特性
  - Epic Siege Mod 中怪物索敌半径从64下降到32
  - 去除 Inferno Mobs 精英怪战利品表中的原版钻石/皮革装备
  - Cyberware 免疫抗性上限从100上调至125
  - 关闭 Inferno Mobs 的Sticky特性
  - 关闭 Ice and Fire 中小精灵偷东西的特性
  - 床现在不能用来跳过夜晚了, 只能用来设置重生点 (Epic Siege Mod)
  - 所有的末影龙生而平等 (Equal Dragons)
  - 匠魂工具和装备的最高等级为2 (Tinker's Tool Levelling)
  - 初始装备 (Custom Starting Gears)
    - 匠魂石剑
    - 匠魂石斧
    - 匠魂石镐
    - 匠魂石铲
    - 皮质盔甲一套
    - 阿卡什宝典 - 包含除死灵之书以外的所有模组指导书
  - 火龙和冰龙的生成率提高至默认设置的1.5倍
  - 龙炎钢和龙霜钢的材料属性有所调整
    - 基础耐久为默认的 25%
    - 基础伤害为默认的 80%
  - 将使用珊瑚珍珠而不是钻石来开启暮色森林传送门
  - Apotheosis
    - 关闭了Apotheosis对原版刷怪笼的修改
    - 关闭了Apotheosis对原版怪物的增强

前排提示
-------

- Scaling Health 对 PVE 的更改
  - $$怪物血量上限=基础血量上限+\frac{玩家难度\times维度难度乘子\times血量上限乘子\times(1+2\cdot rand(0,1))}{20+\max(0, 基础血量上限-20)\times血量修改模式}$$
  - 血量上限最大为1024
  - 难度上限为500
  - 玩家难度改变量
    - 击杀敌对生物: -0.6
    - 击杀 Blight(身上冒紫火的): -7.5
    - 击杀特殊实体将导致不一样的难度变化
      |实体|ID|击杀后难度变化|击杀 Blight 后难度变化
      |----|--|-----------|------------------
      |恐惧傀儡|abyssalcraft:dreadgolem|-0.5|-3.0
      |恐惧守卫|abyssalcraft:dreadguard|+0.5|-3.0
      |小型修格斯|abyssalcraft:lessershoggoth|-0.5|-2.0
      |阴影生物|abyssalcraft:shadowcreature|+0.5|-1.0
      |阴影野兽|abyssalcraft:shadowbeast|+0.5|-1.0
      |阴影怪兽|abyssalcraft:shadowmonster|+0.5|-1.0
      |阿索拉|abyssalcraft:dragonboss|-7.0|-7.0
      |查加罗斯|abyssalcraft:chagaroth|-10.0|-10.0
      |守门人扎哈尔|abyssalcraft:jzahar|-12.0|-12.0
      |火龙|iceandfire:firedragon|-10.0|-10.0
      |冰龙|iceandfire:icedragon|-10.0|-10.0
      |僵尸猪人|minecraft:zombie_pigman|+1.0|-2.0
      |末影人|minecraft:enderman|+1.5|-3.0
      |村民|minecraft:villager|+3.0|+3.0
    - 在线: +0.0015/s(5.4/h)
      - 如果玩家处于静止: +0.0010/s(3.6/h)
    - 死亡: +0.0/次
  - 不同维度在计算难度时会有不同的基础难度
    |维度|ID|基础难度|
    |----|--|---|
    |漆黑世界|-11325| +10|
    |下界|-1| +50|
    |主世界|0|0|
    |末地|1| +75|
    |暮色森林|7| +100|
    |深渊|50| +25|
    |恐惧之地|51| +35|
    |奥穆索|52| +95|
    |深渊黑暗维度|53| +55|
    |狩猎维度|28885| +70|
  - 睡觉: +8/次
    - 因为只有利用bug才能睡觉, 而我不想让玩家利用这个bug
    - 只有夜晚被睡觉跳过时才会增加难度
  - 月相影响难度:
    - $\times1.5$ --- 满月
    - $\times1.3$
    - $\times1.2$
    - $\times1.0$
    - $\times0.8$ --- 新月
    - $\times1.0$
    - $\times1.2$
    - $\times1.3$
  - 难度影响玩家受到的伤害: 伤害倍数 $= 1 + 0.02\times$个人难度, 最大为正常的 11.0 倍
- Epic Siege Mod 的"血月"
  - 当满月时, 会出现"血月"现象
  - 所有怪物的血量会增加, 生成几率也会提高
- Ice and Fire
  - 冰龙、火龙只应该出现于主世界、奥穆索、漆黑世界维度和狩猎维度, 请腐竹自查
  - 冰龙和火龙任何时候都互相敌对, 请养龙玩家注意不要把它们放在一起养, 以避免不必要的损失
  - 有些敌对生物(主要是 Ice and Fire 的生物)在 Journey Map 小地图上的图标与中立生物一样
- Admin shop 中可以出售能量换取金钱, 兑换率为 32768 RF/$
- 匠魂浮空岛只能出现在主世界和暮色森林世界
- 附魔等级上限和铁砧等级上限已被 Apotheosis 模组修改

未来版本计划
------------

- 加入针对暮色森林的魔改
- 完善任务树
  - 大概计划
    - [ ] 装备线
      - [x] 匠魂
        - [x] 发展线
        - [x] ~~TAIGA~~
        - [x] Ice and Fire 龙钢
      - [ ] 神话附魔
        - [ ] 发展线
    - [ ] 工业线
      - [ ] IE
      - [ ] OpenComputers
    - [x] 魔法线
      - [x] Electroblob's Wizardry
    - [ ] 冒险线
      - [ ] 原版
      - [ ] Ice and Fire
      - [x] 深渊
      - [ ] 暮色森林
    - [ ] 挑战
      - [x] 统计
        - [x] 击杀敌对生物数 (所有生物都要有, 包括Boss)
        - [x] 存活时间
        - [x] 死亡次数
        - [x] 放置方块 ("这世界我来过") by ShuiFeng_Keith
        - [x] 受到伤害总和 by quraks
        - [x] ~~抵抗伤害总和 by quraks~~
        - [x] 各种移动方式的距离 (100km量级) by mcer
        - [x] 与村民交易次数 by Stark
      - [ ] 成就
        - [x] Minecraft
          - [x] 探索的时光
        - [x] BOP
          - [x] 走遍BOP的每一个群系 by akarin
        - [ ] Pam's Harvestcraft
          - [ ] 吃过所有食物 ("舌尖上的MC") by ShuiFeng_Keith
        - [ ] IE
          - [ ] 用工程师天钩在电线上移动超过2000m ("观光缆车") by akarin
        - [x] ExU
          - [x] 合成一定数量的不稳定金属锭 by quarks, akarin
          - [x] 合成彩虹发电机 by Stark
          - [x] 完美的 Optium 核心 by Stark
        - [x] 暮色森林
          - [x] 集齐暮色 boss 战利品 by Stark
        - [x] Electroblob's Wizardry
          - [x] 认识所有法术 ("魔法，为我而存在") by ShuiFeng_Keith
          - [x] 集齐所有饰品
        - [ ] Apotheosis
          - [ ] 提交160级单项附魔书各一本 by ShuiFeng_Keith
      - [ ] 其他
        - [ ] 只剩 1% 的生命 by quarks, ShuiFeng_Keith
        - [ ] 只剩 0.25 以下的生命, 且未死亡 by quarks ("截个图吧")
        - [ ] 单次伤害 665.5 ~ 666.5 点 ("恶魔转世") by ShuiFeng_Keith
        - [ ] 保持珊瑚浸染状态超过100s by akarin ("凝视深渊" by ShuiFeng_Keith)
        - [x] 发现温泉
        - [ ] 合成一个恶魔生物, 再杀死一个恶魔生物 ("对不起, 我想做个好人") by akarin
      - [ ] 恶搞
        - [ ] 被一只鸡杀死 by akarin
        - [ ] 被电死 by quarks ("双刃剑(Text:"大人, 时代变了" by akarin)" by ShuiFeng_Keith)
        - [x] 在主世界掉出世界 by quarks ("虚假的基岩" by ShuiFeng_Keith)
        - [x] 扔 1024 个 EFLN by quarks
    - [x] 特殊合成
      - [x] 骏鹰蛋换色
      - [x] 龙蛋换色

鸣谢
------

- USTC-Minecraft 群里的各位
  - Pentyum for providing the USTC server.
  - akarin, ShuiFeng_Keith, quarks, Stark for providing ideas about challenges
- 来自朋友的支持
  - MZH for helping me on cmd and bash coding.
- 来自Discord的支持
  - LatMod Industries Server for teaching me using KubeJS
- Modders for creating such entertaining mods
- Forge team for creating Forge API
- Mojang for creating the game
