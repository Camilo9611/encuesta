from django.db import models
from phone_field import PhoneField

# Create your models here.
#################################################### TABLA #1 ############################################################################
class Usuario(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    nroencuesta=models.AutoField(primary_key=True,null=False)
    nombre=models.CharField(max_length=254, blank=False, null=False)  #help_text="ayuda"
    apellido=models.CharField(max_length=254, blank=False, null=False)
    correo=models.EmailField(max_length=254,blank=False, null=False)
    empresa=models.CharField(max_length=254, blank=True, null=True)
    telefono=PhoneField(E164_only=False,blank=True, null= True, help_text='Numero de contacto')

    def __str__(self):
        return ("Encuesta #"+str(self.nroencuesta) +" realizada por "+ str(self.nombre) + " " + str(self.apellido))

#######################################################################################################################################
###################################################### TABLA #2 #######################################################################
class Preguntas(models.Model):
    nroencuesta= models.OneToOneField(Usuario,on_delete=models.CASCADE,default=None,primary_key=True)

    EXCELENTE = 5
    BUENO = 4
    REGULAR = 3
    DEFICIENTE= 2
    MALO= 1

    STATUS_CHOICES = (
        (EXCELENTE, 'Excelente'),
        (BUENO, 'Bueno'),
        (REGULAR, 'Regular'),
        (DEFICIENTE, 'Deficiente'),
        (MALO, 'Malo'),
    
    )
  
    calidad = models.IntegerField(default='5',blank=False, null=False,help_text='Seleccione una opccion segun la satisfacción del servicio', choices=STATUS_CHOICES)
    presentacion = models.IntegerField(default='5',blank=False, null=False,help_text='Seleccione una opccion segun la satisfacción del servicio', choices=STATUS_CHOICES)
    sabor = models.IntegerField(default='5',blank=False, null=False,help_text='Seleccione una opccion segun la satisfacción del servicio', choices=STATUS_CHOICES)
    temperatura = models.IntegerField(default='5',blank=False, null=False,help_text='Seleccione una opccion segun la satisfacción del servicio', choices=STATUS_CHOICES)

    eficiencia = models.IntegerField(default='5',blank=False, null=False,help_text='Seleccione una opccion segun la satisfacción del servicio', choices=STATUS_CHOICES)
    agilidad = models.IntegerField(default='5',blank=False, null=False,help_text='Seleccione una opccion segun la satisfacción del servicio', choices=STATUS_CHOICES)
    ambientacion = models.IntegerField(default='5',blank=False, null=False,help_text='Seleccione una opccion segun la satisfacción del servicio', choices=STATUS_CHOICES)

##############################################################################################################################################

    EXP_CHOICES = (
        ('Totalmente', 'Totalmente'),
        ('Parcialmente', 'Parcialmente'),
        ('No se cumplieron', 'No se cumplieron'),
    )

    expectativa = models.CharField(max_length=254,blank=False, null=False,help_text='Seleccione una opccion segun las expectativas obtenidas', choices=EXP_CHOICES)
    motivo=models.CharField(max_length=254, blank=False, null=False)
    prox_visita=models.CharField(max_length=254, blank=True, null=True)

##############################################################################################################################################

    EXPE_CHOICES = (
        ('Si', 'Si'),
        ('No', 'No'),
    )

    experiencia = models.CharField(max_length=254,blank=False, null=False,help_text='Seleccione una opccion si algun funcionario hizo si experiencia mas agradable', choices=EXPE_CHOICES)
    funcionario=models.CharField(max_length=254, blank=True, null=True,help_text='En caso que sea SI, por favor escribir el nombre del colaborador')
    comentarios=models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return str(self.nroencuesta)

##############################################################################################################################################