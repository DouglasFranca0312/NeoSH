from math import pi

approximate_materials_density_in_kg_per_cubic_meter = {
    "rocky": 3000,
    "metallic": 8000,
    "carbonato": 2200
}

amdkgp3m = approximate_materials_density_in_kg_per_cubic_meter

def joules_to_megatons(kinectic_energy):
    if isinstance(kinectic_energy, list):
        result = []
        for j in kinectic_energy:
            if isinstance(j, list):
                result.append([x / 4.184e15 for x in j])
            else:
                result.append(j / 4.184e15)
        return result
    else:
        return kinectic_energy / 4.184e15

def kinetic_energy(mass, velocity):
    if isinstance(mass, list):
        result = []
        for m in mass:
            if isinstance(m, list):
                result.append([0.5 * x * velocity ** 3 for x in m])
            else:
                result.append(0.5 * m * velocity ** 3)
        return result
    else:
        return 0.5 * mass * velocity ** 3


def momentum(mass, velocity):
    if isinstance(mass, list):
        result = []
        for m in mass:
            if isinstance(m, list):
                result.append([x * velocity for x in m])
            else:
                result.append(m * velocity)
        return result
    else:
        return mass * velocity


def volume_to_mass(volume):
    if isinstance(volume, list):
        masses = []
        for v in volume:
            masses_interval = []
            for density in amdkgp3m.values():
                masses_interval.append(v * density)
            masses.append(masses_interval)
        return masses

    else:
        masses = []
        for density in amdkgp3m.values():
            masses.append(volume * density)
        return masses


def diameter_to_sphere_volume(diameter):
    if isinstance(diameter, list):
        sphere_volume = []
        for d in diameter:
            radius = d / 2
            sphere_volume.append((4/3) * pi * radius ** 3)
        return sphere_volume

    else:
        radius = diameter / 2
        return (4/3) * pi * radius ** 3
