from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User, Availability
from .serializers import UserCreateSerializer, AvailabilitySerializer


class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAvailabilityView(APIView):
    def post(self, request):
        user_id = request.data.get('user')
        print(user_id)
        user = get_object_or_404(User, id=user_id)
        print(user)

        if user.role not in ['candidate', 'interviewer']:
            return Response({"error": "Only candidates or interviewers can register availability."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = AvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Availability registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSchedulableSlotsView(APIView):
    def get(self, request):
        candidate_id = request.query_params.get('candidate_id')
        interviewer_id = request.query_params.get('interviewer_id')

        if not candidate_id or not interviewer_id:
            return Response(
                {"error": "Candidate ID and Interviewer ID are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            candidate_id = int(candidate_id)
            interviewer_id = int(interviewer_id)
        except ValueError:
            return Response(
                {"error": "Candidate ID and Interviewer ID must be valid integers."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if candidate_id == interviewer_id:
            return Response(
                {"error": "Candidate and Interviewer must be different users."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        candidate_slots = Availability.objects.filter(user_id=candidate_id)
        interviewer_slots = Availability.objects.filter(user_id=interviewer_id)

        if not candidate_slots.exists() or not interviewer_slots.exists():
            return Response(
                {"error": "No availability found for one or both users."},
                status=status.HTTP_404_NOT_FOUND,
            )

        slots = []
        for candidate in candidate_slots:
            for interviewer in interviewer_slots:
                if candidate.date == interviewer.date:
                    start = max(candidate.start_time, interviewer.start_time)
                    end = min(candidate.end_time, interviewer.end_time)

                    while start < end:
                        next_slot = (datetime.combine(candidate.date, start) + timedelta(hours=1)).time()
                        if next_slot <= end:
                            slots.append({
                                "date": candidate.date.strftime('%Y-%m-%d'),
                                "start": start.strftime('%H:%M'),
                                "end": next_slot.strftime('%H:%M')
                            })
                        start = next_slot

        if not slots:
            return Response({"message": "No overlapping slots found."})

        return Response({"slots": slots})
