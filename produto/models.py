import uuid
from django.db import models
from stdimage.models import StdImageField


# metodo que pega o arquivo de imagem, separa a extnsa0 e recria com um novo nome
# uuid faz a geração aleatoria do nome do arquivo de imagem
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename



class Produto(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    picture = StdImageField(upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480}}, verbose_name='Imagem')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Preço')
    information = models.TextField(max_length=700, verbose_name='Caractristicas')

    criado = models.DateField(auto_now_add=True, verbose_name='Criado')
    alterado = models.DateField(auto_now=True, verbose_name='Atualizado')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


    def __str__(self):
        return self.name