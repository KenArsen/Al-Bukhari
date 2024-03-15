from rest_framework import serializers

from apps.user.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomListUser"
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_active",
        )
        extra_kwargs = {"password": {"write_only": True}}


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomDetailUser"
        exclude = ("password", "is_staff", "groups", "user_permissions")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomMeUser"
        exclude = ("password", "is_staff", "groups", "user_permissions")


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "CustomCreateUser"
        exclude = (
            "is_staff",
            "groups",
            "is_superuser",
            "user_permissions",
            "last_login",
            "is_active",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        if validated_data.get("password"):
            instance.set_password(validated_data.get("password"))
        instance.save()
        return instance


class OrderDetailCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = "OrderDetailCustomerSerializer"
        fields = (
            "id",
            "first_name",
            "last_name",
        )
