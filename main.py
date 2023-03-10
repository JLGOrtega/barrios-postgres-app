import os

from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
@app.route("/barrios/all", methods=["GET"])
def get_all_barrios():
    # Crea un motor de conexión a la base de datos PostgreSQL
    engine = create_engine('postgresql://postgres:5qViCt4PBn5ISzNTe3nj@containers-us-west-121.railway.app:7703/railway')
    datos = pd.read_sql('select * from "Barrios"', con=engine)
    return jsonify(datos.to_json())

@app.route("/barrios/by_name", methods=["GET"])
def get_barrio_byname():
    barrio = request.args["name"]
    # Crea un motor de conexión a la base de datos PostgreSQL
    engine = create_engine('postgresql://postgres:5qViCt4PBn5ISzNTe3nj@containers-us-west-121.railway.app:7703/railway')
    datos = pd.read_sql(f"""select * from "Barrios" where nombre = '{barrio}'""", con=engine)
    return jsonify(datos.to_json())

@app.route("/barrios/by_area", methods=["GET"])
def get_barrio_byarea():
    area_min = request.args["area_min"]
    area_max = request.args["area_max"]
    # Crea un motor de conexión a la base de datos PostgreSQL
    engine = create_engine('postgresql://postgres:5qViCt4PBn5ISzNTe3nj@containers-us-west-121.railway.app:7703/railway')
    datos = pd.read_sql(f"""select * from "Barrios" 
                            where gis_gis_barrios_area > {area_min} 
                            and gis_gis_barrios_area < {area_max} """, con=engine)
    return jsonify(datos.to_json())


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
