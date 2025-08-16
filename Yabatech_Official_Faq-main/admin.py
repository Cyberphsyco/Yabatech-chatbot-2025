from flask import session , redirect , url_for , request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from db import db_session, QuestionsAndAnswers , NotAnswerdQuestions 

class SecuredModelView(ModelView):
    def is_accessible(self):
        return session.get("logged_in")
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login' ,next=request.url))
def init_admin(app):
    admin = Admin(app,name="Chatbot Admin" , template_mode="bootstrap4")
    admin.add_view(SecuredModelView(QuestionsAndAnswers,db_session))
    admin.add_view(SecuredModelView(NotAnswerdQuestions,db_session))
    return admin
