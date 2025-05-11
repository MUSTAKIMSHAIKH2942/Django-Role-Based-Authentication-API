from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer, LoginSerializer

# Registration view (No authentication required)
class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=201)
        return Response(serializer.errors, status=400)


# Login view (No authentication required)
class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']  # Get authenticated user from validated_data
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'username': user.username,
                'role': user.role  # If you want to include custom fields
            }, status=200)

        return Response(serializer.errors, status=400)


# Role-based access view for Admin
class AdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only allow users with the 'admin' role
        if hasattr(request.user, 'role') and request.user.role == 'admin':
            return Response({"message": "Welcome Admin!"})
        return Response({"message": "Access denied!"}, status=403)


# Role-based access view for Staff
class StaffView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Allow 'admin' and 'staff' roles to access
        if hasattr(request.user, 'role') and request.user.role in ['admin', 'staff']:
            return Response({"message": "Welcome Staff!"})
        return Response({"message": "Access denied!"}, status=403)
