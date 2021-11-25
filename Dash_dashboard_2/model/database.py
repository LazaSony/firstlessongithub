import pandas as pd
import sqlite3

class SQL():
    DATABASE_PATH = r'C:\Users\user\Python Dan\Dash_dashboard_2\data\flights.db'
    # DATABASE_PATH = '../data/flights.db'
    
    def __init__(self):
        self.conn = sqlite3.connect(self.DATABASE_PATH, check_same_thread=False)
    
    
    def select_all_airlines(self):
        query ="""SELECT * 
                FROM airlines"""
        df = pd.read_sql(query, 
                        self.conn,)
        return df
            
    def select_all_airports(self):
        query ="""SELECT * 
                FROM airports"""
        df = pd.read_sql(query, 
                        self.conn,)
        return df
            
    def select_all_routes(self):
        query ="""SELECT * 
                FROM routes"""
        df = pd.read_sql(query, 
                        self.conn,)
        return df
    
    def select_graph_airports(self, country):
        query ="""SELECT * 
            FROM airports
            WHERE country = '{}'""".format(country)
        df = pd.read_sql(query, 
                        self.conn,)
        df[["latitude","longitude"]] = df[["latitude","longitude"]].astype(float)
        return df
    
    def insert_arilines(self, name, alias, iata, icao, callsign, country, active):
        query = """INSERT INTO airlines ('name', 'alias', 'iata', 'icao', 'callsign', 'country', 'active')
           VALUES (?, ?, ?, ?, ?, ?, ?)"""
        params = (name, alias, iata, icao, callsign, country, active,)

        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        return True
        