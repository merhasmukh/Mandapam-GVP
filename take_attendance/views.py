from django.shortcuts import render
from django.http import JsonResponse
from .services.distance_cal import calculate_distance
from .services.time_cal import calculate_time_difference, is_time_within_range
from pytz import timezone
import logging
from .models import PrathanaLocation, Attendance
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def get_location(request):
    return render(request, "take_attendance/get_location.html")

@login_required
def check_location_view(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')

        if not lat or not lon:
            return JsonResponse({
                "status": "error",
                "message": "Latitude and longitude are required to mark attendance."
            }, status=400)

        try:
            # Fetch the first Prathana location from the database
            prathana_location = PrathanaLocation.objects.first()
            if not prathana_location:
                return JsonResponse({
                    "status": "error",
                    "message": "No Prathana location configured."
                }, status=404)

            # Convert latitude and longitude to float
            prathana_lat = float(prathana_location.latitude)
            prathana_lon = float(prathana_location.longitude)
            lat = float(lat)
            lon = float(lon)
            
            # Set timezone to Asia/Kolkata
            kolkata_tz = timezone('Asia/Kolkata')
            current_time = datetime.now(kolkata_tz)

            # Create naive datetime objects first, then localize them to Asia/Kolkata
            current_date = current_time.date()
            
            # Create naive datetime objects
            naive_start_time = datetime.combine(current_date, prathana_location.start_time)
            naive_end_time = datetime.combine(current_date, prathana_location.end_time)
            
            # Localize them to Asia/Kolkata timezone
            prathan_start_time = kolkata_tz.localize(naive_start_time)
            prathan_end_time = kolkata_tz.localize(naive_end_time)

            # Log the times for debugging
            print(f"Current Time: {current_time}")
            print(f"Start Time: {prathan_start_time}")
            print(f"End Time: {prathan_end_time}")

            # Log raw start_time and end_time from the database
            print(f"Raw Start Time (from DB): {prathana_location.start_time}")
            print(f"Raw End Time (from DB): {prathana_location.end_time}")

            # Log converted datetime objects
            print(f"Converted Start Time: {prathan_start_time}")
            print(f"Converted End Time: {prathan_end_time}")

            # Additional debugging for comparison
            print(f"Start time comparison: {prathan_start_time.time()} vs {prathan_end_time.time()}")
            print(f"Is end_time > start_time? {prathan_end_time > prathan_start_time}")
            print(f"Is end_time <= start_time? {prathan_end_time <= prathan_start_time}")

            if prathan_end_time <= prathan_start_time:
                return JsonResponse({
                    "status": "error",
                    "message": f"Invalid time configuration: end_time ({prathan_end_time.time()}) must be greater than start_time ({prathan_start_time.time()})."
                }, status=400)

            try:
                distance = calculate_distance(lat, lon, prathana_lat, prathana_lon)
                is_inside = distance <= prathana_location.radius
                print(f"Distance calculated: {distance}")
            except Exception as e:
                print(f"Error in calculate_distance: {e}")
                raise

            
            time_difference = calculate_time_difference(prathan_start_time, current_time)
            print(f"Time difference calculated: {time_difference}")
        
          
            # Simple check to see if current time is within range
            is_on_time_simple = prathan_start_time <= current_time <= prathan_end_time
            print(f"Simple time check: {prathan_start_time} <= {current_time} <= {prathan_end_time} = {is_on_time_simple}")
            
            try:
                is_on_time = is_time_within_range(current_time, prathan_start_time, prathan_end_time)
                print(f"Function result: {is_on_time}")
            except Exception as e:
                print(f"Error in is_time_within_range: {e}")
                raise

            return JsonResponse({
                "status": "success",
                "distance": distance,
                "max_radius": prathana_location.radius,
                "location_name": prathana_location.name,
                "is_on_time": is_on_time,
                "time_difference": time_difference,
                "is_inside":  is_inside
            })

        except ValueError as e:
            return JsonResponse({
                "status": "error",
                "message": f"Invalid coordinates: {e}"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": f"An error occurred: {e}"
            }, status=500)

    # Handle GET request
    return render(request, 'take_attendance/check_location.html')

@login_required
def mark_attendance(request):
    if request.method == "POST":
        user = request.user
        # Get user location data from the request
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Save attendance record
        Attendance.objects.create(
            user=user,
            date=timezone.now().date(),
            time=timezone.now().time(),
            present=True,
        )
        # Logic to mark attendance can be added here
        return JsonResponse({
            "status": "success",
            "message": "Attendance marked successfully."
        })
    return render(request, 'take_attendance/mark_attendance.html')