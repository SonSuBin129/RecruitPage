from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse, Http404
import random

import json
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from .models import Year, Team, Member, Info, Photo
from .serializers import YearSerializer, TeamSerializer, MemberSerializer,InfoSerializer,PhotoSerializer

import logging


def getDetailsByTeam(year, team):
    year_str=str(year)
    year_obj=get_object_or_404(Year, year=year_str)
    teamlist=get_list_or_404(Team,year=year_obj, team = team)

    team_obj=None

    for team_check in teamlist:
        if team_check.team==team:
            team_obj=team_check

    photolist=Photo.objects.filter(team=team_obj)
    #memberlist=get_object_or_404(Member, team=team_obj)
    memberlist = Member.objects.filter(team=team_obj)


    photos = []
    for photo in photolist:
        photo_serializer=PhotoSerializer(photo)
        photos.append(photo_serializer.data['photo'])
        print(photo_serializer)

    member_serializer=MemberSerializer(memberlist,many=True).data

    p_name = TeamSerializer(team_obj).data['p_name']


    response_data={
        'p_name': p_name,
        'photos': photos,
        'madeby':member_serializer,
    }

    return response_data


def main(request,year=11):
    #main에 접근했을때 제일 먼저 보이는 page가 11기 관련이도록
    try:
        year_str=str(year)
        year_obj=get_object_or_404(Year, year=year_str)
        teamlist=get_list_or_404(Team,year=year_obj)
        serializer=TeamSerializer(teamlist,many=True)


        ###수정 작업###
        response_datas = []
    
        for team in teamlist:
            team_serializer=TeamSerializer(team)
            team_name = team_serializer.data['team']
            response_datas.append(getDetailsByTeam(year = year, team = team_name))
        

        return JsonResponse(response_datas, safe=False, json_dumps_params={'ensure_ascii': False} )
        #return JsonResponse(serializer.data, safe = False, json_dumps_params={'ensure_ascii': False})

    except Team.DoesNotExist:
        return JsonResponse({'message': '해당 정보를 찾을 수 없습니다.'}, status=404)

def detail(request, year, team):
    try:
        '''
        year_str=str(year)
        year_obj=get_object_or_404(Year, year=year_str)
        teamlist=get_list_or_404(Team,year=year_obj, team = team)

        team_obj=None

        for team_check in teamlist:
            if team_check.team==team:
                team_obj=team_check

        photolist=Photo.objects.filter(team=team_obj)
        #memberlist=get_object_or_404(Member, team=team_obj)
        memberlist = Member.objects.filter(team=team_obj)

     
        photos = []
        for photo in photolist:
            photo_serializer=PhotoSerializer(photo)
            photos.append(photo_serializer.data['photo'])
            print(photo_serializer)

        member_serializer=MemberSerializer(memberlist,many=True).data

        p_name = TeamSerializer(team_obj).data['p_name']


        response_data={
            'p_name': p_name,
            'photos': photos,
            'madeby':member_serializer,
        
        }
        '''
        response_data = getDetailsByTeam(year, team)

        return JsonResponse(response_data, safe = False,json_dumps_params={'ensure_ascii': False} )
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

#추가한 코드(랜덤전시)

def getrandomExhibition(random_teams):
    response_data_list = []

    for random_team in random_teams:
        photolist = Photo.objects.filter(team=random_team)

        if photolist.exists():
            first_photo = photolist.first()
            thumbnail_serializer = PhotoSerializer(first_photo)

            p_name = TeamSerializer(random_team).data['p_name']

            response_data = {
                'p_name': p_name,
                'thumbnail': thumbnail_serializer.data['photo'],
            }

            response_data_list.append(response_data)

    return response_data_list

def randomExhibition(request, year=11):
    try:
        year_str = str(year)
        year_obj = get_object_or_404(Year, year=year_str)
        teamlist = get_list_or_404(Team, year=year_obj)

        random_teams=random.sample(teamlist, min(3,len(teamlist)))

        response_data = getrandomExhibition(random_teams=random_teams)
    
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})
    except Team.DoesNotExist:
        return JsonResponse({'message': '해당 정보를 찾을 수 없음'}, status=404)