from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .models import PasswordResetRequest
from .serializers import (
    RegistrationSerializer,
    LoginSerializer,
    PasswordResetRequestSerializer,
    PasswordResetVerifySerializer,
    PasswordResetConfirmSerializer,
)
from .service import generate_code, send_reset_email

User = get_user_model()


class RegisterView(APIView):
    @extend_schema(
        summary="Регистрация пользователя",
        request=RegistrationSerializer,
        responses={201: "Пользователь создан"}
    )
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "Пользователь успешно зарегистрирован."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @extend_schema(
        summary="Логин пользователя",
        request=LoginSerializer,
        responses={200: "JWT токен"}
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(APIView):
    @extend_schema(
        summary="Запрос на сброс пароля через Gmail",
        request=PasswordResetRequestSerializer,
        responses={200: "Код отправлен на Почту"}
    )
    def post(self, request):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

        code = generate_code()
        reset_request = PasswordResetRequest.objects.create(user=user, code=code)

        send_reset_email(email, code)

        return Response({"message": "Код отправлен на почту", "token": str(reset_request.token)})


class PasswordResetVerifyView(APIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(
        summary="Проверка кода сброса пароля",
        request=PasswordResetVerifySerializer,
        responses={200: "JWT-токен для аутентификации"}
    )
    def post(self, request):
        serializer = PasswordResetVerifySerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            code = serializer.validated_data['code']

            try:
                reset_request = PasswordResetRequest.objects.get(token=token, used=False)
            except PasswordResetRequest.DoesNotExist:
                return Response({"detail": "Некорректный токен."}, status=status.HTTP_400_BAD_REQUEST)

            if reset_request.is_expired():
                return Response({"detail": "Время действия кода истекло."}, status=status.HTTP_400_BAD_REQUEST)

            if reset_request.code != code:
                return Response({"detail": "Неверный код."}, status=status.HTTP_400_BAD_REQUEST)

            user = reset_request.user
            refresh = RefreshToken.for_user(user)

            return Response({
                "detail": "Код подтверждён.",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Установка нового пароля",
        request=PasswordResetConfirmSerializer,
        responses={200: "Пароль успешно изменен"}
    )
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            new_password = serializer.validated_data['new_password']

            user.set_password(new_password)
            user.save()

            return Response({"detail": "Пароль успешно изменён."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
