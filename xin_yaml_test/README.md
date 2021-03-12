##依赖
##### pytest 
##### allure

###目录：
#####action：
行为,主要包括执行和执行检查。执行通过api实现，检查包括数据库检查 例：
create_user : 调用创建用户
check_user: 数据库查找 用户表，用户信息表，资产表等信息是否正常

#####case：
用例，包括所有的用例

#####db
数据库，不同库执行层

#####
request，api执行层

#####
conftest， 配置文件

#####测试库端口映射
ssh 

数据库  ：  127.0.0.1         dev         h~,o(l=4#aiVOgBB

#####redis端口映射

ssh -C -f -N -g  -L 6379:127.0.0.1:6379   root@47.241.10.122   

