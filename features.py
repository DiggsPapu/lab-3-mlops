from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64, Int64
from datetime import timedelta
# TODO: Definir la entidad (house)
house = Entity(
    name='house',
    join_keys=['house_id']
)
# TODO: Definir el source (archivo parquet con los datos)
house_data_source = FileSource(
    path="data/house_features.parquet",  # ruta al archivo parquet
    timestamp_field="event_timestamp",   # campo de timestamp
    created_timestamp_column="created",  # opcional: cuándo se creó el registro
)
# TODO: Crear FeatureView con las features principales
house_feature_view = FeatureView(
    name="house_features",
    entities=[house],
    ttl=timedelta(days=1),  # tiempo de vida de los datos en el feature store
    schema=[
        Field(name="MedInc", dtype=Int64),
        Field(name="HouseAge", dtype=Float64),
        Field(name="AveRooms", dtype=Float64),
        Field(name="AveBedrms", dtype=Float64),
        Field(name="Population", dtype=Float64),
        Field(name="AveOccup", dtype=Float64),
        Field(name="Latitude", dtype=Float64),
        Field(name="Longitude", dtype=Float64),
        Field(name="MedPP", dtype=Float64),
        Field(name="RatioRoomsBed", dtype=Float64),
        Field(name="MedHouseVal", dtype=Float64),
    ],
    source=house_data_source,
    online=True,  # permite servir en tiempo real
)