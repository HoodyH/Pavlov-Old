import configparser as cfg

hourly_towers = [
            [0, 35, 181],
            [1, 23, 100],
            [2, 13, 9],
            [3, 33, 13],
            [4, 23, 26],
            [5, 43, 223],
            [6, 0, 0],
            [7, 0, 0],
            [8, 0, 0],
            [9, 12, 5],
            [10, 32, 154],
            [11, 44, 244],
            [12, 82, 303],
            [13, 23, 100],
            [14, 13, 9],
            [15, 33, 13],
            [16, 23, 26],
            [17, 43, 223],
            [18, 0, 0],
            [19, 0, 0],
            [20, 0, 0],
            [21, 12, 5],
            [22, 32, 154],
            [23, 44, 244]
        ]

daily_towers = [
    ["Lunedì", 234, 345],
    ["Martedi", 233, 1300],
    ["Mercoledì", 123, 59],
    ["Giovedì", 313, 143],
    ["Venerdì", 423, 326],
    ["Sabato", 423, 2323],
    ["Domenica", 530, 540]
]

monthly_towers = [
    ["Gennaio", 2434, 345],
    ["Febbraio", 2433, 1300],
    ["Marzo", 2423, 59],
    ["Aprile", 3313, 143],
    ["Maggio", 2223, 326],
    ["Giugno", 4223, 2323],
    ["Luglio", 5340, 540],
    ["Agosto", 5340, 540],
    ["Settemre", 5340, 540],
    ["Ottobre", 5340, 540],
    ["Novembre", 5340, 540],
    ["Dicembre", 5340, 540]
        ]


def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get("creds", "beta_token")


def make_reply(msg):
    reply = None
    if msg is None:
        return reply
    _msg = str(msg).upper()
    if _msg == "PT":
        reply = _msg
    return reply


input_m = "1 . MADONNA ACCHIAPPAFANTASMI 2 . MADONNA ACCIACCATA 3 . MADONNA ADORATA DA TUTTI I DIAVOLI 4 . MADONNA ALLAMPANATA 5 . MADONNA ALLUPATA 6 . MADONNA AMARENA 7 . MADONNA ANTICRISTO 8 . MADONNA ANTILOPE 9 . MADONNA ARPA   10 . MADONNA ARPIA   11 . MADONNA ARPIONE   12 . MADONNA ASSASSINA 13 . MADONNA ASTRONAUTA 14 . MADONNA ATTRICE DI FILM PORNO 15 . MADONNA AVVELENATA COI FUNGHI 16 . MADONNA BAAUSTRA 17 . MADONNA BACARAZZO 18 . MADONNA BALESTRAIA 19 . MADONNA BALLERINA DE FLAMENCO 20 . MADONNA BANANIERA 21 . MADONNA BANDIERA 22 . MADONNA BANDITA   23 . MADONNA BARATTATA PER UNA GRANDE MIGNOTTA 24 . MADONNA BARATTOLINO SAMMONTANA 25 . MADONNA BARBAGIANNI 26 . MADONNA BARCHETTA 27 . MADONNA BASCULA   28 . MADONNA BASTARDA 29 . MADONNA BASTONATA 30 . MADONNA BASTRONZA 31 . MADONNA BATTERIA PER AUTO 32 . MADONNA BATTERISTA 33 . MADONNA BATTONA 34 . MADONNA BELVA ASSASSINA 35 . MADONNA BISETTRICE 36 . MADONNA BOCCHINARA 37 . MADONNA BOMBATA 38 . MADONNA BOMBONA 39 . MADONNA BRADIPA   40 . MADONNA BUDDHISTA 41 . MADONNA BUSSOLA   42 . MADONNA CACATA   43 . MADONNA CALCOLATRICE 44 . MADONNA CAMMELLA 45 . MADONNA CAMMELLIERA 46 . MADONNA CANCRO   47 . MADONNA CANNIBALE 48 . MADONNA CANTAUTRICE 49 . MADONNA CAPOMIGNOTTA 50 . MADONNA CAPOTROIA 51 . MADONNA CAPOZOCCOLA 52 . MADONNA CAPRA   53 . MADONNA CAPRA   54 . MADONNA CARCATA COL BRECCIONE 55 . MADONNA CAVALLA 56 . MADONNA CAVALLETTA 57 . MADONNA CAVALLETTA ZOPPA 58 . MADONNA CHE SUONA IL PIANO E CRISTO LA TROMBA (IN TUTTI I SENSI) 59 . MADONNA CHIAPPAMOSCE 60 . MADONNA CIAMBOTTA 61 . MADONNA CICORIONA 62 . MADONNA CIMURROSA 63 . MADONNA COCCODRILLA 64 . MADONNA COMPRESSATA 65 . MADONNA COMUNISTA 66 . MADONNA CON UN CAZZO IN CULO E UNO IN FICA 67 . MADONNA CORNUTA 68 . MADONNA CRETINA   69 . MADONNA CROCIFISSA 70 . MADONNA CROCODILE DUNDEE 71 . MADONNA CUBBISTA RUSSA 72 . MADONNA DAMIGIANA 73 . MADONNA DANGER   74 . MADONNA DARBULA 75 . MADONNA DIAVOLA   76 . MADONNA DIAVOLESSA 77 . MADONNA DIAVOLINA 78 . MADONNA DROGATA 79 . MADONNA DROGATA IN COMUNITA' 80 . MADONNA EBRAICA SVERNICIATA 81 . MADONNA EMBOLOSA 82 . MADONNA FAGIANA   83 . MADONNA FARFALLA ARROSTISTA SUL CANNELLO DEL SIGNORE 84 . MADONNA FATTUCCHIRA 85 . MADONNA FEDIFRAGA 86 . MADONNA FENOMENO DA CIRCO 87 . MADONNA FILTRO   88 . MADONNA FISCHIA BOTTO 89 . MADONNA FISCHIETTO 90 . MADONNA FLTRATA   91 . MADONNA FORMICHIRE 92 . MADONNA FORMICOLOSA 93 . MADONNA FORMICONA 94 . MADONNA FRACICA   95 . MADONNA FRAGOLA AMMUFFITA 96 . MADONNA FRICCHETTONA 97 . MADONNA FRRUSTATA 98 . MADONNA FUMATRICE DE MARIJUANA 99 . MADONNA GANGSTER 100 . MADONNA GIAPPONESE 101 . MADONNA GITANA   102 . MADONNA GOLOSA DE CAZZI 103 . MADONNA GRASSONA 104 . MADONNA GRATTAFORMAGGIO 105 . MADONNA GUARDIA CACCIA 106 . MADONNA HANDICAPPATA 107 . MADONNA ILLIMITATA 108 . MADONNA ILLUMINATA 109 . MADONNA IMBALSAMATA 110 . MADONNA IMPECIATA E IMPIUMATA 111 . MADONNA IMPICCATA 112 . MADONNA INCENDIARIA 113 . MADONNA INCULATA DA DU CAVALLI 114 . MADONNA INDIAVOLATA 115 . MADONNA INVEROSIMILE MAIALA 116 . MADONNA INVIPERITA 117 . MADONNA ISTRICE   118 . MADONNA JESSIKA RABBIT 119 . MADONNA KAMIKAZE 120 . MADONNA KOALA   121 . MADONNA LADRA DE GALLINE 122 . MADONNA LARDONA 123 . MADONNA LEBBROSA 124 . MADONNA LEBBROSA 125 . MADONNA LECCACULO 126 . MADONNA LESBICA   127 . MADONNA LESSIE   128 . MADONNA LETAMAIA 129 . MADONNA LIBELLULA CON UN TUMORE PER OGNI CELLULA 130 . MADONNA LICANTROPO 131 . MADONNA LIMATA   132 . MADONNA LINCIATA 133 . MADONNA LODATA PER I BOCCHINI 134 . MADONNA LUCCICOSA 135 . MADONNA LUCIDATA CO LA SPAZZOLA DE ACCIAIO 136 . MADONNA LUMACA   137 . MADONNA LUPA   138 . MADONNA LURIDA VACCA 139 . MADONNA MADRE DI UN DROGATO 140 . MADONNA MAESTRA DI SESSUOLOGIA 141 . MADONNA MAGNABANANE 142 . MADONNA MAIALA   143 . MADONNA MAIALA DA CORSA 144 . MADONNA MAIALA DA RIPRODUZIONEù 145 . MADONNA MALEDETTA 146 . MADONNA MASOCHISTA DA COMPETIZIONE 147 . MADONNA MASSETTO 148 . MADONNA MASTICATO DA SAN PIETRO 149 . MADONNA MASTURBA CAVALLI 150 . MADONNA MASTURBATRICE DE CAVALLI 151 . MADONNA MATTONATO 152 . MADONNA MATTONE 153 . MADONNA MAZINGA 154 . MADONNA MERDACCIA 155 . MADONNA MICROCEFALO 156 . MADONNA MIGNOTTA 157 . MADONNA MILITE IGNOTO 158 . MADONNA MINESTRONE 159 . MADONNA MINORATA 160 . MADONNA MISSILE A TESTATA NUCLEARE DIRETTO VERSO IL PARADISO 161 . MADONNA MITOMANE 162 . MADONNA MODEM   163 . MADONNA MONACO HITLERIANO 164 . MADONNA MONCO   165 . MADONNA MORTO DE FAME 166 . MADONNA MOSAICO   167 . MADONNA MOSCHIETTIERE 168 . MADONNA MOSTRO DI LOCHNESS 169 . MADONNA MUMMIA   170 . MADONNA MUSULMANO 171 . MADONNA NAJA   172 . MADONNA NANA   173 . MADONNA NANO BOCCHINARO 174 . MADONNA NANO CANCEROGENO 175 . MADONNA NANO RADIOTTIVI 176 . MADONNA NANO RICCHIONE 177 . MADONNA NASCOSTO NELL'UTERO DE LA MADONNA 178 . MADONNA NAUFRAGA 179 . MADONNA NEGROMANTE 180 . MADONNA NERCHIOSA 181 . MADONNA OLIVA ASCOLANA 182 . MADONNA OMOSESUALE 183 . MADONNA OPERATA DE PROSTATA 184 . MADONNA ORBA   185 . MADONNA ORCA   186 . MADONNA ORNITOLOGO 187 . MADONNA ORNITORINCO 188 . MADONNA PAGLIACCIO 189 . MADONNA PANTEGANA 190 . MADONNA PAPERO   191 . MADONNA PARAPLEGGICA 192 . MADONNA PARMIGIANO REGGIANO 193 . MADONNA PARTICOLARMENTE GAY 194 . MADONNA PASTORE TEDESCO SPELATO 195 . MADONNA PASTORELLO ZOPPO 196 . MADONNA PECORARO SARDO 197 . MADONNA PECORINO 198 . MADONNA PEDERASTA 199 . MADONNA PEDOFILA 200 . MADONNA PEDOFILO   201 . MADONNA PEDOFILO   202 . MADONNA PELLICOLA 8mm 203 . MADONNA PERCOSSO CON UN MARTELLO PNEUMATINCO 204 . MADONNA PERICOLANTE 205 . MADONNA PESCE CANE 206 . MADONNA PESCE D'APRILE 207 . MADONNA PESCE RAGNO 208 . MADONNA PESTILENZIALE 209 . MADONNA PESTILENZIALE 210 . MADONNA PESTILENZIALE 211 . MADONNA PETO   212 . MADONNA PEZZENTE 213 . MADONNA PICCIONE VIAGGIATORE 214 . MADONNA PIEDE DE PORCO 215 . MADONNA PIETRA FOCAIA 216 . MADONNA PIGLIAMOSCHE 217 . MADONNA PIGMAGLIONE 218 . MADONNA PIOPPO   219 . MADONNA PIPPONE   220 . MADONNA PIROMANE 221 . MADONNA PIROSCAFO 222 . MADONNA PIZZAIOLO 223 . MADONNA POCCIA CAZZI 224 . MADONNA POKER DE SANTI 225 . MADONNA POLINI FOR RACE 226 . MADONNA POMPINARO DA CORSA 227 . MADONNA PORCELLINO D'INDIA 228 . MADONNA PORCO   229 . MADONNA PORCO DA MONTA 230 . MADONNA POSTER   231 . MADONNA PRATAIOLO 232 . MADONNA PROFESSORE DI ANTICRISTIANESIMO 233 . MADONNA PUBBLICO MINISTERO DELLA SANITA' 234 . MADONNA PUTRIDA VACCA 235 . MADONNA PUTROMIZOBA (PUTTANA,TROJA,ZOCCOLA E BATTONA) 236 . MADONNA PUTTANARO 237 . MADONNA PUZZLE   238 . MADONNA PUZZOLA   239 . MADONNA RADIOATTIVO 240 . MADONNA RAGNO   241 . MADONNA RAPATA   242 . MADONNA RATTO DE FOGNA 243 . MADONNA RAZZISTA 244 . MADONNA RAZZO   245 . MADONNA RICCIO   246 . MADONNA RIN TIN TIN 247 . MADONNA ROMPIPALLE 248 . MADONNA ROMPIPALLE 249 . MADONNA ROSI BINDI 250 . MADONNA ROSPO   251 . MADONNA ROSPO   252 . MADONNA ROSPONE   253 . MADONNA ROZZO   254 . MADONNA SADOMASOCHISTA 255 . MADONNA SADOMASOCHISTA 256 . MADONNA SALAMANDRA 257 . MADONNA SALAME   258 . MADONNA SALCICCIOTTO 259 . MADONNA SANDOKAN 260 . MADONNA SASSAIOLO 261 . MADONNA SATANASSA 262 . MADONNA SATANASSO 263 . MADONNA SATELLITARE 264 . MADONNA SBANDIERATRICE 265 . MADONNA SBUDELLATA 266 . MADONNA SCALZO SUI CHIODI 267 . MADONNA SCAMORZA 268 . MADONNA SCANNATA 269 . MADONNA SCANSAFATICHE 270 . MADONNA SCANZACAZZI 271 . MADONNA SCARICA   272 . MADONNA SCARPA   273 . MADONNA SCARSA   274 . MADONNA SCARTATA COME NA CARAMELLA 275 . MADONNA SCARTAVETRATA 276 . MADONNA SCASSACAZZI 277 . MADONNA SCATENATA 278 . MADONNA SCIMATARRA 279 . MADONNA SCIMMIONE 280 . MADONNA SCIMPANZè 281 . MADONNA SCIOLINA   282 . MADONNA SCOMPOSTO 283 . MADONNA SCOREGGIONA 284 . MADONNA SCORTICATA 285 . MADONNA SCORZA   286 . MADONNA SCROFA IN CALORE 287 . MADONNA SDITALINATRICE DI SANTE 288 . MADONNA SEGUACE DE SATANA 289 . MADONNA SENZA VENTRICOLO 290 . MADONNA SENZAPENE 291 . MADONNA SERFISTA SPELACCHIATO 292 . MADONNA SERPENTE 293 . MADONNA SERPENTESSA 294 . MADONNA SERPENTINA 295 . MADONNA SFORNATO 296 . MADONNA SGANASSATA 297 . MADONNA SGOZZATA DA UN'ALBANESE 298 . MADONNA SGOZZATO 299 . MADONNA SICILIANO CO LA LUPARA 300 . MADONNA SILURO   301 . MADONNA SOLA (QUELLA DE LE SCARPE) 302 . MADONNA SOMARA   303 . MADONNA SOMARA DA RIPRODUZIONE 304 . MADONNA SOMARO   305 . MADONNA SOMARO SARDO NANO DA MONTA 306 . MADONNA SORA NANA 307 . MADONNA SORCA   308 . MADONNA SORCONE   309 . MADONNA SPACCIATORE 310 . MADONNA SPAZZACAMINO 311 . MADONNA SPAZZINO AFRICANO 312 . MADONNA SPIGOLOSO 313 . MADONNA SPILORCIO 314 . MADONNA SPOLMONATO 315 . MADONNA SPUPAZZAPRETE 316 . MADONNA STECCHINO 317 . MADONNA STIRATA   318 . MADONNA STRADALE 319 . MADONNA STRALUNATO 320 . MADONNA STRAMPALATO 321 . MADONNA STRAPAZZATO 322 . MADONNA STRAPIOMBO 323 . MADONNA STRATOSFERICA 324 . MADONNA STRAVECCHIA 325 . MADONNA STREZZICATO 326 . MADONNA STRIATA   327 . MADONNA STRIGLITO CO NA SPAZZOLA DE FERRO 328 . MADONNA STRIMPELLATO DAL PAPA 329 . MADONNA STROMBETTATO 330 . MADONNA STRONZO 331 . MADONNA STROZZATO 332 . MADONNA STROZZINO 333 . MADONNA STRUMENTALE 334 . MADONNA STRUMTRUPPEN 335 . MADONNA STRUZZO   336 . MADONNA STRUZZO DA CORSA 337 . MADONNA STUNTMAN 338 . MADONNA STUPRATO DA UN NEGRO CON UN CAZZO DI 35 cm 339 . MADONNA SUCCHIACAZZI 340 . MADONNA SUDICIO   341 . MADONNA SUINA   342 . MADONNA SUINA   343 . MADONNA SUINA MASSIMA 344 . MADONNA SUINO   345 . MADONNA SUPER SAJAN DI 2 LIVELLO 346 . MADONNA SVENATA   347 . MADONNA SVENTRAPAPERE 348 . MADONNA SVENTRATO 349 . MADONNA SVERNICIATA 350 . MADONNA SVIOLINATO 351 . MADONNA SVIRGOLATA 352 . MADONNA SVIZZERO   353 . MADONNA TACCO A SPILLO DE LE SCARPE DE LA MADONNA 354 . MADONNA TAMARINDO 355 . MADONNA TAMPAX   356 . MADONNA TARALLUCCIO 357 . MADONNA TARTUFO   358 . MADONNA TASSISTA 359 . MADONNA TBC (TUBERCOLOSA) 360 . MADONNA TERMOSIFONE 361 . MADONNA TERRONA   362 . MADONNA TEUTONICA 363 . MADONNA TIRA POMPE 364 . MADONNA TIRAMISU' 365 . MADONNA TIRCHIA   366 . MADONNA TOCCO DE LARDO 367 . MADONNA TOPA   368 . MADONNA TOPO D'APPARTAMENTO 369 . MADONNA TOPORAGNO 370 . MADONNA TORO IN CARICA VERSO LA MADONNA VESTITA DE ROSSO 371 . MADONNA TORTA DE MELE 372 . MADONNA TORTELLONE BARILLA 373 . MADONNA TOSSICODIPENDENTE 374 . MADONNA TOSTAPANE 375 . MADONNA TRADITORE 376 . MADONNA TRANQUILLANTE 377 . MADONNA TRANSESSULE 378 . MADONNA TRATTATO CON ACIDO 379 . MADONNA TRATTORE 380 . MADONNA TRATTRICE 381 . MADONNA TRAUMATIZZATO 382 . MADONNA TRAVESTITO 383 . MADONNA TRICOLATA 384 . MADONNA TRIFOSFATO DE SANTI 385 . MADONNA TRINCIATA 386 . MADONNA TRITATA   387 . MADONNA TRIVELLA   388 . MADONNA TRIVELLATA 389 . MADONNA TROGLODITA 390 . MADONNA TROJA DA CONCORSO 391 . MADONNA TROMBATA 392 . MADONNA TROMBETTA 393 . MADONNA TROTA   394 . MADONNA TRUCIOLATA 395 . MADONNA TRUCIOLO 396 . MADONNA TTT (TANTO TE TRITO) 397 . MADONNA TUMOROSO 398 . MADONNA TURCA   399 . MADONNA TURISTICA 400 . MADONNA UFO   401 . MADONNA UNANIME 402 . MADONNA USURAIA 403 . MADONNA VAGABONDO 404 . MADONNA VAMPIRO   405 . MADONNA VASCOLARE 406 . MADONNA VECCHIA COME IL MONDO 407 . MADONNA VELENOSA 408 . MADONNA VENEZUELANO 409 . MADONNA VERME   410 . MADONNA VERNICIATA 411 . MADONNA VIGILANTES 412 . MADONNA VIGILE   413 . MADONNA VIGILESSA 414 . MADONNA VIGLIACCA 415 . MADONNA VIPERA   416 . MADONNA VISCIDA   417 . MADONNA VOMITEVOLE 418 . MADONNA WAFER   419 . MADONNA X-MEN   420 . MADONNA XXX   421 . MADONNA YOGURT   422 . MADONNA ZAMPOGNARA 423 . MADONNA ZINGARA   424 . MADONNA ZOCCOLA DA GARA 425 . MADONNA ZUZZURELLONA"
input_d = "1 . DIO ABACO   2 . DIO 80 MALOSSI   3 . DIO A PECORINA   4 . DIO A STRISCE BIANCO NERE 5 . DIO ABBACCHIO   6 . DIO ABBAGLIANTE   7 . DIO ABBANDONATO   8 . DIO ABBEVERATO   9 . DIO ABBREVIATO   10 . DIO ABBRUSTOLITO SULLA GRATICOLA 11 . DIO ABULICO   12 . DIO ACCALAPPIACANI 13 . DIO ACCECATO   14 . DIO ACCENDINO   15 . DIO ACCETTATO   16 . DIO ACCHIAPPACAZZI 17 . DIO ACCORATO   18 . DIO ACCREDITATO SU CONTO CORRENTE 19 . DIO ACETATO   20 . DIO ACETONE   21 . DIO ACULEO   22 . DIO AEREODINAMICO   23 . DIO AFFILATO   24 . DIO AGNELLO   25 . DIO AGRICOLTORE   26 . DIO AGUZZINO   27 . DIO ALBANESE   28 . DIO ALCE       29 . DIO ALETTONE   30 . DIO ALGERINO   31 . DIO ALIENO   32 . DIO ALLIGATORE   33 . DIO ALLOCCO   34 . DIO ALLUPATO   35 . DIO ALLUVIONATO   36 . DIO ALTIMETRO   37 . DIO ALTOATESINO   38 . DIO ALTOFORNO   39 . DIO AMANTE DEL KAMASUTRA 40 . DIO AMERICANIZZATO 41 . DIO AMMUFFITO   42 . DIO AMMUTOLICO   43 . DIO ANEMICO   44 . DIO ANIMALE DA CACCIA 45 . DIO ANIMALISTA   46 . DIO ANTENNISTA   47 . DIO ANTIBIOTICO   48 . DIO ANTICALCARE   49 . DIO ANTICHIESA   50 . DIO ANTICO   51 . DIO ANTICRISTO   52 . DIO ANTIDOTO   53 . DIO ANTILOPE   54 . DIO ANTROPOMORFO   55 . DIO APETTO   56 . DIO APOSTROFO   57 . DIO APPASSITO   58 . DIO APPESANTITO   59 . DIO APPESTATO   60 . DIO ARATRO   61 . DIO ARCHIBUGIO   62 . DIO ARCIDIAVOLO   63 . DIO AROMATICO   64 . DIO ARRAPATO   65 . DIO ARRESTATO   66 . DIO ARRICCIATO   67 . DIO ARROSTITO   68 . DIO ARTEFATTO   69 . DIO ARTICO   70 . DIO ARTICOLAZIONE   71 . DIO ARTIGIANO   72 . DIO ASINDETO   73 . DIO ASINO       74 . DIO ASOCIALE   75 . DIO ASSASSINO   76 . DIO ASSATANATO   77 . DIO ASSEGNO IN BIANCO 78 . DIO ASSENTE   79 . DIO ASSETATO   80 . DIO ASSORBENTE   81 . DIO ASSUNTO   82 . DIO ASTICE       83 . DIO ASTRATTO   84 . DIO ASTROGATTO   85 . DIO ASTRONAUTA   86 . DIO ATEO       87 . DIO ATOMIZZATO   88 . DIO ATOMO DI MERDA 89 . DIO ATOSSICO   90 . DIO ATTANASIO   91 . DIO ATTORE   92 . DIO ATTORE DE FILM PORNO CON ANIMALI 93 . DIO AUTOMA   94 . DIO AUTOMATICO   95 . DIO AUTOSTOPPISTA   96 . DIO AVVELENATO   97 . DIO AVVITATO   98 . DIO BAGAGLIO A MANO 99 . DIO BALESTRA   100 . DIO BALESTRIERE   101 . DIO BAMBOCCIO   102 . DIO BARATTOLINO SAMMONTANA 103 . DIO BARBABLU   104 . DIO BARBAGIANNI   105 . DIO BARISTA   106 . DIO BASTARDO   107 . DIO BASTIGNATORE INCALLITO 108 . DIO BASTONATO   109 . DIO BASTONATO AL CALEN DI MAGGIO 110 . DIO BASTONATO CON UN PALO CHIODATO 111 . DIO BECCAMORTO   112 . DIO BECCHINO   113 . DIO BELZEBU'   114 . DIO BENGALINO   115 . DIO BESTIA       116 . DIO BIRBA       117 . DIO BISONTE IN CARICA 118 . DIO BOA       119 . DIO BOCCIA   120 . DIO BOIA       121 . DIO BOSSI       122 . DIO BRADIPO   123 . DIO BURRASCOSO   124 . DIO BURRONE   125 . DIO BOSCAIOLO   126 . DIO CACACAZZI   127 . DIO CACIOCAVALLO   128 . DIO CADAVERE   129 . DIO CAFASSO (PROFESSORE STRONZO DI MECCANICA) 130 . DIO CAFFETTIERA   131 . DIO CALCESTRUZZO   132 . DIO CAMALDOLESE   133 . DIO CAMERA MORTUARIA 134 . DIO CAMION DA CAVA 135 . DIO CAMIONISTA   136 . DIO CAMMELLO   137 . DIO CANCEROGENO   138 . DIO CANCHEROSO   139 . DIO CANE       140 . DIO CANE BASTARDINO 141 . DIO CANE DA CORSA   142 . DIO CANE DA TARTUFO 143 . DIO CANE LUPO   144 . DIO CANGURO   145 . DIO CANNCELLIERE TEDESCO 146 . DIO CANNIBALE   147 . DIO CANTANTE HARD CORE 148 . DIO CAPOCOLLO   149 . DIO CAPRETTO   150 . DIO CAPRONE   151 . DIO CARABINIERE   152 . DIO CARRO ARMATO   153 . DIO CASSONETTO   154 . DIO CASTRATO   155 . DIO CAVALIERE   156 . DIO CAVALLO   157 . DIO CELLULARE CO LE BATTERIE SCARICHE 158 . DIO CEMENTO ASRMATO 159 . DIO CERCACAZZI   160 . DIO CIAMBELLONE   161 . DIO CICLISTA   162 . DIO CIMICIONE   163 . DIO CINESE       164 . DIO CINOFILO   165 . DIO CIOCCOLATINO AL CAFFE' 166 . DIO CO LE SCARPE DE GOMMA 167 . DIO COLLEZIONISTA DI FRANCOBOLLO 168 . DIO CONTRABBASSO   169 . DIO CORNUTO   170 . DIO CORNUTO A PRIMAVERA 171 . DIO CPU       172 . DIO CREPACCIO   173 . DIO CROATO   174 . DIO CUBISTA   175 . DIO CUNELLO (CONIGLIO) 176 . DIO DEMENTE   177 . DIO DIAVOLO   178 . DIO DIO BORSONE DA VIAGGIO 179 . DIO DIO CANE DA CACCIA ZOPPO, CIECO DA N'OCCHIO E CO NA RECCHIA MONCA 180 . DIO DIO CAPRONE DA MONTA CO SOTTO LA MADONNA 181 . DIO DIO GORILLA   182 . DIO DIO LECCACULO   183 . DIO DIO MERLUZZO   184 . DIO DIO ORSO POLARE 185 . DIO DIO PECORO SORDOMUTO 186 . DIO DIO PIDOCCHIO   187 . DIO DIO REX   188 . DIO DIO SCIMMIONE   189 . DIO DIO SPIAGGIA, PORCO PER OGNI GRANELLO DE SABBIA 190 . DIO DIO TORERO   191 . DIO DIO TRENO MERCI PIENO DE RISO, DUE VOLTE PORCO PER OGNI CHICCO 192 . DIO DROMEDARIO   193 . DIO EBREO       194 . DIO ELETTRICISTA FUORI FASE 195 . DIO EPILETTICO   196 . DIO ESPLOSIVO   197 . DIO ET       198 . DIO FACCHINO   199 . DIO FAGIANO   200 . DIO FALEGNAME   201 . DIO FANCIULLO IN FIORE SOOTO UNA MACCHINA 202 . DIO FATTUCCHIERE   203 . DIO FEDIFRAGO   204 . DIO FENOMENO DA CIRCO 205 . DIO FINOCCHIONE DA GARA 206 . DIO FISCHIA BOTTO   207 . DIO FORMICHIERE   208 . DIO FORMICOLOSO   209 . DIO FORMICONE   210 . DIO FRACICO   211 . DIO FRACICO DE DEBITO 212 . DIO FRANKSTEIN   213 . DIO FRATE FRANCESCANO 214 . DIO FRATE NANO   215 . DIO FRICCHETTONE   216 . DIO FROCIONE   217 . DIO FRUSTATO   218 . DIO FUCILE A POMPA   219 . DIO FUMACANNE   220 . DIO FUMATORE DE MARIJUNA 221 . DIO FUMATORE DE SIGARI CUBANI 222 . DIO FUMATORE D'OPPIO 223 . DIO FUNGO FRACICO   224 . DIO FUORIBORDO   225 . DIO FURIOSO   226 . DIO GALLIANI   227 . DIO GANGSTER   228 . DIO GATTO       229 . DIO GATTO       230 . DIO GATTOPARDO   231 . DIO GAY       232 . DIO GAZEBO   233 . DIO GIAPPONESE   234 . DIO GIBBONE   235 . DIO GIOCATORE DI CALCIO 236 . DIO GIOVANE GAY IN CARRIERA 237 . DIO GOBBO       238 . DIO GOLOSO DE CAZZI 239 . DIO GRILLO       240 . DIO HITLER   241 . DIO HOMER   242 . DIO IDROCEFALO   243 . DIO IFROCIATO   244 . DIO IMPESTATO   245 . DIO IMPOTENTE   246 . DIO INCASTONATO   247 . DIO INCEMENTATO   248 . DIO INCENDIARIO   249 . DIO INCENERITO CO TUTTA LA CASSA 250 . DIO INCULATO   251 . DIO INFEROCITO   252 . DIO INFERRIATO   253 . DIO INFRASCATO   254 . DIO IPPOPOTAMO   255 . DIO ISTRICE   256 . DIO JOKER       257 . DIO KEROSENE   258 . DIO KOALA   259 . DIO LADRO       260 . DIO LADRO DE GALLINE 261 . DIO LARVA   262 . DIO LEBBROSO   263 . DIO LEGHISTA CONVINTO 264 . DIO LEONE       265 . DIO LETAME   266 . DIO LICANTROPO   267 . DIO LIOFILIZZATO   268 . DIO LUCIDATO CO LA RASPA 269 . DIO LUMACONE   270 . DIO LUPENTE MEZZO LUPO MEZZO SERPENTE 271 . DIO LUPIN       272 . DIO LUPO       273 . DIO MACACO   274 . DIO MACELLAIO   275 . DIO MADONNA   276 . DIO MAESTRO DI KARATE 277 . DIO MAGNACCIA   278 . DIO MAGO       279 . DIO MAIALE   280 . DIO MAIALE DA FIERA CAMPIONARIA 281 . DIO MANOVALE   282 . DIO MARCHIAPONE   283 . DIO MARESCIALLO   284 . DIO MARROCCHINO LAVAVETRI 285 . DIO MARTIRE   286 . DIO MARZIANO   287 . DIO MASCARPONE   288 . DIO MASOCHISTA   289 . DIO MASSETTO   290 . DIO MASTICATO DA SAN PIETRO 291 . DIO MASTURBA CAVALLI 292 . DIO MATTONATO   293 . DIO MATTONE   294 . DIO MAZINGA   295 . DIO MICROCEFALO   296 . DIO MILITE IGNOTO   297 . DIO MINESTRONE   298 . DIO MISSILE A TESTATA NUCLEARE DIRETTO VERSO IL PARADISO 299 . DIO MITOMANE   300 . DIO MODEM   301 . DIO MONACO HITLERIANO 302 . DIO MONCO   303 . DIO MORTO DE FAME   304 . DIO MOSAICO   305 . DIO MOSCHIETTIERE   306 . DIO MOSTRO DI LOCHNESS 307 . DIO MUSULMANO   308 . DIO NANO BOCCHINARO 309 . DIO NANO CANCEROGENO 310 . DIO NANO RADIOTTIVI 311 . DIO NANO RICCHIONE   312 . DIO NASCOSTO NELL'UTERO DE LA MADONNA 313 . DIO NEGROMANTE   314 . DIO OMOSESUALE   315 . DIO ORNITOLOGO   316 . DIO ORNITORINCO   317 . DIO PAGLIACCIO   318 . DIO PAPERO   319 . DIO PARMIGIANO REGGIANO 320 . DIO PARTICOLARMENTE GAY 321 . DIO PASTORE TEDESCO SPELATO 322 . DIO PASTORELLO ZOPPO 323 . DIO PECORARO SARDO 324 . DIO PECORINO   325 . DIO PEDERASTA   326 . DIO PEDOFILO   327 . DIO PEDOFILO   328 . DIO PELLICOLA 8mm   329 . DIO PERCOSSO CON UN MARTELLO PNEUMATINCO 330 . DIO PERICOLANTE   331 . DIO PESCE CANE   332 . DIO PESCE D'APRILE   333 . DIO PESCE RAGNO   334 . DIO PESTILENZIALE   335 . DIO PESTILENZIALE   336 . DIO PETO       337 . DIO PEZZENTE   338 . DIO PICCIONE VIAGGIATORE 339 . DIO PIEDE DE PORCO   340 . DIO PIGLIAMOSCHE   341 . DIO PIGMAGLIONE   342 . DIO PIOPPO       343 . DIO PIPPONE   344 . DIO PIROMANE   345 . DIO PIROSCAFO   346 . DIO PIZZAIOLO   347 . DIO POCCIA CAZZI   348 . DIO POKER DE SANTI   349 . DIO POLINI FOR RACE   350 . DIO POMPINARO DA CORSA 351 . DIO PORCELLINO D'INDIA 352 . DIO PORCO       353 . DIO PORCO DA MONTA 354 . DIO POSTER   355 . DIO PRATAIOLO   356 . DIO PROFESSORE DI ANTICRISTIANESIMO 357 . DIO PUBBLICO MINISTERO DELLA SANITA' 358 . DIO PUTTANARO   359 . DIO PUZZLE   360 . DIO PUZZOLA   361 . DIO RADIOATTIVO   362 . DIO RAGNO       363 . DIO RATTO DE FOGNA   364 . DIO RAZZO       365 . DIO RICCIO       366 . DIO RIN TIN TIN   367 . DIO ROMPIPALLE   368 . DIO ROSI BINDI   369 . DIO ROSPO       370 . DIO ROSPO       371 . DIO ROSPONE   372 . DIO ROZZO       373 . DIO SADOMASOCHISTA 374 . DIO SALAMANDRA   375 . DIO SALAME   376 . DIO SALCICCIOTTO   377 . DIO SANDOKAN   378 . DIO SASSAIOLO   379 . DIO SATANASSO   380 . DIO SATELLITARE   381 . DIO SCALZO SUI CHIODI 382 . DIO SCAMORZA   383 . DIO SCANSAFATICHE   384 . DIO SCANZACAZZI   385 . DIO SCASSACAZZI   386 . DIO SCIMATARRA   387 . DIO SCIMMIONE   388 . DIO SCIOLINA   389 . DIO SCOMPOSTO   390 . DIO SEGUACE DE SATANA 391 . DIO SENZA VENTRICOLO 392 . DIO SENZAPENE   393 . DIO SERFISTA SPELACCHIATO 394 . DIO SERPENTE   395 . DIO SFORNATO   396 . DIO SGOZZATO   397 . DIO SICILIANO CO LA LUPARA 398 . DIO SILURO       399 . DIO SOMARO   400 . DIO SOMARO SARDO NANO DA MONTA 401 . DIO SORCONE   402 . DIO SPACCIATORE   403 . DIO SPAZZACAMINO   404 . DIO SPAZZINO AFRICANO 405 . DIO SPIGOLOSO   406 . DIO SPILORCIO   407 . DIO SPOLMONATO   408 . DIO SPUPAZZAPRETE   409 . DIO STECCHINO   410 . DIO STRALUNATO   411 . DIO STRAMPALATO   412 . DIO STRAPAZZATO   413 . DIO STRAPIOMBO   414 . DIO STREZZICATO   415 . DIO STRIGLITO CO NA SPAZZOLA DE FERRO 416 . DIO STRIMPELLATO DAL PAPA 417 . DIO STROMBETTATO   418 . DIO STRONZO   419 . DIO STROZZATO   420 . DIO STROZZINO   421 . DIO STRUMTRUPPEN   422 . DIO STRUZZO   423 . DIO STRUZZO DA CORSA 424 . DIO STUNTMAN   425 . DIO STUPRATO DA UN NEGRO CON UN CAZZO DI 35 cm 426 . DIO SUDICIO   427 . DIO SUINO       428 . DIO SUPER SAJAN DI 2 LIVELLO 429 . DIO SVENTRAPAPERE   430 . DIO SVENTRATO   431 . DIO SVIOLINATO   432 . DIO SVIZZERO   433 . DIO TACCO A SPILLO DE LE SCARPE DE LA MADONNA 434 . DIO TARALLUCCIO   435 . DIO TARTUFO   436 . DIO TASSISTA   437 . DIO TOCCO DE LARDO   438 . DIO TOPO D'APPARTAMENTO 439 . DIO TOPORAGNO   440 . DIO TORO IN CARICA VERSO LA MADONNA VESTITA DE ROSSO 441 . DIO TOSSICODIPENDENTE 442 . DIO TRADITORE   443 . DIO TRANQUILLANTE   444 . DIO TRANSESSULE   445 . DIO TRATTATO CON ACIDO 446 . DIO TRATTORE   447 . DIO TRAUMATIZZATO 448 . DIO TRAVESTITO   449 . DIO TRIFOSFATO DE SANTI 450 . DIO TROGLODITA   451 . DIO TUMOROSO   452 . DIO UFO       453 . DIO VAGABONDO   454 . DIO VAMPIRO   455 . DIO VENEZUELANO   456 . DIO VERME       457 . DIO VIGILANTES   458 . DIO VIGILE       459 . DIO WAFER   460 . DIO X-MEN       461 . DIO XXX       462 . DIO YOGURT"

def adjuster():

    in_array = input_m.split("MADONNA")
    in_array.pop(0)
    in_array.pop(177)
    in_array.pop(353)
    out_array = []
    i = 1
    for el in in_array:
        i += 1

        cleaned_el = el.replace("{} .".format(i), "")
        out_array.append(" ".join(cleaned_el.lower().split()))

    out = ""
    for el in out_array:
        out += '"{}",\n'.format(el)

    log = open("words.txt", "w")
    log.write(str(out) + "\r\n")
    log.close()


def remove_name():

    filename = 'badass_sentences.txt'
    var_valor = []
    out = open('out.txt', 'a')
    with open(filename) as file:
        for line in file:
            line = line.replace('Chuck ', '%%%')
            line = line.replace('Norris', '')
            out.write(line)
            var_valor.append(line)
    out.close()


DIO_FUNNY = [
    "acchiappafantasmi",
    "acciaccata",
    "adorata da tutti i diavoli",
    "allampanata",
    "allupata",
    "amarena",
    "anticristo",
    "antilope",
    "arpa",
    "arpia",
    "arpione",
    "assassina",
    "astronauta",
    "attrice di film porno",
    "avvelenata coi funghi",
    "baaustra",
    "bacarazzo",
    "balestraia",
    "ballerina de flamenco",
    "bananiera",
    "bandiera",
    "bandita",
    "barattata per una grande mignotta",
    "barattolino sammontana",
    "barbagianni",
    "barchetta",
    "bascula",
    "bastarda",
    "bastonata",
    "bastronza",
    "batteria per auto",
    "batterista",
    "battona",
    "belva assassina",
    "bisettrice",
    "bocchinara",
    "bombata",
    "bombona",
    "bradipa",
    "buddhista",
    "bussola",
    "cacata",
    "calcolatrice",
    "cammella",
    "cammelliera",
    "cancro",
    "cannibale",
    "cantautrice",
    "capomignotta",
    "capotroia",
    "capozoccola",
    "capra",
    "capra",
    "carcata col breccione",
    "cavalla",
    "cavalletta",
    "cavalletta zoppa",
    "che suona il piano e cristo la tromba (in tutti i sensi)",
    "chiappamosce",
    "ciambotta",
    "cicoriona",
    "cimurrosa",
    "coccodrilla",
    "compressata",
    "comunista",
    "con un cazzo in culo e uno in fica",
    "cornuta",
    "cretina",
    "crocifissa",
    "crocodile dundee",
    "cubbista russa",
    "damigiana",
    "danger",
    "darbula",
    "diavola",
    "diavolessa",
    "diavolina",
    "drogata",
    "drogata in comunita'",
    "ebraica sverniciata",
    "embolosa",
    "fagiana",
    "farfalla arrostista sul cannello del signore",
    "fattucchira",
    "fedifraga",
    "fenomeno da circo",
    "filtro",
    "fischia botto",
    "fischietto",
    "fltrata",
    "formichire",
    "formicolosa",
    "formicona",
    "fracica",
    "fragola ammuffita",
    "fricchettona",
    "frrustata",
    "fumatrice de marijuana",
    "gangster",
    "giapponese",
    "gitana",
    "golosa de cazzi",
    "grassona",
    "grattaformaggio",
    "guardia caccia",
    "handicappata",
    "illimitata",
    "illuminata",
    "imbalsamata",
    "impeciata e impiumata",
    "impiccata",
    "incendiaria",
    "inculata da du cavalli",
    "indiavolata",
    "inverosimile maiala",
    "inviperita",
    "istrice",
    "jessika rabbit",
    "kamikaze",
    "koala",
    "ladra de galline",
    "lardona",
    "lebbrosa",
    "lebbrosa",
    "leccaculo",
    "lesbica",
    "lessie",
    "letamaia",
    "libellula con un tumore per ogni cellula",
    "licantropo",
    "limata",
    "linciata",
    "lodata per i bocchini",
    "luccicosa",
    "lucidata co la spazzola de acciaio",
    "lumaca",
    "lupa",
    "lurida vacca",
    "madre di un drogato",
    "maestra di sessuologia",
    "magnabanane",
    "maiala",
    "maiala da corsa",
    "maiala da riproduzioneù",
    "maledetta",
    "masochista da competizione",
    "massetto",
    "masticato da san pietro",
    "masturba cavalli",
    "masturbatrice de cavalli",
    "mattonato",
    "mattone",
    "mazinga",
    "merdaccia",
    "microcefalo",
    "mignotta",
    "milite ignoto",
    "minestrone",
    "minorata",
    "missile a testata nucleare diretto verso il paradiso",
    "mitomane",
    "modem",
    "monaco hitleriano",
    "monco",
    "morto de fame",
    "mosaico",
    "moschiettiere",
    "mostro di lochness",
    "mummia",
    "musulmano",
    "naja",
    "nana",
    "nano bocchinaro",
    "nano cancerogeno",
    "nano radiottivi",
    "nano ricchione",
    "nascosto nell'utero de la",
    "naufraga",
    "negromante",
    "nerchiosa",
    "oliva ascolana",
    "omosesuale",
    "operata de prostata",
    "orba",
    "orca",
    "ornitologo",
    "ornitorinco",
    "pagliaccio",
    "pantegana",
    "papero",
    "parapleggica",
    "parmigiano reggiano",
    "particolarmente gay",
    "pastore tedesco spelato",
    "pastorello zoppo",
    "pecoraro sardo",
    "pecorino",
    "pederasta",
    "pedofila",
    "pedofilo",
    "pedofilo",
    "pellicola 8mm",
    "percosso con un martello pneumatinco",
    "pericolante",
    "pesce cane",
    "pesce d'aprile",
    "pesce ragno",
    "pestilenziale",
    "pestilenziale",
    "pestilenziale",
    "peto",
    "pezzente",
    "piccione viaggiatore",
    "piede de porco",
    "pietra focaia",
    "pigliamosche",
    "pigmaglione",
    "pioppo",
    "pippone",
    "piromane",
    "piroscafo",
    "pizzaiolo",
    "poccia cazzi",
    "poker de santi",
    "polini for race",
    "pompinaro da corsa",
    "porcellino d'india",
    "porco",
    "porco da monta",
    "poster",
    "prataiolo",
    "professore di anticristianesimo",
    "pubblico ministero della sanita'",
    "putrida vacca",
    "putromizoba (puttana,troja,zoccola e battona)",
    "puttanaro",
    "puzzle",
    "puzzola",
    "radioattivo",
    "ragno",
    "rapata",
    "ratto de fogna",
    "razzista",
    "razzo",
    "riccio",
    "rin tin tin",
    "rompipalle",
    "rompipalle",
    "rosi bindi",
    "rospo",
    "rospo",
    "rospone",
    "rozzo",
    "sadomasochista",
    "sadomasochista",
    "salamandra",
    "salame",
    "salcicciotto",
    "sandokan",
    "sassaiolo",
    "satanassa",
    "satanasso",
    "satellitare",
    "sbandieratrice",
    "sbudellata",
    "scalzo sui chiodi",
    "scamorza",
    "scannata",
    "scansafatiche",
    "scanzacazzi",
    "scarica",
    "scarpa",
    "scarsa",
    "scartata come na caramella",
    "scartavetrata",
    "scassacazzi",
    "scatenata",
    "scimatarra",
    "scimmione",
    "scimpanzè",
    "sciolina",
    "scomposto",
    "scoreggiona",
    "scorticata",
    "scorza",
    "scrofa in calore",
    "sditalinatrice di sante",
    "seguace de satana",
    "senza ventricolo",
    "senzapene",
    "serfista spelacchiato",
    "serpente",
    "serpentessa",
    "serpentina",
    "sfornato",
    "sganassata",
    "sgozzata da un'albanese",
    "sgozzato",
    "siciliano co la lupara",
    "siluro",
    "sola (quella de le scarpe)",
    "somara",
    "somara da riproduzione",
    "somaro",
    "somaro sardo nano da monta",
    "sora nana",
    "sorca",
    "sorcone",
    "spacciatore",
    "spazzacamino",
    "spazzino africano",
    "spigoloso",
    "spilorcio",
    "spolmonato",
    "spupazzaprete",
    "stecchino",
    "stirata",
    "stradale",
    "stralunato",
    "strampalato",
    "strapazzato",
    "strapiombo",
    "stratosferica",
    "stravecchia",
    "strezzicato",
    "striata",
    "striglito co na spazzola de ferro",
    "strimpellato dal papa",
    "strombettato",
    "stronzo",
    "strozzato",
    "strozzino",
    "strumentale",
    "strumtruppen",
    "struzzo",
    "struzzo da corsa",
    "stuntman",
    "stuprato da un negro con un cazzo di 35 cm",
    "succhiacazzi",
    "sudicio",
    "suina",
    "suina",
    "suina massima",
    "suino",
    "super sajan di 2 livello",
    "svenata",
    "sventrapapere",
    "sventrato",
    "sverniciata",
    "sviolinato",
    "svirgolata",
    "svizzero",
    "tacco a spillo de le scarpe de la",
    "tamarindo",
    "tampax",
    "taralluccio",
    "tartufo",
    "tassista",
    "tbc (tubercolosa)",
    "termosifone",
    "terrona",
    "teutonica",
    "tira pompe",
    "tiramisu'",
    "tirchia",
    "tocco de lardo",
    "topa",
    "topo d'appartamento",
    "toporagno",
    "toro in carica verso la",
    "vestita de rosso",
    "torta de mele",
    "tortellone barilla",
    "tossicodipendente",
    "tostapane",
    "traditore",
    "tranquillante",
    "transessule",
    "trattato con acido",
    "trattore",
    "trattrice",
    "traumatizzato",
    "travestito",
    "tricolata",
    "trifosfato de santi",
    "trinciata",
    "tritata",
    "trivella",
    "trivellata",
    "troglodita",
    "troja da concorso",
    "trombata",
    "trombetta",
    "trota",
    "truciolata",
    "truciolo",
    "ttt (tanto te trito)",
    "tumoroso",
    "turca",
    "turistica",
    "ufo",
    "unanime",
    "usuraia",
    "vagabondo",
    "vampiro",
    "vascolare",
    "vecchia come il mondo",
    "velenosa",
    "venezuelano",
    "verme",
    "verniciata",
    "vigilantes",
    "vigile",
    "vigilessa",
    "vigliacca",
    "vipera",
    "viscida",
    "vomitevole",
    "wafer",
    "x-men",
    "xxx",
    "yogurt",
    "zampognara",
    "zingara",
    "zoccola da gara",
    "zuzzurellone"
]


def list_to_file(list_in):
    out = open('out.txt', 'a')
    for line in list_in:
        out.write(line+"\n")
    out.close()


list_to_file(DIO_FUNNY)

example_level_rank = {
    'title': 'Ranking of most Active Users',
    'rank': {
        '1': {
            'username': 'Username',
            'highlights': True,
            'level': '10',
            'level_label': 'LEVEL',
            'value': '2341',
            'max': '8000',
        },
    },
    'text': 'Cool keep going like that',
}

"""                   
    +-----------------------------------------+  
    |              SPAN_BORDER                | span  |              
    +-----------------------------------------+       |                               
    |              SPAN_TITLE                 | span  |  SPAN_TITLE_SECTION                         
    |                                         | span  |                                                                    
    +-----------------------------------------+       | 
    |              SPAN_BORDER                | span  |                         
    +-----------------------------------------+            
    |                                         | span  |                         
    |              SPAN_RANK                  |       |    
    |                                         | span  |  SPAN_RANK_SECTION                     
    +-----------------------------------------+       |
    |              SPAN_SEPARATOR             | span  |    
    +-----------------------------------------+  
    |              SPAN_TEXT                  | span                         
    +-----------------------------------------+  
    |              SPAN_BORDER                | span     at the end of all                        
    +-----------------------------------------+        

"""

SPAN_BORDER = 0.3
SPAN_TITLE = 1.6
SPAN_RANK = 0.8
SPAN_SEPARATOR = 0.6

SPAN_TITLE_SECTION = SPAN_BORDER + SPAN_TITLE + SPAN_BORDER
SPAN_RANK_SECTION = SPAN_RANK + SPAN_SEPARATOR

"""
        +-+------+--------------------+---------------------+-+----------+-+            
        | |      |                    |                     | |          | |                      
   +--> | | RANK |      USERNAME      |    XP_BAR           | | LEVEL    | |      
   |    | |      |                    |                     | |          | |                   
   |    +-+------+--------------------+---------------------+-+----------+-+
OFFSET

"""
DIM_OFFSET = 0.5
DIM_RANK = 2
DIM_USERNAME = 8
DIM_XP_BAR = 6
DIM_LEVEL = 3
