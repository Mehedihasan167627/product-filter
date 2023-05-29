from django.shortcuts import render
from django.http import JsonResponse
from django.views import View  
import itertools,folium
from math import radians, sin, cos, sqrt, atan2




class CreateBestRouteView(View):
    def get(self,request):
        branches=[
        {"latitude": 23.8728568, "longitude": 90.3984184, "place": "Uttara Branch"},
        {"latitude": 23.8513998, "longitude": 90.3944536, "place": "City Bank Airport"},
        {"latitude": 23.8330429, "longitude": 90.4092871, "place": "City Bank Nikunja"},
        {"latitude": 23.8679743, "longitude": 90.3840879, "place": "City Bank Beside Uttara Diagnostic"},
        {"latitude": 23.8248293, "longitude": 90.3551134, "place": "City Bank Mirpur 12"},
        {"latitude": 23.827149, "longitude": 90.4106238, "place": "City Bank Le Meridien"},
        {"latitude": 23.8629078, "longitude": 90.3816318, "place": "City Bank Shaheed Sarani"},
        {"latitude": 23.8673789, "longitude": 90.429412, "place": "City Bank Narayanganj"},
        {"latitude": 23.8248938, "longitude": 90.3549467, "place": "City Bank Pallabi"},
        { "latitude": 23.813316, "longitude": 90.4147498, "place": "City Bank JFP"}
        ]
        return render(request,"salesman_traveling/create.html",{"branches":branches})
    
    def post(self,request):
        branches=[
            [23.8728568,90.3984184,"Uttara Branch"],
            [23.8513998,90.3944536,"City Bank Airport"],
            [23.8330429,90.4092871,"City Bank Nikunja"],
            [23.8679743,90.3840879,"City Bank Beside Uttara Diagnostic"],
            [23.8248293,90.3551134,"City Bank Mirpur 12"],
            [23.827149,90.4106238,"City Bank Le Meridien"],
            [23.8629078,90.3816318,"City Bank Shaheed Sarani"],
            [23.8673789,90.429412,"City Bank Narayanganj"],
            [23.8248938,90.3549467,"City Bank Pallabi"],
            [23.813316,90.4147498,"City Bank JFP"],
        ]
        data=self.generate_all_possible_permutations(branches)
    
        m=folium.Map(location=[data[0][0],data[0][1]],zoom_start=12)
        location_points=[]
        for i in range(len(branches)):
            location_points.append([data[i][0],data[i][1]])
            folium.Marker(
            [data[i][0],data[i][1]],popup=data[i][2],
                icon=folium.Icon(icon="gift",color="red"),tooltip=data[i][2],
                ).add_to(m)

        folium.PolyLine(location_points,color="blue",dash_array="5").add_to(m)

        m.save("salesman_traveling/templates/salesman_traveling/map.html")
        
        return JsonResponse({"data":"success"})
       

    def calculate_distance(self,lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2) * sin(dlon/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        return distance

    # Generate all possible permutations of the branch indices
    def generate_all_possible_permutations(self,branches):
        permutations = list(itertools.permutations(range(len(branches))))

        # Initialize with a large distance
        best_distance = float('inf')
        best_route = None

        # Iterate through each permutation and calculate the total distance
        for permutation in permutations:
            route = list(permutation)
            route.insert(0, 0)  # Start at the Uttara branch
            route.append(0)  # End at the Uttara branch
            distance = 0
            for i in range(len(route) - 1):
                start = route[i]
                end = route[i + 1]
                distance += self.calculate_distance(
                    branches[start][0],
                    branches[start][1],
                    branches[end][0],
                    branches[end][1]
                )

            if distance < best_distance:
                best_distance = distance
                best_route = route
                
        data=[branches[i] for i in best_route]
        return data 
        

class ShowBestRouteView(View):
    def get(self,request):
        return render(request,"salesman_traveling/map.html")