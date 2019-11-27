@echo off
    title Modpack模式选择器
    echo ==========================
    echo 请选择modpack模式

    dir /b .\mods\ | findstr "\[[C|D|L|S]\].*\.jar" >> temp.del
    for /F "delims=" %%a in ('type "temp.del"') do if exist ".\mods\"%%a del ".\mods\"%%a
    del temp.del

:errored
    echo ==========================
    echo 服务器: s
    echo 客户端: c
    echo 单机端(默认选项): sp
    echo 开发端: d
    echo 显示详细信息: h
    echo ==========================

:select
    set mode=sp
    set /p mode=请输入模式代码: 
    set client=0
    if %mode%==s echo 您已选择: 服务端 && echo 正在复制文件... && goto :server
    if %mode%==c echo 您已选择: 客户端 && echo 正在复制文件... && set client=1 && goto :client
    if %mode%==d echo 您已选择: 开发端 && echo 正在复制文件... && goto :dev
    if %mode%==h goto :help

    echo 您已选择: 单机端
    echo 正在复制文件... 
    goto :lan

:help
    echo [s]服务端: 服务端的mod配置
    echo [c]客户端: 与服务端相对, 只可以链接服务端的mod配置
    echo [l]单机端: 可以进行单机游戏, 并可以与好友联机的mod配置(离线模式)
    echo [d]开发端: 用于本mod包开发的mod配置
    goto :select

:dev
    xcopy /Q .\mods\dev\*.jar .\mods
:lan
    xcopy /Q .\mods\sp_lan\*.jar .\mods
:client
    xcopy /Q .\mods\client\*.jar .\mods
    if %client%==1 goto :finished
:server
    xcopy /Q .\mods\server\*.jar .\mods
:finished
    echo 配置完毕
    pause



