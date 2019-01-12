#Django Rest Framework(DRF)
##1.Rest
    - 前后端分离
    - API:Application Programming Interface
        - 为了应付千变万化的前端需求
    - Rest:Repres State Trans
        - Restful:遵守Rest规范的技术设计的软件可以称为Restful
    - Rest规范
        - URL代表一个资源，一个资源是一个名词
        - 动作有HTTP的method方法提供
        - URL应该包含版本信息，版本信息也可以放在HTTP协议中
        - 过滤信息，使用URL的参数代表过滤
        - 返回值：每一个返回代码都有具体特殊含义
        - 返回格式：推荐固定具体格式
##Django Rest Framework官网    
    https://q1mi.github.io/Django-REST-framework-documentation/
    - 安装：pip install djangorestframework
    - 版本问题：version3.7是基于1.xx版本的django，之后是基于2.xx版本的django
    - django_filter依赖djangorestframework 3.7