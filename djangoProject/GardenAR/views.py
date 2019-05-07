from django.shortcuts import render
from django.conf import settings
from sqlalchemy.orm import Session
from sqlalchemy import and_
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import Users
from .models import Plantstype
from .models import Plants
from .models import Сells
from .models import Products
from .models import Fetus
from .models import Seeds

engine = settings.ENGINE


# Create your views here.

@csrf_exempt
def garden(request):
    if request.method != 'GET':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    ruserid = request_data['userid']
    session = Session(bind=engine)
    response = {
        'coins': session.query(Users).filter(Users.userid == ruserid).first().coins,
        'plants_type': [
            {
                'id': instance.plantstypeid,
                'file': instance.file,
                'fetus': instance.fetus,
                'max_points': instance.max_points,
                'name': instance.name,
                'seed_price': instance.seed_price,
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
                'create_time': instance.create_time,
                'update_time': instance.update_time
            } for instance in session.query(Plants).filter(Plants.userid == ruserid)
        ],
        'cells': [
            {
                'id': instance.cellid,
                'userid': instance.userid,
                'plantid': instance.plantid,
                'is_dug_up': instance.is_dug_up,
                'is_fertilized': instance.is_fertilized,
                'weed': instance.weed,
                'grass_stage': instance.grass_stage,
                'dug_up_time': instance.dug_up_time,
                'fertil_time': instance.fertil_time
            } for instance in session.query(Сells).order_by(Сells.cellid).filter(Сells.userid == ruserid)
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
def thirst(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    session = Session(bind=engine)
    for instance in session.query(Plants).filter(and_(Plants.userid == request_data['userid'],
                                                 Plants.plantid == request_data['plantid'])):
        instance.thirst = request_data['thirst']
    session.commit()
    response = {'success': True}
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
def bugs(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    session = Session(bind=engine)
    for instance in session.query(Plants).filter(and_(Plants.userid == request_data['userid'],
                                                 Plants.plantid == request_data['plantid'])):
        instance.bugs = request_data['bugs']
    session.commit()
    response = {'success': True}
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
def bugs(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    session = Session(bind=engine)
    for instance in session.query(Plants).filter(and_(Plants.userid == request_data['userid'],
                                                 Plants.plantid == request_data['plantid'])):
        instance.bugs = request_data['bugs']
    session.commit()
    response = {'success': True}
    response = json.dumps(response, ensure_ascii=False, default=str)
    return HttpResponse(response)


@csrf_exempt
def new_plant(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request method")
    request_data = json.loads(request.body)
    response = {'success': False, 'plants': []}
    session = Session(bind=engine)
    seed = session.query(Seeds).filter(Seeds.plant_type == request_data['type_id']).first()
    if seed.seedcount < 1:
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
    else:
        response['success'] = True
        seed.seedcount -= 1
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        n_plant = Plants(request_data['type_id'], request_data['userid'], request_data['cellid'], 1, 0, 0, 0,
                         time, time)
        session.add(n_plant)
        session.commit()
        response['plants'].append({
            'id': n_plant.plantid,
            'type_id': n_plant.type_id,
            'userid': n_plant.userid,
            'cell': n_plant.cell,
            'stage': n_plant.stage,
            'points': n_plant.points,
            'thirst': n_plant.thirst,
            'bugs': n_plant.bugs,
            'create_time': n_plant.create_time,
            'update_time': n_plant.update_time
        })
        response = json.dumps(response, ensure_ascii=False, default=str)
        return HttpResponse(response)
