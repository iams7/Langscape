from django.shortcuts import render
from rest_framework import viewsets
from .models import Headword, POS, Meaning
from .serializers import HeadwordSerializer, POSSerializer, MeaningSerializer

# Create your views here.

class HeadwordViewSet(viewsets.ModelViewSet):
    serializer_class = HeadwordSerializer
    queryset = Headword.objects.all()

    # TODO: Create
    def create(self, request, *args, **kwargs):
        serializer = MeaningSerializer(data = request.data) # { "pos":2 }
        print("Serializer",serializer)
        print("Data",request.data)
        # if serializer.is_valid(raise_exception=True):
        #     data = serializer.validated_data
        #     print(data)
        #     sense = Meaning.objects.filter(pos_id = data.get('pos')).count()+1
        #     Meaning.objects.create( {**data, "sense":sense} )
        #     print("count", count)

            # self.perform_create(serializer)
            # headers = self.get_success_headers(serializer.data)
            # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # TODO: List
    # TODO: Retrive
    # TODO: Delete
