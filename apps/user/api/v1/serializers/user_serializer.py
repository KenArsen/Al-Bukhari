from rest_framework import serializers

from apps.user.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomListUser"
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomDetailUser"
        exclude = ("password", "is_staff", "groups", "user_permissions")


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_superuser(**validate_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomUpdateUser"
        exclude = (
            "is_staff",
            "is_superuser",
            "user_permissions",
            "last_login",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        if validated_data.get("password"):
            instance.set_password(validated_data.get("password"))
        instance.save()
        return instance


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "MeUser"
        exclude = ("password", "is_staff", "groups", "user_permissions")
