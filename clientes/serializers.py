from rest_framework import serializers

from .models import Clientes


class CNABSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Clientes
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data):

        gerar_dados = Clientes.objects.get_or_create(
            **validated_data)
        return gerar_dados
        
