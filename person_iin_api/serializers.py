import datetime

from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['id', 'iin', 'age']

    def get_age(self, obj):
        century = obj.iin[6]
        date = obj.iin[:6]
        year, month, day = [date[i:i + 2] for i in range(0, len(date), 2)]
        year = '20' + year if century in [3, 4] else '19' + year
        new_date = datetime.date(year=int(year), month=int(month), day=int(day))
        return int((datetime.datetime.now().date() - new_date).days / 365.2425)

