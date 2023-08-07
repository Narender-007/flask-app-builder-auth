from flask import Flask
from flask_appbuilder import AppBuilder, expose, has_access
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECURITY_TRACKABLE'] = True

db = SQLAlchemy(app)
appbuilder = AppBuilder(app, db.session, security_manager_class=SecurityManager)
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String
from flask_appbuilder.security.sqla.models import User

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from flask_appbuilder.security.sqla.models import Role

class MyRole(Role):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

    def __repr__(self):
        return self.name
    
from flask_appbuilder import BaseView, expose, has_access
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask import request, jsonify

class RoleView(BaseView):
    route_base = "/api/roles"

    @expose("/", methods=["POST"])
    @has_access
    def create_role(self):
        name = request.json.get("name")

        if not name:
            return jsonify({"error": "Role name is required."}), 400

        role = MyRole(name=name)
        db.session.add(role)
        db.session.commit()

        return jsonify({"message": "Role created successfully."})

    @expose("/", methods=["GET"])
    @has_access
    def list_roles(self):
        roles = db.session.query(MyRole).all()
        return jsonify({"roles": [role.name for role in roles]})

appbuilder.add_view_no_menu(RoleView())

