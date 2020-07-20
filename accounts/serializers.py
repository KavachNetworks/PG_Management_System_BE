from rest_framework import serializers
from .models import Enterprise, AdminUser
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework import exceptions
import random
from .sendMail import sendmail


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ["enterpriseName", "enterpriseAddress", "enterpriseEmailAddress", "enterpriseContactNumber",
                  "enterpriseGSTNumber",
                  "enterpriseType", "dateOfRegistration", "timeOfRegistration", "enterpriseWebsite", "enterpriseDetails"
                  ]

    def create(self, validated_data):
        enterprises = Enterprise(
            enterpriseName=self.validated_data['enterpriseName'],
            enterpriseAddress=self.validated_data['enterpriseAddress'],
            enterpriseEmailAddress=self.validated_data['enterpriseEmailAddress'],
            enterpriseContactNumber=self.validated_data['enterpriseContactNumber'],
            enterpriseGSTNumber=self.validated_data['enterpriseGSTNumber'],
            enterpriseType=self.validated_data['enterpriseType'],
            enterpriseWebsite=self.validated_data['enterpriseWebsite'],
            enterpriseDetails=self.validated_data['enterpriseDetails']
        )
        enterprises.save()

        c_name = self.validated_data['enterpriseName'].strip().split()
        admin_id = ""
        for i in c_name:
            admin_id += i[0]
        admin_id += "001"
        pwd = random.randint(100000, 999999)
        admin_model = AdminUser(adminId=admin_id,
                                enterpriseId=Enterprise.objects.get(enterpriseGSTNumber=self.validated_data['enterpriseGSTNumber']),
                                adminName=self.validated_data['enterpriseName']+"_admin", Password=pwd
                                )

        user = User.objects.create_user(username=admin_id, password=pwd, first_name=self.validated_data['enterpriseName']+"_admin")
        
        # sendmail(to=validated_data["enterpriseEmailAddress"], admin_id=admin_id, password=pwd)
        admin_model.save()
        return enterprises


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = "User is Not Found"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Wrong Credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must Provide username and Password"
            raise exceptions.ValidationError(msg)
        return data