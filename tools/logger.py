# author:lee:2021/8/5 0005 17:00
'''
三大块
1.日志器   日志的入口，然后往里面写，比如：日记本
  debug(调试级别)  info(信息级别)  warnning(警告级别) error(错误级别)  critical(致命的 严重的) ---> 级别越来越高
  原则：设置的级别，比它高的都会显示出来，比它低级的不会显示
2.格式器   以什么样的格式去写这个日志
3.处理器   表示对日志内容的一个处理方式，比如可以直接把日志输出到console里，或者输出到文件里面
'''
# 导包 把日志模块和处理器都一并导入进来
import logging.handlers
from Testfan.apiFrame import config
class GetLogger:
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger == None:
            # 1.获取日志器  日记本g
            cls.logger = logging.getLogger()

            # 给日志器设置总的级别  级别封装在logging里
            # 设置错误级别,大写
            cls.logger.setLevel(logging.INFO)

            # 2.获取格式器
            # 2.1 定义要输出的样式
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'

            # %(name)s Logger的名字
            # %(levelname)s 文本形式的日志级别
            # %(filename)s 调用日志输出函数的模块的文件名
            # %(lineno)d 调用日志输出函数的语句所在的代码行
            # %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”
            # %(message)s 用户输出的消息
            # 2.2 获取格式器 参数 具体要输出什么样的样式
            fm = logging.Formatter(fmt)

            # 3. 获取处理器
            # TimedRotatingFileHandler 按时间切割的文件处理器   如：一小时生成一个文件
            # 工作中一般用 midnight
            tf = logging.handlers.TimedRotatingFileHandler(filename=f'{config.ABS_PATH}/logger/test.log',when='midnight',interval=1,backupCount=3,
                                                      encoding='utf-8')

            # 在处理器中添加格式器
            tf.setFormatter(fm)

            # 给处理器设置级别
            # tf.setLevel(logging.INFO)

            # 在日志器中添加处理器
            cls.logger.addHandler(tf)

        return cls.logger


if __name__ == '__main__':
    # 测试日志调用的时候
    GetLogger().get_logger().debug('调试')
    GetLogger().get_logger().info('信息')
    GetLogger().get_logger().warning('警告')
    GetLogger().get_logger().error('错误')
    GetLogger().get_logger().critical('致命d')