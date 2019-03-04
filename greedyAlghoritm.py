'''looking for  smallest radio stations set to cover the biggest possible area'''

states_needed = set(["lodz","warszawa","wroclaw", "gdansk","krakow"])

stations = {}
stations["zet"] = set(["lodz","warszawa"])
stations["gold"] = set(["krakow","warszawa","wroclaw"])
stations["eska"] = set(["lodz","wroclaw","krakow"])
stations["lodz"] = set(["lodz"])
stations["RMF"] = set(["krakow","gdansk"])


final_stations = set()


while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)
