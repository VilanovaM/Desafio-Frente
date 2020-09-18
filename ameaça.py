de  enum  import  Enum
do  operador  importar  itemgetter
da  digitação  import  Iterable , Tuple
from  pydantic  import  BaseModel , validator
da  importação de ferramentas por  último 
de  iheroes_api . núcleo . comum . localização  importação  Localização
de  iheroes_api . núcleo . ameaças . importação de ocorrência  Ocorrência , Estado 
# Enums
classe  DangerLevel ( str , Enum ):
    WOLF  =  "lobo"
    TIGRE  =  "tigre"
    DRAGON  =  "dragão"
    DEUS  =  "deus"
# Entidades
classe  Threat ( BaseModel ):
    classe  Config :
        allow_mutation  =  False
    id : int   # noqa: A003
    nome : str
    perigo_level : DangerLevel
    localização : localização
    ocorrências : Tupla [ Ocorrência , ...]
    @ validator ( "ocorrências" , pré = verdadeiro , sempre = verdadeiro )
    def  sort_occurrences (
        cls , v : Iterável [ Ocorrência ],   # noqa: N805
    ) ->  Iterável [ Ocorrência ]:
        retorno  classificado ( v , key = itemgetter ( " updated_at " ))
        retorno  classificado ( v , key = itemgetter ( " created_at " ))

    @ validator ( "ocorrências" )
    def  validate_occurrences (
        cls , v : Iterável [ Ocorrência ],   # noqa: N805
    ) ->  Iterável [ Ocorrência ]:
        Monitoring_states  = [ State . PENDENTE , Estado . ATIVO ]
        contagem  = [ Occ  para  Occ  em  V  Se  Occ . estado  em  monitorados_estados ]
        se  len ( contagem ) >  1 :
            raise  ValueError ( "a ameaça tem mais de um estado monitorado" )
        voltar  v
    def  is_being_monitored ( self ) ->  bool :
        Se  len ( auto . ocorrências ) ==  0 :
            retornar  falso
        last_occurrence  =  last ( self . ocorrências )
        retorna  False  se  last_occurrence . state  ==  State . RESOLVIDO  mais  verdadeiro
classe  ThreatRecord ( BaseModel ):
    classe  Config :
        allow_mutation  =  False
    perigo_level : DangerLevel
    localização : localização
classe  ThreatHistory ( BaseModel ):
    classe  Config :
        allow_mutation  =  False
    ameaça_id : int
    registros : Tupla [ ThreatRecord , ...]
# DTOs
classe  ReportThreatDto ( BaseModel ):
    classe  Config :
        allow_mutation  =  False
    nome : str
    perigo_level : DangerLevel
    localização : localização