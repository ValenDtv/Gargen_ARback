from django.shortcuts import render
from django.conf import settings
from sqlalchemy.orm import Session
from sqlalchemy import and_
import jwt
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import datetime
import random
from .models import Users
from .models import Plantstype
from .models import Plants
from .models import Cells
from .models import Products
from .models import Fetus
from .models import Seeds

engine = settings.ENGINE
SECRET_KEY = "Kb4qVFP5m4gQxWKn9tQoIg1qt"
Tokens = {}

# Create your views here.


def authentication(function):
    def check_token(request):
        token = request.META['HTTP_AUTHORIZATION']
        if token in Tokens.keys():
            if (datetime.datetime.now() - Tokens[token]['last_update']).days < 7:
                Tokens[token]['last_update'] = datetime.datetime.now()
                return function(request, Tokens[token]['userid'])
                # return function(request)
            else:
                Tokens.pop(token)
                response = {'authentication': False}
                response = json.dumps(response, ensure_ascii=False, default=str)
                return HttpResponse(response)
        else:
            response = {'authentication': False}
            response = json.dumps(response, ensure_ascii=False, default=str)
            return HttpResponse(response)
    return check_token


@csrf_exempt
@authentication
def garden(request, ruserid):
    if request.method != 'GET':
        return HttpResponse("Invalid request method")
    # request_data = json.loads(request.body)
    # ruserid = userid
    # ruserid = request.GET.get('userid', 0)
    session = Session(bind=engine)
    for plant in session.query(Plants).filter(Plants.userid == ruserid):
        update_plant(plant, session)
    response = {
        'authentication': True,
        'coins': session.query(Users).filter(Users.userid == ruserid).first().coins,
        'plants_type': [
            {
                'id': instance.plantstypeid,
                'file': instance.file,
                'fetus': instance.fetus,
                'max_points': instance.max_points,
                'name': instance.name,
                'seed_priсe': instance.seed_price,
                'fetus_price': instance.fetus_price,
                'fetus_min': instance.fetus_min,
                'fetus_max': instance.fetus_max
            } for instance in session.query(Plantstype)
        ],
        'plants': [
            {
                'id': instance.plantid,
                'type_id': instance.type_id,
                'userid': instance.userid,
                'cell': instance.cell,
                'stage': instance.stage,
                'points': instance.points,
                'thirst': instance.thirst,
                'bugs': instance.bugs,
                'create': instance.create_time,
                'update': instance.update_time
            } for instance in session.query(Plants).filter(Plants.userid == ruserid)
        ],
        'cells': [
            {
                'id': instance.cellid,
                'userid': instance.userid,
                'plant': instance.plantid,
                'is_dug_up': instance.is_dug_up,
                'is_fertilized': instance.is_fertilized,
                'weed': instance.weed,
                'grass_stage': instance.grass_stage,
                'dug_up_time': instance.dug_up_time,
                'fertil_time': instance.fertil_time
            } for instance in session.query(Cells).order_by(Cells.cellid).filter(Cells.userid == ruserid)
        ],
        'store': [
            {
                'source': instance.source,
                'type': instance.type
            } for instance in session.query(Products)
        ],
        'stock': [
            {
                'plant_type': instance.plant_type,
                'count': instance.fetyscount
            } for instance in session.query(Fetus).filter(Fetus.userid == ruserid)
        ],
        'seeds': [
            {
                'plant_type': instance.plant_type,
                'count': instance.seedcount
            } for instance in session.query(Seeds).filter(Seeds.userid == ruserid)
        ]
    }
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
@authentication
def thirst(request, userid):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    response = {'authentication': True, 'success': False, 'thirst': 0}
    session = Session(bind=engine)
    for instance in session.query(Plants).filter(and_(Plants.userid == userid,
                                                 Plants.plantid == request_data['plantid'])):
        if instance.thirst > 0:
            instance.thirst -= 1
            response['success'] = True
        response['thirst'] = instance.thirst
    session.commit()
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
@authentication
def bugs(request, userid):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    response = {'authentication': True, 'success': False, 'bugs': 0}
    session = Session(bind=engine)
    for instance in session.query(Plants).filter(and_(Plants.userid == userid,
                                                 Plants.plantid == request_data['plantid'])):
        if instance.bugs > 0:
            instance.bugs -= 1
            response['success'] = True
        response['bugs'] = instance.bugs
    session.commit()
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
@authentication
def new_plant(request, userid):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    response = {'authentication': True, 'success': False, 'plants': []}
    session = Session(bind=engine)
    seed = session.query(Seeds).filter(and_(Seeds.plant_type == request_data['type_id'],
                                            Seeds.userid == userid)).first()
    cell = session.query(Cells).filter(Cells.cellid == request_data['cellid']).first()
    if seed.seedcount < 1:
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    elif not cell.is_dug_up:
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    else:
        response['success'] = True
        seed.seedcount -= 1
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        n_plant = Plants(request_data['type_id'], userid, request_data['cellid'], 1, 0, 0, 0,
                         time, time)
        session.add(n_plant)
        session.commit()
        plant = session.query(Plants).order_by(Plants.plantid.desc()).first()
        cell.plantid = plant.plantid
        session.commit()
        response['plants'].append({
            'id': plant.plantid,
            'type_id': plant.type_id,
            'userid': plant.userid,
            'cell': plant.cell,
            'stage': plant.stage,
            'points': plant.points,
            'thirst': plant.thirst,
            'bugs': plant.bugs,
            'create_time': plant.create_time,
            'update_time': plant.update_time
        })
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)


@csrf_exempt
@authentication
def seed_purchase(request, userid):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    session = Session(bind=engine)
    planttype = session.query(Plantstype).filter((Plantstype.plantstypeid == request_data['source'])).first()
    user = session.query(Users).filter(Users.userid == userid).first()
    response = {'authentication': True, 'success': False, 'coins': user.coins}
    if planttype.seed_price > user.coins:
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    else:
        response['success'] = True
        user.coins -= planttype.seed_price
        session.query(Seeds).filter(and_(Seeds.plant_type == request_data['source'],
                                         Seeds.userid == userid)).first().seedcount += 1
        session.commit()
        response['coins'] = user.coins
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)


@csrf_exempt
@authentication
def sell_fetus(request, userid):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    session = Session(bind=engine)
    fetus = session.query(Fetus).filter(and_(Fetus.plant_type == request_data['plant_type'],
                                             Fetus.userid == userid)).first()
    user = session.query(Users).filter(Users.userid == userid).first()
    response = {'authentication': True, 'success': False, 'coins': user.coins}
    if fetus.fetyscount < 1:
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    else:
        response['success'] = True
        user.coins += session.query(Plantstype).filter(Plantstype.plantstypeid == request_data['plant_type'])\
            .first().fetus_price
        fetus.fetyscount -= 1
        session.commit()
        response['coins'] = user.coins
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)


def update_plant(plant, session):
    create = plant.create_time
    update = plant.update_time
    planttype = session.query(Plantstype).filter(Plantstype.plantstypeid == plant.type_id).first()
    hourspassed = ((datetime.datetime.now() - create) - (update - create))
    hourspassed = (hourspassed.days * 24) + (hourspassed.seconds // 3600)
    for i in range(3, hourspassed, 3):
        points_added = 125
        if plant.thirst < 5:
            plant.thirst += 1
        if plant.bugs < 5:
            chance = random.random()
            print(chance)
            if chance < 0.3:
                plant.bugs += 1
        if plant.points >= planttype.max_points:
            plant.points = planttype.max_points
            continue
        else:
            points_added -= 12 * plant.thirst + 12 * plant.bugs
            plant.points += points_added
    for i in range(0, 6):
        if plant.points > i * planttype.max_points / 6:
            plant.stage = i + 1;
    plant.update_time = datetime.datetime.now()
    session.commit()
    return


@csrf_exempt
@authentication
def update_garden(request, userid):
    if request.method != 'GET':
        return HttpResponse("Invalid request method")
    # ruserid = request.GET.get('userid', 0)
    session = Session(bind=engine)
    response = {'authentication': True, 'success': False, 'plants': []}
    for plant in session.query(Plants).filter(Plants.userid == userid):
        update_plant(plant, session)
        response['plants'].append({
            'id': plant.plantid,
            'stage': plant.stage,
            'points': plant.points,
            'thirst': plant.thirst,
            'bugs': plant.bugs
        })
    response['success'] = True
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
@authentication
def collect_fetus(request, userid):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    session = Session(bind=engine)
    plant = session.query(Plants).filter(and_(Plants.plantid == request_data['plantid'],
                                              Plants.userid == userid)).first()
    planttype = session.query(Plantstype).filter(Plantstype.plantstypeid == plant.type_id).first()
    fetus = session.query(Fetus).filter(and_(Fetus.plant_type == planttype.plantstypeid,
                                             Fetus.userid == userid)).first()
    response = {'authentication': True, 'success': False, 'fetyscount': fetus.fetyscount, 'points': plant.points, 'stage': plant.stage}
    if plant.points < planttype.max_points:
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    else:
        response['success'] = True
        fetus.fetyscount += random.randint(planttype.fetus_min, planttype.fetus_max)
        plant.points = 5 * planttype.max_points / 6
        plant.stage = 5
        session.commit()
        response['fetyscount'] = fetus.fetyscount
        response['points'] = plant.points
        response['stage'] = plant.stage
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)


@csrf_exempt
def authorization(request):
    if request.method != 'GET':
        return HttpResponse("Invalid request method")
    login = request.GET.get('login', '')
    password = request.GET.get('password', '')
    session = Session(bind=engine)
    response = {'success': False, 'token': "", 'error': ""}
    user = session.query(Users).filter(and_(Users.login == login, Users.password == password)).first()
    if not user:
        response['error'] = "Неверный логин или пароль"
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    token = jwt.encode({'login': user.login}, SECRET_KEY, algorithm='HS256').decode("utf-8")
    Tokens[token] = {'userid': user.userid, 'last_update': datetime.datetime.now()}
    response['success'] = True
    response['token'] = token
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
@authentication
def automatic_login(request, userid):
    response = {'authentication': True}
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
def registration(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    login = request_data['login']
    password = request_data['password']
    email = request_data['email']
    session = Session(bind=engine)
    response = {'success': False, 'error': ""}
    user = session.query(Users).filter(Users.login == login).first()
    if user:
        response['error'] = "Пользователь с таким логином уже существует"
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    user = session.query(Users).filter(Users.email == email).first()
    if user:
        response['error'] = "Пользователь с таким электронным адресом уже существует"
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    user = Users(login, password, email, 10)
    session.add(user)
    session.commit()
    response['success'] = True
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)



