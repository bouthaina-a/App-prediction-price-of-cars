import streamlit as st
# import streamlit.components.v1 as components
import pickle 
import numpy as np
# from PIL import Image
# import getCars

def load_model():
    with open('saved_steps.rar/saved_steps.pkl', 'rb') as file:
        data =  pickle.load(file)
    return data

data = load_model()

model = data['model']
encoder_location = data['encoder_location']
encoder_model = data['encoder_model']
encoder_brand = data['encoder_brand']
encoder_origine = data['encoder_origine']
brands_models = { 
 'Renault': ['Clio', 'Laguna', 'Megane', 'R19', 'Kangoo', 'R9', 'Scenic', 'R25', 'Fluence', 'Captur', 'Megane 3',
  'Super 5', 'Trafic', 'Symbol', 'Express', 'Megane Coupe', 'Espace', 'Latitude', 'R21', 'R5', 'R4', 'Laguna Coupe',
  'Megane CC', 'Koleos', 'Talisman', 'Twingo', 'R11', 'R18', 'Kangoo Express', 'Grand Espace', 'Kadjar',
  'Grand Scenic', 'Master', 'Microbus', 'Megane Sedan', 'Grand Modus', 'Modus', 'Zoe', 'Master Ccb',
  'Safrane', 'R8', 'Avantime', 'Laguna Estate', 'B110', 'B120', 'Samsung SM3', 'Vel Satis', 'amarok'],

 'Peugeot': ['205', 'Partner', '208', '206', '206+', '406', '405', '504', '508', '407', '307', '306', '2008', '301',
  '807', '308', 'Tepee', '3008', '309', '204', '207', '106', '207 SW', 'Expert', 'Boxer', '307 SW', '107', '206 SW',
  'Bipper', '5008', '607', '505', '206 CC', '108', '307 CC', 'RCZ', 'J5', '806', '403', '407 SW', '407 COUPE', '305',
  'J9', '308 SW', '104', '605', '207 CC', '304', '404', '4007', '1007'],

 'Skoda': ['Octavia', 'Superb', 'RAPID', 'Fabia', 'Kodiaq', 'Yeti', 'Roomster'],

 'Ford': ['Fiesta', 'Focus', 'Ecosport', 'Kuga', 'Fusion', 'ESCORT', 'Mondeo', 'Mustang', 'Ka', 'Ranger', 'ORION',
  'Transit', 'Tourneo', 'CONNECT', 'Galaxy', 'C-Max', 'CAPRI', 'EXPLORER', 'FOCUS C-MAX', 'SCORPIO', 'MINIBUS', 'F150',
  'ESCAPE', 'BEDFORD', 'COURRIER', 'S-Max'],
 
 'Fiat': ['Uno', 'Palio', 'Siena', 'GRANDE PUNTO', 'Pinto', 'FIORINO', 'Ducato', 'Panda', 'Doblo', 'Punto', '500',
  '126', 'Bravo', '131', 'TIPO', '500C', '500X', 'BRAVA', 'REGATA', 'Linea', 'ULYSSE', 'Albea', '127', 'TEMPRA',
  'MAREA', 'STILO', 'RITMO', '500L', 'IDEA', 'MULTIPLA', 'FREEMONT'],
 
 'Toyota': ['Corolla', 'Prado', 'Avensis', 'Auris', 'Land Cruiser', 'Yaris', 'Hilux', 'RAV 4', 'VERSO', 'Tercel',
  'STARLET', 'Corolla verso', 'FJ CRUISER', 'Aygo', '4RUNNER', 'Hi Ace', 'FJ', 'SIENNA', 'Camry', 'CORONA', 'PREVIA',
  'CELICA', 'MR', 'AVENSIS VERSO'],
 
 'Mercedes-Benz': ['220',
  'Classe C',
  '190',
  'Classe B',
  '270',
  'CLASSE C COUPE',
  'Classe A',
  'Classe E',
  'Classe CLK',
  '250',
  'Classe CLA',
  'Classe GLA',
  'CLASSE ML',
  '240',
  'Classe G',
  'Vito',
  '207D',
  'CITAN',
  'Classe S',
  'CLASSE SLS',
  'Sprinter',
  '210',
  '280',
  'Classe CLS',
  'AMG GT',
  'Classe GLE',
  'Classe M',
  'Classe GLC',
  'Viano',
  'CLASSE GLK',
  '300',
  '400',
  '310D',
  'Classe GL',
  'MB',
  'VANEO',
  'Classe SLK',
  'Classe GLS',
  '410',
  '230',
  '408',
  'Classe V',
  'Classe CL',
  'Classe SL',
  'CLASSE CLC'],
 
 'Volkswagen': ['Passat',
  'GOLF 4',
  'COMBI',
  'Gol',
  'GOLF 2',
  'Caddy',
  'Tiguan',
  'GOLF 7',
  'Touran',
  'GOLF 6',
  'Golf',
  'GOLF 3',
  'Polo',
  'Jetta',
  'PASSAT CC',
  'CC',
  'Touareg',
  'GOLF PLUS',
  'GOLF 5',
  'LUPO',
  'TRANSPORTER',
  'Bora',
  'Fox',
  'Scirocco',
  'Arteon',
  'EOS',
  'MULTIVAN',
  'Vento',
  'SHARAN',
  'Amarok',
  'Beetle',
  'COCCINELLE',
  'Caravelle',
  'PARATI',
  'KARMAN',
  'NEW BEETLE'],
 
 'Dacia': ['Duster', 'Sandero', 'Logan', 'Dokker', 'Dokker Van', 'Logan Mcv', 'Lodgy'],

 'Audi': ['A5',
  'Q7',
  'A3',
  'A6',
  'A4',
  'Q3',
  'Q5',
  '80',
  'S5',
  'A1',
  'RS3',
  'Q2',
  'A8',
  'Coupe',
  'S3',
  'A7',
  'TT',
  'cc',
  '100'],
 
 'Hyundai': ['Santa Fe',
  'Accent',
  'i 40',
  'IX55',
  'ix 35',
  'i 10',
  'i 30',
  'H-1',
  'Tucson',
  'Atos',
  'Elantra',
  'i 20',
  'Veracruz',
  'Atos Prime',
  'CRETA',
  'LANTRA',
  'H-100',
  'Coupe',
  'GALLOPER',
  'TERRACAN',
  'Grand i10',
  'EXCEL',
  'picanto',
  'H',
  'GETZ',
  'XG',
  'Azera',
  'GRANDEUR',
  'Matrix',
  'SANTAMO',
  'CENTENNIAL',
  'SONATA',
  'Genesis'],
 
 'Suzuki': ['Alto',
  'SAMURAI',
  'Swift',
  'Grand Vitara',
  'IGNIS',
  'Carry',
  'SX4',
  'Celerio',
  'Maruti',
  'Vitara',
  'WAGON R',
  'AERIO',
  'JIMNY',
  'SPLASH',
  'BALENO',
  'APV'],
 
 'Opel': ['Corsa',
  'Insignia',
  'COMBO',
  'Astra',
  'Crossland X',
  'ADAM',
  'Vectra',
  'Tigra',
  'MOKKA',
  'Grandland X',
  'VIVARO',
  'Meriva',
  'KADETT',
  'Zafira',
  'Agila',
  'ASCONA',
  'ANTARA',
  'FRONTERA',
  'OPC',
  'CAMPO'],
 
 'Nissan': ['Qashqai',
  'Micra',
  'X-Trail',
  'Juke',
  'NOTE',
  'primera',
  '300',
  'Altima',
  'Murano',
  'Navara',
  'Sunny',
  'ALMERA',
  'Pathfinder',
  'PATROL',
  'VANETTE',
  'Pick up',
  'TERRANO',
  'Tiida',
  'EVALIA',
  'MAXIMA',
  '280',
  '370Z',
  'SERENA',
  'GTR',
  'VERSA',
  '350Z',
  'Patrol GR'],
 
 'Jaguar': ['XF',
  'X-Type',
  'XKR',
  'F-Type',
  'XE',
  'S-Type',
  'XJ',
  'XK8',
  'XJ6'],
 
 'Daihatsu': ['Sirion', 'YRV', 'Terios', 'Copen'],
 
 'Citroen': ['C15',
  'C3',
  'Berlingo',
  'C4',
  'Nemo',
  'C5',
  'SAXO',
  'XSARA',
  'BX',
  'C4 Picasso',
  'C-ELYSEE',
  '2 CV',
  'AX',
  'DS3',
  'C6',
  'XANTIA',
  'GRAND C4 PICASSO',
  'C-Elysée',
  'C1',
  'Xsara Picasso',
  'DS5',
  'Jumper',
  'C3 Cactus',
  'DS7',
  'C4 CACTUS',
  'C-CROSSER',
  'C3 Picasso',
  'DS4',
  'CX',
  'ZX',
  'C2',
  'C8',
  'Jumpy',
  'C3 PLURIEL',
  'DS19',
  'C25',
  'DS'],
 
 'Volvo': ['S60', 'V40', 'XC60', 'C30', 'XC90', 'S40', 'C70', 'S80', 'XC70'],
 
 'Kia': ['Picanto',
  'K2500',
  'Sportage',
  'Sorento',
  'Carens',
  'Rio',
  'Seltos',
  'Cerato',
  'Ceed',
  'Soul',
  'PREGIO',
  'Optima',
  'K2700',
  'Opirus',
  'BESTA',
  'CARNIVAL',
  'CADENZA',
  'CLARUS'],
 
 'BMW': ['Serie 3',
  'Serie 4 gran coupé',
  'Serie 5',
  'Serie 1',
  'X5',
  'M3',
  'Serie 2 coupé',
  'M2',
  'X3',
  'CABRIOLET',
  'Serie 6',
  'Serie 4',
  'Serie 5 GT',
  'Serie 3 coupé',
  'X1',
  'M5',
  'Serie 7',
  'X6',
  'Serie 5 M2',
  'Serie 4 coupé',
  'Serie 3 GT',
  'Z1',
  'M4',
  'M',
  'Serie 2',
  'M6',
  'Serie 8',
  'COMPACT'],
 
 'Land Rover': ['Range Rover Sport',
  'Freelander',
  'Range Rover Evoque',
  'Range Rover',
  'Defender',
  'Discovery',
  'Velar',
  'Discovery Sport'],
 
 'Honda': ['Civic',
  'Accord',
  'CR-V',
  'Vigor',
  'Jazz',
  'FR-V',
  'City',
  'AERODECK',
  'PRELUDE',
  'Legend',
  'INTEGRA',
  'BOSS',
  'fluence',
  'CR-X',
  'ACTY',
  'HR-V',
  'CONCERTO'],
 
 'Porsche': ['Cayenne', 'Panamera', 'Macan', 'Cayman'],
 
 'mini': ['cooper', 'country man', 'one', 'CLUBMAN', 'cabrio'],
 
 'Mitsubishi': ['pajero sport',
  'lancer',
  'pajero',
  'L200',
  'nativa',
  'outlander',
  'pick up',
  'canter',
  'Grandis'],
 
 'Jeep': ['Grand Cherokee', 'Wrangler', 'Cherokee', 'Compass', 'Renegade'],
 
 'Seat': ['Ibiza',
  'Cordoba',
  'Leon',
  'ALTEA XL',
  'Toledo',
  'Ateca',
  'Altea',
  'ALHAMBRA',
  'INCA',
  'LEON ST',
  'MALAGA'],
 
 'Daewoo': ['Lanos',
  'Kalos',
  'Evanda',
  'Matiz',
  'Nubira',
  'Rezzo',
  'Musso',
  'Espero',
  'Lacetti'],
 
 'Alfa Romeo': ['Mito',
  'GIULIA',
  '159',
  'Giulietta',
  'Stelvio',
  '147',
  '75',
  '147 gta',
  '156',
  '145',
  'Gt',
  '33',
  'Spider'],
 
 'Ssangyong': ['Kyron',
  'Korando',
  'Actyon',
  'STAVIC',
  'Rexton',
  'Ceo',
  'FAMILY'],
 
 'Chevrolet': ['Spark',
  'Cruze',
  'Optra',
  'Aveo',
  'Captiva',
  'Camaro',
  'Lacetti',
  'Alero',
  'Corvette',
  'TACUMA',
  'Astro',
  'CMP',
  'CR8'],
 
 'Chery': ['Tiggo', 'QQ', 'A113', 'a5', 'QQ6', 'A516', 'Eastar', 'a1'],
 
 'Mazda': ['6', '323', '3', '2', 'MX-5', 'CX-9', '5', 'PREMACY', 'RX-8', 'B 2500', 'CX7', 'MX6', '121'],
 
 'Maserati': ['Ghibli', 'Quattroporte']
}
models_4x4 = ['Santa Fe', 'Qashqai', 'Prado', 'Range Rover Sport', 'Q7',
       'Cayenne', 'pajero sport', 'Kuga', 'Grand Cherokee', 'IX55',
       'Freelander', 'Land Cruiser', 'lancer', 'ix 35', 'X-Trail',
       'Kyron', 'Sportage', 'Sorento', 'Juke', 'CR-V', 'XC60', 'Hilux',
       'pajero', 'Seltos', 'RAV 4', 'Wrangler', 'Touareg', 'Q3', 'Tiggo',
       'Grand Vitara', 'Korando', 'Tucson', 'Range Rover Evoque', 'Q5',
       'L200', 'Ranger', 'CLASSE ML', 'nativa', 'Classe G', 'Range Rover',
       'X5', 'country man', 'Veracruz', 'Defender', 'CRETA', 'Cherokee',
       'S5', 'X3', 'Captiva', 'RS3', 'Discovery', 'Murano', 'Stelvio',
       'Actyon', 'X1', 'Navara', 'Ateca', 'STAVIC', 'Rexton',
       'Classe GLE', 'Kodiaq', 'DS7', 'Q2', 'Classe M', 'Compass',
       'Velar', 'XC90', 'outlander', 'Ceo', 'Classe GLC', 'Macan',
       'CLASSE GLK', 'CX-9', 'Pathfinder', 'X6', 'S3', 'FAMILY',
       'Discovery Sport', 'pick up', 'MOKKA', 'Grandland X', 'GALLOPER',
       'Renegade', '4RUNNER', 'Classe GL', 'TERRACAN', 'PATROL',
       'EXPLORER', 'Amarok', 'Pick up', 'TERRANO', 'Classe GLS', 'F150',
       'XC70', 'FREEMONT', 'B 2500', 'GTR', 'ANTARA', 'FRONTERA',
       'CARNIVAL', 'CAMPO', 'HR-V', 'Patrol GR']

def show_predict_page():
    st.title("Prédiction de prix des voitures d'occasions")
    st.write("""### Nous avons besoin de certaines informations pour générer l'estimation""")

    # location
    locations = encoder_location.classes_.tolist()
    location_choose = st.selectbox("Ville", locations, index=locations.index('Casablanca')) 

    # brand
    brands = encoder_brand.classes_.tolist()
    brand_choose = st.selectbox("Marque", brands)
    
    # model
    if brand_choose:
        models = brands_models[brand_choose]
        model_choose = st.selectbox("Modèle", models) 

    # fuel type
    fuel_type_choose = st.selectbox("Carburant", ['Diesel', 'Essence']) 

    # st.button("+ Plus de filters")
    # st.write("\n")
    # fiscal power
    fiscal_power_choose = st.slider("Puissance Fiscale (CV)", 4, 40, (6, 9), step=1)
    fiscal_power_min = fiscal_power_choose[0]
    fiscal_power_max = fiscal_power_choose[1]
    fiscal_power_avg = fiscal_power_min + round((fiscal_power_max-fiscal_power_min)/2)

    # model year
    model_year_choose = st.slider("Année", 1979, 2021, (2018, 2020), step=1)
    model_year_min = model_year_choose[0]
    model_year_max = model_year_choose[1]
    model_year_avg = model_year_min + round((model_year_max-model_year_min)/2)

    # mileage
    mileage_choose = st.slider("Kilométrage", 0, 500_000, (25_000, 100_000), step=5000)
    min_mileage_choose = mileage_choose[0]
    max_mileage_choose = mileage_choose[1]
    avg_mileage_choose = min_mileage_choose + round((max_mileage_choose-min_mileage_choose)/2)

    # gear box
    gear_box_choose = st.selectbox("Boite de vitesses", ['Manuelle', 'Automatique']) 

    # nomber of doors
    nombre_portes_choose = st.selectbox("Nombre de portes", [5, 3])

    # first hand
    first_hand_choose = st.selectbox("Première main", ["Oui important", "Non important"])
    if first_hand_choose == "Oui important":
        first_hand_choose = 1
    else:
        first_hand_choose = 0

    # origine
    origines = encoder_origine.classes_.tolist()
    origine_choose = st.selectbox("Origine", origines, index=origines.index('WW au Maroc'))

    # 4x4
    is_4x4_choose = 0

    if model_choose in models_4x4:
        is_4x4_choose = 1
    
    ok = st.button("Prédire le prix")

    if ok:
        location_choose_ = encoder_location.transform([location_choose])
        brand_choose_ = encoder_brand.transform([brand_choose])
        model_choose_ = encoder_model.transform([model_choose])
        origine_choose_ = encoder_origine.transform([origine_choose])

        if fuel_type_choose == 'Diesel':
            fuel_type_choose_ = 1
        else:
            fuel_type_choose_ = 0
        
        fiscal_power_choose_ =  fiscal_power_avg

        model_year_choose_ = model_year_avg

        if gear_box_choose == "Automatic":
            gear_box_choose_ = 1
        else:
            gear_box_choose_ = 0

        X = np.array([
            [ 
                location_choose_,
                fuel_type_choose_, 
                fiscal_power_choose_, 
                gear_box_choose_, 
                brand_choose_, 
                model_choose_, 
                model_year_choose_, 
                nombre_portes_choose, 
                origine_choose_, 
                first_hand_choose, 
                min_mileage_choose, 
                max_mileage_choose, 
                is_4x4_choose
            ]
        ])

        X_min = np.array([
            [ 
                location_choose_,
                fuel_type_choose_, 
                fiscal_power_min, 
                gear_box_choose_, 
                brand_choose_, 
                model_choose_, 
                model_year_min, 
                nombre_portes_choose, 
                origine_choose_, 
                first_hand_choose, 
                min_mileage_choose, 
                max_mileage_choose, 
                is_4x4_choose
            ]
        ])

        X_max = np.array([
            [ 
                location_choose_,
                fuel_type_choose_, 
                fiscal_power_max, 
                gear_box_choose_, 
                brand_choose_, 
                model_choose_, 
                model_year_max, 
                nombre_portes_choose, 
                origine_choose_, 
                first_hand_choose, 
                min_mileage_choose, 
                max_mileage_choose, 
                is_4x4_choose
            ]
        ])
  
        price = model.predict(X)
        price = round(price[0]/1000)*1000
        st.subheader(f"Le prix moyen estimé est {price:.2f} DH")

        price_min = model.predict(X_min)
        price_min = round(price_min[0]/1000)*1000

        price_max = model.predict(X_max)
        price_max = round(price_max[0]/1000)*1000
        st.subheader(f"{price_min:.2f} DH - {price_max:.2f} DH")
        

        # cars = getCars.cars(location_choose, price_min, price_max, brand_choose, model_choose)

        # st.subheader(f"Exemple des voitures : ")
        # components.iframe(getCars.url(location_choose,price_min, price_max, brand_choose, model_choose), width=700, height=1000, scrolling=True)

        # for car in cars:
        #     st.write(f"{car[0]} : {car[1]} ")
        #     # image = Image.open(car[3])
        #     st.image(car[3], width=250, use_column_width=True)
        #     st.button('Voir Plus')

