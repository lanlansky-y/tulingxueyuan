#Django Rest Framework(DRF)
##Rest
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
##DRF的主要任务    
    - 案例：TlxyDRF
        - django-admin startproject TlxyDRF
        - python manage.py startapp case01
        - 配置settings(app)
        - 配置urls
        - 创建三个模型：Student, Teacher, Classroom
        - 创建序列化器
        - 创建视图聚合
##序列化
    - 序列化：把系统运行中的一些实例等转换成一种可直接表示出来的格式，用来保存、传输等
    - 反序列化：序列化的反操作   
    练习2：
    创建项目 DRF2
    创建app MySer
    配置settings
##serializer的类型的参数
    - read_only:仅用于序列化输出
    - write_only:仅用于反序列化输入
    - required:反序列化时必须输入，默认是True
    - allow_null:允许传入None
    - validators:使用验证器
##创建serializer对象和使用
    - 构造方法
        Serializer(instance=None, data=empty, **kwarg)
    - 反序列化        
        - 验证
            - is_valid:
                - 验证数据是否合法，返回boolean
                - 在使用从外部传入的数据之前，必须使用此函数进行验证
                - 如果验证失败，返回数据错误异常
            - validated_data:
                - 经过验证后的数据，存入此结构
    - 视图
        - DRF的视图从处理任务到处理流程等跟Django基本一致
        - 此视图基本是django视图的扩展   
        - Request
            - 把请求解析成一个request实例
            - 属于DRF的， 跟django的HttpRequest不太一样
            - 在得到Request之前有一个Parse对传入的数据请求进行解析
            - data属性
                - 请求数据体，类似于Django的request.POST, request.FILES
                - 在DRF中主要指的是Json
            - query_params
                - 所有传入的关键字 
    - Response
        - rest_framework.response.Response
        - 用renderer渲染器对返回内容进行渲染
    - 返回的构造方式
        return Response(data, status=None, template_name=None, headers=None, content_type=None)
        data:返回的数据
        status:返回的状态码
            1xx:信息告知
            2xx:成功
            3xx:重定向
            4xx:请求错误
            5xx:服务器错误   
    - 视图类
        APIView
            - rest_framework.views.APIView
            - 是django中view的子类
            - 跟View有不同的地方
                - 传入传出数据用的是drf的请求和反馈类
                - 会引发并处理APIException
                - 在dispatch之前，会进行身份验证，权限检查，流量控制
            - 支持的属性有
                - authentication_classes:列表或者元祖，身份验证类
                - permisson_classes:进行权限验证
                - throttle_classes:流量控制