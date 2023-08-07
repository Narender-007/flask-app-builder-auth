from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
from flask import request
from flask_appbuilder.api import BaseApi, expose, rison
from flask_appbuilder.security.decorators import protect
from . import appbuilder


class ExampleApi(BaseApi):

    resource_name = 'example'

    @expose('/greeting',methods=['POST', 'GET'])
    @rison()
    # @protect()
    @protect(allow_browser_login=True)
    def greeting(self, **kwargs):
        if 'name' in kwargs['rison']:
            return self.response(200, message="Hello "+str(kwargs['rison']['name']))
        else:
            return "wroinn"


class MyApi(BaseApi):
    resource_name = 'example'
    @expose('/dosonmething', methods=['GET'])
    # @protect(allow_browser_login=True)
    # @safe
    def do_something(self):
        pass
        return "wroinn"

    @expose('/dosonmethingelse', methods=['GET'])
    # @protect()
    # @safe
    def do_something_else(self):
        pass
        return "wroinn"

appbuilder.add_api(ExampleApi)
appbuilder.add_api(MyApi)
db.create_all()
