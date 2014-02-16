# Bot patrolling jails in Peru from Twitter

This bot has been developed by [@AniversarioPeru](https://twitter.com/aniversarioperu).

This bot uses the Twitter API 1.1 to collect tweets sent from the proximity of
each jail in Peru.
All tweets are kept into a local SQLite database and mapped onto a Google Maps
page.

You can see the mapped tweets here <http://horis.me/arturitobot>

If a tweet is sent from within any jail, the bot will retweet it from its own
Twitter account [@ArturitoBot](https://twitter.com/ArturitoBot).
More details on the making of **ArturitoBot** can be found in the blog [Útero de
Marita](http://aniversarioperu.utero.pe/2014/02/11/vigilando-las-carceles-del-peru-desde-twitter/)
[in Spanish].

# Jails missing coordinates

* E.P. DE TUMBES	Predio Zarumilla - Puerto El Cura, TUMBES, TUMBES
* E.P. DE CHOTA   Jr. Garcilazo de la Vega N° 231, CHOTA, CHOTA
* E.P. DE PIURA (RIO SECO)	Pan. Norte-Carretera Paita, PIURA, CASTILLA
* E.P. DE HUANCABAMBA	Av. Ramón Castilla S/N., HUANCABAMBA, HUANCABAMBA
* E.P. DE SAN IGNACIO	Caserio Santiago Km. 1, SAN IGNACIO, SAN IGNACIO
* E.P. CHIMBOTE (CAMBIO PUENTE) 	Cambio de Puente S/N, SANTA , CHIMBOTE
* E.P. DEL CALLAO	Prolong. Centenario S/N. Callao, CALLAO, CALLAO
* E.P. DE ICA	Caserio Cachiche S/N., ICA, ICA
* EP. DE YAUYOS	Jr. Trujillo Nº 189 , YAUYOS, YAUYOS
* E.P. DE LA UNION	Jr. Comercio S/N. Cuadra 18, DOS DE MAYO, LA UNION
* E.P. DE CERRO DE PASCO	Barrio Buenos Aires S/N., CERRO DE PASCO, SIMON BOLIVAR
* E.P. DE IQUITOS 	Carret. Guayabamba km. 18.200, MAYNAS, IQUITOS
* E.P. DE BAGUA GRANDE 	Av. Daniel Alcides Carrión 772 Urb. Gonchillo., UTCUBAMBA, BAGUA GRANDE
* E.P. DE TARAPOTO	Av. Circunvalación S/N. Cdra. 11, TARAPOTO, TARAPOTO
* E.P. DE SANAGUILLO	Pampas de Sananguillo, TARAPOTO, TARAPOTO
* E.P. DE HUANCAYO	Av. 28 de Julio S/N, CHUPACA, HUMANCACA CHICO
* E.P. MUJERES DE CONCEPCION	Barrio Tambo Alapa S/N., CONCEPCION, CONCEPCION
* E.P. CHANCHAMAYO	Av. Pacherra S/N., CHANCHAMAYO, LA MERCED
* E.P. DE SATIPO	Av. Augusto B. Leguia N° 767, SATIPO, SATIPO
* E.P. DE LA OROYA	Av. M. Grau y Psje. Los Angeles, OROYA, STA. ROSA DE SACCO
* E.P. DE AYACUCHO (Yanamilla)	Caserio Yanamilla ??Aeropuerto, HUAMANGA, AYACUCHO
* E.P. DE HUANTA	Av. Gervacio Santillana N° 914, HUANTA, HUANTA
* E.P. DE ABANCAY	Jr. Diaz Barcena N° 104, ABANCAY, ABANCAY
* E.P. DE ANDAHUAYLAS	Jr. Ayacucho S/N. (costado Mod.Básico Justicia), ANDAHUAYLAS, ANDAHUAYLAS
* E.P. DE SICUANI	Av. Centenario N° 530, CANCHIS, SICUANI
* E.P. DE QUILLABAMBA	Av. Nicanor Larrea S/N., LA CONVENCION, QUILLABAMBA
* E.P. DE AREQUIPA 	Quebrada La Chuca, AREQUPA, SOCABAYA
* E.P. DE CAMANA 	Centro Poblado Pucchún, CAMANA, MRCAL. CACERES
* E.P. DE MOQUEGUA	Av. Andrés A. Caceres S/N., MRCAL. NIETO, SAMEGUA
* E.P. DE TACNA	Prolong. Av. Hnos. Reynoso S/N, TACNA, POCOLLAY
* E.P. DE LAMPA	Av. Enrique Torres Belón/Jr.28 de Julio, LAMPA, LAMPA	
* EP. DE JULIACA (LA CAPILLA)	"Av.José Santos Chocano Mz""H"" Lote""M4"", SAN ROMAN, JULIACA"
* EP. DE PUNO (YANAMAYO)	Carretera Tiquillaca Km. 5, PUNO, PUNO	
* EP. DE CHALLAPALCA	Fuerte Inclán ??Ejercito Peruano, TARATA, TICACO


* Buscar coordenadas de direcciones: http://www.agenciacreativa.net/coordenadas_google_maps.php
* Todas las cárceles: http://www.inpe.gob.pe/contenidos.php?id=543&np=1&direccion=1
