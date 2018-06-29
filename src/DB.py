from webapp import db


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actorname = db.Column(db.String(20), unique=True, nullable=False)
    frameno = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    x = db.Column(db.String)
    y = db.Column(db.String)
    z = db.Column(db.String)
    w = db.Column(db.String)

    # def __repr__(self):
    #     return "User('{self.actorname}', '{self.frameno}', '{self.image_file}','{self.x}','{self.y}','{self.z}','{self.w}')"