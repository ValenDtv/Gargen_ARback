import sqlalchemy as al
from sqlalchemy.ext.declarative import declarative_base

# Create your models here.
Base = declarative_base()


class Users(Base):
    __tablename__ = 'ruser'
    userid = al.Column("userid", al.Integer, primary_key=True)
    login = al.Column("login", al.String)
    password = al.Column("password", al.String)
    email = al.Column("email", al.String)
    coins = al.Column("coins", al.Integer)

    def __init__(self, login, password, email, coins):
        self.login = login
        self.password = password
        self.email = email
        self.coins = coins


class Plantstype(Base):
    __tablename__ = 'splantstype'
    plantstypeid = al.Column("plantstypeid", al.Integer, primary_key=True)
    file = al.Column("file", al.String)
    fetus = al.Column("fetus", al.String)
    max_points = al.Column("max_points", al.Integer)
    name = al.Column("name", al.String)
    seed_price = al.Column("seed_price", al.Integer)
    fetus_price = al.Column("fetus_price", al.Integer)
    fetus_min = al.Column("fetus_min", al.Integer)
    fetus_max = al.Column("fetus_max", al.Integer)

    def __init__(self, file, fetus, max_points, name, seed_price, fetus_price, fetus_min, fetus_max):
        self.file = file
        self.fetus = fetus
        self.max_points = max_points
        self.name = name
        self.seed_price = seed_price
        self.fetus_price = fetus_price
        self.fetus_min = fetus_min
        self.fetus_max = fetus_max


class Сells(Base):
    __tablename__ = 'rcell'
    cellid = al.Column("cellid", al.Integer, primary_key=True)
    userid = al.Column("userid", al.Integer)
    plantid = al.Column("plantid", al.Integer)
    is_dug_up = al.Column("is_dug_up", al.Boolean)
    is_fertilized = al.Column("is_fertilized", al.Boolean)
    weed = al.Column("weed", al.Boolean)
    grass_stage = al.Column("grass_stage", al.Integer)
    dug_up_time = al.Column("dug_up_time", al.DateTime)
    fertil_time = al.Column("fertil_time", al.DateTime)

    def __init__(self, userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time):
        self.userid = userid
        self.plantid = plantid
        self.is_dug_up = is_dug_up
        self.is_fertilized = is_fertilized
        self.weed = weed
        self.grass_stage = grass_stage
        self.dug_up_time = dug_up_time
        self.fertil_time = fertil_time


class Plants(Base):
    __tablename__ = 'rplants'
    plantid = al.Column("plantid", al.Integer, primary_key=True)
    type_id = al.Column("type_id", al.Integer)
    userid = al.Column("userid", al.Integer)
    cell = al.Column("cell", al.Integer)
    stage = al.Column("stage", al.Integer)
    points = al.Column("points", al.Integer)
    thirst = al.Column("thirst", al.Integer)
    bugs = al.Column("bugs", al.Integer)
    create_time = al.Column("create_time", al.DateTime)
    update_time = al.Column("update_time", al.DateTime)

    def __init__(self, type_id, userid, cell, stage, points, thirst, bugs, create_time, update_time):
        self.type_id = type_id
        self.userid = userid
        self.cell = cell
        self.stage = stage
        self.points = points
        self.thirst = thirst
        self.bugs = bugs
        self.create_time = create_time
        self.update_time = update_time


class Products(Base):
    __tablename__ = 'rproduct'
    productid = al.Column("productid", al.Integer, primary_key=True)
    source = al.Column("source", al.Integer)
    type = al.Column("type", al.String)

    def __init__(self, source, type):
        self.source = source
        self.type = type


class Fetus(Base):
    __tablename__ = 'rfetus'
    fetusid = al.Column("fetusid", al.Integer, primary_key=True)
    plant_type = al.Column("plant_type", al.Integer)
    userid = al.Column("userid", al.Integer)
    fetyscount = al.Column("fetyscount", al.Integer)

    def __init__(self, plant_type, userid, fetyscount):
        self.plant_type = plant_type
        self.userid = userid
        self.fetyscount = fetyscount


class Seeds(Base):
    __tablename__ = 'rseed'
    seedid = al.Column("seedid", al.Integer, primary_key=True)
    plant_type = al.Column("plant_type", al.Integer)
    userid = al.Column("userid", al.Integer)
    seedcount = al.Column("seedcount", al.Integer)

    def __init__(self, plant_type, userid, seedcount):
        self.plant_type = plant_type
        self.userid = userid
        self.fetyscount = seedcount
