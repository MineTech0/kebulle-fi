from src import db
from psycopg2.extras import NamedTupleCursor


def get_all():
    cursor = db.connection.cursor(cursor_factory=NamedTupleCursor)
    cursor.execute("SELECT id, name FROM regions")

    regions = cursor.fetchall()
    cursor.close()
    return regions


def get_all_with_cities():
    cur = db.connection.cursor()
    cur.execute("SELECT id, name FROM regions ORDER BY name;")
    regions = []
    for region_id, region_name in cur.fetchall():
        cur.execute("SELECT id, name FROM cities WHERE region_id = %s ORDER BY name;", (region_id,))
        cities = [{"id": city_id, "name": city_name} for city_id, city_name in cur.fetchall()]
        regions.append({"id": region_id, "name": region_name, "cities": cities})
    print(regions)
    return regions
