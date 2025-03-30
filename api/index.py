from flask import Flask, Response
import os
import sys

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 从主应用导入app
from app import app

# Vercel需要的处理函数
def handler(request):
    return app(request.environ, lambda status, headers, exc_info=None: Response(None, status, headers))
    
# 直接导出app对象
application = app 