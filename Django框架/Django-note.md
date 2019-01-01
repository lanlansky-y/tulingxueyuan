#Django系统
    -环境
        python3.6
        django1.8
    -参考资料：
        http://python.usyiyi.cn/
        django架站的16堂课
##环境搭建
    anaconda+pycharm
    anaconda使用：
        conda list:显示当前环境安装的包
        conda env list:显示安装的虚拟环境列表
        conda create -n env_name python=3.6:
        创建一个名字为env_name的虚拟环境，并且此环
        境使用python3.6解释器
        激活conda的虚拟环境：
            source activate env_name(Linux)
            activate env_name(windows)
        pip install django=1.8
        
##后台需要的流程


##创建第一个django程序
    命令行启动：
        django-admin startproject tulingxueyuan
        cd tulingxueyuan
        python manage.py runserver
    pycharm启动：
        需要配置
    
##创建app：
    app:负责一个具体业务或者一类具体业务的模块
    python manage.py startapp teacher(创建一个名字为teacher的app)
    
##路由
    按照具体的请求url，导入到相应的业务处理模块的一个功能模块
    django的信息控制中枢
    本质上是接收的url和相应的处理模块的一个映射
    在接收url请求的匹配上使用了RE
    url的具体格式如urls.py中所示
    需要关注两点：
        1.接收的url是什么， 即如何用RE对传入url进行匹配
        2.已知url匹配到哪个处理模块
    url匹配规则：
    
    正常映射：
        把某一个符合RE的url映射到事物处理函数中去
        
##Views 视图
###手动编写视图   
    -实验目的：
        利用django快捷函数手动编写视图处理函数
        编写过程中理解视图运行原理
    -分析：
        - django把所有的请求信息封装入request
        - django通过urls模块把相应请求跟事件处理函数连接起来，
          并把request作为参数传入
        - 在相应的处理函数中，我们需要完成两部分
            - 处理业务
            - 把结果封装并返回，我们可以使用简单的HttpResponse，
              同样也可以自己处理此功能
        -本案例不介绍业务处理，把目光集中在如何渲染结果并返回
    案例：teacher_app/views/render_test(render2_test、render3_test)

###系统内建视图  
    系统内建视图可以直接使用
 
##Models 模型
    -ORM(Object Relation Map)
    -django链接数据库
        -自带默认数据库Sqlite3
            -关系型数据库
            -轻量级
        -建议开发用sqlite3, 部署用mysql之类的数据库
        -切换数据库在settings中进行设置
    django连接mysql:
        DATABASES = {
            'default' : {
            'ENGINE':'django.db.backends.mysql',
            'NAME':'数据库名',
            'PASSWORD':'数据库密码',
            'HOST':'127.0.0.1',
            'PORT':'3306',
        } 
        }  
    需要在项目文件下的__init__文件中导入pymysql包
##查看数据库中的数据
    1.启动命令行：python3 manage.py shell
        ps:对orm的操作分为静态函数和非静态函数两种
    2.在命令行中导入对应的映射类
        from 应用.models import 类名
    3.使用objects属性操作数据库。objects是模型中实际和数据库
    进行交互的
    4.查询命令
        - 类名.objects.all()查询数据库表中的所有内容，返回的
        结果是一个Query
        - 类名.objects.filter(条件)
##models类的使用
    -定义和数据库表映射的类
        -在应用中的models.py文件中定义class
        -所有需要使用ORM的class都必须是models.Model的子类
        -class中的所有属性对应表格中的字段
        -字段的类型都必须使用models.xxx不能使用python中的类型
        -字段常用参数：
            1.max_length:规定数值的最大长度
            2.blank:是否允许字段为空，默认不允许
            3.null:在DB中控制是否保存为null，默认为false
            4.default:默认值
            5.unique:唯一
            6.verbose_name:假名
    -数据库的迁移
        1.在命令行中，生成数据迁移的语句(生成sql语句)
            python3 manage.py makemigrations
                 
        2.在命令行中，输入数据迁移的指令(执行sql语句)
            python3 manage.py migrate
        
        ps:如果迁移中出现没有变化或者报错，可以尝试强制迁移
            强制迁移命令：
                python3 manage.py makemigrations 应用名(APP的名称)
                python3 manage.py migrate 应用名(APP的名称)
        
        3.对于默认数据库，为了避免出现混乱，如果数据库中没有数据，
        可以将自带的sqlite3数据库删除
    -常见查找方法
        1.通用查找格式：属性名__(用下面的内容) = 值
            - gt：大于
            - gte：大于等于
            - lt：小于
            - lte：小于等于
            - range：范围
            - year：年份
            - isnull：是否为空
        2.查找等于指定值的格式：属性名 = 值
        3.模糊查找：属性名__(使用下面的内容) = 值
            - exact：精确等于
            - iexact：不区分大小写
            - contains：包含
            - startwith：以...开头
            - endwith：以...结尾
    - 数据库表关系
        多表联查：利用多个表联合查找某一项信息或者多项
        信息
        1:1：OneToOne
    - 建立关系：在模型任意一边即可，使用OneToOne
    - add:
        添加没有关系的一边，直接实例化保存就可以
        >>> s = School()
        >>> s.School_id = 1
        >>> s.School_name = 'tulingxueyuan'
        >>> s.save()
        
        添加有关系的一边，使用create方法或者使用实例化然后save
        1.
            >>> m = Manager.objects.create(manager_id=2, 
            manager_name="dana", my_school=s[0])
            
        2.
            >>> m = Manager()
            >>> m.manager_id = 2
            >>> m.manager_name = "dana"
            >>> m.my_school = s
            >>> m.save()    
        - query(查询):
            1.由子表查母表，由子表的属性直接提取信息:
                >>> m = Manager.objects.get(manager_name='dana')
                >>> m
                >>> m.my_school
                >>> <School:nanjingtulingxueyuan>
            2.由母表查子表：
                >>> s = School.objects.get(manager__manager_name='dana')
                >>> s
                >>> <School:nanjingtulingxueyuan>
        - change(修改):
            - 单个修改使用save:
                >>> s.school_name = '南京图灵学院'
                >>> s.save()
            - 批量修改使用update
        - delete:直接使用delete删除
        
        1:N：OneToMany
            - 一个表格的数据项/对象等，可以对应多个另一个表格的
            数据项(比如一个学校可以有很多个老师，但一个老师只能
            在一个学校里上班)
            - 使用：
                使用ForeignKey
                在多的那一边，比如上班的例子就是在Teacher的表
                格里进行定义
            Add:
                - 跟一对一方法类似，通过create和new来添加
                - create:把属性都填满，不需要手动保存
                    t = Teacher.objects.create(teacher_name="刘二拿", my_school=ss[0])
                - new:属性或者参数可以为空，但必须使用save保存
            Query:
                        
        N:N：ManyToMany 
            - 表示任意一个表的数据可以拥有对方表格
            多项数据，反之亦然
            - 比如：典型的例子就是老师和学生的关系
            - 使用上，在任意一方，使用ManyToMany定义，
            只需要定义一边
            - Add:
                - 添加老师：student.teachers.add()
            - query:
                - 跟一对多类似，使用_set查询        
##模板系统                
    - 模板：一组相同或者相似的页面，在需要个性化的地方
    进行留白，需要的时候只是用数据填充就可以使用了
    - 步骤：
        1.在settings中进行设置：TEMPLATES
            在settings中的TEMPLATES中的DIRS中添加:
            os.path.join(BASE_DIR, 'templates')
            #上面的意思是告诉django,在当前项目目录下查
            找叫templates的文件夹，下面都是我的模板
        2.在templates文件夹下编写模板并调用
    - 模板中的变量
        - 变量的表示方法：{{name}}    
        - 在系统调用模板的时候，会用相应的数据查找相应的
        变量名称，如果能找到，则填充或者叫渲染，否则跳过
    - 模板中的标签
        - for标签：{% for .. in .. %} 
        - 用法：
            {% for .. in .. %}  
                循环语句
            {% endfor %} 
        - 案例：three,显示班级成绩
        - if标签
        - 用来判断条件  
        - 代码示例：
            {% if 条件 %}
                条件成立执行语句
            {% elif 条件 %}
                条件成立执行语句
            {% else %}
                以上条件都不成立执行语句
            {% endif %}   
        案例：four  
        
#Session
    - 为了应对HTTP协议的无状态性
    - 用来保存用户比较敏感的信息
    - 属于request的一个属性
    - 常用操作：
        - request.session.get(key, defaultValue)
        - request.session.clear():清楚session中的全部值
        - request.session[key] = value:赋值
        - request.session.flush():删除当前会话且清楚会话的cookie
        - del request.session[key]
        
#分页
    - django提供现成的分页器用来对结果进行分页
    - from django.core.paginator import Paginator

#基于类的视图
    - 可以针对http协议不同的方法创建不同的函数
    - 可以使用Mixin等opp技术
    - Mixin
        - 把来自父类的行为或者属性组合在一起
        - 解决多重继承的问题    
    - ListView
     
#admin  