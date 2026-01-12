from rest_framework import serializers
from .models import Categoria, Receita, Interacao

# ----------------------
# Serializer de Categoria
# ----------------------
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


# ----------------------
# Serializer de Receita
# ----------------------
class ReceitaNestedSerializer(serializers.ModelSerializer):
    """
    Serializer enxuto para aninhamento (Ex: em Interacao)
    """
    class Meta:
        model = Receita
        fields = ['id', 'titulo']


class ReceitaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        source='categoria',
        write_only=True
    )

    autor = serializers.HiddenField(default=serializers.CurrentUserDefault())
    imagem = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Receita
        fields = [
            'id', 'titulo', 'descricao', 'ingredientes',
            'modo_preparo', 'imagem', 'criado_em',
            'categoria', 'categoria_id', 'autor'
        ]
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if rep['imagem'] and request:
            rep['imagem'] = request.build_absolute_uri(rep['imagem'])
        return rep



# ----------------------
# Serializer de Interacao
# ----------------------
class InteracaoSerializer(serializers.ModelSerializer):
    receita = ReceitaNestedSerializer(read_only=True)
    receita_id = serializers.PrimaryKeyRelatedField(
        queryset=Receita.objects.all(),
        write_only=True,
        source='receita'
    )

    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Interacao
        fields = '__all__'

    def validate(self, data):
        tipo = data.get('tipo')
        comentario = data.get('comentario')
        estrelas = data.get('estrelas')

        # Valida comentários
        if tipo == Interacao.COMENTARIO and not comentario:
            raise serializers.ValidationError({
                'comentario': 'O comentário é obrigatório.'
            })

        # Valida avaliações
        if tipo == Interacao.AVALIACAO:
            if estrelas is None:
                raise serializers.ValidationError({
                    'estrelas': 'A avaliação precisa ter estrelas.'
                })
            if estrelas < 1 or estrelas > 5:
                raise serializers.ValidationError({
                    'estrelas': 'A avaliação deve ser entre 1 e 5 estrelas.'
                })

        return data
