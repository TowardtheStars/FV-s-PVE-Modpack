@echo off
    title Modpackģʽѡ����
    echo ==========================
    echo ��ѡ��modpackģʽ

    dir /b .\mods\ | findstr "\[[C|D|L|S]\].*\.jar" >> temp.del
    for /F "delims=" %%a in ('type "temp.del"') do if exist ".\mods\"%%a del ".\mods\"%%a
    del temp.del

:errored
    echo ==========================
    echo ������: s
    echo �ͻ���: c
    echo ������(Ĭ��ѡ��): sp
    echo ������: d
    echo ��ʾ��ϸ��Ϣ: h
    echo ==========================

:select
    set mode=sp
    set /p mode=������ģʽ����: 
    set client=0
    if %mode%==s echo ����ѡ��: ����� && echo ���ڸ����ļ�... && goto :server
    if %mode%==c echo ����ѡ��: �ͻ��� && echo ���ڸ����ļ�... && set client=1 && goto :client
    if %mode%==d echo ����ѡ��: ������ && echo ���ڸ����ļ�... && goto :dev
    if %mode%==h goto :help

    echo ����ѡ��: ������
    echo ���ڸ����ļ�... 
    goto :lan

:help
    echo [s]�����: ����˵�mod����
    echo [c]�ͻ���: ���������, ֻ�������ӷ���˵�mod����
    echo [l]������: ���Խ��е�����Ϸ, �����������������mod����(����ģʽ)
    echo [d]������: ���ڱ�mod��������mod����
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
    echo �������
    pause



