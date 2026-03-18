import orbital_calculations as f
import nasa_api_client

def list_neos(page) -> list:

    parsed_data = nasa_api_client.neos_page(page)

    neos_set_list_name = []
    neos_set_list = main(page)

    for number_neo in range(0, int(parsed_data["page"]["size"])):
        neos_set_list_name.append(neos_set_list[number_neo][0])
    return neos_set_list_name

def main(page) -> list:

    parsed_data = nasa_api_client.neos_page(page)
    parsed_data_neo = parsed_data["near_earth_objects"]

    neos_set_list = []

    for number_asteroid in range(0, int(parsed_data["page"]["size"])):

        neo_single_dict = {}

        parsed_data_neo_asteroid = parsed_data_neo[number_asteroid]
        name = parsed_data_neo_asteroid["name"]

        try:
            diameter_min = float(parsed_data_neo_asteroid["estimated_diameter"]["miles"]["estimated_diameter_min"])
            diameter_max = float(parsed_data_neo_asteroid["estimated_diameter"]["miles"]["estimated_diameter_max"])

            diameter_interval = [diameter_min, diameter_max]
            diameter_interval = [d * 1000 for d in diameter_interval]

            neo_single_dict["name"] = name
            neo_single_dict["diameter_interval"] = diameter_interval
            neo_single_dict["approaches"] = []

            for approach in parsed_data_neo_asteroid["close_approach_data"]:

                approach_date = approach["close_approach_date_full"]
                velocity_ms = float(approach["relative_velocity"]["kilometers_per_hour"]) / 3.6
                miss_distance = approach["miss_distance"]["kilometers"]

                momentum = f.momentum(
                    f.volume_to_mass(f.diameter_to_sphere_volume(diameter_interval)),
                    velocity_ms
                )

                kinectic_energy = f.kinetic_energy(
                    f.volume_to_mass(f.diameter_to_sphere_volume(diameter_interval)),
                    velocity_ms
                )

                kinectic_energy_in_megatons = f.joules_to_megatons(
                    f.kinetic_energy(
                        f.volume_to_mass(f.diameter_to_sphere_volume(diameter_interval)),
                        velocity_ms
                    )
                )

                neo_single_dict["approaches"].append({
                    "date": approach_date,
                    "velocity_ms": velocity_ms,
                    "momentum": momentum,
                    "kinetic_energy": kinectic_energy,
                    "energy_megatons": kinectic_energy_in_megatons,
                    "miss_distance": miss_distance
                })

        except IndexError:
            pass

        neos_set_list.append([neo_single_dict])

    with open("log.txt", "w") as log:
        log.write(str(neos_set_list))
    return neos_set_list

def select(name, date):
    page = 0

    while True:
        neos = main(page)

        if not neos:
            return None
        
        for neo in neos:
            if neo[0]["name"] == name:

                neo_ = neo[0]
                name = neo_["name"]
                diameter_interval = neo_["diameter_interval"]
                neo_approaches = neo_["approaches"]
                approaches_dates = [neo_approaches[c]["date"] for c in range(0, len(neo_approaches))]
                approaches_data = [[neo_approaches[c]["date"],
                                   neo_approaches[c]["velocity_ms"],
                                   neo_approaches[c]["momentum"],
                                   neo_approaches[c]["kinetic_energy"],
                                   neo_approaches[c]["energy_megatons"],
                                   neo_approaches[c]["miss_distance"]] for c in range(0, len(neo_approaches))]
                if date == 0:
                    return [name, diameter_interval, approaches_dates]
                else:
                    return [name, diameter_interval, approaches_data]
              

        page += 1

